import random

def get_jokes(n, repeat=False):
    jokes=[]
    if not repeat:
        nouns_copy = nouns.copy()
        random.shuffle(nouns_copy)
        adverbs_copy = adverbs.copy()
        random.shuffle(adverds_copy)
        adjectives_copy = adjectives.copy()
        random.shuffle(adjectives_copy)
        for num, (noun, adverb, adjectiv) in enumerate(zip(nouns_copy, adverbs_copy, adjectives_copy), 1):
            jokes.append(f'{noun} {adjectiv} {adverb}')
            if num == n:
                break
    else:
        for _ in range(n):
            jokes.append(f'{random.choice(nouns)} {random.choice(adverds)} {random.choice(adjectives)}')
    return jokes


nouns=["автомобиль", "лес", "огонь", "город", "дом"]
adverds=["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives=["веселый","яркий","зеленый","утопичный","мягкий"]

print(get_jokes(3, repeat=True))
