def thesaurus(names):
    names_dict = {}
    for name in names:
        first_letter=name[0]
        if  names_dict.get(first_letter):
            names_dict[first_letter].apped(name)
        else:
            names_dict.setdefault(first_letter,[name])
    return  names_dict

user = ("Уля","Слава")
print(thesaurus(user))