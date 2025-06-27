from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True, verbose_name="Obsah profilu")
    points = models.IntegerField(default=0, verbose_name="Body")
    money = models.IntegerField(default=1000, verbose_name="Peníze")
    earn = models.IntegerField(default=1, verbose_name="Výdělek")
    golden_tickets = models.IntegerField(default=0, verbose_name="Tikety")
    attempts = models.PositiveIntegerField(default=3, verbose_name="Počet pokusů")
    last_activity_date = models.DateField(auto_now_add=True, verbose_name="Datum Poslední aktivity") 
    room_index = models.PositiveIntegerField(default=1, verbose_name="Číslo aktuální místnosti") 
    tickets_per_day = models.PositiveIntegerField(default=0, verbose_name="Počet nakoupených tiketů") 
    has_quiz = models.BooleanField(default=False, verbose_name="Má kvíz")

    def __str__(self):
        return f"Profil uživatele {self.user.username}" 

class Codes(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kódu")
    used_by = models.ManyToManyField(User, related_name='used_items', blank=True)
    add_points = models.IntegerField(default=0, verbose_name="Kolik přidá bodů")
    add_money = models.IntegerField(default=0, verbose_name="Kolik přidá peněz")
    add_golden_tickets = models.IntegerField(default=0, verbose_name="kolik přidá tiketů") 
    add_earn = models.IntegerField(default=0, verbose_name="Kolik přidá výdělek")
    message = models.TextField(blank=True, null=True, verbose_name="Zpráva co kód vypíše")   

    class Meta:
        verbose_name_plural = "Codes"

    def __str__(self):
        return f"Kód: '{self.name}'" 
    
class Days(models.Model):
    day_number = models.PositiveIntegerField(verbose_name="Číslo dne")
    golden_ticket_cost = models.PositiveIntegerField(verbose_name="Cena tiketu")
    type_of_quiz = models.CharField(max_length=100, verbose_name="Typ kvízu")
    secret_text = models.CharField(max_length=100, verbose_name="Tajný text")#, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Days"

    def __str__(self):
        return f"Den číslo: {self.day_number}"
    
class Quiz(models.Model):
    day_number = models.PositiveIntegerField(verbose_name="Číslo dne")
    text_question = models.CharField(max_length=250, verbose_name="Text otázky")
    choise_1 = models.CharField(max_length=100, verbose_name="Odpověď č.1")
    choise_2 = models.CharField(max_length=100, verbose_name="Odpověď č.2")
    choise_3 = models.CharField(max_length=100, verbose_name="Odpověď č.3")
    answer_quiz = models.CharField(max_length=100, verbose_name="správná odpověď")
    points = models.IntegerField(default=1, verbose_name="Kolik přidá bodů")

class Work_with_text(models.Model):
    day_number = models.PositiveIntegerField(verbose_name="Číslo dne")
    text_question = models.CharField(max_length=250, verbose_name="Text otázky")

class Small_answer(models.Model):
    day_number = models.PositiveIntegerField(verbose_name="Číslo dne")
    text_question = models.CharField(max_length=250, verbose_name="Text otázky")
    answer_quiz = models.CharField(max_length=100, verbose_name="správná odpověď")

class Story(models.Model):
    day_number = models.PositiveIntegerField(verbose_name="Číslo dne")
    text_question = models.TextField(verbose_name="Text příběhu")
    answer_quiz = models.CharField(max_length=100, verbose_name="správná odpověď")

class Room(models.Model):
    day_number = models.PositiveIntegerField(verbose_name="Číslo dne")
    room_number = models.PositiveIntegerField(verbose_name="Číslo místnosti")
    question = models.CharField(max_length=250, verbose_name="Otázka")
    right_answer = models.CharField(max_length=100, verbose_name="Správná odpověď na otázku")
    add_points = models.IntegerField(default=0, verbose_name="Kolik přidá bodů")
    add_money = models.IntegerField(default=0, verbose_name="Kolik přidá peněz")
    add_golden_tickets = models.IntegerField(default=0, verbose_name="kolik přidá tiketů") 
    add_earn = models.IntegerField(default=0, verbose_name="Kolik přidá výdělek")
    message = models.TextField(blank=True, null=True, verbose_name="Zpráva co kód vypíše")
    attempts = models.PositiveIntegerField(default=3, verbose_name="Počet pokusů")


    def __str__(self):
        return f"Místnost {self.room_number} - {self.question}"