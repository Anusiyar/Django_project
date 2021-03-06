# Generated by Django 4.0.3 on 2022-04-10 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0003_whatido_whatidoitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='aboutbrief',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='aboutprojects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('counts', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='aboutskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('counts', models.IntegerField(max_length=10)),
            ],
        ),
    ]
