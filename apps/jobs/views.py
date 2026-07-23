from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from apps.recruiters.models import Recruiter

from .forms import JobForm
from .models import Job, JobStatus


def create_job(request):

    recruiter = get_object_or_404(
        Recruiter,
        user=request.user,
    )

    if request.method == "POST":

        form = JobForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            job = form.save(commit=False)

            job.company = recruiter.company

            job.recruiter = request.user

            if job.status == JobStatus.PUBLISHED:
                job.published_at = timezone.now()

            job.save()

            form.save_m2m()

            messages.success(
                request,
                "Job created successfully.",
            )

            return redirect(
                "jobs:job_list",
            )

    else:

        form = JobForm()

    context = {

        "form": form,

        "page_title": "Create Job",

    }

    return render(
        request,
        "jobs/create-job.html",
        context,
    )
    
def job_list(request):

    recruiter = get_object_or_404(
        Recruiter,
        user=request.user,
    )

    jobs = Job.objects.filter(
        company=recruiter.company,
    ).order_by(
        "-created_at",
    )

    return render(
        request,
        "jobs/job-list.html",
        {
            "jobs": jobs,
        },
    )
    
def job_detail(
    request,
    pk,
):

    recruiter = get_object_or_404(
        Recruiter,
        user=request.user,
    )

    job = get_object_or_404(
        Job,
        pk=pk,
        company=recruiter.company,
    )

    return render(
        request,
        "jobs/job-detail.html",
        {
            "job": job,
        },
    )
    
def edit_job(
    request,
    pk,
):

    recruiter = get_object_or_404(
        Recruiter,
        user=request.user,
    )

    job = get_object_or_404(
        Job,
        pk=pk,
        company=recruiter.company,
    )

    if request.method == "POST":

        form = JobForm(
            request.POST,
            request.FILES,
            instance=job,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Job updated successfully.",
            )

            return redirect(
                "jobs:job_detail",
                pk=job.pk,
            )

    else:

        form = JobForm(
            instance=job,
        )

    return render(
        request,
        "jobs/edit-job.html",
        {
            "form": form,
            "job": job,
        },
    )
    
def delete_job(
    request,
    pk,
):

    recruiter = get_object_or_404(
        Recruiter,
        user=request.user,
    )

    job = get_object_or_404(
        Job,
        pk=pk,
        company=recruiter.company,
    )

    if request.method == "POST":

        job.delete()

        messages.success(
            request,
            "Job deleted successfully.",
        )

        return redirect(
            "jobs:job_list",
        )

    return render(
        request,
        "jobs/delete-job.html",
        {
            "job": job,
        },
    )