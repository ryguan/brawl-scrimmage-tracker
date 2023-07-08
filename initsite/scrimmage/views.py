from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import requests
import time
import credentials
from scrimmage.forms import NameForm, RoomForm, UserForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from .models import Room
# Create your views here.

def room_create_view(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RoomForm()
    context = {'form': form}
    return render(request,'scrimmage/create.html', context)
    

def user_create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    context = {'form': form}
    return render(request,'scrimmage/create.html', context)

@api_view(('POST',"GET"))
def search_bar(request):
    
    if request.method=='POST':
        
        form = NameForm(request.POST) 
        
        if request.POST:
            attempt_num = 0
            curr_name = request.POST['your_name']  
            api_key = credentials.api_key
            while attempt_num < 10:
                
                url = "https://api.brawlstars.com/v1/players/%23" + curr_name + "/battlelog"
                
                headers = {'Authorization': 'Bearer {}'.format(api_key)}
                r = requests.get(url, headers=headers,timeout=5)
                if r.status_code == 200:
                    data = r.json()
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    attempt_num += 1
               
                    time.sleep(2)  
            return Response({"error": "Request failed"}, status=r.status_code)
        else:
            return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = NameForm()
    
    return render(request,
        'scrimmage/search_bar.html',
        {'form': form}) # pass that form to the template

def index(request):
    return HttpResponse("current index")

#hardcoded example for debugging
@api_view(('GET',))
def external_api_view(request):
    if request.method == "GET":
        attempt_num = 0  
        api_key = credentials.api_key
        while attempt_num < 10:
            url = "https://api.brawlstars.com/v1/players/%23GCRG22QJ/battlelog"
            print(url)
            headers = {'Authorization': 'Bearer {}'.format(api_key)}
            r = requests.get(url, headers=headers,timeout=5)
            if r.status_code == 200:
                data = r.json()
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
               
                time.sleep(2)  
        return Response({"error": "Request failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)


