tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def gen_tuple ():
    for index in range(len(tutors)):
        if index < len(klasses):
            yield tutors[index], klasses[index]
        else:
            yield tutors[index], None

generator = gen_tuple()

print(*generator)

print(next(generator))
