from django.shortcuts import render
from django.views.generic import \
    ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import FormValidMessageMixin
# Create your views here.
from .models import Article
from .forms import ArticleForm,ArticleUpdateForm

class IndexView(ListView):
    model = Article
    template_name = 'devblog/list.html'



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'devblog/detail.html'



class ArticleCreateView(FormValidMessageMixin,LoginRequiredMixin, CreateView):
    # success_url = reverse_lazy('devblog:index')
    form_class = ArticleForm
    template_name = 'devblog/forms.html'
    form_valid_message = _(u"Blog post created!")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArticleCreateView, self).form_valid(form)



class ArticleDeleteView(FormValidMessageMixin,LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'devblog/confirm_delete.html'
    success_url = reverse_lazy('devblog:index')

    form_valid_message = _(u"Blog post deleted!")



class ArticleUpdateView(FormValidMessageMixin,LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'devblog/forms.html'
    form_valid_message = _(u"Blog post updated!")
    # fields = ['title', 'text']
    form_class = ArticleUpdateForm
