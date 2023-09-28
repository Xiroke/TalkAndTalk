from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from pytils.translit import slugify         #use for russian language #from django.template.defaultfilters import slugify 
from ckeditor.fields import RichTextField
from django.urls import reverse

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,            
        )

        user.set_password(password)        
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,            
        )
        user.is_staff = True
        user.is_superuser = True   
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(verbose_name='name', max_length=30, blank=True, unique=True)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    is_superuser = models.BooleanField(verbose_name='superuser', default=False)
    avatar = models.ImageField(verbose_name='avatar', upload_to='avatar/%Y-%m-%d/', blank=True, default='avatar.svg')
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Ip(models.Model):
    ip = models.CharField(max_length=100)

def __str__(self):
    return self.ip

class Category(models.Model):
    title = models.CharField(verbose_name='title', max_length=255, blank=True)
    slug = models.SlugField(verbose_name='slug', unique=True, blank=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('articles', kwargs={'category_slug': self.catgory.slug})
    
class Article(models.Model):
    title = models.CharField(verbose_name='title', max_length=255, blank=True)
    content = RichTextField(verbose_name='content', blank=True)
    date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='slug', unique=True, blank=False)
    category = models.ManyToManyField(Category, verbose_name='category', blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})
    
    def total_views(self):
        return self.views.count()

class Comment(models.Model):
    text = models.TextField(verbose_name='text')
    date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name='article', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    

