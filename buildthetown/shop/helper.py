# shop/helpers.py
import random
from django.contrib import messages

# def raise_money():

#     profile.money += profile.earn
#     profile.save()

def upgrade_multiplication(profile, request, multiplication, cost, good):
    if profile.golden_tickets >= cost:
        profile.golden_tickets -= cost
        if good:
          profile.earn = round(profile.earn * multiplication)
          messages.success(request, f"Tvůj příjem je teď {multiplication}x větší")
        else:
            profile.earn = profile.earn / multiplication
            messages.error(request, f"Tvůj příjem je teď {multiplication}x menší")
       
    else:
        messages.error(request, "Nemáš dostatek zlatých tiketů")
    profile.save()

def points(profile, request, points_num, cost):
    if profile.golden_tickets >= cost:
        profile.golden_tickets -= cost
        profile.points += points_num
        messages.success(request, F"Získal jsi {points_num} bodů")
    else:
        messages.error(request, "Nemáš dostatek zlatých tiketů")
    profile.save()

def again_earn(profile, request, cost):
    if profile.golden_tickets >= cost:
        profile.golden_tickets -= cost
        profile.money += profile.earn
        messages.success(request, "Znova příjem")
    else:
        messages.error(request, "Nemáš dostatek zlatých tiketů")
    profile.save()

def buy_golden_ticket(profile, request, cost, tickets):
    if cost == "free":
        profile.golden_tickets += tickets
        messages.success(request, f"Dostal jsi {tickets} zlatý ticket")

    elif profile.money >= cost:
        profile.money -= cost
        profile.golden_tickets += tickets
        messages.success(request, f"Dostal jsi {tickets} zlatý ticket") 
    else:
        messages.error(request, "Nemáš dostatek peněz")

    profile.save()

def get_random_money(profile, request, start_value, end_value, cost):

    if profile.golden_tickets >= cost:
        profile.golden_tickets -= cost
        new_money = random.randint(start_value, end_value)
        profile.money += new_money
        messages.success(request, f"Získal jsi {new_money}")
    else:
        messages.error(request, "Nemáš dostatek zlatých tiketů")

    profile.save()

def get_random_god_thing(profile, request, cost):

    if profile.golden_tickets >= cost:
        profile.golden_tickets -= cost
        choises = [
            lambda:upgrade_multiplication(profile, request, 2, 0, True),
            lambda:upgrade_multiplication(profile, request, 4, 0, True),
            lambda:points(profile, request, 5, 0),
            lambda:again_earn(profile, request, 0),
            lambda: get_random_money(profile, request, 0, 2000, 0),
            lambda: buy_golden_ticket(profile, request, "free", random.randint(1, 5))
        ]
        
        choise=random.choice(choises)
        choise()
    
    else:
        messages.error(request, "Nemáš dostatek zlatých tiketů")

    profile.save()

def get_random_thing(profile, request, cost):
    if profile.golden_tickets >= cost:
        profile.golden_tickets -= cost
        choices = [
            lambda: upgrade_multiplication(profile, request, 2, 0, random.choice([True, False])),
            lambda: upgrade_multiplication(profile, request, 4, 0, random.choice([True, False])),
            lambda: points(profile, request, random.randint(-5, 5), 0),
            lambda: again_earn(profile, request, 0),
            lambda: get_random_money(profile, request, -2000, 2000, 0),
            lambda: buy_golden_ticket(profile, request, "free", random.randint(-5, 5))
        ]
        
        choice = random.choice(choices)
        choice()
    
    else:
        messages.error(request, "Nemáš dostatek zlatých tiketů")

    profile.save()