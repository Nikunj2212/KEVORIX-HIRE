from django.urls import path
from . import views

app_name = "recruiters"

urlpatterns = [

    path("", views.dashboard, name="dashboard"),

    path("company/create/", views.create_company, name="create_company"),

    path("company/edit/", views.edit_company, name="edit_company"),

    path("company/profile/", views.company_profile, name="company_profile"),

]