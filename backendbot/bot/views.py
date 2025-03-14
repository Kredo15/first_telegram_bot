from django.shortcuts import render
from rest_fraemwork import APIView
from . import models
from django.db.models import Prefetch


class WordForLearn(APIView):
    def get(self, *args, **kwargs): 
        """select * from dictionary A
            LEFT JOIN Userdictionaries B ON A.id = B.word
            WHERE B.user = user_id AND A.category = category"""
        word = models.Dictionary.objects.prefetch_related(Prefetch)#(category=kwargs.get('name_category'))[:1]

