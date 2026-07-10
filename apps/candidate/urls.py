from django.urls import path

from . import views

app_name = "candidate"

urlpatterns = [

    path("dashboard/", views.dashboard,name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/",views.edit_profile,name="edit_profile"),
    path("profile/personal-information/",views.personal_edit,name="personal_edit"),
    path("profile/about/",views.about_edit,name="about_edit"),
    path("profile/education/",views.education,name="education"),
    path("profile/education/add/",views.education_add,name="education_add"),
    path("profile/education/<int:pk>/edit/",views.education_edit,name="education_edit"),
    path("profile/education/<int:pk>/delete/",views.education_delete,name="education_delete"),
    path("profile/experience/add/", views.experience_add, name="experience_add"),
    path("profile/experience/<int:pk>/edit/", views.experience_edit, name="experience_edit"),
    path("profile/experience/<int:pk>/delete/", views.experience_delete, name="experience_delete"),
    path("profile/skill/add/", views.skill_add, name="skill_add"),
    path("profile/skill/<int:pk>/edit/", views.skill_edit, name="skill_edit"),
    path("profile/skill/<int:pk>/delete/", views.skill_delete, name="skill_delete"),
    path("profile/project/add/", views.project_add, name="project_add"),
    path("profile/project/<int:pk>/edit/", views.project_edit, name="project_edit"),
    path("profile/project/<int:pk>/delete/", views.project_delete, name="project_delete"),
    path("profile/certificate/add/", views.certificate_add, name="certificate_add"),
    path("profile/certificate/<int:pk>/edit/", views.certificate_edit, name="certificate_edit"),
    path("profile/certificate/<int:pk>/delete/", views.certificate_delete, name="certificate_delete"),
    path("profile/language/add/", views.language_add, name="language_add"),
    path("profile/language/<int:pk>/edit/", views.language_edit, name="language_edit"),
    path("profile/language/<int:pk>/delete/", views.language_delete, name="language_delete"),
    path("profile/social/add/", views.social_add, name="social_add"),
    path("profile/social/<int:pk>/edit/", views.social_edit, name="social_edit"),
    path("profile/social/<int:pk>/delete/", views.social_delete, name="social_delete"),

]