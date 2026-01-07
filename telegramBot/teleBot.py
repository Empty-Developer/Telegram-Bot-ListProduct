import telebot

# <s></s> - strikethrough text
bot = telebot.TeleBot('8579260504:AAFYQtkbam2lWeSyDPfu6DO_wnZCO3bRoyM')

@bot.message_handler(commands=['help'])
def send_help(message):
    help = (
        '💎 <b>Quick Command Guide</b>\n\n'

        '⚡️ <b>Essentials:</b>\n'
        '• <code>/start</code> – show intro & rules\n'
        '• <code>/help</code> – this message\n\n'

        '🛒 <b>Shopping Mode:</b>\n'
        '• <code>/add milk, eggs, bread</code>\n'
        '• <code>/list</code> – view numbered list\n'
        '• <code>/done 2</code> – mark #2 as bought\n'
        '• <code>/clear</code> – delete everything\n\n'

        '🎯 <b>Format:</b>\n'
        '<code>/add item1, item2, item3</code>\n'
        '<code>/done [number]</code>\n\n'

        '📌 <i>Items get <s>crossed out</s> when bought</i>'
    )
    bot.send_message(message.chat.id, help, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_start(message):
    start = (
        '🛒 <b>SHOP BOT – YOUR PERSONAL MEMORY PROSTHESIS</b> 👽\n\n'

        '💅 <b>MAIN VIBES:</b>\n'
        '🤖 <code>/start</code> – show this ultimate guide\n'
        '🤖 <code>/help</code> – same energy, different name\n\n'

        '🔥 <b>SHOPPING HACKS:</b>\n'
        '➕ <code>/add</code> – manifest products into existence\n'
        'Example: <code>/add oat milk, avocado, crypto</code>\n'
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
        '1. <code>/add matcha, kombucha, vibes</code>\n'
        '2. <code>/list</code> – check your loot\n'
        '3. At store: <code>/done 1</code> – matcha secured\n'
        '4. <code>/list</code> – see <s>matcha</s> ✅ flex\n\n'

        'Bottom line: never forget avocado again 🥑✨\n'
        'Your brain\'s favorite cheat code 🧠💥'
    )
    bot.send_message(message.chat.id, start, parse_mode='HTML')

bot.polling(none_stop=True)