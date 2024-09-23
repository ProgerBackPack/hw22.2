# Generated by Django 5.1 on 2024-09-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'Версия продукта', 'verbose_name_plural': 'Версии продукта'},
        ),
        migrations.RemoveField(
            model_name='version',
            name='category',
        ),
        migrations.RemoveField(
            model_name='version',
            name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, help_text='Введите дату создания продукта', verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now=True, help_text='Введите дату последнего изменения продукта', null=True, verbose_name='Дата последнего изменения'),
        ),
    ]
