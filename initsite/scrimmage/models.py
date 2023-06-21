from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User(models.Model):

    user_id = models.BigAutoField(primary_key = True)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    player_id = models.CharField(max_length = 12)

class Room(models.Model):

    room_id = models.BigAutoField(primary_key = True)
    blue_first = models.CharField(max_length = 12, blank = True)
    blue_second = models.CharField(max_length = 12, blank = True)
    blue_third = models.CharField(max_length = 12, blank = True)
    red_first = models.CharField(max_length = 12, blank = True)
    red_second = models.CharField(max_length = 12, blank = True)
    red_third = models.CharField(max_length = 12, blank = True)
    map_type = models.CharField(max_length = 10)
    map_name = models.CharField(max_length = 12, blank = True)