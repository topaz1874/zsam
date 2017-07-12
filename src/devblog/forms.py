from django import forms
from .models import Article,Weights
from pagedown.widgets import PagedownWidget

class ArticleForm(forms.ModelForm):
    text = forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta:
        model = Article
        fields = ['title', 'text', 'files']

        
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     qs = Article.objects.filter(title__iexact=title)
    #     if qs:
    #         raise forms.ValidationError("You've already using this title.")
    #     return title


class ArticleUpdateForm(ArticleForm):


    def __init__(self, *args, **kwargs):
        super(ArticleUpdateForm, 
            self).__init__(*args, **kwargs)

    class Meta(ArticleForm.Meta):
        fields = ['title', 'text', 'files']


class NoteWeightsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NoteWeightsForm, self).__init__(*args, **kwargs)
        # self.fields['name'].choices=[
        #     (x.name, x.name) for x in Weights.objects.all()
        # ]
        print dir(self.fields['name'])

    class Meta:
        model = Weights
        fields = '__all__'
        widgets = {
            'dates': forms.widgets.SelectDateWidget(),
        }



    def clean_weights(self):
        weight = self.cleaned_data['weights']
        if weight <= 0:
            raise forms.ValidationError("Weight should be positive.")
        return weight









