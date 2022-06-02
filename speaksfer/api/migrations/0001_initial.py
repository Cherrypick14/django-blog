# Generated by Django 4.0.5 on 2022-06-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=240, unique=True)),
                ('title', models.CharField(max_length=240, unique=True)),
                ('body', models.TextField()),
                ('description', models.CharField(blank=True, max_length=155)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
    ]
