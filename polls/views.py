from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# Create your views here.
def index(request):
    return HttpResponse("heyho Minecraftfreunde!!")
