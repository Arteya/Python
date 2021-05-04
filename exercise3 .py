percent = int(input('Ведите число от 0 до 20: '))

while percent >= 21:
    print('Не правильное число')
    percent = int(input('Ведите число от 0 до 20: '))

if percent == 1:
    print(percent, 'процент')
elif 1 < percent < 5:
    print(percent, 'процента')
elif percent >= 5 and percent <= 20 or percent == 0:
    print(percent, 'процентов')
