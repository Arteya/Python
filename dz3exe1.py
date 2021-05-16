#Эти решения не мои. Они после разборов дз другого преподователя.
#Если возможно, то разбирайте на лекциях задания без звездочек тоже.

numerals = {"one": "один",
         "two": "два",
         "three": "три",
         "four": "четыре",
         "five": "пять",
         "six": "шесть",
         "seven": "семь",
         "eight": "восемь",
         "nine": "девять",
         "ten": "десять"}


def num_translate(key):
    if key in numerals:
        return numerals[key]
    else:
       return None


print(num_translate('nine'))



