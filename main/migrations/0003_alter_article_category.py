# Generated by Django 4.2.5 on 2023-09-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_can_manage_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='main.category', verbose_name='category'),
        ),
    ]
