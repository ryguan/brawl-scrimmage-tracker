from django.db import models
import requests
# Create your models here.

#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published') 


#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
game_modes = [('bounty','bounty'),('knockout','knockout'),('gemGrab','gemGrab'),('brawlBall','brawlBall'),('hotZone','hotZone'),('wipeout','wipeout'), ('payload','payload')]

class User(models.Model):

    user_id = models.BigAutoField(primary_key = True)
    username = models.CharField(max_length = 20, unique = True)
    password = models.CharField(max_length = 20) #set unique = true later, this keeps it a bit easier to use dummy passwords
    player_id = models.CharField(max_length = 12, unique = True)
    
    def __str__(self):
        return str(self.username)
    
    #def get_absolute_url(self):

class Room(models.Model):

    room_id = models.BigAutoField(primary_key = True)
    blue_first = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+') # there needs to be at least one player on each side
    blue_second = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True, related_name='+')
    blue_third = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True, related_name='+')
    #red_team = models.ManyToManyField(User)
    red_first = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='+') 
    red_second = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True, related_name='+') #I THINK WE SHOULD EVENTUALLY CHANGE THESE TO  A MANYTOMANY FIELD
    red_third = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  blank = True, related_name='+')
    map_type = models.CharField(max_length = 10, choices = game_modes, default = 'brawlBall')
    map_name = models.CharField(max_length = 20, blank = True) #dont know if theres a good way for the api to help pull for this
    
    def __str__(self):
        return str(self.room_id)
    
    #def get_absolute_url(self):