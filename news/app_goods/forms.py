from django import forms


class UploadNewsForm(forms.Form):
    file = forms.FileField()