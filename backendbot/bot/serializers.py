from rest_framework import serializers
from .models import Dictionary, Enwords, Ruwords, Categories


class EnwordsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enwords
        fields = ["word"]


class RuwordsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruwords
        fields = ["word"]


class CategoriesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["name"]


class DictionaryModelSerializer(serializers.ModelSerializer):
    enword = EnwordsModelSerializer()
    ruword = RuwordsModelSerializer()
    category = CategoriesModelSerializer()

    class Meta:
        model = Dictionary
        fields = ['enword', 'ruword', 'category']

    def create(self, validated_data):
        category_create, _ = Categories.objects.get_or_create(name=validated_data.get('category').get('name'))
        ruword_create, _ = Ruwords.objects.get_or_create(word=validated_data.get('enword').get('word'))
        enword_create, _ = Enwords.objects.get_or_create(word=validated_data.get('ruword').get('word'))
        return Dictionary.objects.create(category=category_create, enword=enword_create, ruword=ruword_create)
