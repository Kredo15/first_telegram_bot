from rest_framework import serializers
from .models import Dictionary, Enwords, Ruwords, Categories, Profile, Ratings


class RatingsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ["name"]


class ProfileModelSerializer(serializers.ModelSerializer):
    rating = RatingsModelSerializer()

    class Meta:
        model = Profile
        fields = ['name', 'count_words', 'rating']


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
        return Dictionary(**validated_data)
