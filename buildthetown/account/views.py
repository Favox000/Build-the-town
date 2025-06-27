from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.utils.timezone import now
from django.utils.timezone import now
from datetime import date

def index(request):
    return render(request, "account/index.html")

class MyLoginView(LoginView):
    def form_valid(self, form):
        # Přihlášení proběhlo úspěšně
        user = form.get_user()
        
        # 🔧 Zde spustíš svou funkci
        self.after_login(user)

        return super().form_valid(form)

    def after_login(self, user):
        today = now().date()
        last_login = user.last_login

        if last_login.date() != today:
            profile = getattr(user, 'profile', None)
            if profile is None:
                profile = Profile.objects.create(user=user)
            profile.money += profile.earn
            profile.save()

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
         
    return render(request, "account/register.html", {
        'form': form
    })

def account_of_person(request, slug):
    user = get_object_or_404(User, username=slug)
    profile = getattr(user, 'profile', None)

    if request.method == 'POST':
        if profile is None:
            # pokud profil neexistuje, vytvoř ho
            profile = Profile.objects.create(user=user)
        # Uprav profil uživatele, kterého zobrazujeme (ne přihlášeného)
        profile.content = request.POST.get('message')
        profile.save()

    return render(request, "account/profile.html", {
        "name": user.username,
        "profile": profile,
        "content": profile.content if profile else "",
    })

def ranking(request):
    users = Profile.objects.all().order_by('-points')


    return render(request, "account/ranking.html", {
            "users":users
        })

def codes(request):
    if request.method == 'POST':
        code_name = request.POST.get('code_name')
        print(code_name)
        try:
            code = Codes.objects.get(name=code_name)
            profile = request.user.profile

            if request.user in code.used_by.all():
                messages.error(request, "Chyba: Kód jste již použil(a).")
            else:
                # Přidání bodů, peněz, tiketů a výdělku
                profile.points += code.add_points
                profile.money += code.add_money
                profile.golden_tickets += code.add_golden_tickets
                profile.earn += code.add_earn

                # Uložení profilu
                profile.save()

                # Přidání uživatele do seznamu použitých kódů
                code.used_by.add(request.user)

                # Zobrazit zprávu, pokud existuje
                messages.success(request, code.message)

        except Codes.DoesNotExist:
            messages.error(request, "Chyba: Kód neexistuje.")

    return render(request, "account/codes.html")

def news(request):
    game_starts = now().date() #game_starts = date(2025, 6, 25)
    today = now().date()
    day_passed = ((game_starts - today).days ) + 1
    day = Days.objects.get(day_number=day_passed)
    profile = request.user.profile

    if day.type_of_quiz == "quiz":
        name_quiz = "Kvíz"
        any_quiz = Quiz.objects.get(day_number=day_passed)
        if request.method == "POST":
            user_answer = request.POST.get("answer")
            if user_answer == any_quiz.answer_quiz:
                messages.success(request, "Správná odpověď! Body byly přidány.")
                profile.points += any_quiz.points
                profile.has_quiz = True
                profile.save()
            else:
                messages.error(request, "Špatná odpověď. Zkus to znovu.")

    elif day.type_of_quiz == "room":
        name_quiz = "Místnost"
        current_room_index = profile.room_index 

        if profile.room_index >= 3:
            messages.success(request, "Gratulujeme! Dokončil(a) jsi všechny místnost.")
            any_quiz = None
        else:

            room = Room.objects.get(day_number=day_passed, room_number=current_room_index)

            if request.method == "POST" and room:
                user_answer = request.POST.get("room_answer")
                # Zpracuj odpověď uživatele (volitelně)
                room.user_answer = user_answer
                room.save()
                # Posuň uživatele do další místnosti
                profile.room_index = current_room_index + 1
                profile.save()
                # Načti další místnost
                room = Room.objects.get(day_number=day_passed, room_number=profile.room_index)

            any_quiz = room

    elif day.type_of_quiz == "work_with_text":
        name_quiz = "Práce s textem"
        any_quiz = Work_with_text.objects.get(day_number=day_passed)

    elif (day.type_of_quiz == "serche") or (day.type_of_quiz ==  "example"):
        if day.type_of_quiz == "serche":
            name_quiz = "Pátračka"
        else:
            name_quiz = "Příklad"
        any_quiz = Small_answer.objects.get(day_number=day_passed)

    elif day.type_of_quiz == "story":
        name_quiz = "Příběh"
        any_quiz = Story.objects.get(day_number=day_passed)

    return render(request, "account/news.html", {
        'day': day,
        'any_quiz': any_quiz,
        'name_quiz': name_quiz,
        'day_passed': day_passed,
        "has_quiz": profile.has_quiz,
    })