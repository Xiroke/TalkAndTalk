from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.other_profile, name='profile'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('articles/', views.articles, name='articles'),
    path('articles/<slug:category_slug>/', views.articles_category, name='articles'),
    path('article/<slug:article_slug>/', views.article, name='article'),
    path('create_article/', views.create_article, name='create_article'),
    path('edit_article/<slug:article_slug>/', views.edit_article, name='edit_article'),
    path('about_us/', views.about_us, name='about_us'),
]