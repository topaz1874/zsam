from django.contrib import admin

# Register your models here.
from .models import Article,Weights

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Weights)