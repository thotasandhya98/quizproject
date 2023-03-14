from rest_framework import serializers

from .models import User, Questions, Options, Answers, Test


class TestSerializers(serializers.ModelSerializer):
    get_test = serializers.SerializerMethodField()

    class Meta:
        model = Test
        fields = '__all__'

    def get_test(self, obj):
        return obj.Test.user


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class QuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class OptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'


class AnswersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'
