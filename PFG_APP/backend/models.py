from django.db import models


class User(models.Model):
    class Roles(models.TextChoices):
        STUDENT = "ST"
        PROFESSOR = "PF"

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    role = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default=Roles.STUDENT,
    )
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=40)


class Questionnaire(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=10000)
    weight = models.IntegerField()
