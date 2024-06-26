# Generated by Django 3.2.3 on 2024-06-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('content', models.TextField(verbose_name='本文')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿時間')),
                ('category', models.CharField(choices=[('dailylife', '日常のこと'), ('tech', '技術的なこと'), ('hobby', '趣味のこと')], max_length=50, verbose_name='カテゴリー')),
            ],
        ),
    ]
