# app.py
from flask import Flask, render_template, flash, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'secret'

PRICE = {
    'common': 50,
    'rare': 150,
    'legendary': 300
}

case_image = {
    "common": "https://cdn-icons-png.flaticon.com/512/17307/17307948.png",
    "rare": "https://cdn-icons-png.flaticon.com/512/4020/4020583.png",
    "legendary": "https://cdn-icons-png.flaticon.com/512/6060/6060831.png"
}

ITEMS = {
    "old_pistol": {"name": "Старий пістолет", "rarity": "common"},
    "leather_jacket": {"name": "Шкіряна куртка", "rarity": "common"},
    "basic_helmet": {"name": "Базовий шолом", "rarity": "common"},
    "tool_kit": {"name": "Набір інструментів", "rarity": "common"},
    "old_car": {"name": "Старий автомобіль", "rarity": "common"},
    "rifle": {"name": "Штурмова гвинтівка", "rarity": "rare"},
    "sport_bike": {"name": "Спортивний мотоцикл", "rarity": "rare"},
    "body_armor": {"name": "Бронежилет", "rarity": "rare"},
    "drone": {"name": "Розвідувальний дрон", "rarity": "rare"},
    "modern_house": {"name": "Сучасний будинок", "rarity": "rare"},
    "golden_rifle": {"name": "Золота гвинтівка", "rarity": "legendary"},
    "supercar": {"name": "Суперкар", "rarity": "legendary"},
    "tank": {"name": "Бойовий танк", "rarity": "legendary"},
    "private_jet": {"name": "Приватний літак", "rarity": "legendary"},
    "luxury_villa": {"name": "Елітна вілла", "rarity": "legendary"}
}

CASES = {
    "common": ["old_pistol", "leather_jacket", "basic_helmet", "tool_kit", "old_car", "old_pistol", "tool_kit", "rifle",
               "golden_rifle"],
    "rare": ["rifle", "sport_bike", "body_armor", "drone", "modern_house", "rifle", "body_armor", "old_pistol",
             "basic_helmet", "supercar"],
    "legendary": ["golden_rifle", "supercar", "tank", "private_jet", "luxury_villa", "supercar", "tank", "rifle",
                  "drone", "old_pistol"]
}

IMAGES = {
    "old_pistol": "https://cdn-icons-png.flaticon.com/512/1320/1320476.png",
    "leather_jacket": "https://cdn-icons-png.flaticon.com/512/16220/16220325.png",
    "basic_helmet": "https://cdn-icons-png.flaticon.com/512/3939/3939624.png",
    "tool_kit": "https://cdn-icons-png.flaticon.com/512/4176/4176717.png",
    "old_car": "https://cdn-icons-png.flaticon.com/512/2569/2569962.png",
    "rifle": "https://cdn-icons-png.flaticon.com/512/7445/7445184.png",
    "sport_bike": "https://cdn-icons-png.flaticon.com/512/3149/3149029.png",
    "body_armor": "https://cdn-icons-png.flaticon.com/512/5258/5258123.png",
    "drone": "https://cdn-icons-png.flaticon.com/512/3294/3294560.png",
    "modern_house": "https://cdn-icons-png.flaticon.com/512/1018/1018675.png",
    "golden_rifle": "https://cdn-icons-png.flaticon.com/512/238/238503.png",
    "supercar": "https://cdn-icons-png.flaticon.com/512/2820/2820613.png",
    "tank": "https://cdn-icons-png.flaticon.com/512/1693/1693487.png",
    "private_jet": "https://cdn-icons-png.flaticon.com/512/3049/3049559.png",
    "luxury_villa": "https://cdn-icons-png.flaticon.com/512/2484/2484009.png"
}


@app.route('/cases')
def cases_page():
    if 'balance' not in session:
        session['balance'] = 1000
    return render_template('cases.html', cases=CASES, price=PRICE, case_image=case_image, items=ITEMS, images=IMAGES,
                           balance=session['balance'])


@app.route('/open/<case_type>')
def open_case(case_type):
    if case_type not in CASES:
        flash('Кейс не знайдено')
        return redirect(url_for('cases_page'))

    if session.get('balance', 0) < PRICE[case_type]:
        flash('Недостаточно коштів')
        return redirect(url_for('cases_page'))

    session['balance'] -= PRICE[case_type]
    item_id = random.choice(CASES[case_type])
    item = ITEMS[item_id]

    flash(f'Отримано: {item["name"]} ({item["rarity"]})')
    return redirect(url_for('cases_page'))


if __name__ == '__main__':
    app.run(debug=True)