from rest_framework import serializers
from bot.models import Dictionary


class DictionaryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ['en_word_id', 'ru_word_id']
