from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse
# Create your views here.
from .models import Article
from .forms import ArticleForm

class IndexView(ListView):
    model = Article

    template_name = 'devblog/list.html'

class ArticleDetailView(DetailView):
    model = Article

    template_name = 'devblog/detail.html'

class ArticleCreateView(CreateView):
    # success_url = reverse('devblog:list')
    form_class = ArticleForm
    template_name = 'devblog/forms.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArticleCreateView, self).form_valid(form)