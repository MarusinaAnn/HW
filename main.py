print('\nЗадание 1')
cook_book = []

with open('data.txt', 'r', encoding = 'utf8') as cook_list:
    for line in cook_list:
        dish_name = line.strip()
        ingredients = []
        dish = {dish_name: ingredients}
        ing_count = cook_list.readline()
        for i in range(int(ing_count)):
            ing = cook_list.readline()
            ingredient_name, quantity, measure = ing.split(' | ')
            ingred = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.rstrip('\n')}
            ingredients.append(ingred)
        cook_list.readline()
        cook_book.append(dish)

for n in range(len(cook_book)):
    print(f'{cook_book[n]}\n')

print('\nЗадание 2')
result = {}  
def get_shop_list_by_dishes(dishes, person_count):
    for recipes in cook_book:
        for dish in dishes:
            if dish in recipes.keys():
                for ing in recipes[dish]:
                    dict = {ing['ingredient_name']: {'measure': ing['measure'], 'quantity': person_count*ing['quantity']}}
                    if result.get(ing['ingredient_name']):
                        extra_item = (int(result[ing['ingredient_name']]['quantity']) +
                                  int(result[ing['ingredient_name']]['quantity']))
                        result[ing['ingredient_name']]['quantity'] = extra_item
                    else:
                        result.update(dict)
    print(result)            

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print('\nЗадание 3')



                   
                    
                                    

