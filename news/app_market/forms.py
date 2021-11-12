from django import forms
from app_market.models import CartProduct


#PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ('product', 'quantity', 'final_price',)

'''    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)'''