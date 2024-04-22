import telebot 
import random
import os

bot = telebot.TeleBot('7022386893:AAE_7Is6Lo08iobq-5-CdZBq8eDnFzp8koA')


# Индекс практики
current_practice_index = {}

# Для цитат
def read_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = [line.strip() for line in file]
    return quotes

# Пути к файлу
quotes_file = 'D:/telegrambot/quotes.txt'
quotes = read_quotes(quotes_file)
lessons_folder = 'D:/telegrambot/lessons/'

# Для прогресса человека в уроках
current_lesson = {}

# Все уроки
lesson_info = {
    1: "Урок #1. Ключевая идея, от которой зависит успех речи.",
    2: "Урок #2. Базовая структура выступления.",
    3: "Урок #3. Как вести себя в кадре",
    4: "Урок #4. Словарный запас",
    5: "Урок #5. Слова-паразиты",
    6: "Урок #6. Скорость речи и паузы",
    7: "Урок #7. Интонация",
    8: "Урок #8. С чего начать и как закончить речь",
    9: "Урок #9. Сторителлинг",
    10: "Урок #10. Состояние спикера",
    11: "Урок #11. Как справиться с волнением и страхом во время общения и публичных выступлений",
    12: "Урок #12. Самопрезентация",
    13: "Урок #13. Ошибки самопрезентации",
    14: "Урок #14. Вопросы и возражения ",
    15: "Урок #15. SERMON",
    16: "Поздравляем! Вы завершили обучение🙌🏻",
}

@bot.message_handler(commands=['start'])
def start_message(message):
    welcome_message = """Добро пожаловать!
🎙 Приветствую вас в ораторском боте! Здесь вы найдете все необходимое для развития вашего ораторского мастерства.

📚 Начните с раздела "Обучение", чтобы узнать больше о том, как стать более уверенным оратором.

💬 В разделе "Практика" вы сможете оттачивать свои навыки на практике.

📰 "Вдохновение" предлагает вдохновляющие цитаты, чтобы поддерживать вашу мотивацию.

📖 В разделе "Ресурсы" вы найдете полезные книги для более глубокого изучения ораторского искусства.

❓ Если у вас возникнут вопросы, не стесняйтесь задавать их, пишите админам!(@generalissimoone, @uvdmlx)

Удачи в вашем ораторском путешествии! 🚀"""
    bot.send_message(message.chat.id, welcome_message)

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Обучение🧑‍🎓")
    item2 = telebot.types.KeyboardButton("Практика📓")
    item3 = telebot.types.KeyboardButton("Вдохновение💡")
    item4 = telebot.types.KeyboardButton("Ресурсы📚")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Обучение🧑‍🎓":
        send_lesson(message)
    elif message.text == "Практика📓":
        send_practice(message)
    elif message.text == "Вдохновение💡":
        random_quote = random.choice(quotes)
        bot.send_message(message.chat.id, random_quote)
    elif message.text == "Ресурсы📚":
        with open('D:/telegrambot/resourse.txt', 'r', encoding='utf-8') as file:
            file_content = file.read()
        bot.send_message(message.chat.id, file_content)
    else:
        bot.send_message(message.chat.id, "Я умею читать только опции из меню, пожалуйста, пользуйтесь им🙃")


def send_practice(message):
    user_id = message.chat.id
    current_index = current_practice_index.get(user_id, 0)
    bot.send_message(user_id, practice_texts[current_index])
    current_practice_index[user_id] = (current_index + 1) % len(practice_texts)

    #Урок
def send_lesson(message):
    current_lesson_number = current_lesson.get(message.chat.id, 1)
    lesson_text = lesson_info.get(current_lesson_number, "Информация об уроке отсутствует.")
    bot.send_message(message.chat.id, lesson_text)

    lesson_file_path = os.path.join(lessons_folder, f"lesson_{current_lesson_number}.pdf")
    if os.path.exists(lesson_file_path):
        bot.send_document(message.chat.id, open(lesson_file_path, 'rb'))
        current_lesson[message.chat.id] = current_lesson_number + 1
    else:
        bot.send_message(message.chat.id, "Новых уроков пока нет, но мы обещаем добавить их в скором времени🙃")


        #Практика вопрос/ответ
practice_texts = ["Что такое телодвижения в ораторском искусстве?", "Движения тела, используемые для подчеркивания речи", "Что такое логическое заключение в речи?","Подведение итогов аргументации", "Что такое пауза в ораторской речи?", "Короткая пауза для эмфазы или перехода к следующему фрагменту речи","Что такое «каналы коммуникации» в ораторском контексте?", "Различные способы передачи информации: слова, жесты, интонация и т. д.", "Что означает адресовать аудиторию в контексте публичных выступлений?","Чрезмерное использование техники узкого копирования.", "Какова роль внутреннего диалога в подготовке к публичному выступлению?", "Осознание эмоционального состояния и контроль нервозности"]  

bot.polling()