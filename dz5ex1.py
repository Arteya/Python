#Первые 2 сделала сама, а 2 другие это Ваше решение. Стараюсь разобраться.

def odd_nums(num):
    for num in range(1,num+1,2):
        yield num

odd_to_15 = odd_nums(15)
print(*odd_to_15)

