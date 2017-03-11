from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Article

class IndexView(ListView):
    model = Article

    template_name = 'devblog/list.html'

class ArticleDetailView(DetailView):
    model = Article

    template_name = 'devblog/detail.html'
    