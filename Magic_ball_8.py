from random import choice


answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом",
           "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
           "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
           "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
           "Перспективы не очень хорошие", "Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос. Как тебя зовут?')
user_name = input()
print('Привет,', user_name)
print('Ты пришел ко мне с вопросом, ибо будущее твое туманно.')
while True:
    print('Задай же вопрос и получишь ответ.')
    question, answer = input(), choice(answers)
    print(answer)
    print('Хочешь ли ты задать еще вопрос?')
    question2 = input()
    if question2 == 'Да' or question2 == 'да' or question2 == 'ДА':
        continue
    else:
        break
print('Возвращайся если возникнут вопросы!')