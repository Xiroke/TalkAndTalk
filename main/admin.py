from django.contrib import admin
from .models import *
# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Article, MyModelAdmin)
admin.site.register(Comment, MyModelAdmin)
admin.site.register(User)
admin.site.register(Ip)
admin.site.register(Category)