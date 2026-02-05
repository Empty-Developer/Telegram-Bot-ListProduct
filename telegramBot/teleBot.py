import telebot

# <s></s> - strikethrough text
TOKEN = '8579260504:AAFYQtkbam2lWeSyDPfu6DO_wnZCO3bRoyM'
bot = telebot.TeleBot(TOKEN)


# help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        '💎 <b>Quick Command Guide</b>\n\n'

        '⚡️ <b>Essentials:</b>\n'
        '• <code>/start</code> – show intro & rules\n'
        '• <code>/help</code> – this message\n\n'

        '🛒 <b>Shopping Mode:</b>\n'
        '• <code>/add milk</code>\n'
        '• <code>/list</code> – view numbered list\n'
        '• <code>/done 2</code> – mark #2 as bought\n'
        '• <code>/clear</code> – delete everything\n\n'

        '🎯 <b>Format:</b>\n'
        '<code>/add item</code>\n'
        '<code>/done [number]</code>\n\n'

        '📌 <i>Items get <s>crossed out</s> when bought</i>'
    )
    bot.send_message(message.chat.id, help_text, parse_mode='HTML')


# start
@bot.message_handler(commands=['start'])
def send_start(message):
    start_text = (
        '🛒 <b>SHOP BOT – YOUR PERSONAL MEMORY PROSTHESIS</b> 👽\n\n'

        '💅 <b>MAIN VIBES:</b>\n'
        '🤖 <code>/start</code> – show this ultimate guide\n'
        '🤖 <code>/help</code> – same energy, different name\n\n'

        '🔥 <b>SHOPPING HACKS:</b>\n'
        '➕ <code>/add</code> – manifest products into existence\n'
        'Example: <code>/add oat</code>\n'
        'Use commas or just vibe with it\n\n'

        '📋 <code>/list</code> – flex your organized self\n'
        'Bought stuff gets <s>slashed</s> ✅\n\n'

        '✅ <code>/done [number]</code> – yeet item from the list\n'
        'Example: <code>/done 3</code> – deletes the third item\n\n'

        '💀 <code>/clear</code> – nuclear option\n'
        '(no take-backsies)\n\n'

        '⚠️ <b>PRO TIPS:</b>\n'
        '• Your list = your business 👀\n'
        '• Auto-save = zero brain cells required 🧠\n'
        '• Add multiple items = big brain move 🧠\n'
        '• Numbers update automatically = magic ✨\n\n'

        '🎮 <b>HOW TO PLAY:</b>\n'
        '1. <code>/add matcha</code>\n'
        '2. <code>/list</code> – check your loot\n'
        '3. At store: <code>/done 1</code> – matcha secured\n'
        '4. <code>/list</code> – see <s>matcha</s> ✅ flex\n\n'

        'Bottom line: never forget avocado again 🥑✨\n'
        'Your brain\'s favorite cheat code 🧠💥'
    )
    bot.send_message(message.chat.id, start_text, parse_mode='HTML')


# add
user_todo_list = {}

@bot.message_handler(commands=['add'])
def send_add(message):
    user_id = int(message.from_user.id)
    text = message.text.replace('/add', '').strip()

    if not text:
        bot.reply_to(message, "Error")
        return

    if user_id not in user_todo_list:
        user_todo_list[user_id] = []

    user_todo_list[user_id].append(text)
    bot.reply_to(message, "Added =)")

# list
@bot.message_handler(commands=['list'])
def send_list(message):
    user_id = int(message.from_user.id)

    if user_id not in user_todo_list or not user_todo_list[user_id]:
        bot.send_message(message.chat.id,"empty")
        return

    task = user_todo_list[user_id]
    text = '<b>List</b>\n\n'

    for i, task in enumerate(task, 1):
        text += f'{i}. {task}\n'

    text += 'Delete product /done (number)\n'
    bot.send_message(message.chat.id, text, parse_mode='HTML')

@bot.message_handler(commands=['done'])
def send_done(message):
    user_id = int(message.from_user.id)

    if user_id not in user_todo_list or not user_todo_list[user_id]:
        bot.send_message(message.chat.id,"empty")
        return

    text = message.text.replace('/done', '').strip()

    if not text.isdigit():
        bot.reply_to(message, "Error")
        return

    task_num = int(text)

    tasks = user_todo_list[user_id]
    if task_num < 1 or task_num > len(tasks):
        bot.reply_to(message, "Error")
        return

    delete_task = tasks.pop(task_num - 1)
    bot.reply_to(message, "Done")

# clear

@bot.message_handler(commands=['clear'])
def send_clear(message):
    user_id = int(message.from_user.id)
    if user_id in user_todo_list:
        count = len(user_todo_list[user_id])
        user_todo_list[user_id] = []
        bot.reply_to(message, "Clear =)")
    else:
        bot.reply_to(message, "Error")

print('bot started')
bot.polling(none_stop=True)