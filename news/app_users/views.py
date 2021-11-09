from django.contrib.auth.views import LoginView, TemplateView
from django.shortcuts import render
from django.contrib.auth import logout
from app_users.forms import ExtendedRegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from app_users.models import User
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from app_users.forms import BalanceForm
from django.db.models import F


class AnotherLoginView(LoginView):
    template_name = 'app_users/login.html'


def logout_view(request):
    logout(request)
    return render(request, 'app_users/logout.html')


def register_view(request):
    if request.method == 'POST':
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedRegisterForm()
        return render(request, 'app_users/register.html', {'form': form})


class UserAccountView(TemplateView):
    template_name = 'app_users/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.user.username
        user_id=self.request.user.id
        user=User.objects.get(id=user_id)
        context['balance'] = user.account.balance

        promotions_cache_key = 'promotions:{}'.format(username)
        promotions = user.account.promotions
        prom = cache.get_or_set(promotions_cache_key, promotions, 30*60)
        context['promotions'] = prom

        offers_cache_key = 'offers:{}'.format(username)
        offers = user.account.offers
        offer = cache.get_or_set(offers_cache_key, offers, 30*60)
        context['offers'] = offer

        context['payment_history'] = user.account.payment_history
        context['username'] = self.request.user.username

        return context

    def cleaned_cache(request):
        if request.method =='POST':
            key = make_template_fragment_key('footer', request.user.username)
            cache.delete(key)


class UserBalanceView(TemplateView):
    template_name = 'app_users/balance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #username = self.request.user.username
        user_id=self.request.user.id
        user=User.objects.get(id=user_id)
        context['balance'] = user.account.balance
        context['username'] = self.request.user.username
        form = BalanceForm()
        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):
        form = BalanceForm(request.POST)
        if form.is_valid():
            user_id=self.request.user.id
            user=User.objects.get(id=user_id)
            client = user.account
            data=form.cleaned_data.get('balance')
            client.balance=F('balance') + data
            client.save()
            return redirect('/users/account/')
        else:
            form = BalanceForm()
        return render(request, 'app_users/balance.html', {'form': form})


'''
def user_account(request):
    username = request.user.username
    user_id=request.user.id
    user=User.objects.get(id=user_id)
    balance = user.account.balance

    promotions_cache_key = 'promotions:{}'.format(username)
    promotions = user.account.promotions
    cache.get_or_set(promotions_cache_key, promotions, 30*60)

    offers_cache_key = 'offers:{}'.format(username)
    offers = user.account.offers
    cache.get_or_set(offers_cache_key, offers, 30*60)

    payment_history = user.account.payment_history

    return render(request, 'app_users/account.html', context={
        'balance': balance,
        'promotions': promotions,
        'offers': offers,
        'payment_history': payment_history,
    })

'''
'''
def update_user_account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
        return render(request, 'app_users/account.html', {'form': form})

'''
