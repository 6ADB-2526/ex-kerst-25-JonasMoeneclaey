from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.forms import model_to_dict
from django.http import JsonResponse
from .models import User
import json
# Create your views here.
# met deze functie kun je alle gebruikers opvragen
def all_users(req):
    gebruiker = User.objects.all()
    return JsonResponse(list(gebruiker), safe=False)

# met deze functie kun je 1 gebruiker opvragen
def one_user(req, id):
    gebruiker = User.objects.get(id)
    return JsonResponse(model_to_dict(gebruiker))

# met deze functie kun je een gebruiker toevoegen
@csrf_exempt
def add_user(req):
    post_data =  json.loads(req.body.decode('utf-8'))
    new_gebruiker = User.objects.create()
    new_gebruiker.login = post_data["login"]
    new_gebruiker.password = post_data["password"]
    new_gebruiker.email = post_data["email"]
    new_gebruiker.role = post_data["role"]
    new_gebruiker.isSuperuser = post_data["isSuperuser"]
    new_gebruiker.save()
    return JsonResponse(model_to_dict(new_gebruiker))