src = [2,2,2,7,23,1,44,44,3,2,10,7,4,11]

seen=set()
without_repetition = []

for number in src:
    if (number in seen) and (number in without_repetition):
        without_repetition.remove(number)
    else:
        without_repetition.append(number)
    seen.add(number)

print(without_repetition)