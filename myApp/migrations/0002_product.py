# Generated by Django 4.2.1 on 2023-05-23 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img/%y')),
                ('product_id', models.CharField(max_length=200)),
            ],
        ),
    ]
