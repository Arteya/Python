seconds = int(input("Введите секунды: "))
if seconds < 3600:
    days = seconds // 86400
    hours = seconds // 3600
    minutes = seconds // 60
    seconds %= 60
    print(days, "Сут.", hours, "Час.", minutes, "Мин.", seconds, "Сек.")
elif seconds >= 3600:
    days = seconds // 86400
    hours = seconds//3600
    minutes = seconds//60
    seconds %= 60
    minutes %= 60
    hours %= 24
    print(days, "Сут.", hours, "Час.", minutes, "Мин.", seconds, "Сек.")
