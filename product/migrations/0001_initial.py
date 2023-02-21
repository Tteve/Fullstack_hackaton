# Generated by Django 4.1.5 on 2023-02-21 09:14

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('brand', models.CharField(choices=[('Nike', 'Nike'), ('adidas', 'adidas'), ('PUMA', 'PUMA'), ('Reebok', 'Reebok'), ('Timberland', 'Timberland'), ('YSL', 'YSL')], max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('preview', models.ImageField(upload_to='images')),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('stock', models.CharField(choices=[('in_stock', 'В наличии'), ('out_of_stock', 'Нет в наличии')], max_length=50)),
                ('sex', models.CharField(choices=[('men', 'Мужской'), ('women', 'Женский'), ('unisex', 'Юнисекс')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to='category.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_products', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='product.product')),
            ],
            options={
                'unique_together': {('owner', 'product')},
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='product.product')),
            ],
            options={
                'unique_together': {('owner', 'product')},
            },
        ),
    ]
