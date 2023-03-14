from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TestSerializers, OptionsSerializers, QuestionsSerializers, UserSerializers, AnswersSerializers
from .models import Test, Options, Answers, Questions, User


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializers
    queryset = Test.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()



class QuestionsViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionsSerializers
    queryset = Questions.objects.all()



class OptionsViewSet(viewsets.ModelViewSet):
    serializer_class = OptionsSerializers
    queryset = Options.objects.all()



class AnswersViewSet(viewsets.ModelViewSet):
    serializer_class = AnswersSerializers
    queryset = Answers.objects.all()


# Create your views here.
