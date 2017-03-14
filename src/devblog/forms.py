from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']

        
    def clean_title(self):
        title = self.cleaned_data['title']
        qs = Article.objects.filter(title__iexact=title)
        if qs:
            raise forms.ValidationError("You've already using this title.")
        return title