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
    # COMMON
    "old_pistol":       {"name": "Старий пістолет",         "rarity": "common"},
    "leather_jacket":   {"name": "Шкіряна куртка",          "rarity": "common"},
    "basic_helmet":     {"name": "Базовий шолом",           "rarity": "common"},
    "tool_kit":         {"name": "Набір інструментів",      "rarity": "common"},
    "old_car":          {"name": "Старий автомобіль",       "rarity": "common"},

    # RARE
    "rifle":            {"name": "Штурмова гвинтівка",      "rarity": "rare"},
    "sport_bike":       {"name": "Спортивний мотоцикл",     "rarity": "rare"},
    "body_armor":       {"name": "Бронежилет",              "rarity": "rare"},
    "drone":            {"name": "Розвідувальний дрон",     "rarity": "rare"},
    "modern_house":     {"name": "Сучасний будинок",        "rarity": "rare"},

    # LEGENDARY
    "golden_rifle":     {"name": "Золота гвинтівка",        "rarity": "legendary"},
    "supercar":         {"name": "Суперкар",                "rarity": "legendary"},
    "tank":             {"name": "Бойовий танк",            "rarity": "legendary"},
    "private_jet":      {"name": "Приватний літак",         "rarity": "legendary"},
    "luxury_villa":     {"name": "Елітна вілла",            "rarity": "legendary"}
}


CASES = {
    "common": [
        # common
        "old_pistol", "leather_jacket", "basic_helmet", "tool_kit", "old_car",
        "old_pistol", "tool_kit",

        # rare
        "rifle",

        # legendary
        "golden_rifle"
    ],

    "rare": [
        # rare
        "rifle", "sport_bike", "body_armor", "drone", "modern_house",
        "rifle", "body_armor",

        # common
        "old_pistol", "basic_helmet",

        # legendary
        "supercar"
    ],

    "legendary": [
        # legendary
        "golden_rifle", "supercar", "tank", "private_jet", "luxury_villa",
        "supercar", "tank",

        # rare
        "rifle", "drone",

        # common
        "old_pistol"
    ]
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