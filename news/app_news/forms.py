from django import forms
from app_news.models import News, Comment, File
#from tinymce.widgets import TinyMCE


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class NewsSearchForm(forms.Form):
    #name_field = forms.TextInput(attrs={'size': 10, 'title': 'Your name'})
    title_field = forms.CharField(max_length=50)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    file = forms.FileField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('description', 'file',)


class MultiFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class UploadNewsForm(forms.Form):
    file = forms.FileField()
