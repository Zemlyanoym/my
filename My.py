"""num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))
print("Сумма чисел: ", num_1 + num_2 + num_3)
print("Произведение чисел: ", num_1 * num_2 * num_3)



num_1 = int(input("Введите зарплату за месяц: "))
num_2 = int(input("Введите сумму месячного платежа по кредиту в банке: "))
num_3 = int(input("Введите задолженность за коммунальные услуги: "))
print("Остаток после всех выплат: ", num_1 - num_2 - num_3)



d_1 = int(input("Введите первую диагональ ромба: "))
d_2 = int(input("Введите вторую диагональ ромба: "))
print("Площадь ромба равна: ", 1/2 * d_1 * d_2)



print("\t\t\t\t\tTo be")
print("\t\t\t\t\tor not")
print("\t\t\t\t\tto be")





print("\t\t\t\"Life is what happens")
print("\t\t\t\twhen")
print("\t\t\t\t\tyou're busy making other plans\"")
print("\t\t\t\t\t\t\t\t\t\t\t\tJohn Lennon")




# Задание 2



num = input("Введите три числа, через запятую: ")
a = num[0] + num[2] + num[4]
print(a)




num = int(input("Введите четырехзначное число: "))
x =[int(a) for a in str(num)]
y = x[0] * x[1] * x[2] * x[3]
print(y)





metr = int(input("Введите длинну в метрах: "))
print("Длинна в сантиметрах:", metr * 100)
print("Длинна в дециметрах :", metr * 10)
print("Длинна в миллиметрах :", metr * 1000)
print("Длинна в милях :", metr / 1609)



a = int(input("Введите длинну основания треугольника: "))
h = int(input("Введите высоту треугольника: "))
print ("Площадь треугольника равна: ", 0.5 * a * h)



num = input("Введите четырехзначное число: ")
num_2 = num[::-1]
print("Перевернутуе число: ", num_2)



# Задание 3

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))
print("Что вы хотите с ними сделать? ")
action = input("Вам доступны: сумма (+), произведение(*): ")
if action == "сумма" or action == "+":
		 print(num_1 + num_2 + num_3)
else:
		print(num_1 * num_2 * num_3)



num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))
print("Что вы хотите с ними сделать? ")
action = input("Вам доступны: максимум из трех чисел , минимум из трех чисел , среднеарифмитическое: ")
if action == "максимум" or action == "max":
		print(max(num_1, num_2, num_3))
elif action == "минимум" or action == "min":
		print(min(num_1, num_2, num_3))
else:
		print((num_1 + num_2 + num_3) / 3)


long_metr = int(input("Введите количество метров: "))
print("В какую единицу измерения вы хотите перевести метры? ")
action = input("Вам доступны: мили, дюймы и ярды: ")
if action == "мили":
		print("Миль: ", long_metr * 0.000621)
elif action == "дюймы":
		print("Дюймов: ", long_metr * 39.3701)
elif action == "ярды":
		print("Ярдов: ", long_metr * 1.094)



start_num = int(input("Введите начало диапазона: "))
end_num = int(input("Введите конец диапазона: "))
for i in range(start_num, end_num + 1):
		if i % 7 == 0:
				print(i)



start_num = int(input("Введите начало диапазона: "))
end_num = int(input("Введите конец диапазона: "))
print("Все числа диапазона: ")
for i in range(start_num, end_num + 1):
					 print(i)
print("Все числа в убывающем порядке: ")
for i in reversed(range(start_num, end_num + 1)):
					 print(i)
print("Все числа кратные 7: ")
for i in range(start_num, end_num + 1):
		if i % 7 == 0:
				print(i)
print("Количество чисел кратных 5: ")
print(len([i for i in range(start_num, end_num + 1) if int(i) % 5 == 0]))



d=[str(i) for i in range(int(input("Введите начало диапазона: ")),int(input("Введите конец диапазона: "))+1)]
print(' '.join(d))
print(' '.join(d[::-1]))
print(' '.join([i for i in d if int(i)%7==0]))
print(len([i for i in d if int(i)%5==0]))



while True:
 start_num = int(input("Введите начало диапазона: "))
 end_num = int(input("Введите конец диапазона: "))
for i in range(start_num, end_num + 1):
	 if i % 3 == 0:
				print("Fizz")
	 elif:
			if i % 5 == 0:
		#for i in range(start_num, end_num + 1):
#    if i % 5 == 0:
			 print("Buzz")
#for i in range(start_num, end_num + 1):
#    if i % 3 == 0:
#        i % 5 == 0
 #       print("FizzBuzz")


for i in range(int(input()), int(input()) + 1): print(
		'Fizz Buzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i)



start_num = int(input("Введите начало диапазона: "))
end_num = int(input("Введите конец диапазона: "))
for i in range(start_num, end_num + 1):
	if i % 3 == 0 and i % 5 == 0:
		print("Fizz Buzz")
	else:
		if i % 3 == 0:
			print("Fizz")
		else:
		 if i % 5 == 0:
				print("Buzz")
		 else:
				 print(i)




x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
print(x ** y)




#print(len([i for i in range(100, 1000) if len(set(str(i))) == 2]))


n = 0
for i in range(100, 1000):
		if len(set(str(i))) < 3:
			 n = n + 1
print(n)


count = 0
for i in range(100, 999):
		num_1, num_2, num_3 = str(i)
		if num_1 != num_2 or num_1 != num_3 or num_2 != num_3:
				count += 1
print(count)


print(9 * 9 * 8 + 9 * 9 * 8 * 7)




print(input("Введите число: ").replace("3", "").replace("6", ""))




count1=0
count2=0
for a in range(100,9999):
		n1=(a//1000)
		n2=(a//100)%10
		n3=(a%100)//10
		n4=a%10
		if a <= 1000:
				(n2!=n3 or n2!=n4 or n3!=n4)
				count1 += 1
		if a >=1000:
				(n1!=n2 or n1!=n3 or n1!=n4 or n2!=n3 or n2!=n4 or n3!=n4)
				count2 += 1
print("Количество разных целых чисел в диапазоне от 100 до 9999:",count1+count2 )




start_num = int(input("Введите начало диапазона: "))
end_num = int(input("Введите конец диапазона: "))
for i in range(start_num, end_num + 1):
		if i % 2 != 0:
				 print(i)



print("Таблица умножения")
i = 1
# print("." * 82)
for i in range(1, 11):
		for j in range(1, 11):
				print(f'{i} * {j} = {i * j}', end="|   ")
		print("  ")
		print("." * 82)




num_1 = int(input("Введите число начала диапазона таблицы умножения: "))
num_2 = int(input("Введите число конца диапазона таблицы умножения: "))
i = 1
for i in range(num_1, num_2 + 1):
		for j in range(1, 11):
				print(f'{i} * {j} = {i * j}', end="|   ")
		print("")
		print("." * 82)



user_string = input("Введите строку, для определения, является ли она полиндромом: ")
if user_string != user_string[::-1]: 
		print("Стока не является полиндромом.")
else:
		print("Стока является полиндромом.")





user_text = input("Введите любой текст: ")
user_word = input("Введите через запятую слова, которые хотите зарезервировать: ".split())
for word in user_word:
			user_text = user_text.replace(word, word.upper)
print(user_text)




text = input()
words = input().split()
for word in words:
	text = text.replace(word, word.upper())
print(text)



user_text = input("Введите любой текст: ")
user_word = input("Введите через пробел слова, которые хотите зарезервировать: ").split()
for word in user_word:
			user_text = user_text.replace(word, word.upper())
print(user_text)






user_text = input("Введите текст, и мы посчитаем сколько в нем предложений: ")
print("Предложений в тексте: ", len([i for i in user_text.split('. ')]))



string = input()
print(eval(string))



import random






list_of_random_numbers = [random.randint(-10, 10) for i in range(10)]
print ("список чисел: " +  str(list_of_random_numbers))
print("максимальное число: ", max(list_of_random_numbers))
print("минимальное число: ", min(list_of_random_numbers))
i = 0
print('кол-во положительных чисел: ', sum(i > 0 for i in list_of_random_numbers))
print('кол-во отрицательных чисел: ', sum(i < 0 for i in list_of_random_numbers))
print('кол-во нулей в списке: ', sum(i == 0 for i in list_of_random_numbers))




user_calc = input("Введите арифметическое выражение. Возможные операции: +, -,*,/: ")
if '+' in user_calc:
		a, b = user_calc.split('+')
		print(int(a) + int(b))
elif '-' in user_calc:
	a, b = user_calc.split('-')
	print(int(a) - int(b))
elif '*' in user_calc:
	a, b = user_calc.split('*')
	print(int(a) * int(b))  
elif '/' in user_calc:
	a, b = user_calc.split('/')
	print(int(a) / int(b)) 





def bill_gates_citat():
	print('\t“Don't compare yourself with anyone in this world…')
	print('\tif you do so, you are insulting yourself.”\n\t\t\t\t\t\t\t\t\t\tBill Gates')


bill_gates_citat()  




def user_even_num():
	start_num = int(input("Введите число начала диапазона: "))
	end_num = int(input("Введите число конца диапазона: "))
	for i in range(start_num, end_num + 1):
		if i % 2 == 0:
				 print(i, end=" ")


user_even_num() 






def min_user_num():
	print("Введите пять чисел через пробел: ")
	user_nums = input().split()
	user_nums = list((map(int, user_nums)))
	print("Минимальное число из пяти: ", min(user_nums))

min_user_num()




import random



list_of_random_numbers = [random.randint(-10, 10) for i in range(10)]
list_of_random_numbers_2 = [random.randint(-10, 10) for i in range(10)]
list_of_random_general = list_of_random_numbers + list_of_random_numbers_2
list_without_repetition = set(list_of_random_general)       #Список содержащий элементы с первого и второго списков без повторений
list_of_general_nums = []              #Список содержащий общие элементы с первого и второго списков
for i in list_of_random_numbers:
	for j in list_of_random_numbers_2:
	 if i == j:
	 	list_of_general_nums.append(i)
	 	break
list_of_uniqum_nums = []	            # проверка списка на уникальные элементы
for i in list_without_repetition:
		 if list_of_random_general.count(i) == 1:
		 	list_of_uniqum_nums.append(i)
		 	
	

print("Список со случайными цифрами №1: ", list_of_random_numbers)
print("Список со случайными цифрами №2: ", list_of_random_numbers_2)
print("Общий список содержащий элементы с первого и второго списков: ", list_of_random_general)
print("Список содержащий элементы с первого и второго списков без повторений: ", list_without_repetition)
print("Список содержащий общие элементы с первого и второго списков: ", list_of_general_nums)
print("Список содержащий уникальные элементы с первого и второго списков: ", list_of_uniqum_nums)
print("Максимальные и минимальные элементы первого списка: ", max(list_of_random_numbers), min(list_of_random_numbers))
print("Максимальные и минимальные элементы второго списка: ", max(list_of_random_numbers_2), min(list_of_random_numbers_2))




d = [1, 1, 2, 3, 3, 4, 5]  # проверка списка на уникальные элементы
d1 = set(d)
print(d1)
uniq = []
for i in d1:
    if d.count(i) == 1:
        uniq.append(i)
print(uniq)
print(len(uniq))


"""


# user_list = [int(i) for i in input("Введите ряд чисел через пробел: ").split(", ")]
# print(user_list)

# user_list = []
# while True:
# 	user_number = int(input("число: "))
# 	if user_number == 0:
# 		break
# 	user_list.append(user_number)	
# print(user_list)


# a = []  # заводим пустой список
# n = int(input())  # считываем количество элемент в списке
# for i in range(n):  
#     new_element = int(input())  # считываем очередной элемент
#     a.append(new_element)  # добавляем его в список
#     # последние две строки можно было заменить одной:
#     # a.append(int(input()))
# print(a)


# 

# user_nums = list(map(int, input("Введите числа через пробел: ").split()))
# user_list = []
# for i in user_nums:
#       user_list.append(i**2)
# sum_of_element = sum(user_list)      
# #print('user_nums = {}\nuser_list = {}'.format(user_nums, user_list))
# print("Сумма списка элементов возведенных в квадрат: ", sum_of_element)

# lst = list(map(int, input().split()))
# print(lst)



# user_list = []
# числа_больше_нуля = 0
# while True:
#     user_number = int(input("число: "))
#     if user_number == 0:
#         break
#     if user_number > 0:
#         числа_больше_нуля += 1

#     user_list.append(user_number)


# list_2 = sorted(user_list)

# print(user_list)
# user_list.sort()

# print(user_list)



# user_list = []
# while True:
# 	user_number = int(input("число: "))
# 	if user_number == 0:
# 		break
# 	user_list.append(user_number)	
# print(user_list)
# list_2 = sorted(user_list)
# user_list.sort()

# print(user_list)

import tkinter as tk



# def button_cliks():
# 	print("Click!!!")


# label = tk.label(master=root,
# 	      text="Hello world!…"



# 	     )



# button_1 = tk.Button(master=root,
# 	                    #image=user_image,
# 	                    text=".",
# 	                    font=("Arial", 20, "bold"),
# 	                    bg="#f0f0f0",
# 	                    fg="black",
# 	                    padx=50,
# 	                    pady=50,
# 	                    b
# 	                    command=lambda: button_cliks(1))
# button_1.pack()


"""
import tkinter as tk




def is_alive():
	global timer
	global press_return
	if timer <= 0:
		timer = 100
		info_label.configure(text="Бабах!!!!!")

def update_display():
	global timer
	global score
	if timer >= 80:
		bomb_label.configure(image=img_1)
	elif 50 <= timer < 80:
    bomb_label.configure(image=img_2)
	elif 0 <= timer < 50:
    bomb_label.configure(image=img_3)
	else:
		bomb_label.configure(image=img_4)
timer_label.configure()		
	

def update_score():
   pass


def click():
  global timer
  if is_alive()
  timer += 1


def start(event):
  global press_return
  if press_return:
  update_timer()
  update_score()
  update_display()
  info_label.configure(text="")     	

timer = 100





root = tk. Tk()
root.title("Кликер")
root.geometry("600x600")
info_label = tk.Label(root,
	                     text="Нажмите Enter для начала игры.",
	                     font=("Comic Sans MS", 15))
info_label.pack()

info_label = tk.Label(root,
	                    text= "Время: {timer}",
	                    font=("Comic Sans MS", 15))
nfo_label = tk.Label(root,
	                    text= "Очки: {score}",
	                    font=("Comic Sans MS", 15))	 	                    	                       


img_1 = tk.PhotoImage(file=)
img_2 = tk.PhotoImage(file=)
img_3 = tk.PhotoImage(file=)
img_4 = tk.PhotoImage(file=)

bomb_label = tk.Label(image=img_1)
bomb_label.pack()

click_button = tk.Button(root,
	                       text="Нажми на меня!",
	                       bg="red",
	                       fg="black",
	                       width=15,
	                       font=("Comic Sans MS", 15),
	                       command=click
	                       )


click_button.pack()

root.bind("<Return>", start)



root.mainloop()





def horse_path(field, x, y, position):
	  field[x][y] = position
  

  if position >= n * n:
  	for i in field:
  		print(i)
  	print("\n\n\n")
  	field[x][y] = 0

  	return

	for k in range(8):
		newX = x + row[k]
		newY = y + col[k]

	   if (newX < 0 or newX >= n or newY < 0 or newY >= n) is False:
	    	if field[newX][newY] == 0:
	    		horse_path(field, newX, newY, position + 1)

  field[x][y] = 0


n = 5
field = [[0 for x in range(n)]for y in range(n)]
position = 1
print(field)
row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1, 1]

horse_path(field, 0, 0, position)




import random
import time



def bubble_sort(array):
  n = len(array)	
  for step in range(1, n):
      for bubble in range(0, n - step):
        if array[bubble] > array[bubble + 1]:
           array[bubble], array[bubble + 1] = array[bubble + 1], array[bubble] 


  return array
    

def test_sorting():



    random_list = [random.randint(-5, 10) for i in range(10000)]
    start = time.time_ns()
    bubble_sort(random_list)
    print(random_list)
    print("Time bubble sort: ", time.time_ns - start)


test_sorting()    




 def selection_sort():
 	n = len(array)
 	for lowest_item in range(0, n - 1):
 		for position in range(lowest_item - 1, n):
         if array[position] < array[lowest_item]:
         	array[position], array[lowest_item] = array[lowest_item], array[position]

  return array       	





import random


def merge_sort(array):
   if len(array) <= 1:
   	return array

   middle = len(array) // 2
   left_list = merge_sort(array[:middle])
   right_list = merge_sort(array[:middle])
   return merge_lists(left_list, right_list)


def marge_lists(left_list, right_list):
  sorted_list = []
  left_list_index = 0
  right_list_index = 0
  left_list_length = len(left_list)
  right_list_length = len(right_list)


  for i in range(left_list_length + right_list_length):
    if left_list[left_list_index] < right_list[right_list_index]:
      sorted_list.append(left_list[left_list_index])
      left_list_index += 1
    else:
      sorted_list.append(right_list[right_list_index])
      right_list_index += 1 

  if left_list_index == left_list_length:
    sorted_list.extend(right_list[right_list_index:])
    return sorted_list
  elif right_list.index == right_list_length:
    sorted_list.extend(left_list[left_list_index:])
    return sorted_list  



def count_sort(array):
  maximal = max(array)
  minimal = min(array)
  count_list = [0] * (maximal - minimal + 1)
  for i in array:
  	count_list[i] += 1
  sorting_index = 0
  print(count_list)
  for number, count in enumerate(count_list, minimal):
  	print(number, count)
    for i in range(count):
    	array[sorting_index] = number
    	sorting_index += 1

random_list = [random.randint(-5, 10) for i in range(10000)]
count_sort(random_list)  	


"""
# def listsum(numList):
#    if len(numList) == 1:
#         return numList[0]
#    else:
#         return numList[0] + listsum(numList[1:])

# print(listsum([1,3,5,7,9]))



#1

# def product_of_number(array):
# 	multiplication = 1
# 	for i in array:
# 		multiplication = multiplication * i
# 	return multiplication
	
# print(product_of_number([1, 2, 3, 4]))		


#2

# def min_num(array):
#     if not array:
#         return None
#     index = 0
#     for i in range(1, len(array)):
#         if array[i] < array[index]:
#             index = i
#     return array[index]

# print(min_num([1, 2, 3]))    





# def max_num(array):
#     if not array:
#         return None
#     index = 1
#     for i in range(1, len(array)):
#         if array[i] > array[index]:
#             index = i
#     return array[index]


# print(max_num([1, 2, 3]))   

# list_of_random_numbers = [random.randint(-10, 10) for i in range(10)]
# list_of_random_numbers_2 = [random.randint(-10, 10) for i in range(10)]
# list_of_random_general = list_of_random_numbers + list_of_random_numbers_2

# 

# my_list_a = [1, 2, 3]
# my_list_b = [11, 22, 33]

# def list_gen(my_list_a, my_list_b):
#   combined_list = my_list_a + my_list_b
#   new_list = [i for sublist in combined_list for i in sublist]
#   return new_list


# print(list_gen())


# student_estimates = input("Введите оценки студента: ").split()
# print(student_estimates)


# def create_estimates_grade():
# index = 0
# for i in student_estimates:
# 	student_estimates[index] = int(i)
# index += 1
# print(student_estimates)

# def show_estimates():
# for grade in student_estimates:
# 	print(grade, end=" ") 
# else:
#   print()
# print(*student_estimates, sep=", ")          


# def retake(student_estimates, index_grade, new_grade):
# 	student_estimates[index_grade - 1] = new_grade






# def check_scholarships(student_estimates):
# 	print(sum(student_estimates) / len(student_estimates) > 10.7)



# def show_sorted_grades(student_estimates):	
# 	if input("ВВедите +, если хотите ввести оценки по возрастанию, - если по убыванию.") == "+"
# 		student_estimates.sort()
# 		print(student_estimates)
# 	else:
# 		student_estimates.sort()
# 		student_estimates.reserved()
# 		print(student_estimates)

# def create_estimates_table():
# 	index = 0



# create_estimates_table(student_estimates)
# show_estimates(student_estimates)
# retake(student_estimates, 1, 999)
# print(student_estimates)


# panckekes = [3, 5, 1, 2, 4]


# def panckekes_sorting(array):
# 	n = len(array)
# 	last_index = n - 1
# 	while last_index > 0:
# 			current_biggest_index = array.index(max(array[0: last_index + 1]))
# 	  if current_biggest_index == last_index:
# 			 last_index -= 1
# 			 continue

#   	if current_biggest_index != 0:
#   		top_array = array[0: current_biggest_index + 1]
#   		top_array.reverse()
#   		array = top_array + array[current_biggest_index + 1:]
#     	current_biggest_index = 0


# 		if current_biggest_index == 0:
# 			top_array = array[0: last_index + 1]
# 			top_array.reverse()
# 			array = top_array + array[last_index + 1:]


# 	return array		


# sorted_panckekes = panckekes_sorting	

# panckekes_sorting(panckekes)			



# some_numbers = set()
# some_numbers.add(41)
# some_numbers.add(56)
# some_numbers.add(88)
# print(some_numbers)
# some_numbers.update(11, 156)


# some_numbers_2 = {200, 56, 51}
# print(some_numbers_2)


# print("union")
# first_food_set = {"banana", "apple", "orange", 45}
# second_food_set = {"coconut", "pear", "lemon"}
# print(first_food_set.union(second_food_set))
# print(first_food_set | second_food_set)
# print("\n" * 2)



# print("intersection")
# first_food_set = {"banana", "apple", "orange", 45}
# second_food_set = {"coconut", "pear", "lemon", "orange"}
# print(first_food_set.intersection(second_food_set))
# print(first_food_set & second_food_set)
# print("\n" * 2)



# third_food_set = {"poteito", "tomato"}
# print("difference")
# first_food_set = {"banana", "apple", "orange", 45}
# second_food_set = {"coconut", "pear", "lemon"}
# print(first_food_set.difference(second_food_set))
# print(first_food_set - second_food_set)
# print("\n" * 2)


# new_set = {i for i in range(10)}
# new_set = set([i for i in range(10)])
# print(new_set)



# import random

# new_set = {random.randint(0, 1) for i in range(10)}



# fruits = ("banana", "ananas", "apple", "banana", "banana", "banana", "ananas", "apple", "banana", "banana")
# user_choice = input("Какой фрукт хотите посчитать?   ")
# user_fruit = fruits.count(user_choice)  
# count_user_fruits = 0
# for i in fruits:
# 	if i.find(user_choice) != -1: #find метод отнимает от подсчета
# 		count_user_fruits += 1

# print(count_user_fruits)		


# student = {"first_name": "Vasia", "second_name": "Vasin", "age": 20, "weight": 80, "height": 180, "width": 250}
# print(student)
# student["age"] = 90
# print(student)
# height = int(input("Введите новый рост: "))
# student["height"] = height
# print(student)
# student.pop("age")
# print(student)



# new_dictionary = dict.fromkeys(("name", "lastname", 123), 0)
# print(new_dictionary)



# student = {"first_name": "Vasia", "second_name": "Vasin", "age": 20, "weight": 80, "height": 180, "width": 250}
# print(student)

# student_keys = list(student.keys())
# print(student_keys)
# student_values = tuple(student.values())
# print(student_values)
# student_items = list(student.items())

# for key, value in student.items():
# 	print(key, "-", value)



# football_players = {"Massi":{"surname": "messi",
# 										"firstname": "Lionel",
# 										"height": 160
# 										}}
# print(football_players["Messi"]["height"])
# new_player_surname = input("Введите фамилию нового игрока: ")
# new_player_firstname = input("Введите фамилию нового игрока: ")										

# def delete_player():
# 	deketing_player = input("Введите фамилию игрока, которого хотите удалить со списка: ")
# 	if deketing_player in football_players.keys():
# 		football_players.pop(deketing_player)
# 	else:
# 		print("Такого нет.")

# def find_player():
# 	searching_player = input("Кого хотите найти?: ")
# 	user_choice = input("Вывести конкретные данные (нажмите 2)или вывести все (нажмите 1)?: ")
# 	if user_choice == 1:
# 		player = football_players[searching_player]
# 		for key, value in player.items():
# 			print(key, "-", value)
# 	elif user_choice == 2:
# 		for i in player:
# 			print(i)
# 		player_properties = input("Какое свойство хотите узнать?: ")		
# 		print(player[player_properties])

# find_player()			


#1

# first_number_list = ("1", "2", "3", "4", "5")
# second_number_list = ("4", "2", "5", "8", "5")
# third_number_list = ("1", "2", "9", "4", "5")
# repeating_element_in_lists = tuple(set(first_number_list) & set(second_number_list) & set(third_number_list))
# print(repeating_element_in_lists)

#2


# first_number_list = ("1", "2", "3", "4", "5")
# second_number_list = ("4", "2", "5", "8", "5")
# third_number_list = ("1", "2", "9", "4", "5")
# unique_numbers_in_lists = list(set(first_number_list) & set(second_number_list) & set(third_number_list))
# print(unique_numbers_in_lists)


# Множества


#1

# country_set = {"Russia", "China", "Germany", "Italy", "Spain"}
# def add_country():
#     new_counry_in_list = input("Введите новую строну, которую хотите добавить: ")
#     country_set.add(new_counry_in_list)

# add_country()
# print(country_set)


# def delete_counry():
#     deleting_country = input("Введите страну, которую хотите удалить: ")
#     if deleting_country in country_set.pop():
#         country_set.discard(deleting_country)
#     else:
#         print("Такой страны нет в словаре.")

# delete_counry()
# print(country_set)


# def verification_country():
# 	verification_country_in_list = input("Введите название страны для проверки есть ли она в списке: ")
# 	if verification_country_in_list in country_set:
# 		print("Есть в списке.")
# 	else:
# 	  print("Нет в списке.")	


# verification_country()


# 2


# first_city_set = {"London", "Parish", "Boston"}
# second_city_set = {"Moscow", "St.Petersburg", "Samara"}
# third_city_set = first_city_set | second_city_set
# print(third_city_set)




football_players = {"Messi": {
                            "surname": "Messi",
                            "firstname": "Lionel",
                            "height": 160
                            },
                    "Ronaldo": {
                            "surname": "Ronaldo",
                            "firstname": "Cristiano",
                            "height": 185
                            }
                    }


# def add_player():
#     new_character_surname = input("Введите фамилию нового спортсмена: ")
#     new_character_firstname = input("Введите имя данного спортсмена: ")
#     new_character_height = int(input("Введите рост данного спортсмена: "))
#     football_players[new_character_surname] = {"surname": new_character_surname,
#                                                "firstname": new_character_firstname,
#                                                "height": new_character_height}


# def delete_player():
#     deleting_player = input("Введите фамилию игрока, которого хотите удалить: ")
#     if deleting_player in football_players.keys():
#         football_players.pop(deleting_player)
#     else:
#         print("Такого игрока нет в словаре.")


# def find_player():
#     searched_player = input("Кого хотите найти? ")
#     if searched_player not in football_players.keys():
#         print("Такого игрока нет в словаре!")
#         return
#     user_choice = input("Вывести все данные - (введите 1) или только конкретные?(введите 2) ")
#     player = football_players[searched_player]
#     if user_choice == "1":
#         for key, value in player.items():
#             print(key, " - ", value)
#     elif user_choice == "2":
#         for i in player.keys():
#             print(i)
#         player_properties = input("Какое свойство хотите узнать? ")
#         print(player[player_properties])


# def remove_plaers():
# 	rem_players = input("Введите фамилию игрока, которого хотите заменить: ")
# 	rem_new_player = input("Введите фамилию игрока, на которую хотите заменить: ")
# 	if rem_players in football_players.keys():
#   		football_players.remove(rem_new_players)
# 	else:
#   		print("Такого игрока нет в словаре.")

# remove_plaers()

	# def delete_player():
#     deleting_player = input("Введите фамилию игрока, которого хотите удалить: ")
#     if deleting_player in football_players.keys():
#         football_players.pop(deleting_player)
#     else:
#         print("Такого игрока нет в словаре.")



# find_player()
# delete_player()
# add_player()

# print(football_players)



# Словари

#1


# dictionary_eng_fr = {
# 							  'black': 'noire',
# 							  'cat': 'chat',
# 							  'mouse': 'souris'
# 								}
 
# def add_dictionary():
#     new_word_eng = input("Введите новое слово на английском языке: ")
#     new_word_fr = input("Введите перевод слова на французком: ")
#     dictionary_eng_fr[new_word_eng] = new_word_fr

# add_dictionary()
# print(dictionary_eng_fr)

# def delete_word():
# 	deleting_word = input("Введите слово, которое хотите удалить: ")
# 	if deleting_word in dictionary_eng_fr.keys():
# 		dictionary_eng_fr.pop(deleting_word)
# 	else:
#   		print("Такого слова нет.")

# delete_word()
# print(dictionary_eng_fr)

# def search_word():
# 	searched_word = input("Какое слово хотите найти?: ")


# def eng():
#   eng_words=dict([[v, k] for k,v in dictionary_eng_fr.items()])
#   find_word=input('Введите слово на французком языке: ' '')
#   print(eng_words.get(find_word) or print('Слово не найдено.'))

# def rus():
#   key=input('Введите слово: ' '')
#   print (dictionary_eng_fr.get(key) or 'Искомое слово не найдено')

# if __name__ == '__main__':
#     x=input('Найти перевод английского слова? ' '')
#     if x == 'да':
#         rus()
#     elif x == 'нет':
#         eng()
#     else:
#         print('Увидимся позже')
	  






# words={'word': 'мир',\
#     'earth':'земля',\
#     'you': 'ты',\
#     'I':'я',\
#     'We':'мы',\
#     'probably':'вероятно',\
#     'piece':'кусок',\
#     'tired':'усталый',\
#     'should':'должен',\
#     'be able':'быть в состоянии',\
#     'not enough':'не хватает',\
#     'enough':'достаточно',\
#     'should':'должен',\
#     'represent':'представлять',\
#     'sequence':'последовательность'}	   

# def eng():
#     eng_words=dict([[v, k] for k,v in words.items()])
#     find_word=input('Enter word ' '')
#     print(eng_words.get(find_word) or print('No such key'))

# def rus():
#     key=input('Введите слово ' '')
#     print (words.get(key) or 'Искомое слово не найдено')

# if __name__ == '__main__':
#     x=input('Найти перевод английского слова? ' '')
#     if x == 'y':
#         rus()
#     elif x == 'n':
#         eng()
#     else:
#         print('Увидимся позже')




# def add_capital():
# 	new_country = input("Название страны: ")
# 	if new_country in capitals:
# 		print("Такая страна и столица уже существует.")
# 		return
# 	capitals[new_country] = input("Столица: ").title( )	

# def seach_capital():
# 	looking_for = input("У какой страны ")


# def delete_capital():
# 	deleting_country = input("Какую страну хотите удалить? ")
# 	if deleting_country not in capitals:
# 		print("Такой страны нет с словаре.")
# 		return


# def replace_capital():
# 	countries_capital_replace = input("У какой страны заменить сталицу?")
# 	if countries_capital_replace not in capitals:
# 		print("Такой страны нет в словаре.")


# def change_capitals():
# 	countries_capital_chenge = input("У какой страны заменить сталицу?")
# 	if looking_for not in capitals:
# 		print("Такой страны нет в словаре.")
# 		return
# 	print(f"Столица страны {looking_for} - {capitals[looking_for	]}")	


# capitals = {}


# while True:
# print("\n" * 10)	
# print("Вы можете добавить(1), удалить (2), найти (3) и заменить:")
# print("Для выхода введите 0.")
# while True:
# 	user_choice = int(input("Введите цифру соответствующую команде: "))
# 	if user_choice not in ("0", "1", "2", "3", "4", "5")
# 		print("Некорректная команда. Введите от 0 до 5.")
# 		continue
# 	user_choice = int(user_choice)	
		
# match user_choice:
# 	case 0:
# 		break
# 	case 1:	
# 			add_capital()
# 	case 2:	
# 			delete_capital()
# 	case 3:	
# 			seach_capital()
# 	case 4:
				
# 	case 5:		



# def show_capitals():
# 	for country, capital in capitals:


# def calculate_hash(x):
# 	k = 0
# 	i = 136558
# 	j = 1
# 	while x > 0:
# 		k += x % 2 * 5 ** 3
# 		j += 1
# 		x = x // i + j - k


# 	return x + i

# x = 55
# print(calculate_hash)		

# print(ord("f"))


# def func_map(i):
# 	return i * i

# array = [4, 8, 55]
# print(list(map(func_map, array)))	



# new_array = [4, 8, 55]
# for i in array:
# 	new_array.append(i * i)
# print(new_array)


# print(list(map(lambda x: x * x, array)))



# array = [123, 54, 33]
# names = ["asd", "zxc", "pep"]
# c = zip(array, names)
# print(dict(c))


# def filter_func(i):
# 	return i > 0


# array = [123, 54, 62, 2, 12, 54, 6, -12]
# print(list(filter(filter_func, array)))	






# date_base_users = {}

# def add_new_user():
# 	user_login = input("New login: ")
# 	if user_login in date_base_users:
# 		print("Уже есть в базе.")

#   date_base_users[user_login] = hash(input("Password: "))


# def check_logi_password():
# 	user_login = input("Login: ")
# 	if user_login not in date_base_users:
# 		print("Такого нет.")
# 		return
# 	if hash(input("Password: ")) == date_base_users[user_login]:
# 		print("Вы вошли в аккаунт.")


# while True:
# 	add_new_user()
# 	check_logi_password()
# 	print(date_base_users)








"""
В словаре хранится набор пар: Название страны ->
Столица. Нужно реализовать функциональность по добавлению, 
удалению, поиску и замене.
"""

# def add_capital():
#     new_country = input("Название страны: ").strip().title()
#     if new_country in capitals:
#         print("Такая страна и столица уже существуют! ")
#         return
#     capitals[new_country] = input("Столица: ").title()


# def delete_capital():
#     deleting_country = input("Какую страну удалить? ").title()
#     if deleting_country not in capitals:
#         print("Такой страны нет в словаре! ")
#         return
#     capitals.pop(deleting_country)


# def search_capital():
#     looking_for = input("У какой страны хотите узнать столицу? ").strip().title()
#     if looking_for not in capitals:
#         print("Такой страны нет в словаре! ")
#         return
#     print(f"Столица страны {looking_for} - {capitals[looking_for]}")


# def change_capital():
#     countries_capital_change = input("У какой страны нужно заменить столицу? ")
#     if countries_capital_change not in capitals:
#         print("Такой страны нет в словаре! ")
#         return
#     capitals[countries_capital_change] = input("Новая столица: ")


# def show_capitals():
#     for country, capital in capitals.items():
#         print(f"Страна: {country}, столица: {capital}")


# capitals = {}

# while True:
#     print("\n" * 10)
#     print("Вы можете добавить(1), удалить(2), найти(3), заменить(4) и показать(5) пары 'страна-столица'.")
#     print("Для выхода введите 0.")
#     while True:
#         user_choice = input("Введите цифру соответствующую команде: ")
#         if user_choice not in ("0", "1", "2", "3", "4", "5"):
#             print("Некорректная команда! Введите цифру от 0 до 5.")
#             continue
#         user_choice = int(user_choice)
#         break
#     match user_choice:
#         case 0:
#             break
#         case 1:
#             add_capital()
#         case 2:
#             delete_capital()
#         case 3:
#             search_capital()
#         case 4:
#             change_capital()
#         case 5:
#             show_capitals()







"""
Есть кортеж с целыми числами. Нужно вывести статистику 
по количеству цифр в элементах кортежа. Например:
■ Одна цифра — 3 элемента;
■ Две цифры — 4 элемента;
■ Три цифры — 5 элементов.
"""


# random_tuple = (0, -34, 45, 23, 23, 5, 7, 3, 23)
# count_digits = {}
# for i in random_tuple:
#     count = len(str(abs(i))) #   len("34") = 2
#     if count not in count_digits:
#         count_digits[count] = 1
#     else:
#         count_digits[count] += 1

# print(count_digits)











# случайное создание хеш-функции

# def calculate_hash(x):
#     k = 5
#     i = 138
#     j = 1
#     while x > 0:
#         k += x % 2 * i ** 3
#         j += 1
#         x = x // i*i - k

#     return x + i

# x = 55
# print(calculate_hash(x))

# print(calculate_hash(ord("釋")))







"""
функция map применяет указанную функцию в персом аргументе к итерируемомцу объекту во втором аргументе
"""

# def func_map(i):
#     return i * i


# array = [123, 54, 65, 2, 12, 54, 6, 12, -12, 2, -1, 0]
# array_2 = [123, 54, 65, 2, 12, 54, 6, 12, -12, 2, -1, 0]
# print(list(map(func_map, array)))

# print(list(map(lambda x: x * x, array)))

# new_array = []
# for i in array:
#     new_array.append(i * i)
# print(new_array)

# new_array = [i * i for i in array]
# print(new_array)






"""
zip создаёт пары
"""

# array = [123, 54, 65, 2]
# names = ["asd", "zxc", "cvb", "pep"]
# c = zip(array, names)
# print(dict(c))







"""
filter фильтрует по заданной функции и оставляет только те значения, коорые в функции вернули True
"""

# def filter_func(i):
#     return i > 0


# array = [123, 54, 65, 2, 12, 54, 6, 12, -12, 2, -1, 0]
# print(list(filter(filter_func, array)))


# print(all(array))
# print(any(array))











# import functools


# array = [1, 2, 3, 4, 5, 6]
# print(functools.reduce(lambda x, y: x * y, array))








# data_base_users = {}


# def add_new_user():
#     user_login = input("Новый логин: ")
#     if user_login in data_base_users:
#         print("уже есть")

#     data_base_users[user_login] = hash(input("Пароль: "))


# def check_login_password():
#     user_login = input("Логин: ")
#     if user_login not in data_base_users:
#         print("Такого акка нет: ")
#         return
#     if hash(input("Пароль: ")) == data_base_users[user_login]:
#         print("Ура, вы вошли в акк.")
#     else:
#         print("Неправильный логин или пароль. Попробуйте ещё раз.")

# while True:
#     add_new_user()
#     check_login_password()
#     print(data_base_users)










# import hashlib


# print(hashlib.sha512(b"Asd"))


# import os


# sayt = input()

# if 'https://' in sayt:
# 	os.system('start' + sayt)
# 	print('if')
# elif 'www.' in sayt:
# 	sayt = 'https://' + sayt
# 	os.system('start' + sayt)
# 	print('elif')	
# else:
# 	sayt = 'https://www.' + sayt
# 	os.system('start' + sayt)
# 	print('else')			



# x = ''

# while len(x) < 5:
# 	y = input('Введите данные: ')

# 	x += y

# else:
# 	print(x)	


# textfile = open("textfile.txt", "w")			
# textfile.write("Hello world!")			# write написать
# textfile.close()



# import difflib as df


# textfile = open('textfile.txt', 'r', encoding='utf-8')                              # совпадения
# lines1 = set(textfile.read().split())
# textfile.close()
# textfile = open('textfile_2.txt', 'r', encoding='utf-8')
# lines2 = set(textfile.read().split())
# textfile.close()

# # print(lines1)
# # print(lines2)

# print(lines1.intersection(lines2))




#1
# data = [set(open(i).read().split()) for i in ('textfile.txt', 'textfile_2.txt')]
# diff = data[0].difference(data[1])
# if diff:
#     print(diff)
# else:
#     print('Нет различий')



#2
# with open('textfile.txt') as f:
# 	with open('textfile_statistic.txt', 'w', encoding='utf-8') as textfile_statistic:	
# 			res = f.readlines()
# 			f.seek(0)
# 			textfile_statistic = f.read().split()
# 			let = sum(len([y for y in x if y.isalpha()]) for x in textfile_statistic)

# print('В файле содержатся:')
# print(f'{let} букв')
# print(f'{len(textfile_statistic)} слов')
# print(f'{len(res)} строк(и)')




# with open('textfile.txt', 'r') as f:
#     lines = f.readlines()
#     lines = lines[:-1]


# user_symbol = input("Введи символ: ").lower()
# count = 0
# with open("textfile.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         line = line.strip()
#         line = line.split()
#         print(line)
#         for word in line:
#             print(word)
#             if word[0].lower() == user_symbol:
#                 count += 1

# print(count)




# with open('worldcities.csv', 'r', encoding="utf-8") as data_file:
#     with open('Russia_cities.txt', 'w', encoding="utf-8") as russia_cities:
#         maximal_pop = 0
#         minimal_pop = 2000000
#         most_population_city = ''
#         minimal_population_city = ''
#         sum_latitude = 0
#         count_cities = 0
#         sum_longitude = 0
#         for line in data_file:
#             line = line[1: -1]
#             line = line.split('","')

#             if line[4] == 'Russia':
#                 russia_cities.write(','.join(line) + '\n')
#                 if int(line[9]) > maximal_pop:
#                     maximal_pop = int(line[9])
#                     most_population_city = line[1]
#                 if int(line[9]) < minimal_pop:
#                     minimal_pop = int(line[9])
#                     minimal_population_city = line[1]
#                 sum_latitude += float(line[2])
#                 count_cities += 1
#                 sum_longitude += float(line[3])
# print(line)
# print(f'Самый населенный город России: {most_population_city}, его население : {maximal_pop}')
# print(f'Самый пустой город России: {minimal_population_city}, его население : {minimal_pop}')




#3
# text_file = open('textfile.txt')
# practic_2 = open('Практика_2.txt', 'w')
 
# text_file_lines = text_file.readlines()
# text_file_result = text_file_lines[:-1]
 
# for line in text_file_result:
#     practic_2.write(line)
 
# text_file.close()
# practic_2.close()







# text_file = open('textfile.txt', 'r')

# lines = 0
# words = 0
# symbols = 0

# for line in text_file:
#     lines += 1
#     words += len(line.split())
#     symbols += len(line.strip('\n'))

# print("Lines:", lines)
# print("Words:", words)
# print("Symbols:", symbols)
# print()


#4

# with open('textfile.txt', 'r') as file:
# 	print(max(file, key = len))
 


#5

# with open("textfile.txt", "r") as text_file:
#     count_user = 0
#     for line in text_file:
#     	if line.count("он"):     
#       		count_user += 2

# print("Заданное слово встречается - ", count_user, " раз(а)")





# with open("textfile.txt", "r+") as file_in:
#     text = file_in.read()

# text = text.replace("он", "лещь")


# file = open('textfile.txt', 'r+')
# word_old = input('Введите слово, которое хотите заменить: ')
# word_new = input("Введиет слово на которое хотите заменить: ")
# file = file.replace(word_old, word_new)
# file.close()


# with open('textfile.txt', 'r') as file_in:
#     text = file_in.read()
# word_old = input('Введите слово, которое хотите заменить: ')
# word_new = input("Введиет слово на которое хотите заменить: ")
# text = text.replace(word_old, word_new)

# with open("textfile_3.txt", "w") as file_out:
#     file_out.write(text)




# old_file = open("textfile.txt", "r")
# new_file = open("textfile_3.txt", "w")
# word_old = input('Введите слово, которое хотите заменить: ')
# word_new = input("Введиет слово на которое хотите заменить: ")
# for line in old_file:
#     s = line.replace(word_old, word_new)
#     new_file.write(s)
# old_file.close()
# new_file.close()




# cities = {"tokio": [35, 139],			# список городов и их координат по широте и долготе
#           "delhi": [28, 77],	
#           "seul": [37, 126],
#           "sao-paolo": [-23, -46]
#           }



# target_lat = float(input("Введите широту: "))
# target_lng = float(input("Введите долготу: "))
# minimal_distance = 5000
# maximal_distance = -5000
# closest_city = []
# farthest_city = []
# with open("worldcities.csv", "r", encoding="utf-8") as cities_file:
#     cities_file.readline()
#     for line in cities_file:
#         line = line.split('","')
#         # print(line)
#         lat = float(line[2])
#         lng = float(line[3])
#         population = line[9]
#         lat_difference = abs(target_lat - lat)
#         lng_difference = abs(target_lng - lng)
#         coordinate_distance = lat_difference + lng_difference
#         if coordinate_distance < minimal_distance:
#             minimal_distance = coordinate_distance
#             closest_city = [line[1], lat, lng, line[9]]
#             population > 1000000
#         # if population in cities_file:

#         if coordinate_distance > maximal_distance:
#             maximal_distance = coordinate_distance
#             farthest_city = [line[1], lat, lng, line[9]]
# print(closest_city)
# print(farthest_city)
# with open("cities_distance.txt", "w", encoding="utf-8") as file:
#     # 2 способа записи
#     # file.write(f"{closest_city[0]} {str(closest_city[1])} {str(closest_city[2])}\n")
#     # file.write(farthest_city[0] + str(farthest_city[1]) + str(farthest_city[2]) + "\n")

#     # можно преобразовать все данные списка в строки и применить метод .join()
#     closest_city = map(str, closest_city)
#     farthest_city = map(str, farthest_city)
#     file.write(f'Ближайший город: {", ".join(closest_city)}\n')
#     file.write(f'Самый дальний город: {", ".join(farthest_city)}\n')
  


# list_1 = [1, 2, 3, 4, 5]
# list_2 = [6, 7, 8, 9, 0]
# list_3 = [11, 12, 13, 14, 15]
# list_4 = [-3, -5, -9, 16, 20]
# list_all = list_1 + list_2 + list_3 + list_4
# print(list_all)
# user_sort = input('Для сотировки списка по убыванию нажмите "1", по возростанию "2": ')
# # list_all.sort()   #по возрастанию
# # print(list_all)



# while True:
#     print('Для сотировки списка по убыванию нужно нажать "1".')
#     print('Для сотировки списка по возрастанию нужно нажать "2".')
#     user_choice = input("Ваш выбор: ")

#     match user_choice:
#   	    case "1":
#     		    list_all.sort()   #по возрастанию
#     		    print(list_all)
#         case "2":
#       			list_all.sort(reverse= True)
#       			print(list_all)
        


# # list_all.sort(reverse= True)
# # print(list_all)

# def LinearSearch(input_list: list, element: int):
#     list_len = len(input_list)
#     for i in range(list_len):
#         if input_list[i] == element:
#             return i
#     return -1

# user_element = int(input('Введите элемент, который хотите найти в списке: '))
# print("Список: ", list_all)
# position = LinearSearch(list_all, user_element)
# print("Элемент", user_element, " в списке на позиции: ", position)


# import math


# class Fraction:


# 	def __init__(self, numerator=1, denumerator=1):
# 			self.numerator = numerator
# 			self.denumerator = denumerator

# 	def input_data(self, numerator=1, denumerator=1):
# 			self.numerator = numerator
# 			self.denumerator = denumerator

# 	def output_data(self, numerator=1, denumerator=1):
# 			return f"{self.numerator}/{self.denumerator}"

# 	def show_denumerator(self):
# 			return self.denumerator		

# 	def show_numerator(self):
# 			return self.numerator		

# 	def summ_fraction(self, second_number):
# 		  new_denumerator = math.lcm(self.numerator, second_number.denumerator)
# 		  first_numerator = new_denumerator / self.denumerator * self.numerator
# 		  second_numerator = new_denumerator / second_number.denumerator * second_number.numerator
# 		  return f"{int(first_numerator)+int(second_numerator)}/{new_denumerator}"

# 	def multiolication_fraction(self, second_number):
# 			new_numerator = self.numerator * second_number.numerator
# 			new_denumerator = self.denumerator * second_number.denumerator
# 			if new_denumerator % new_numerator == 0:
# 					divider = new_denumerator	/	(new_denumerator % new_numerator)	
# 					return f"{int(new_numerator / divider)}/{int(new_denumerator / divider)}"		

# 			return f"{int(new_numerator)}/{int(new_denumerator)}"			

# number_1 = Fraction(numerator=2, denumerator=3)
# number_2 = Fraction(numerator=1, denumerator=6)
# print(number_1.output_data())
# print(number_1.show_denumerator())	
# print(number_1.show_numerator())
# print(number_1.summ_fraction(number_2))	



# class Country:
# 		country_list = []

		
# 		def __init__(self, country_name=None, country_area=None, country_population=None):
# 				self.country_name = country_name
# 				self.country_area = country_area
# 				self.country_population = country_population
# 				Country.country_list.append(self)


# class City(Country):

# 		def __init__(self, city_name=None, country=None, country_area=None, country_population=None):
# 				self.city_name = city_name
# 				self.country = country
# 				self.city_area = city_area
# 				self.city_population = city_population
# 				if country.country_name == "Great britan":
# 						with open("Britan_cities.txt", "a") as cities_file:
# 								cities_file.write(f"Great britan; {city_name}; {city_population}\n")

# Japan = Country("Japan", 10000, 135_000_000)
# Great_britan = Country("Great britan", 11000, 80_000_000)
# Tokio = City(Japan, "Tokio", 1000, 20_000_000)
# Manchester = City(Great_britan, "Manchester", 500, 3_000_000)
# Liverpool = City(Great_britan, "Liverpool", 600, 2_000_000)
# York = City(Great_britan, "York", 200, 300_000)
# Lids = City(Great_britan, "Lids", 150, 400_000)
# London = City(Great_britan, "London", 1000, 30_000_000)
# print(Tokio.__dict__)
# print(Tokio.country.country_name)
# print(London.country.country_name, London.country.country_population)










# from random import randint

# list_1 = [randint(-10, 10) for i in range(12)]

# for i in range(-10, len(list_1), 8):
# 		if sum(list_1) / len(list_1) in list_1 and i // 8 % 2 == 0:	
#         list_1[i: i + 8] = sorted(list_1[i: i + 8])
#     else: 
#         list_1[i: i + 4] = sorted(list_1[i: i + 4], reverse=True)
# print(list_1)


# from random import randint
 
# def fun(lst, n):
#     return sorted(lst[:n]) + lst[n:][::-1]
# a = [randint(-10,11) for _ in range(11)]
# #a = list(map(int, input().split()))
# m = len(a)
# k = m//3 + (m==0)
# print(a)
# res = fun(a, (1 + (sum(a)/k > 0))*k)
# print(res) 





# class Characters():
# 		id_num = 0
# 		def __init__(self, hp=10, team=None, name=None, role=None):
# 	  	  self.hp = hp
# 	    	self.id = Characters.id_num
# 	    	self.team = team
# 	    	self.name = name
# 	    	self.role = role	


# class King(Characters):
# 		pass


# class Warrior(Characters):
# 		pass


# class Knight(Characters):
# 		pass





# import pygame
# import  sys


# pygame.init()
# fps = 60


# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)

# screen = pygame.display.set_mode((1000, 1000))
# pygame.display.update()
# finished = False
# clock = pygame.time.Clock()

# while not finished:
#     clock.tick(fps)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             finished = True
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 pygame.draw.circle(screen, red, event.pos, 40)
#                 pygame.display.update()
            # if event.button == 3:
            #     pygame.draw.circle(green, red, event.pos, 40)
            #     pygame.display.update()




# def check_braces(data):
# 		stack = []

# 		for symbol in data:
# 			if symbol in ("({["):
# 					stack.append(symbol)
# 			elif symbol in (")]}"):
# 					if len(stack) != 160
# 							left = stack.pop()
# 					if left == "(" and symbol == ")":
# 							continue
# 					else:
# 							return False
# 			if len(stack) != 0
# 					return False
# 			else:
															





# import pygame
# import random





# pygame.init()
# fps = 40

# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Cool game! Братан.")

# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# yellow = (255, 255, 0)
# violet = (255, 0, 255)
# white = (255, 255, 255)

# colors = (red, green, blue, yellow, violet, white)

# pygame.display.update()
# clock = pygame.time.Clock()
# finish = False
# score_font = pygame.font.SysFont("areal", 35)
# score = 0

# def new_position_ball():
# 		global ball_x, ball_y, ball_radius, color, colors
# 		ball_x = random.randint(30, 490)
# 		ball_y = random.randint(30, 490)
# 		ball_radius = random.randint(10, 30)
# 		colors = random.choice(colors)
# 		pygame.draw.circle(screen, colors, (ball_x, ball_y), ball_radius)

# def click(event):
# 		global score
# 		print(event.pos)
# 		if ((ball_x - ball_radius/2) < event.pos[0] < (ball_x + ball_radius)
# 		and (ball_y - ball_radius/2) < event.pos[0] < (ball_y + ball_radius)):
# 				score += 1



# while not finish:
# 		clock.tick(fps)
# 		for event in pygame.event.get():
# 				if event.type == pygame.QUIT:
# 						finish = True
# 						pygame.quit()
# 				# print(event)
# 				if event.type == pygame.MOUSEBUTTONDOWN:
# 						print("Click")
# 						click(event)

# score_show = score_font.render(f"Score:", {score}, True, (0, 200, 150))
# screen.blit(score_show, (10, 10))
# timer_show = timer_font.render(f"Time:", {second}, True (0, 200, 150))
# screen.blit(timer_show, (10, 50))
# new_position_ball()	
# pygame.display.update()
# screen.fill((0, 0, 0))
# time.sleep(1)
# second += 1
# # print(time.time())

# pygame.quit()



# def fun(n):
# 		res = [1]
# 		for i in range(2, int(n** 0.5) + 1):
# 				if n % i == 0:
# 						res.append(i)
# 				if n % 2 == 0:
# 						res.append(n//2)
# 				res.append(n)
# 				return res

# print(fun(36))



# import matplotlib.pyplot as plt
# import numpy as np


# team_results = {}

# with open("results.txt", encoding="utf-8") as football_data_file:
#     football_data_file.readline()
#     for line in football_data_file:
#         line = line.split(",")
#         if line[1] in team_results:
#             team_results[line[1]] += int(line[3])
#         else:
#             team_results[line[1]] = int(line[3])
#         if line[2] in team_results:
#             team_results[line[2]] += int(line[4])
#         else:
#             team_results[line[2]] = int(line[4])


# label = np.array(list(team_results.keys()))
# values = np.array(list(team_results.values()))

# plt.barh(label, values, height=0.1, color="red")
# plt.show()







# import pygame
# import random
# import time


# pygame.init()
# fps = 60
# screen = pygame.display.set_mode([600, 600])
# pygame.display.set_caption("The best game!")

# red = (255, 0, 0)
# green = (0, 255, 0)
# blue = (0, 0, 255)
# yellow = (255, 255, 0)
# violet = (255, 0, 255)
# white = (255, 255, 255)
# colors = (red, green, blue, yellow, violet, white)
# pygame.display.update()
# clock = pygame.time.Clock()
# finished = False
# score_font = pygame.font.SysFont("arial", 35)
# timer_font = pygame.font.SysFont("arial", 35)
# score = 0
# seconds = 0


# def new_position_ball():
#     global ball_x, ball_y, ball_radius, ball_color, colors
#     ball_x = random.randint(30, 570)
#     ball_y = random.randint(30, 570)
#     ball_radius = random.randint(10, 30)
#     ball_color = random.choice(colors)
#     pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)


# def click(event):
#     global score
#     print(event.pos)
#     if ((ball_x - ball_radius) < event.pos[0] < (ball_x + ball_radius)
#         and (ball_y - ball_radius) < event.pos[1] < (ball_y + ball_radius)):
#             score += 1
#             pygame.display.update()
#             screen.fill((0, 0, 0))
#             # print(time.time())


# while not finished:
#     clock.tick(fps)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             finished = True
#             pygame.quit()
#         # print(event)
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # print("Click")
#             click(event)

#     score_show = score_font.render(f"Score: {score}", True, (0, 200, 150))
#     screen.blit(score_show, (10, 10))
#     timer_show = timer_font.render(f"Time: {seconds}", True, (0, 200, 150))
#     screen.blit(timer_show, (10, 50))
#     new_position_ball()
#     pygame.display.update()
#     screen.fill((0, 0, 0))
#     time.sleep(0.75)
#     seconds += 0.75
#     # print(time.time())

# pygame.quit()





# array = [1]
# array.append([2, None])
# array[1][1] = ([3, None])





# class Linkedlist:

# 		limit_count = 4
# 		array_value = {}
# 		def __init__(self):
# 				self.array = None

#     def append(self, value):
#     		if Linkedlist.array_value[self] > Linkedlist.limit_count:
#     				raise "Oversized array!!!" 	
#     		self.array = [value, self.array]

		
# 		def pop(self):
# 				if self.array is None:
# 						raise "This array is emply!"		

# first_array = Linkedlist()
# first_array.pop()
# first_array.append(22) 
# first_array.append(44)   

# def display_array(self):
# 		all_values = []
# 		current_last_item = self.head
# 		while current_last_item.next is not None:
# 				current_last_item = current_last_item.next
# 				all_values.append(current_last_item.value)

# 				return all_values 	







# class Node:

#     def __init__(self, value=None):
#         self.value = value
#         self.next = None


# class SecondLinkedList:

#     def __init__(self):
#         self.head = Node()

#     def append(self, value):
#         new_node = Node(value)
#         current_last_item = self.head
#         while current_last_item.next is not None:
#             current_last_item = current_last_item.next
#         current_last_item.next = new_node

#     def length(self):
#         current_last_item = self.head
#         count = 0
#         while current_last_item.next is not None:
#             current_last_item = current_last_item.next
#             count += 1

#         return count

#     def show_list(self):
#         all_values = []
#         current_last_item = self.head
#         while current_last_item.next is not None:
#             current_last_item = current_last_item.next
#             all_values.append(current_last_item.value)

#         return all_values

#     def print_values(self, mode="new_line", sep=", "):
#         current_last_item = self.head
#         if mode == "new_line":
#             while current_last_item.next is not None:
#                 current_last_item = current_last_item.next
#                 print(current_last_item.value)
#         elif mode == "one_line":
#             while current_last_item.next is not None:
#                 current_last_item = current_last_item.next
#                 print(current_last_item.value, end=sep)
#             else:
#                 deleting_count = len(sep)
#                 print("\b" * deleting_count)
#                 print()

#     def get_value(self, index):
#         if index >= self.length():
#             raise "Index out of range!"

#         current_index = 0
#         current_last_item = self.head
#         while True:
#             current_last_item = current_last_item.next
#             if current_index == index:
#                 return current_last_item.value
#             current_index += 1

#     def delete_item(self, index):
#         if index >= self.length():
#             raise "Index out of range!"
#         if index < 0:
#             raise "Index must bigger than 0"
#         current_index = 0
#         current_last_item = self.head
#         while True:
#             array_tail = current_last_item
#             current_last_item = current_last_item.next
#             if current_index == index:
#                 array_tail.next = current_last_item.next
#                 break
#             current_index += 1

#     def check_value(self, search_value):

#         current_last_item = self.head
#         while current_last_item.next is not None:
#             if current_last_item.value == search_value:
#                 return True
#             current_last_item = current_last_item.next

#         return False

#     def count_value(self, search_value):

#         current_last_item = self.head
#         count = 0
#         while current_last_item.next is not None:
#             if current_last_item.value == search_value:
#                 count += 1
#             current_last_item = current_last_item.next

#         return count

#     def find_index_value(self, search_value):
#         """

#         :param search_value:
#         :return: First index of search_value, else return None
#         """
#         current_last_item = self.head
#         index = 0
#         while current_last_item.next is not None:
#             index += 1
#             if current_last_item.value == search_value:
#                 return index
#             current_last_item = current_last_item.next

#         return None


# second_array = SecondLinkedList()
# second_array.append(22)
# second_array.append(33)
# second_array.append(33)
# second_array.append(44)
# second_array.append(55)
# second_array.append(66)
# print(second_array.length())
# print(second_array.show_list())
# second_array.print_values(mode="one_line", sep=" ")
# print(second_array.get_value(2))
# second_array.delete_item(3)
# second_array.print_values(mode="one_line", sep=", ")
# print(second_array.check_value(333))
# print(second_array.count_value(333))




# linked_user_list = SecondLinkedList()
# while True:
# 		user_num = input("Введите число для добавления в списки(пустая строка для выхода): ")
# 		if user_num != "":
# 				linked_user_list.append(int(user_num))
# 				continue
# 		break		


# prints(linked_user_list)






# linked_user_list = SecondLinkedList()
# while True:
# 		print("1. Вставить элемент в конец.")
# 		print("2. Удалить элемент из списка.")
# 		print("3. Показать элементы списка.")
# 		print("4. Проверить содержимое списка.")
# 		print("5. Заменить значение в списке.")
# 		print("6. Выход.")
# 		user_choice = int(input("Ваш выбор: "))
# 		match user_choice:
# 				case 1:
# 						linked_user_list.append(int(input("Какое число добавить в список?: ")))
# 				case 2:
# 						linked_user_list.delete_item(int(input("Какое число удалить по индексу?: ")))
# 				case 3:	
# 						print("Как вы хотите вывести список?")
# 						print("1. В Виде обычного списка (list).")	
# 						print("2. В виде строки с произвольным разделителем.")
# 						print("3. Каждый элемент с новой строки.")
# 						show_method = int(input("Ваш выбор: "))						
# 						if show_method == 1:
# 								print(linked_user_list.show_list())
# 						elif show_method == 2:
# 						    sepsrator = input("Введите символы которые будут разделять строки: ")
# 						    linked_user_list.print_values(mode="one_line", sep=sepsrator)	
# 						elif show_method == 3:		
# 								linked_user_list.print_values(mode="new_line")
# 				case 4:
# 						user_value = int(input("Какое значение хотите проверить? Введите значение: "))
# 						if linked_user_list.check_value(user_value):
# 								print("Значение {user_value} есть в вашем списке.")
# 								continue
# 						print(f"Значение {user_value} отсутствует в вашем списке.")	
# 				case 5:
# 						user_replace_index = int(input("Введите номер элемента, который нужно заменить: "))	
# 						user_new_value = int(input("Новое значение: "))	
# 				case 6:
# 				    break								






# class ListStartedOne(list):


# 		def __getitem__(self, index):
# 				if type(index) != "int":
# 						raise "Index is must be only integer."
# 				if index == 0:
# 						raise "Index must not be equal 0."
# 				elif index > 0:
# 						return super().__getitem__(index - 1)
# 				else :
# 						return super().__getitem__(index)


# user_list = ListStartedOne([345, 1, "usd", 55])						
# print(user_list[2])				








# import collections
# from collections import deque	


# new_queue = collections.deque

# new_queue.append(123)
# new_queue.append(54)	
# new_queue.append(789)	

# print(new_queue)	






# fruits = collections.Counter():
# for element in ["apple", "chery", "banana", "apple"]:
# 		fruits[element] += 1

# print(fruits)		






# for i in range(10, 20, 0.5):
# 		print(i)			



# class FloatRange:


# 		def __init__(self, start=0, stop=0, step=1):
# 				if step == 0:
# 						raise "Step is 0!!!!! Are you///"
# 				if (start > stop) and step > 0:
# 						raise "Infinity loop. Start bigger trhan stop, and step is positive."
# 				self.start = start
# 				self.stop = stop
# 				self.step = step


# 		def __iter__(self):
# 				self.value = self.start - self.step
# 				return self

# 		def __next__(self):
# 				if self.value + self.step < self.stop:
# 						self.value += self.step
# 						return self.value
# 				else:
# 						raise StopIteration		


# for numbers in FloatRange(0, 10, 0.23):		
# 		print(round(numbers, 2))			






# planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn',], ['Uran', 'Neptune', 'Pluto']]
# # flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 5]

# flatten_planets = []

# for sublist in planets:
# 		for planet in sublist:
# 				if len(planet) < 6:
# 						flatten_planets.append(planet) 


# print(flatten_planets)





# list = []
# for i in range(10):
# 		if i % 2 == 0:
# 				list.append(i)

# list = [i for i in range(11) if i % 2 ==0]
# list = [[j for j in range(5)] for i in range(5)]


# print(list)				





# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# flatten_matrix = []

# for sublist in matrix:
# 	for val in sublist:
# 		flatten_matrix.append(val)

		
# print(flatten_matrix)




# matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# flatten_matrix = [val for sublist in matrix for val in sublist]
# print(flatten_matrix)



# class Star:
# 		def__init__(self, name, galaxy):
# 				self.name= name
# 				self.galaxy= galaxy
# 		def__str__(self):
# 				return self.name+ ' in '+ self.galaxy
# sun = Star("Sun", "Milky Way")
# print(sun)


# from collections import deque 
# import math


# graph = {"A": {"B", "C"},
# 					"B": {"D", "E"},
# 					"C": {"F"},
# 					"D": {"B", "E", "G"},
# 					"E": {"B", "D", "G", "F"},
# 					"F": {"C", "E", "H"},
# 					"G": {"D", "E", "H"},
# 					"H": {"G", "F"}
# 					}

# N = len(graph)
# distances = {}
# for vertex in graph:
# 		distances[vertex] = math.inf
# print(distances)		
# start_vertex = "A"
# distances[start_vertex] = 0
# queue = deque(start_vertex)
# while queue:
# 		current_vertex = queue.popleft()
# 		for neighbour_vertex in graph[current_vertex]:
# 				if distances[current_vertex] + 1 < distances[neighbour_vertex]:
# 						distances[neighbour_vertex] = distances[current_vertex] + 1
# 						queue.append(neighbour_vertex)

# print(distances)


# from collections import deque 
# import math





# table_of_distance = {{0, 5, 4, 0, 0, 0, 0},
# 										 {5, 0, 0, 4, 2, 0, 0},
# 										 {4, 0, 0, 0, 0, 3, 0},
# 										 {0, 4, 0, 0, 0, 0, 3},
# 										 {0, 2, 0, 3, 0, 1, 0},
# 										 {0, 0, 3, 0, 1, 0, 5},
# 										 {0, 0, 0, 3, 0, 5, 0}
# 										}

# N = len(table_of_distance)
# names = "abcdef"

# start_vertex = 0
# visited_vertex = {start_vertex}
# shortes_distances = [math.inf] * N
# shortes_distances[start_vertex] = 0
# neighbour_indexes = []


# while visited_vertex != 1:
# 		neighbour_indexes.clear()
# 		for index, distance in enumerate(table_of_distance[start_vertex]):
# 				# print(index, distance)
#         if distance > 0:
#         		neighbour_indexes.append(index)
#     for vertex_index in neighbour_indexes:
#     		if vertex_index not in visited_vertex:
#     				current_distance    		
# yuh


# def get_neighbours(x, y):
# 		ways = (-1, 0), (1, 0), (0, 1), (0, -1)
# 		near_tiles = []
# 		for dx, dy in ways:
# 				if 0 <= x = dx < cols and 0 <= y + dy < rows:
# 						near_tiles.append((grid[y + dy][x + dx], (x + dx, y + dy)))

		
# 		return near_tiles				

# cols = 30
# rows = 20
# tike_size = 50

# pygame.init()
# screen = pygame.display.set_mode((cols * tike_size, rows * tike_size))
# grid = [[0 for i in range(color)] for j in range(rows)]
# print(grid)


# for i in range(cols):
# 		for j in range(rows):
# 				if random.randint(1, 100) < 20:
# 						grid[j][i] = math.inf
# 				else:
# 						grid[j][i] = random.randint(1, 5)


# graph = {}
# for y, row in enumerate(grid):
# 		for x, col in enumerate(row):
# 				print(x, y)							






"""
with deque
"""
# import pygame
# import random
# import math
# from collections import deque


# def get_neighbours(x, y):
#     """
#     Функция, которая берёт координаты и возвращает список кортежей. В данных кортежах
#     указаны веса и координаты соседних клеток, в которые можно прыгнуть.
#     """
#     ways = (-1, 0), (0, -1), (1, 0), (0, 1)
#     near_tiles = []
#     for dx, dy in ways:
#         if 0 <= x + dx < cols and 0 <= y + dy < rows:
#             near_tiles.append((grid[y + dy][x + dx], (x + dx, y + dy)))

#     return near_tiles


# cols = 30
# rows = 20
# tile_size = 50

# pygame.init()
# screen = pygame.display.set_mode((cols * tile_size, rows * tile_size))
# clock = pygame.time.Clock()


# grid = [[0 for i in range(cols)] for j in range(rows)]          # создаём игровое поле, заполненное нулями

# """
# изменение значений в ячейках игрового поля на случайные в указанном алгоритме
# """
# for i in range(cols):
#     for j in range(rows):
#         if random.randint(1, 100) < 20:
#             grid[j][i] = math.inf
#             pygame.draw.rect(screen,
#                              (0, 255, 255),
#                              (i * tile_size,
#                               j * tile_size,
#                               tile_size - 2,
#                               tile_size - 2)
#                              )
#         else:
#             grid[j][i] = random.randint(1, 5)
#             pygame.draw.rect(screen,
#                              (grid[j][i] * 40, 0, 0),
#                              (i * tile_size,
#                               j * tile_size,
#                               tile_size - 2,
#                               tile_size - 2)
#                              )
# # for i in grid:
# #     print(i)

# start = (15, 5)
# finish = (5, 18)

# """
# Граф будет содержать в себе координату точки в виде ключа, а значением будет список кортежей доступных соседей (вес, (х, у)) 
# """
# graph = {}      # {(0, 0): [(5, (1, 0)), (inf, (0, 1))], (1, 0): [(2, (0, 0)), (4, (2, 0)), (5, (1, 1))], (2, 0): [(5, (1....
# for y, row in enumerate(grid):
#     for x, col in enumerate(row):
#         graph[(x, y)] = get_neighbours(x, y)

# # print(graph)
# visited_tiles = {start: None}       # словарь, в котором указаны точки и откуда выгоднее всего в них попасть

# steps_weight = {start: 0}           # словарь, в котором указаны минимальные расстояния от старта до указанных точек

# queue = deque()                     # очередь ячеек, из которых нужно прыгнуть в соседние для дальнейшей проверки пути
# queue.appendleft((0, start))        # добавляем сразу в очередь первую вершину
# # print(queue)
# while True:
#     screen.fill((0, 0, 0))          # залить всё чёрным

#     """
#     Отображение ячеек на экране. Цвет будет подобран в соответствии с весом данной ячейки
#     """
#     for i in range(cols):
#         for j in range(rows):
#             if grid[j][i] == math.inf:
#                 pygame.draw.rect(screen,
#                                  (0, 255, 255),
#                                  (i * tile_size,
#                                   j * tile_size,
#                                   tile_size - 2,
#                                   tile_size - 2)
#                                  )
#             else:
#                 pygame.draw.rect(screen,
#                                  (grid[j][i] * 40, 0, 0),
#                                  (i * tile_size,
#                                   j * tile_size,
#                                   tile_size - 2,
#                                   tile_size - 2)
#                                  )

#     if queue:
#         current_weight, current_node = queue.popleft()      # 0 (0, 5)          берём первый элемент из очереди
#         if current_node == finish:
#             queue.clear()
#             continue

#         near_nodes = graph[current_node]        # [(inf, (0, 4)), (inf, (1, 5)), (5, (0, 6))]
#         # print(near_nodes)
#         for next_node_weight, next_node in near_nodes:  # пройтись по всем соседям
#             # print(next_node_weight, next_node)
#             if next_node_weight == math.inf:            # это нужно чтобы избегать ячейки сс водой
#                 continue

#             new_weight = steps_weight[current_node] + next_node_weight
#             if next_node not in visited_tiles or new_weight < steps_weight[next_node]:
#                 steps_weight[next_node] = new_weight
#                 queue.append((new_weight, next_node))
#                 visited_tiles[next_node] = current_node
#         # print(visited_tiles)

#     #     print(current_weight, current_node)
#     # print(queue)
#     """
#     показать все ячейки на поле, в которые хотя бы раз наступили
#     """
#     for x, y in visited_tiles:

#         pygame.draw.rect(screen,
#                          (255, 255, 255),
#                          (x * tile_size,
#                           y * tile_size,
#                           tile_size - 2,
#                           tile_size - 2),
#                          5
#                          )


#     """
#     отобразить ячейки, которые стоят в очереди на проверку пути
#     """
#     for _, coord in queue:
#         x = coord[0]
#         y = coord[1]
#         pygame.draw.rect(screen,
#                          (0, 255, 0),
#                          (x * tile_size,
#                           y * tile_size,
#                           tile_size - 2,
#                           tile_size - 2),
#                          5
#                          )


#     # start circle      нарисовать точку старта
#     pygame.draw.circle(screen,
#                        (255, 255, 0),
#                        (start[0] * tile_size + tile_size // 2,
#                         start[1] * tile_size + tile_size // 2),
#                        tile_size // 3
#                        )
#     # finish circle     нарисовать точку финиша
#     pygame.draw.circle(screen,
#                        (0, 255, 0),
#                        (finish[0] * tile_size + tile_size // 2,
#                         finish[1] * tile_size + tile_size // 2),
#                        tile_size // 3
#                        )


#     """
#     Отрисовка наикратчайшего пути до точки. отрисовка будет идти от финиша к старту за счёт visited tiles   
#     """
#     segment_of_path = current_node          # можно было обойтись просто current_node...
#     while segment_of_path:
#         pygame.draw.circle(screen,
#                            (0, 0, 255),
#                            (segment_of_path[0] * tile_size + tile_size // 2,
#                             segment_of_path[1] * tile_size + tile_size // 2),
#                            tile_size // 6
#                            )
#         segment_of_path = visited_tiles[segment_of_path]            # пользуемся словарём, где хранится наиболее выгодная предыдущая точка. Прыгаем от финишной точки к предыдущей и так далее. Пока не наткнёмся на None у стартовой точки


#     pygame.display.update()             # общее обновление дисплея
#     clock.tick(7)                       # ограничение количества кадров в секунду.


# button_start = Buttons("start", 0, 0, 100, 100, (100, 100, 100))
# button_finish = Buttons("finish", 0, 100, 100, 200, (0, 200, 0))
# button_road = Buttons("road", 0, 300, 400, 300, (100, 100, 100))
# button_grass = Buttons("grass", 0, 400, 100, 400, (0, 200, 0))
# button_sand = Buttons("sand", 0, 500, 100, 500, (100, 100, 0))
# button_water = Buttons("water", 0, 600, 100, 600, (0, 60, 200))
# all_surfaces = {"road": 1, "grass": 3, "sand": 5, "water": math.inf}


# 		for event in pygame.event.get():
# 				if event.type == pygame.MOUSEMOTION and event.button



# 		for event in pygame.event.get():
# 				if event.type == pygame.MOUSEBUTTONDOWN:
# 						for button in Buttons


# def draw_rect(color):
# 		match color == "grass":


																			


# import bs4 import BeautifulSoup 
# import requests


# url = "https://ru.wikipedia.org/w/index.php?search=Ляудона&title=Служебная%3AПоиск&ns0=1"

# def get_data():
# 		page = requests.get(url)
# 		# print(page.text)
# 		soup = BeautifulSoup(page.text, 'html.parcer')
# 	 	# print(soup)
# 		article_title = soup.find('span', class_='mw-page-title-main')
# 		print(article_title.text)
# 		article_image = soup.find('a', class_='image').find('img').get('scr').split("/")
# 		print(article_image)
# 		image_url = "https:"
# 		for i in article_image[1:-1]:
# 				if i == "thumb":
# 						continue
# 				image_url = image_url + "/" + i
# 		print(image_url)    


# 		image_url_stream = requests.get(image_url, stream=True)
# 		with open(article_image[-2], "wb") as image_file:
# 				for valve in image_url_stream.iter_content(1024):
# 						image_file.write(value)

# get_data()		

 






# url = "https://ru.wikipedia.org/w/index.php?search=Ляудона&title=Служебная%3AПоиск&ns0=1"

# def get_data():
# 		page = requests.get(url)
# 		# print(page.text)
# 		soup = BeautifulSoup(page.text, 'html.parcer')
# 	 	# print(soup)
# 		article_table = soup.find('table')
# 		countries_list = article_table.find_all('tr')
# 		for country in countries_list:
# 				elements = country.find_all('td')
# 				print(country)
# 				country_name = country.find('span', class_="wrap")
# 				print(country_name)    


# 		image_url_stream = requests.get(image_url, stream=True)
# 		with open(article_image[-2], "wb") as image_file:
# 				for valve in image_url_stream.iter_content(1024):
# 						image_file.write(value)

# get_data()		 







# https://www.marvel.com/v1/pagination/grid_cards?offset=0&limit=2737&entityType=character&sortField=title&sortDirection=asc





# for hero_link in link_list:
# 	url = "https://www.marvel.com" + hero_link
# 		page = requests.get(url)
# 		soup = BeautifulSoup(page.text, 'html.parcer')
# 		hero_physical 




# def calculate_string(expression):
# 		list_of_actions = ('+', '-', '*', '/')
# 		current_action = ''
# 		for i in expression:
# 				if i in list_of_actions:
# 						current_action = i
# 						break
# 				else:
# 						raise ValueError("Exprected 1 action, but no one in this expression.")		
# 		numbers = expression.split(current_action)
# 		if len (numbers[0]) == 0 or len(numbers[1]) == 0:
# 				raise ValueError("Number is not correct.")
# 		# print(numbers, current_action)				 
# 		if not ((str.isdigit(numbers[0]) is True) and (str.isdigit(numbers[1]) is True)):
# 				raise ValueError("Is not a number!")			


# def check_type_num(side):
# 		if '.' in side:
# 				return float(side)
# 		else:
# 				return int(side)		

# match current_action:
# 		case "+":
# 				return numbers[0] + numbers[1]
# 		case "-":
# 				return numbers[0] + numbers[1]
# 		case "*":
# 				return numbers[0] * numbers[1]
# 		case "/":
# 				if check_type_num(numbers[1]) == 0:
# 						raise ValueError("Division ZERO")						

# calculate_string('200+30')

# def testing_calculate_string():
# 		if calculate_string('2+2') == 4:
# 				print('test 1st OK. Successfully!   2+2, returns 4')
# 		else:
# 				print('test 1st is WRONG!  2+2, exprected 4, but return not 4')	

# 		if calculate_string('20-2') == 18:
# 				print('test 2st OK. Successfully!   20-2, returns 18')
# 		else:		
# 				print('test 2st is WRONG!  20-2, exprected 18, but return not 18')

# 		if calculate_string('200*2') == 400:
# 				print('test 3st OK. Successfully!  200*2, returns 400')
# 		else:		
# 				print('test 3st is WRONG!  200*2, exprected 400, but return not 400')

# 		if calculate_string('12/4') == 3:
# 				print('test 4st OK. Successfully!   12/4, returns 3')
# 		else:		
# 				print('test 4st is WRONG!  12/4, exprected 3, but return not 3')	



# testing_calculate_string()



# assert calculate_string("6+2") == 10																			




def some_function(number):
    digits = str(number)
    result = 0
    while len(digits) > 1:
        result += 1
        new_num = 1
        for i in digits:
            new_num *= int(i)
            digits = str(new_num)
    return result

    
some_function(27)
