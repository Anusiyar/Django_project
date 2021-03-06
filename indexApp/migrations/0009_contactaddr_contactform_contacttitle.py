# Generated by Django 4.0.3 on 2022-04-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0008_experiencelist_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactaddr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('messages', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='contacttitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
