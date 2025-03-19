# Generated by Django 5.1.6 on 2025-03-19 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Enwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ruwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.categories', verbose_name='category')),
                ('enword', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.enwords', verbose_name='enword')),
                ('ruword', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.ruwords', verbose_name='ruword')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('count_words', models.IntegerField()),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.ratings', verbose_name='rating')),
            ],
        ),
        migrations.CreateModel(
            name='Userdictionaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translate_choose_ru', models.BooleanField(default=False)),
                ('translate_choose_en', models.BooleanField(default=False)),
                ('translate_write_ru', models.BooleanField(default=False)),
                ('translate_write_en', models.BooleanField(default=False)),
                ('write_word_using_audio', models.BooleanField(default=False)),
                ('is_learn', models.BooleanField(default=False)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.dictionary', verbose_name='word')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bot.users', verbose_name='user')),
            ],
        ),
    ]
