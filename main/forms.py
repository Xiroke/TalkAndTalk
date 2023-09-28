from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Comment, Category
from ckeditor.widgets import CKEditorWidget


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password1', 'password2']
        
class ArticleForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Article
        fields = ['title', 'category', 'content', ]
        exclude = ['author']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']