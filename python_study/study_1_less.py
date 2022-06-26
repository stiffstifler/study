# all even questions are necesserly heve answer

question_1 = "Какая последняя версия Python? (число до запятой) "
question_2 = 'Какой это тип данных "int()"? '
question_3 = "Какой результат может быть в булевых вырожениях? "
question_4 = "Что означает None для Python 3? "
question_5 = "В какой кодировке Python 3 распознает текст? "
question_6 = "print - это вывод текста на экран, * - это ввод текста пользователем "
question_7 = "Каким знаком задается переменная? "
question_8 = "if/elif/else - к чему относятся эти параметры? "
question_9 = "while/for - к чему относятся эти параметры? "
question_10 = "Булевы выражения True and Folse можно сопоставить такими с цифрыми: "

right_ansver_1 = "3"
right_ansver_2 = "цельное число"
right_ansver_3 = "True and False"
right_ansver_4 = "Ничего"
right_ansver_5 = "UTF-8"
right_ansver_6 = "input"
right_ansver_7 = "="
right_ansver_8 = "Условия"
right_ansver_9 = "Циклы"
right_ansver_10 = "True - все, что не ноль, False - 0"

drop_answer = "!"

questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]
question_x = 0

right_ansver = [right_ansver_1, right_ansver_2, right_ansver_3, right_ansver_4, right_ansver_5, right_ansver_6, right_ansver_7, right_ansver_8, right_ansver_9, right_ansver_10]
right_ansver_x = 0

count_right_answers = 0
count_wrong_answers = 0
count_total_answers = 0
count_skip_answers = 0

i = 1

while i in range(1, 11):
    print(right_ansver[right_ansver_x])
    user_answer = input(questions[question_x])
    if user_answer.casefold() == right_ansver[right_ansver_x].casefold():
        print("Great!")
        i += 1
        question_x += 1
        count_right_answers += 1
        right_ansver_x += 1
        count_total_answers += 1

    elif user_answer.casefold() == drop_answer.casefold():
        if count_total_answers % 2  != 0:
            print("Skip question!")
            right_ansver_x += 1
            count_skip_answers += 1
            i += 1
            question_x += 1
            continue
        else:
            print("You can not skip the question!")
            continue
            

    else:
        print("Wrong answer!")
        count_wrong_answers += 1
        right_ansver_x += 1 
        count_total_answers += 1
        i += 1
        question_x += 1


print("Всего ответов = " + str(count_total_answers))
print("Правильных ответов = " + str(count_right_answers))
print("Неправильных ответов = " + str(count_wrong_answers))
print("Пропущено вопросов = " + str(count_skip_answers))
