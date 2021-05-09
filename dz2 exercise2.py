list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_1[1] = "05"
list_1[8] = "+05"
list_1.insert(1, '"')
list_1.insert(3, '"')
list_1.insert(5, '"')
list_1.insert(7, '"')
list_1.insert(12, '"')
list_1.insert(14, '"')
print(" ".join(list_1))
