# Generated by Django 4.1.7 on 2023-04-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auther_name', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1500)),
            ],
            options={
                'db_table': 'articlemodel',
            },
        ),
    ]
