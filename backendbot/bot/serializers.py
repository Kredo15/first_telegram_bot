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
        category_create = validated_data.pop('category').pop('name')
        enword_create = validated_data.pop('enword').pop('word')
        ruword_create = validated_data.pop('ruword').pop('word')
        dict_a_post = Dictionary.objects.create(category=category_create, enword=enword_create, ruword=ruword_create)
        print(dict_a_post.query)
        return super().create(validated_data)
