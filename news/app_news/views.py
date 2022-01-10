from django.shortcuts import render
from app_news.forms import CommentForm, UploadFileForm, DocumentForm, MultiFileForm, UploadNewsForm, NewsSearchForm
from app_news.models import News, File
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import DetailView
from django import forms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.db.models import Q
#from django.views.generic.edit import FormView


def sample_view(request):
    html = '<body><h1>Django sample_view</h1><br><p>Отладка sample_view</p></body>'
    return HttpResponse(html)


class NewsSearchView(generic.ListView):
    model = News
    template_name = 'news_search.html'

    def get_queryset(self):
        form = NewsSearchForm(self.request.GET)
        if form.is_valid():
            serch_field = form.cleaned_data.get('search_field')
            object_list = News.objects.filter(Q(title__icontains=serch_field) | Q(text__icontains=serch_field))

            return object_list




'''    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = News.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
        return object_list'''



'''    def get(self, *args, **kwargs):
        form = NewsSearchForm(self.request.GET)
        if form.is_valid():
            title_field = form.cleaned_data.get('title_field')
            query = self.request.GET.get(title_field)
            object_list = News.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
            render(self.request, 'app_news/news_search.html', object_list)'''





class NewsListView(generic.ListView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.order_by('-date_publication')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = NewsSearchForm()
        context['form2'] = form
        return context


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        #data = File.objects.all()
        if self.request.user.is_authenticated:
            form.fields['author'].widget = forms.HiddenInput()
            form.fields['author'].initial = self.request.user.username
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        news = self.get_object()
        if request.user.is_authenticated:
            user = request.user
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.news = news
                comment.author = user
                comment.user = user
                comment.save()
                return redirect('news_detail', pk=news.pk)
            else:
                form = CommentForm()
            return render(request, 'app_news/news_detail.html', {'form': form})
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.news = news
                comment.author = comment.author + ' (Anonym)'
                comment.save()
                return redirect('news_detail', pk=news.pk)
            else:
                form = CommentForm()
            return render(request, 'app_news/news_detail.html', {'form': form})




class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'app_news.can_publish'
    model = News
    template_name = 'app_news/add_news.html'
    fields = ['title', 'text']




def upload_file(request):
    if request.method =='POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name, status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form2': upload_file_form
    }
    return render(request, 'app_news/upload.html', context=context)

#def model_form_upload(request):
    #if request.method =='POST':
        #form = DocumentForm(request.POST, request.FILES)
        #if form.is_valid():
            #form.save()
            #return redirect('/')
    #else:
        #form = DocumentForm()
    #return render(request, 'app_news/form_upload.html', {
        #'form': form
        #})


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_news.can_edit'
    model = News
    template_name = 'app_news/news_edit.html'
    fields = ['title', 'text']


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'app_news.can_delete'
    model = News
    template_name = 'app_news/news_delete.html'
    success_url = reverse_lazy('news_list')


def form_upload(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method =='POST':
        form_upload = DocumentForm(request.POST, request.FILES)
        if form_upload.is_valid():
            file = form_upload.save(commit=False)
            file.news = news
            form_upload.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form_upload = DocumentForm()
    return render(request, 'app_news/form_upload.html', {
        'form_upload': form_upload
        })


def upload_files(request, pk):
    if request.user.is_authenticated:
        news = get_object_or_404(News, pk=pk)
        if request.method =='POST':
            form = MultiFileForm(request.POST, request.FILES)
            if form.is_valid():
                files = request.FILES.getlist('file_field')
                for f in files:
                    instance = File(file=f)
                    instance.news = news
                    instance.save()
                return redirect('news_detail', pk=news.pk)
        else:
            form = MultiFileForm()
        return render(request, 'app_news/upload_files.html', {'form': form})
    else:
        return HttpResponse(content='Для загрузки файлов необходимо авторизоваться!', status=200)


def upload_news(request):
    if request.method == 'POST':
        form = UploadNewsForm(request.POST, request.FILES)
        if form.is_valid():
            price_file = form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split('\n')
            #csv_reader = reader(price_str, delimiter=",", quotechar='"')
            for row in price_str[: -1]:
                tmp = News.objects.create()
                tmp.title = row.split(';')[0]
                tmp.text = row.split(';')[1]
                tmp.save()
            return HttpResponse(content='Новости были успешно загружены', status=200)
    else:
        form = UploadNewsForm()

        context = {
            'form': form
            }
    return render(request, 'app_news/upload.html', {'form': form})#было context=context вместо form: form


def add_comment_to_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = CommentForm()
    return render(request, 'app_news/add_comment_to_news.html', {'form': form})
