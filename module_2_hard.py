
# ВАРИАНТ 1: ПЕРВОЕ ЧИСЛО ГЕНЕРИРУЕТСЯ СЛУЧАЙНЫМ ОБРАЗОМ В ДИАПАЗОНЕ 3 -20:

import random

end_num = 21
print(f'Правильные пароли:')

for num_random in range(1, end_num):
   first_num = random.randint(3, 20)
   second_num = str()
   for i in range(1, end_num):
      for j in range(i + 1, end_num):
         if first_num % (i + j) == 0:
            second_num += f'{i}{j}'
   print(f'{first_num} - {second_num}')

print('----------------------------------------------------------------------------------------------------')

# ВАРИАНТ 2: ПЕРВОЕ ЧИСЛО ИДЕТ ПО ПОРЯДКУ В ДИАПАЗОНЕ 3 -20:

end_num = 21
print(f'Правильные пароли:')

for num in range(3, end_num):
   first_num = num
   second_num = str()
   for i in range(1, end_num):
      for j in range(i + 1, end_num):
         if first_num % (i + j) == 0:
            second_num += f'{i}{j}'
   print(f'{first_num} - {second_num}')
