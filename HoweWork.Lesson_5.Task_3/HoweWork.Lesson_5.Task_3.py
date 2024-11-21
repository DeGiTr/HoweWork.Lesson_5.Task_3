# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно. 
# У Майкла A долларов, у Ивана B долларов. 
# Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

summ_invest = int(input("Введите минимальную сумму инвестиций в долларах (X): "))
mike_invest = int(input("Введите вклад Майкла в долларах (A): "))
ivan_invest = int(input("Введите вклад Ивана в долларах (B): "))
print()
print("Минимальная сумма инвестиций (X): ", summ_invest, "$")
print("Вклад Майкла (A): ", mike_invest, "$")
print("Вклад Ивана (B): ", ivan_invest, "$")
print()
print("Результат: ")
if (mike_invest and ivan_invest) >= summ_invest: 
    print(2)
elif (mike_invest >= summ_invest) and (ivan_invest <= summ_invest):
    print("Mike")
elif (mike_invest <= summ_invest) and (ivan_invest >= summ_invest):
    print("Ivan")
elif (mike_invest < summ_invest) and (ivan_invest < summ_invest) and (mike_invest + ivan_invest >= summ_invest):
    print("1")
else:
    print(0)