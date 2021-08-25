from django.shortcuts import render
from .forms import NewsForm, CommentForm
from .models import News
from django.views import generic
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404


class NewsListView(generic.ListView):
    model = News
    template_name = 'app_news/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()[::-1]


class NewsDetailView(generic.DetailView):
    model = News

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_detail', pk=news.pk)

    else:
        form = NewsForm()
    return render(request, 'app_news/add_news.html', {'form': form})


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'app_news/news_edit.html'
    fields = ['title', 'text']

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
