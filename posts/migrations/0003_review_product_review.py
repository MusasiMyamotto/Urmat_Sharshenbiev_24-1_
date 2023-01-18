# Generated by Django 4.1.5 on 2023-01-18 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.review'),
        ),
    ]
