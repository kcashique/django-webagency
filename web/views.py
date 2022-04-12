from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json


def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    return render(request, "web/about-us.html", context)


def startup(request):
    context = {"is_startup": True}
    return render(request, "web/index-startup.html", context)


def contact(request):
    context = {"is_contact": True}
    return render(request, "web/contact.html", context)


def notfound(request):
    context = {"is_notfound": True}
    return render(request, "web/404.html", context)


def projects(request):
    context = {"is_projects": True}
    return render(request, "web/projects.html", context)


def projectdetails(request):
    context = {"is_projectdetails": True}
    return render(request, "web/project-details.html", context)

def servicestwo(request):
    context = {"is_servicestwo": True}
    return render(request, "web/services-2.html", context)

def servicesdetails(request):
    context = {"is_servicesdetails": True}
    return render(request, "web/services-details.html", context)


def blogwithsidebar(request):
    context = {"is_blogwithsidebar": True}
    return render(request, "web/blog-with-sidebar.html", context)


def blogsinglewithsidebar(request):
    context = {"is_blogsinglewithsidebar": True}
    return render(request, "web/blog-single-with-sidebar.html", context)