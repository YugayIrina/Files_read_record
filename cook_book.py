import json

keys = ['ingridient_name', 'quantity', 'measure', ]
cook_book_dict = {}

with open('recipes.txt') as text:
    # только непустые линии
    lines = []
    for line in text:
        line = line.strip()
        if line:
            lines.append(line)
        continue
    lines = iter(lines)

    # Определяем блюдо и его номер.
    for name in lines:
        cook_book_dict[name] = []
        num = next(lines)
        # Определяем номер линии состава блюда, разбиваем на ингридиенты. Словарь.
        for _ in range(int(num)):
            sostav_line = next(lines)
            ingrid = sostav_line.split(' | ')
            z = zip(keys, ingrid)
            sostav_dict = {k: v for (k, v) in z}
            cook_book_dict[name].append(sostav_dict)
            continue
        continue
print('cook_book =', (json.dumps(cook_book_dict, indent=2, ensure_ascii=False)))
