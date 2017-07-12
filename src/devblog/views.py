from django.shortcuts import render
from django.views.generic import \
    ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import FormValidMessageMixin
# Create your views here.
from .models import Article,Weights
from .forms import ArticleForm,ArticleUpdateForm,NoteWeightsForm

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

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.files:
            print obj.files
            obj.files.delete(save=True)
        return super(ArticleDeleteView, self).delete(request, *args, **kwargs)


class ArticleUpdateView(FormValidMessageMixin,LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'devblog/forms.html'
    form_valid_message = _(u"Blog post updated!")
    # fields = ['title', 'text']
    form_class = ArticleUpdateForm

#using chartjs 
from django.views.generic import TemplateView

class AnalyticsIndexView(TemplateView):
    template_name = 'devblog/analytics/index.html'

    def get_context_data(self, **kwargs):
        context = super(AnalyticsIndexView, self).get_context_data(**kwargs)
        context['latest_5_weights'] = self.latest_5_weights()
        context['label'] = 'ZhQT latest 5 weights'
        context['latest_5_dates'] = self.latest_5_dates()
        return context

    def latest_5_weights(self):
        qs = Weights.objects.get_latest_5()
        weights_in_float = []
        for entry in qs:
            weights_in_float.append(float(entry.weights)*2)
        return weights_in_float


    def latest_5_dates(self):
        dates_in_float = []
        qs = Weights.objects.get_latest_5()
        for entry in qs:
            dates_in_float.append(float(entry.dates.strftime('%m.%d')))
        print dates_in_float
        return dates_in_float

class AnalyticsNoteWeights(CreateView):
    template_name = 'devblog/analytics/noteweights.html'
    form_class = NoteWeightsForm

    success_url = reverse_lazy('devblog:analytics')









