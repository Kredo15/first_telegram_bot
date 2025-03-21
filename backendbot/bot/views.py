from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from django.db.models import OuterRef, Subquery, Prefetch
from .serializers import DictionaryModelSerializer, ProfileModelSerializer


class ProfileAPIView(APIView):
    """Отдаём данные пользователя/
    создаем профиль пользователя"""
    def get(self, *args, **kwargs):
        data_user = models.Profile.objects.filter(user=kwargs.get('user')).values('name', 'count_words', 'rating')
        serializer = ProfileModelSerializer(data_user, many=True)
        return Response(serializer.data)


class DictionaryAPIView(APIView):
    """Отдаём слово, которое еще не изучалось/
    добавляем новые слова в словарь"""
    def get(self, *args, **kwargs):
        words_in_learn = models.Userdictionaries.objects.filter(user=kwargs.get('user'))
        if words_in_learn:
            word = models.Dictionary.objects.annotate(word=Subquery(words_in_learn)).filter(category__name=kwargs.get('name_category')).values('enword', 'ruword').first()
        else:
            word = models.Dictionary.objects.select_related('enword', 'ruword', 'category').all()[:1]
        serializer = DictionaryModelSerializer(word, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DictionaryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
