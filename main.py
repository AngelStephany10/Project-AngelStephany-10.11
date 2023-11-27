from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "6900152821:AAEqfiXVoci9208K5HgQtfl34eBVzGEDZ1c"
USERNAME_BOT = "@Angel_tugascoding_bot"

async def start_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Gunakan /help untuk melihat perintah yang kamu butuhkan.')

async def help_command(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hai...TerimaKasih telah menggunakan bot ini. Ketik perintah dengan huruf kecil. Berikut Daftar perintah yang bisa kamu pilih :\n hallo \n tentang kamu \n siapa kamu? \n kamu bersekolah dimana? \n kamu kelas berapa? \n kamu tinggal dimana?\n')

async def text_massage(update : Update, context: ContextTypes.DEFAULT_TYPE):
    text_diterima: str = update.message.text

    print('text diterima: ', text_diterima)

    if 'hallo' in text_diterima:
        await update.massage.reply_text('hallo juga... ')
    elif 'tentang kamu' in text_diterima:
        await update.message.reply_text('hai namaku bot yang di buat oleh Angel Stephany')
    elif 'siapa kamu?' in text_diterima:
        await update.message.reply_text('Aku adalah bot yang bisa membantu kamu...')
    elif 'kamu bersekolah dimana?' in text_diterima:
        await update.message.reply_text(' Saya bersekolah di Inatius Global School')
    elif 'kamu kelas berapa?' in text_diterima:
        await update.message.reply_text(' saya kelas 10.11 IPS')
    elif 'kamu tinggal dimana?' in text_diterima:
        await update.message.reply_text('aku tinggal dibumi')
    

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'eror : {context.error}')

if __name__ == '__main__':
    print('Bot Dimulai...')
    
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler( 'start', start_command ))

    app.add_handler(CommandHandler( 'help', help_command))

    app.add_handler(MessageHandler( filters.TEXT, text_massage))

    app.add_error_handler(error)

    app.run_polling(poll_interval=1)