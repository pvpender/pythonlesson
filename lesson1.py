# если перед началом какого-либо текста стоит #, то это комментарий
# комментарии служат для пояснения чего-либо в коде, и не считываются компилятором
print("Я не такой, как все!")

# Чтобы вывести число необязательно писать двойные кавычки
print(1234)
# Однако если кавычки написать - ничего не измениться
print("1234")


# чтобы вывести число с десятичной частью, необходимо после целой части ставить .
print(123.4)
# Если написать , то компилятор будет считать, что необходимо вывести два целых числа через пробел
print(123,4)
# можно писать несколько текстов и чисел через запятую
print("Привет", 8, "Пока!")
# в функцию можно также записать математическое выражение - выведиться его ответ
print(123*4)

# если написать кавычки перед математическим выражение - выведиться само выражение
print("123*4")
# внутри двойных кавычек можно написать вообще всё что угодно
print("sdd14&!/*+face0293")

# чтобы перенести часть текста на дрогую строку, нужно написать \n
print("Я не такой, \nкак все!")

# однако порой удобнее использовать тройные кавычки
print("""Я
не такой,
как 
все!""")

# у функции есть несколько необязательных аргументов: sep, end, file, flush
# sep отвечает за то, что будет написано между разными элементами(по умолчанию - пробел)
print(1, 2, 3, sep="+")

# end отвечает за то, что будет стоять вконце вывода (по умолчанию - переход на новую строку)
print(1)
print(2)
print(3)
print(1, end=" ")
print(2, end=" ")
print(3)

# сбрасываем поток (визуально мы ничего не незаметим)
print("Hello", flush=True)
