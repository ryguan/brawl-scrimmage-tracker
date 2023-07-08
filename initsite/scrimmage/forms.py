from django import forms
from .models import Room,User
class NameForm(forms.Form):
    your_name = forms.CharField(label='brawl-tag', max_length=100)
    
    
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'room_id',
            'blue_first',
            'blue_second',
            'blue_third',
            'red_first',
            'red_second',
            'red_third',
            'map_type',
            'map_name',
        ]
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'user_id',
            'username',
            'password',
            'player_id',
        ]