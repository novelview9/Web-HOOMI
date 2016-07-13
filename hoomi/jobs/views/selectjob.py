from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class SelectJob(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        return render(
                request,
                "jobs/selectjob.html",
                context={}
        )

    def post(self, request, *args, **kwargs):

        value = request.POST.get("jobtitle")
        request.user.job_id = int(value)
        request.user.save()
        return redirect("jobs:job_history")
