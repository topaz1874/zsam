from django import forms
from .models import Article
from pagedown.widgets import PagedownWidget

class ArticleForm(forms.ModelForm):
    text = forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta:
        model = Article
        fields = ['title', 'text']

        
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
        fields = ['title', 'text']
