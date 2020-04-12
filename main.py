


import datetime

class Logger:

  def __init__(self, log_path, encoding='utf-8'):
    self.log_file = open(log_path, 'a', encoding=encoding)

  def __enter__(self):
    return self

  def write_log(self, action):
    self.log_file.write(f'{datetime.datetime.utcnow()}: {action}\n')

  def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is not None:
      self.write_log(f'error: {exc_val}')
    self.write_log("end")
    self.log_file.close()




with open("recipes.txt") as f:
  ingredients = []
  cook_book = {}
  while True:
    dish_name = f.readline().strip()
    if not dish_name:
      break
    number_of_entries = f.readline()
    ingredients = []
    for ingredient in range(int(number_of_entries)):
      ingredients_dict = {}
      ingredient = f.readline().strip().split("|")
      ingredient_name, quantity, measure = ingredient
      ingredients_dict["ingredient_name"] = ingredient_name
      ingredients_dict["quantity"] = quantity
      ingredients_dict["measure"] = measure
      ingredients.append(ingredients_dict)
    cook_book[dish_name] = ingredients
    f.readline()
  # print(cook_book)
  # print()



def get_shop_list_by_dishes(dishes, person_count):
  # print(type(person_count))
  shop_dict = {}
  result_dict = {}
  for dish in dishes:
    # print(dish)
    for (key, value) in cook_book.items():
      if dish == key:
        for entry in value:
          k = (entry["ingredient_name"]).strip()
          l = (entry["measure"]).strip()
          m = int((entry["quantity"]).strip())
          if k in result_dict.keys():
            result_dict[k]["quantity"] =  m * person_count + (result_dict[k]['quantity'])
          else:
            result_dict[k] = {"measure": l, "quantity": m * person_count}
  print(result_dict)
  
if __name__ == "__main__":
  with Logger('my.log') as log:
    log.write_log('Начало работы')
    d_start = datetime.datetime.now()
    print(f'Время запуска кода {d_start}')
    get_shop_list_by_dishes(["Омлет", "Фахитос"], 2)
    log.write_log('Запущена функция вывода словаря для закупки')
    d_end = datetime.datetime.now()
    print(f'Время окончания работы кода {d_end}')
    d_duration = d_end - d_start
    print(f'Время выполнения кода {d_duration}')


