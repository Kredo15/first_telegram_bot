from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from django.db.models import OuterRef, Subquery, Prefetch
from bot.serializers import DictionaryModelSerializer


class WordForLearn(APIView):

    def get(self, user_id=None, name_category=None):
        '''words_in_learn = models.Userdictionaries.objects.filter(user=user_id)
        if words_in_learn:
            word = models.Dictionary.objects.annotate(word=Subquery(words_in_learn)).filter(category=name_category).values('en_word', 'ru_word')[:1]
        else:'''
        word = models.Dictionary.objects.prefetch_related(Prefetch('en_word', queryset=models.Enwords.objects.prefetch_related('id')))[:1]
        print(word.query)
        serialized_word = DictionaryModelSerializer(word, many=False)
        return Response(serialized_word.data)
