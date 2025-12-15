from django.urls import path
from . import views

# hier voeg ik een pad toe aan men views zodat ik ze kan opvragen en doen werken
urlpatterns = [
    path("admin/gebruikers/", views.all_users),
    path("admin/gebruikers/<int:id>", views.one_user),
    path("admin/gebruikertoevoegen", views.add_user),
]