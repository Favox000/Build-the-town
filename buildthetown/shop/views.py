# shop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Upgrade
from account.models import Profile, Days
# Importujeme pomocné funkce z našeho helpers souboru
from .helper import *
from django.utils.timezone import now

@login_required
def shop_or_upgrades(request, page_type):
    profile = request.user.profile

    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item_type = request.POST.get('item_type')

        if item_type == 'product':
            product = get_object_or_404(Product, id=item_id)
            
            if profile.money >= product.cost:
                profile.money -= product.cost
                profile.earn += product.profit
                profile.save()
                messages.success(request, f"Úspěšně jsi koupil/a budovu '{product.name}'! Tvůj příjem se zvýšil o {product.profit}.")
            else:
                messages.error(request, "Nemáš dostatek peněz na koupi této budovy.")
                        
        elif item_type == 'upgrade':
            upgrade = get_object_or_404(Upgrade, id=item_id)
            

            if upgrade.name == "Náhodný počet peněz od -2 000 do 2 000":
                get_random_money(profile, request, -2000, 2000, upgrade.cost) # je i v get randon (good) thing
                               
            elif upgrade.name == "Náhodná kladná věc":
                get_random_god_thing(profile, request, upgrade.cost)

            elif upgrade.name == "Znova příjem":
                again_earn(profile, request, upgrade.cost)

            elif upgrade.name == "Náhodná věc":
                get_random_thing(profile, request, upgrade.cost)

            elif upgrade.name == "-1 bod pro":
                 messages.error(request, "Není v provozu")

            elif upgrade.name == "5 bodů":
                points(profile, request, 5, upgrade.cost)

            elif upgrade.name == "Čtyřnásobný příjem":
                upgrade_multiplication(profile, request, 4, upgrade.cost, True)
            
            elif upgrade.name == "Zdvojnásobý příjem":
                upgrade_multiplication(profile, request, 2, upgrade.cost, True)

            elif upgrade.name == "1 zlatý ticket":
                game_starts = now().date() #game_starts = date(2025, 6, 25)
                today = now().date()
                day_passed = (game_starts - today).days 
                day = Days.objects.get(day_number=day_passed)
                buy_golden_ticket(profile, request, upgrade.cost, day.golden_ticket_cost)

        return redirect(page_type)

    # --- Logika pro GET požadavky (zobrazení stránky) --- #
    if page_type == 'shop':
        items = Product.objects.all()
    elif page_type == 'upgrade':
        items = Upgrade.objects.all()
    else:
        messages.error(request, f"Neplatný typ stránky.({page_type})") # Opraveno: item_type -> page_type
        return redirect('main_page')

    return render(request, "shop/shop.html", {
        "items": items,
        "profile": profile,
        "page_type": page_type,
    })