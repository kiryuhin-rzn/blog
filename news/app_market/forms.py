from django import forms
from app_market.models import CartProduct


class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ('product', 'quantity', 'final_price',)


class ReportSalesForm(forms.Form):
    start_date_field = forms.DateTimeField()
    finish_date_field = forms.DateTimeField()
