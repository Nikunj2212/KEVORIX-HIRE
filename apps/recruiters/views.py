from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CompanyForm,RecruiterForm
from .models import Company, Recruiter
from apps.accounts.decorators import recruiter_required


    
@recruiter_required
def dashboard(request):

    recruiter = Recruiter.objects.select_related(
        "company"
    ).filter(
        user=request.user
    ).first()

    if recruiter is None:
        return redirect("recruiters:create_company")

    company = recruiter.company

    context = {

        "recruiter": recruiter,

        "company": company,

        "total_jobs": 0,

        "active_jobs": 0,

        "total_applicants": 0,

        "scheduled_interviews": 0,

    }

    return render(
        request,
        "recruiters/dashboard.html",
        context,
    )


@login_required(login_url="accounts:login")
def create_company(request):

    recruiter = Recruiter.objects.filter(
        user=request.user
    ).first()

    if recruiter:
        return redirect("recruiters:dashboard")

    if request.method == "POST":

        company_form = CompanyForm(
            request.POST,
            request.FILES,
        )

        recruiter_form = RecruiterForm(
            request.POST,
            request.FILES,
        )

        if company_form.is_valid() and recruiter_form.is_valid():

            company = company_form.save()

            recruiter = recruiter_form.save(commit=False)

            recruiter.user = request.user
            recruiter.company = company
            recruiter.is_primary = True
            recruiter.is_admin = True

            recruiter.save()

            messages.success(
                request,
                "Company created successfully."
            )

            return redirect("recruiters:dashboard")
        
    else:

        company_form = CompanyForm()

        recruiter_form = RecruiterForm()

    context = {

    "company_form": company_form,

    "recruiter_form": recruiter_form,

    }

    return render(
        request,
        "recruiters/create-company.html",
        context,
    )


@login_required(login_url="accounts:login")
def edit_company(request):

    recruiter = Recruiter.objects.filter(
        user=request.user
    ).select_related("company").first()

    if recruiter is None:
        return redirect("recruiters:create_company")

    company = recruiter.company

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            request.FILES,
            instance=company,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Company updated successfully."
            )

            return redirect(
                "recruiters:company_profile"
            )

    else:

        form = CompanyForm(instance=company)

    return render(
        request,
        "recruiters/edit-company.html",
        {
            "form": form,
            "company": company,
        },
    )


@login_required(login_url="accounts:login")
def company_profile(request):

    recruiter = Recruiter.objects.filter(
        user=request.user
    ).select_related("company").first()

    if recruiter is None:
        return redirect("recruiters:create_company")

    return render(
        request,
        "recruiters/company-profile.html",
        {
            "company": recruiter.company,
            "recruiter": recruiter,
        },
    )