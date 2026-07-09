from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CandidateProfile
from .forms import UserForm, CandidateProfileForm



@login_required(login_url="accounts:login")
def dashboard(request):

    return render(request,"candidate/dashboard.html")
    
    

def profile(request):

    profile = CandidateProfile.objects.get(user=request.user)

    context = {

        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/profile.html",
        context
    )
    
    
@login_required
def edit_profile(request):

    profile, created = CandidateProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        user_form = UserForm(
            request.POST,
            instance=request.user
        )

        profile_form = CandidateProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()

            profile_form.save()

            return redirect("candidate:profile")

    else:

        user_form = UserForm(
            instance=request.user
        )

        profile_form = CandidateProfileForm(
            instance=profile
        )

    context = {

        "user_form": user_form,

        "profile_form": profile_form,

        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/edit-profile.html",
        context
    )
    
    
def personal_edit(request):
    return render(request,"candidate/profile/personal-edit.html")