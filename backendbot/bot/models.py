from django.db import models


class Ruwords(models.Model):
    "Таблица для русских слов/фраз"
    word = models.TextField(verbose_name='word')

    def __str__(self):
        return self.word


class Enwords(models.Model):
    "Таблица для английских слов/фраз"
    word = models.TextField(verbose_name='word')

    def __str__(self):
        return self.word


class Categories(models.Model):
    "Таблица для хранения названий категорий"
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Dictionary(models.Model):
    "Таблица для слов/фраз с переводом, разделенные на категории"
    en_word = models.ForeignKey('Enwords', on_delete=models.PROTECT)
    ru_word = models.ForeignKey('Ruwords', on_delete=models.PROTECT)
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.en_word.word}, {self.ru_word.word}, {self.category}'


class Ratings(models.Model):
    "Таблица для рейтинга (присваивается от количества выученных слов)"
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Users(models.Model):
    "Таблца пользователей"
    name = models.CharField(max_length=255)
    count_words = models.IntegerField()
    rating = models.ForeignKey('Ratings', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}_{self.rating}'


class Userdictionaries(models.Model):
    "Таблица для отслеживания изучения слов пользователями"
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    word = models.ForeignKey('Dictionary', on_delete=models.PROTECT)
    translate_choose_ru = models.BooleanField(default=False)
    translate_choose_en = models.BooleanField(default=False)
    translate_write_ru = models.BooleanField(default=False)
    translate_write_en = models.BooleanField(default=False)
    write_word_using_audio = models.BooleanField(default=False)
    is_learn = models.BooleanField(default=False)
