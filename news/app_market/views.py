#from django.shortcuts import render
from django.views import generic
from app_users.models import Account
from app_market.models import Shop, Product, CartProduct, Cart
from app_market.forms import CartAddProductForm
from django.views.generic import DetailView
from django.contrib.auth.models import User
#from django.contrib.auth.views import TemplateView
#from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django import forms
from django.db.models import F
from django.db.models import Sum
from decimal import Decimal


class ShopListView(generic.ListView):
    model = Shop
    template_name = 'app_market/shop_list.html'
    context_object_name = 'shop_list'
    queryset = Shop.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CartAddProductForm()

        form.fields['product'].widget = forms.HiddenInput()
        form.fields['product'].initial = self.request.POST.get('product', None)

        form.fields['final_price'].widget = forms.HiddenInput()

        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            id_product = request.POST.get('product', None)#нужно ли тут None?
            product = Product.objects.get(id=id_product)
            price = product.price
            quantity = form.cleaned_data.get('quantity')
            final_price = quantity * price
            cartproduct = CartProduct(product=product, quantity=quantity, final_price=final_price)
            user_id=self.request.user.id
            user=User.objects.get(id=user_id)
            cartproduct.user=user
            cartproduct.save()
            cart, created = Cart.objects.get_or_create(user=user, defaults={'final_price': final_price})
            cart2 = Cart.objects.get(user=user)
            cart2.product.add(cartproduct)

        return redirect('cart')


class CartListView(generic.ListView):
    template_name = 'app_market/cart.html'

    def get_queryset(self):
        user_id=self.request.user.id
        user=User.objects.get(id=user_id)
        self.cart = CartProduct.objects.filter(user=user)
        return CartProduct.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super(CartListView, self).get_context_data(**kwargs)
        context['cart'] = self.cart

        user_id=self.request.user.id
        user=User.objects.get(id=user_id)

        a = CartProduct.objects.filter(user=user)
        b = a.aggregate(price_1=Sum(F('final_price')))# нужно ли тут F?

        cart = Cart.objects.get(user=user)
        cart.final_price = b['price_1']
        cart.save()
        context['final_price'] = cart.final_price

        return context

    def post(self, request, *args, **kwargs):
        user_id=self.request.user.id
        user=User.objects.get(id=user_id)
        cart = Cart.objects.get(user=user)
        cartproduct = CartProduct.objects.filter(user=user)
        prod = cartproduct.values_list('id', flat=True)
        for i in prod:
            a=CartProduct.objects.get(id=i)
            b=a.product
            b.number = b.number - a.quantity
            b.save()
        final_price = cart.final_price
        account = Account.objects.get(user=user)
        balance = Decimal(float(account.balance))
        account.balance = balance - final_price
        account.save()
        cartproduct.delete()
        cart.delete()

        return redirect('account')


class ShopDetailView(DetailView):
    model = Product


'''class CartView(TemplateView):
    template_name = 'app_market/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #username = self.request.user.username
        user_id=self.request.user.id
        user=User.objects.get(id=user_id)
        cart = Cart.objects.get(user=user)
        context['final_price'] = cart.final_price

        return context
'''


'''

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #username = self.request.user.username
        user_id=self.request.user.id
        user=User.objects.get(id=user_id)
        context['product'] = user.cartproduct.product

        return context
'''


'''
class CartView(TemplateView):
    template_name = 'app_market/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #username = self.request.user.username
        user_id=self.request.user.id
        user=User.objects.get(id=user_id)
        context['product'] = user.cart.product
        context['quantiti'] = user.cart.quaniti
        context['total'] = user.account.total

        return context
'''