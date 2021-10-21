from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth import logout
from app_users.forms import ExtendedRegisterForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


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

'''
def user_account(request):
    balance = get_balance()
    promotions = get_promotions()
    offers = get_offers()
    payment_history = get_payment_history()

    return render(request, 'app_users/account.html', context={
        'balance': balance,
        'promotions': promotions,
        'offers': offers,
        'payment_history': payment_history
    })

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
