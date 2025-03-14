from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from django.db.models import OuterRef, Subquery


class WordForLearn(APIView):
    def get(self, *args, **kwargs): 
        """select * from dictionary
            WHERE category = category AND id not in
            (SELECT word FROM Userdictionaries WHERE user = user_id)"""
        words_in_learn = models.Userdictionaries.objects.filter(user=kwargs.get('user_id'))
        word = models.Dictionary.objects.annotate(word=Subquery(words_in_learn)).filter(category=kwargs.get('name_category')).values('en_word', 'ru_word')[:1]
        return Response(word)
