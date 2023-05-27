# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

S = int(input("Введите значение суммы 'x' и 'y': "))
P = int(input("Введите значение произведения 'x' и 'y': "))
print(f"{S} {P} ->", end = " ")     # для вывода строки согласно ТЗ " 4 4 -> 2 2"
for x in range (1001):
    y = S - x
    if x <= y and P == x * y:
        print(x, y)