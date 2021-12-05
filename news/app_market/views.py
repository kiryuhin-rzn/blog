#from django.shortcuts import render
from django.views import generic
from app_users.models import Account
from app_market.models import Shop, Product, CartProduct, Cart, ReportSales
from app_market.forms import CartAddProductForm, ReportSalesForm
from django.views.generic import DetailView
from django.contrib.auth.models import User
#from django.contrib.auth.views import TemplateView
#from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django import forms
from django.db.models import F
from django.db.models import Sum
from decimal import Decimal
from django.shortcuts import render
from django.contrib.auth.views import TemplateView
#from django.db.models import FloatField
from django import template
import logging


logger = logging.getLogger(__name__)


class ShopListView(generic.ListView):
    model = Shop
    template_name = 'app_market/shop_list.html'
    context_object_name = 'shop_list'
    queryset = Shop.objects.prefetch_related('product_set').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CartAddProductForm()

        form.fields['product'].widget = forms.HiddenInput()
        form.fields['product'].initial = self.request.POST.get('product', None)

        form.fields['final_price'].widget = forms.HiddenInput()

        context['form'] = form
        logger.debug('Запрошена страница со списком магазинов')
        return context

    def post(self, request, *args, **kwargs):
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            id_product = request.POST.get('product', None)#нужно ли тут None?
            product = Product.objects.get(id=id_product)
            price = product.price
            quantity = form.cleaned_data.get('quantity')
            final_price = int(quantity) * price
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
            r = ReportSales(product=b, number=a.quantity)
            r.save()
            b.save()
        final_price = cart.final_price
        account = Account.objects.get(user=user)
        balance = Decimal(float(account.balance))
        account.balance = balance - final_price
        account.status += final_price
        account.save()
        cartproduct.delete()
        cart.delete()

        return redirect('account')


class ReportSalesView(TemplateView):
    #model = ReportSales
    template_name = 'app_market/report_sales.html'



    def post(self, request, *args, **kwargs):
        form = ReportSalesForm(self.request.POST)
        if form.is_valid():
            start_date_field = form.cleaned_data.get('start_date_field')
            finish_date_field = form.cleaned_data.get('finish_date_field')
            report_sales = ReportSales.objects.all().exclude(created__lte=start_date_field).exclude(created__gte=finish_date_field)#.order_by(F('number').desc())

            prod = report_sales.values_list('id', flat=True)
            #pubs = report_sales.aggregate(Sum(F('number')))
            w = {}
            s = []
            for i in prod:
                a = Product.objects.filter(reportsales__id=i).values_list('id', flat=True)
                w[a[0]]=a[0]
            for i in w:
                s.append(i)

            total={}
            for i in s:
                g = report_sales.filter(product__id=i).aggregate(price=Sum(F('number')))
                total[i] = g['price']

            return render(request, 'app_market/report_sales.html', {'report_sales': Product.objects.filter(reportsales__created__range=(start_date_field, finish_date_field)).annotate(Sum('reportsales__number')), 'price_total': total, 'w': total})
        else:
            form = ReportSalesForm()
            return render(request, 'app_market/report_sales.html', {'form': form})



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['report_sales'] = self.report_sales
        #context = super().get_context_data(**kwargs)
        form = ReportSalesForm()
        context['form'] = form

        return context



register = template.Library()

@register.filter(name='cutes')
def cutes(value, arg):
    return value[arg]

class ShopDetailView(DetailView):
    model = Product



'''
class ReportSalesView(TemplateView):
    #model = ReportSales
    template_name = 'app_market/report_sales.html'



    def post(self, request, *args, **kwargs):
        form = ReportSalesForm(self.request.POST)
        if form.is_valid():
            start_date_field = form.cleaned_data.get('start_date_field')
            finish_date_field = form.cleaned_data.get('finish_date_field')
            report_sales = ReportSales.objects.all().exclude(created__lte=start_date_field).exclude(created__gte=finish_date_field)#.order_by(F('number').desc())
            #report_sales = report_sales1.filter(id=3).count()
            #report_sales = ReportSales.objects.all().exclude(created__lte=datetime(start_date_field)).exclude(created__gte=datetime(finish_date_field))
            prod = report_sales.values_list('id', flat=True)
            w = {}
            s = []
            for i in prod:
                a = Product.objects.filter(reportsales__id=i).values_list('id', flat=True)
                w[a[0]]=a[0]
            for i in w:
                s.append(i)

            #price_total = request.META.get('HTTP_X_REAL_IP')
            price_total={}
            for i in s:
                g = report_sales.filter(product__id=i).aggregate(price=Sum(F('number')))
                price_total[i] = g['price']
            return render(request, 'app_market/report_sales.html', {'report_sales': Product.objects.filter(id__in=s), 'price_total': price_total})# убрал report_sales.filter(id__in=s).aggregate(price_total=Sum(F('number')))
        else:
            form = ReportSalesForm()
            return render(request, 'app_market/report_sales.html', {'form': form})
'''
