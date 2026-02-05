import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

# Если переменная окружения пустая, используем токен напрямую
if not TOKEN:
    TOKEN = "8579260504:AAFYQtkbam2lWeSyDPfu6DO_wnZCO3bRoyM"

# Хранилище данных пользователей (в памяти)
user_data = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    user = update.effective_user
    welcome_text = f"""
👋 Привет, {user.first_name}!

Я простой чат-бот. Вот что я умею:

📝 <b>Основные команды:</b>
/start - показать это сообщение
/help - помощь по командам
/echo [текст] - повторить текст
/count - посчитать сообщения

💬 <b>Просто общение:</b>
Напиши мне что-нибудь, и я отвечу!

📊 <b>Статистика:</b>
Используй /count чтобы посмотреть сколько сообщений ты отправил.

Наслаждайся общением! ✨
    """
    await update.message.reply_html(welcome_text)

    # Инициализируем счетчик для пользователя
    user_data[user.id] = {"message_count": 0}


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /help"""
    help_text = """
🆘 <b>Помощь по командам:</b>

<b>Основные команды:</b>
/start - начать работу с ботом
/help - показать эту справку

<b>Интерактивные команды:</b>
/echo [текст] - бот повторит ваш текст
/count - показать количество ваших сообщений
/reset - сбросить счетчик сообщений

<b>Примеры использования:</b>
<code>/echo Привет, мир!</code>
<code>/count</code>
<code>/reset</code>

Просто напиши любое сообщение, и я отвечу тебе! 😊
    """
    await update.message.reply_html(help_text)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /echo"""
    user_id = update.effective_user.id

    # Получаем текст после команды /echo
    if context.args:
        text_to_echo = ' '.join(context.args)
        await update.message.reply_text(f"📣 {text_to_echo}")
    else:
        await update.message.reply_text("📝 Напиши: /echo [текст]\nПример: /echo Привет мир!")


async def count_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /count"""
    user_id = update.effective_user.id
    user = update.effective_user

    # Инициализируем счетчик если нет
    if user_id not in user_data:
        user_data[user_id] = {"message_count": 0}

    count = user_data[user_id]["message_count"]

    if count == 0:
        response = f"📊 {user.first_name}, ты еще не отправлял мне сообщений!"
    else:
        response = f"📊 {user.first_name}, ты отправил мне {count} сообщений!"

    await update.message.reply_text(response)


async def reset_count(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /reset"""
    user_id = update.effective_user.id

    if user_id in user_data:
        user_data[user_id]["message_count"] = 0
        await update.message.reply_text("🔄 Счетчик сообщений сброшен!")
    else:
        await update.message.reply_text("🤔 У тебя еще нет счетчика. Напиши что-нибудь сначала!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик обычных сообщений"""
    user_id = update.effective_user.id
    user_message = update.message.text
    user_name = update.effective_user.first_name

    # Увеличиваем счетчик сообщений
    if user_id not in user_data:
        user_data[user_id] = {"message_count": 1}
    else:
        user_data[user_id]["message_count"] += 1

    # Простые ответы на базовые фразы
    user_message_lower = user_message.lower()

    if any(word in user_message_lower for word in ["привет", "hello", "hi", "хай"]):
        response = f"Привет, {user_name}! 👋"

    elif any(word in user_message_lower for word in ["как дела", "how are you", "как ты"]):
        response = "У меня всё отлично, спасибо! А у тебя? 😊"

    elif any(word in user_message_lower for word in ["спасибо", "thanks", "thank you"]):
        response = "Всегда пожалуйста! 😊"

    elif any(word in user_message_lower for word in ["пока", "до свидания", "bye", "goodbye"]):
        response = "Пока! Буду рад тебя видеть снова! 👋"

    elif "?" in user_message:
        responses = [
            "Интересный вопрос! 🤔",
            "Хм, давай подумаем... 💭",
            "Может быть! 🤷‍♂️",
            "Сложно сказать...",
            "Попробуй спросить иначе?",
            f"{user_name}, хороший вопрос! 😊"
        ]
        import random
        response = random.choice(responses)

    else:
        # Общий ответ на другие сообщения
        responses = [
            f"Понял тебя, {user_name}!",
            "Интересно!",
            "Расскажи подробнее?",
            "Продолжаем разговор!",
            "Записал! 📝",
            "Спасибо за сообщение!",
            f"Классно, {user_name}!",
            "Ух ты! 😮"
        ]
        import random
        response = random.choice(responses)

    await update.message.reply_text(response)


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик неизвестных команд"""
    await update.message.reply_text(
        "🤔 Не знаю такую команду.\n"
        "Попробуй /help чтобы увидеть все доступные команды."
    )


def main():
    """Основная функция запуска бота"""
    print(f"🔧 Загружаем токен: {TOKEN[:10]}...")

    # Проверяем токен
    if not TOKEN:
        print("❌ ОШИБКА: Токен не найден!")
        print("Добавьте TELEGRAM_TOKEN в .env файл или укажите напрямую в коде")
        return

    try:
        # Создаем приложение
        app = ApplicationBuilder().token(TOKEN).build()

        # Добавляем обработчики команд
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))
        app.add_handler(CommandHandler("echo", echo))
        app.add_handler(CommandHandler("count", count_messages))
        app.add_handler(CommandHandler("reset", reset_count))

        # Обработчик обычных сообщений (все текстовые сообщения кроме команд)
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Обработчик неизвестных команд (должен быть последним)
        app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

        print("🤖 Бот запускается...")
        print("⚠️  Убедись, что у тебя нет активного webhook (ошибка 409)")
        print("   Если есть, выполни: curl https://api.telegram.org/bot{TOKEN}/deleteWebhook")

        # Запускаем бота
        app.run_polling(allowed_updates=Update.ALL_TYPES)

    except Exception as e:
        print(f"❌ Ошибка при запуске бота: {e}")
        print("🔧 Проверь:")
        print("   1. Правильность токена")
        print("   2. Наличие интернет-соединения")
        print("   3. Библиотеки установлены (pip install python-telegram-bot python-dotenv)")


if __name__ == '__main__':
    main()