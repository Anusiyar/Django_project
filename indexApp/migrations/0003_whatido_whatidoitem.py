# Generated by Django 4.0.3 on 2022-04-10 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0002_slider_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='whatido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='whatidoitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
