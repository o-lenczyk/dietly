def calculateMacro(latest_meals_list):
    calories=0
    fat=0
    protein=0
    carbohydrate=0
    dietaryfiber=0
    sugar=0
    salt=0
    saturatedfattyacids=0
    
    for meal in latest_meals_list:
        calories+=meal.calories
        fat+=meal.fat
        protein+=meal.protein
        carbohydrate+=meal.carbohydrate
        dietaryfiber+=meal.dietaryfiber
        sugar+=meal.sugar
        salt+=meal.salt
        saturatedfattyacids+=meal.saturatedfattyacids

    try:
        pfat=(fat/(fat+protein+carbohydrate))*100
    except ZeroDivisionError:
        pfat=0
    try:
        pprotein=(protein/(fat+protein+carbohydrate))*100
    except ZeroDivisionError:
        pprotein=0
    try:
        pcarbohydrate=(carbohydrate/(fat+protein+carbohydrate))*100
    except ZeroDivisionError:
        pcarbohydrate=0

    context = {
        "latest_meals_list": latest_meals_list, 
        "calories": int(calories),
        "fat": int(fat),
        "protein": int(protein),
        "carbohydrate": int(carbohydrate),
        "dietaryfiber": int(dietaryfiber),
        "sugar": int(sugar),
        "salt": int(salt),
        "saturatedfattyacids": int(saturatedfattyacids),
        "pfat": int(pfat),
        "pprotein": int(pprotein),
        "pcarbohydrate": int(pcarbohydrate),
    }

    return context