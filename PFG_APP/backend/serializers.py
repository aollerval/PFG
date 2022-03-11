from rest_framework import serializers

from backend import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questionnaire
        fields = "__all__"

