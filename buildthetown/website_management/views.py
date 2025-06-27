from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from account.models import *
from django.contrib.auth.models import User

# Create your views here.
@staff_member_required
def index(request):
    return render(request, "website_management/index.html")

@staff_member_required
def competition(request):
    return render(request, "website_management/competition.html", {
        "days": Days.objects.all(),
        "quizs": Quiz.objects.all(),
        "work_with_texts": Work_with_text.objects.all(),
        "small_answers": Small_answer.objects.all(),
        "stories": Story.objects.all(),
        "rooms": Room.objects.all(),
    })

@staff_member_required
def codes(request):
    return render(request, "website_management/codes.html", {
        "codes": Codes.objects.all()
    })      

def users(request):
    return render(request, "website_management/users.html", {
        "users": User.objects.all(),
        "profiles": Profile.objects.all()
    })