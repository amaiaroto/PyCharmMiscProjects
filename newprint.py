def exclaim(*text, upper=False, num=1, keep=False, __suffix='!'):
    if not text:
        raise ValueError('text cannot be empty')

    text = [l.replace(__suffix, '' if not keep else __suffix).upper() if upper else l for l in text]
    print(*text, end=f'{__suffix}' * num + '\n')


exclaim(input('i am parrot'))
