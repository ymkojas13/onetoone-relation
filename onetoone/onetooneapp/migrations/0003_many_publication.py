# Generated by Django 3.2.6 on 2021-08-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onetooneapp', '0002_article_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='many',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='onetooneapp.Publication')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]
