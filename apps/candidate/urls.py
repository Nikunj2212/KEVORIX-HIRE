from django.urls import path

from . import views

app_name = "candidate"

urlpatterns = [

    path("dashboard/", views.dashboard,name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/",views.edit_profile,name="edit_profile"),
    path("profile/personal-information/",views.personal_edit,name="personal_edit"),

]