from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CandidateProfile
from .forms import UserForm, CandidateProfileForm
from .forms import UserForm,CandidateProfileForm,PersonalInformationForm
from django.contrib import messages
from django.db import transaction
from .forms import UserForm,CandidateProfileForm,PersonalInformationForm,AboutForm
from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserForm,CandidateProfileForm,PersonalInformationForm,AboutForm,EducationForm
from .models import *
from .models import CandidateProfile, Education, Experience
from .forms import UserForm, CandidateProfileForm, PersonalInformationForm, AboutForm, EducationForm, ExperienceForm
from .models import CandidateProfile, Education, Experience, Skill
from .forms import UserForm, CandidateProfileForm, PersonalInformationForm, AboutForm, EducationForm, ExperienceForm, SkillForm
from .models import CandidateProfile, Education, Experience, Skill, Project
from .forms import UserForm, CandidateProfileForm, PersonalInformationForm, AboutForm, EducationForm, ExperienceForm, SkillForm, ProjectForm
from django.urls import reverse
from .models import CandidateProfile, Education, Experience, Skill, Project, Certificate
from .forms import UserForm, CandidateProfileForm, PersonalInformationForm, AboutForm, EducationForm, ExperienceForm, SkillForm, ProjectForm, CertificateForm
from .models import CandidateProfile, Education, Experience, Skill, Project, Certificate, Language
from .forms import UserForm, CandidateProfileForm, PersonalInformationForm, AboutForm, EducationForm, ExperienceForm, SkillForm, ProjectForm, CertificateForm, LanguageForm
from .models import CandidateProfile, Education, Experience, Skill, Project, Certificate, Language, SocialLink
from .forms import UserForm, CandidateProfileForm, PersonalInformationForm, AboutForm, EducationForm, ExperienceForm, SkillForm, ProjectForm, CertificateForm, LanguageForm, SocialLinkForm



@login_required(login_url="accounts:login")
def dashboard(request):

    return render(request,"candidate/dashboard.html")
    
    

@login_required(login_url="accounts:login")
def profile(request):

    profile = CandidateProfile.objects.get(user=request.user)

    educations = profile.educations.all()
    
    experiences = profile.experiences.all()
    
    skills = profile.skills.all()
    
    projects = profile.projects.all()
    
    certificates = profile.certificates.all()
    languages = profile.languages.all()
    social_links = SocialLink.objects.filter(profile=profile).first()

    context = {

        "profile": profile,
        "educations": educations,
        "experiences": experiences,
        "skills": skills,
        "projects": projects,
        "certificates": certificates,
        "languages": languages,
        "social_links": social_links,
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

            return redirect(f"{reverse('candidate:profile')}#profile")

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
    
    
@login_required(login_url="accounts:login")
def personal_edit(request):

    profile, created = CandidateProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = PersonalInformationForm(
            request.POST,
            instance=profile,
            user=request.user,
        )

        if form.is_valid():

            with transaction.atomic():

                form.save()

            messages.success(
                request,
                "Personal information updated successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#personal")

        else:

            messages.error(
                request,
                "Please correct the errors below."
            )

    else:

        form = PersonalInformationForm(
            instance=profile,
            user=request.user,
        )

    context = {

        "form": form,

        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/personal-edit.html",
        context,
    )
    
@login_required(login_url="accounts:login")
def about_edit(request):

    profile, created = CandidateProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = AboutForm(
            request.POST,
            instance=profile,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "About information updated successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#about")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = AboutForm(
            instance=profile,
        )

    context = {

        "form": form,

        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/about-edit.html",
        context,
    )
    

@login_required(login_url="accounts:login")
def education(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user,
    )

    educations = profile.educations.all()

    context = {

        "profile": profile,

        "educations": educations,

    }

    return render(
        request,
        "candidate/profile/education.html",
        context,
    )
    
@login_required(login_url="accounts:login")
def education_add(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user,
    )

    if request.method == "POST":

        form = EducationForm(request.POST)

        if form.is_valid():

            education = form.save(commit=False)

            education.profile = profile

            education.save()

            messages.success(
                request,
                "Education added successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#education")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = EducationForm()

    context = {

        "form": form,

        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/education-add.html",
        context,
    )
    
@login_required(login_url="accounts:login")
def education_edit(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user,
    )

    education = get_object_or_404(
        Education,
        pk=pk,
        profile=profile,
    )

    if request.method == "POST":

        form = EducationForm(
            request.POST,
            instance=education,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Education updated successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#education")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = EducationForm(
            instance=education,
        )

    context = {

        "form": form,

        "education": education,

        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/education-edit.html",
        context,
    )
    
@login_required(login_url="accounts:login")
def education_delete(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user,
    )

    education = get_object_or_404(
        Education,
        pk=pk,
        profile=profile,
    )

    if request.method == "POST":

        education.delete()

        messages.success(
            request,
            "Education deleted successfully."
        )

        return redirect(f"{reverse('candidate:profile')}#education")

    return redirect("candidate:education")

@login_required(login_url="accounts:login")
def experience_add(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    if request.method == "POST":

        form = ExperienceForm(request.POST)

        if form.is_valid():

            experience = form.save(commit=False)

            experience.profile = profile

            experience.save()

            messages.success(
                request,
                "Experience added successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#experience")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = ExperienceForm()

    context = {

        "form": form,
        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/experience-add.html",
        context
    )


@login_required(login_url="accounts:login")
def experience_edit(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    experience = get_object_or_404(
        Experience,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        form = ExperienceForm(
            request.POST,
            instance=experience
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Experience updated successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#experience")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = ExperienceForm(
            instance=experience
        )

    context = {

        "form": form,
        "profile": profile,
        "experience": experience,

    }

    return render(
        request,
        "candidate/profile/experience-edit.html",
        context
    )


@login_required(login_url="accounts:login")
def experience_delete(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    experience = get_object_or_404(
        Experience,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        experience.delete()

        messages.success(
            request,
            "Experience deleted successfully."
        )

    return redirect(f"{reverse('candidate:profile')}#experience")


@login_required(login_url="accounts:login")
def skill_add(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    if request.method == "POST":

        form = SkillForm(request.POST)

        if form.is_valid():

            skill = form.save(commit=False)

            skill.profile = profile

            skill.save()

            messages.success(
                request,
                "Skill added successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#skills")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = SkillForm()

    context = {

        "form": form,
        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/skill-add.html",
        context
    )


@login_required(login_url="accounts:login")
def skill_edit(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    skill = get_object_or_404(
        Skill,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        form = SkillForm(
            request.POST,
            instance=skill
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Skill updated successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#skills")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = SkillForm(
            instance=skill
        )

    context = {

        "form": form,
        "profile": profile,
        "skill": skill,

    }

    return render(
        request,
        "candidate/profile/skill-edit.html",
        context
    )


@login_required(login_url="accounts:login")
def skill_delete(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    skill = get_object_or_404(
        Skill,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        skill.delete()

        messages.success(
            request,
            "Skill deleted successfully."
        )

    return redirect(f"{reverse('candidate:profile')}#skills")


@login_required(login_url="accounts:login")
def project_add(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            project = form.save(commit=False)

            project.profile = profile

            project.save()

            messages.success(
                request,
                "Project added successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#projects")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = ProjectForm()

    context = {

        "form": form,
        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/project-add.html",
        context
    )


@login_required(login_url="accounts:login")
def project_edit(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    project = get_object_or_404(
        Project,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        form = ProjectForm(
            request.POST,
            request.FILES,
            instance=project
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Project updated successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#projects")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = ProjectForm(
            instance=project
        )

    context = {

        "form": form,
        "profile": profile,
        "project": project,

    }

    return render(
        request,
        "candidate/profile/project-edit.html",
        context
    )


@login_required(login_url="accounts:login")
def project_delete(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    project = get_object_or_404(
        Project,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        project.delete()

        messages.success(
            request,
            "Project deleted successfully."
        )

    return redirect(f"{reverse('candidate:profile')}#projects")


@login_required(login_url="accounts:login")
def certificate_add(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    if request.method == "POST":

        form = CertificateForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            certificate = form.save(commit=False)

            certificate.profile = profile

            certificate.save()

            messages.success(
                request,
                "Certificate added successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#certificates")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = CertificateForm()

    context = {

        "form": form,
        "profile": profile,

    }

    return render(
        request,
        "candidate/profile/certificate-add.html",
        context
    )


@login_required(login_url="accounts:login")
def certificate_edit(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    certificate = get_object_or_404(
        Certificate,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        form = CertificateForm(
            request.POST,
            request.FILES,
            instance=certificate
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Certificate updated successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#certificates")

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = CertificateForm(
            instance=certificate
        )

    context = {

        "form": form,
        "profile": profile,
        "certificate": certificate,

    }

    return render(
        request,
        "candidate/profile/certificate-edit.html",
        context
    )


@login_required(login_url="accounts:login")
def certificate_delete(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    certificate = get_object_or_404(
        Certificate,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        certificate.delete()

        messages.success(
            request,
            "Certificate deleted successfully."
        )

    return redirect(f"{reverse('candidate:profile')}#certificates")


@login_required(login_url="accounts:login")
def language_add(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    if request.method == "POST":

        form = LanguageForm(request.POST)

        if form.is_valid():

            language = form.save(commit=False)

            language.profile = profile

            language.save()

            messages.success(
                request,
                "Language added successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#languages")

    else:

        form = LanguageForm()

    return render(
        request,
        "candidate/profile/language-add.html",
        {
            "form": form,
            "profile": profile,
        }
    )


@login_required(login_url="accounts:login")
def language_edit(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    language = get_object_or_404(
        Language,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        form = LanguageForm(
            request.POST,
            instance=language
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Language updated successfully."
            )

            return redirect(f"{reverse('candidate:profile')}#languages")

    else:

        form = LanguageForm(instance=language)

    return render(
        request,
        "candidate/profile/language-edit.html",
        {
            "form": form,
            "profile": profile,
            "language": language,
        }
    )


@login_required(login_url="accounts:login")
def language_delete(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    language = get_object_or_404(
        Language,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        language.delete()

        messages.success(
            request,
            "Language deleted successfully."
        )

    return redirect(f"{reverse('candidate:profile')}#languages")



@login_required(login_url="accounts:login")
def social_links(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    social, created = SocialLink.objects.get_or_create(
        profile=profile
    )

    if request.method == "POST":

        form = SocialLinkForm(
            request.POST,
            instance=social
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Social links updated successfully."
            )

            return redirect(
                f"{reverse('candidate:profile')}#social-links"
            )

    else:

        form = SocialLinkForm(
            instance=social
        )

    return render(
        request,
        "candidate/profile/social-links.html",
        {
            "form": form,
            "profile": profile,
        }
    )
    
@login_required(login_url="accounts:login")
def social_add(request):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    social = SocialLink.objects.filter(
        profile=profile
    ).first()

    if social:

        return redirect(
            "candidate:social_edit",
            pk=social.pk
        )

    if request.method == "POST":

        form = SocialLinkForm(request.POST)

        if form.is_valid():

            social = form.save(commit=False)

            social.profile = profile

            social.save()

            messages.success(
                request,
                "Social links added successfully."
            )

            return redirect(
                f"{reverse('candidate:profile')}#social-links"
            )

    else:

        form = SocialLinkForm()

    return render(
        request,
        "candidate/profile/social-add.html",
        {
            "form": form,
            "profile": profile,
        }
    )


@login_required(login_url="accounts:login")
def social_edit(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    social = get_object_or_404(
        SocialLink,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        form = SocialLinkForm(
            request.POST,
            instance=social
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Social links updated successfully."
            )

            return redirect(
                f"{reverse('candidate:profile')}#social-links"
            )

    else:

        form = SocialLinkForm(
            instance=social
        )

    return render(
        request,
        "candidate/profile/social-edit.html",
        {
            "form": form,
            "profile": profile,
            "social": social,
        }
    )


@login_required(login_url="accounts:login")
def social_delete(request, pk):

    profile = get_object_or_404(
        CandidateProfile,
        user=request.user
    )

    social = get_object_or_404(
        SocialLink,
        pk=pk,
        profile=profile
    )

    if request.method == "POST":

        social.delete()

        messages.success(
            request,
            "Social links deleted successfully."
        )

    return redirect(
        f"{reverse('candidate:profile')}#social-links"
    )