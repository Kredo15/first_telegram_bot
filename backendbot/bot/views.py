from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from django.db.models import OuterRef, Subquery, Prefetch
from .serializers import DictionaryModelSerializer


class WordForLearn(APIView):

    def get(self, *args, **kwargs):
        words_in_learn = models.Userdictionaries.objects.filter(user=kwargs.get('user_id'))
        if words_in_learn:
            word = models.Dictionary.objects.annotate(word=Subquery(words_in_learn)).filter(category__name=kwargs.get('name_category')).values('enword', 'ruword').first()
        else:
            word = models.Dictionary.objects.select_related('enword', 'ruword', 'category').all()[:1]
        serialized_word = DictionaryModelSerializer(word, many=True)
        return Response(serialized_word.data)

    def post(self, request):
        serializer = DictionaryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
