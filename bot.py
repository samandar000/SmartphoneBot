from telegram.ext import (
    Updater, 
    CallbackContext, 
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler
)
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import os
import db
from cartdb import Cart
TOKEN = os.environ['TOKEN']



def start(update: Update, context: CallbackContext):
    keyboart = ReplyKeyboardMarkup([
        ['🛍 Shop','🛒 Cart'],
        ['📞 Contact','📝 About']
    ])
    update.message.reply_html(
    text='Assalom alaykum xush kelibsiz botimizga👍',
    reply_markup=keyboart
    )

def brands(update: Update, context: CallbackContext):
    all_brands = db.get_tables()
    keyboart = []
    for brand in all_brands:
        keyboart.append([InlineKeyboardButton(text=brand, callback_data=f'brand:{brand}')])
    update.message.reply_text(
    text='all brands',
    reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboart))


def products(update: Update, context: CallbackContext):
    brand = update.callback_query.data.split(':')[1]
    all_products = db.get_products(brand)
    
    update.callback_query.answer(brand)
    inline_keyboard = []
    for product in all_products:
        inline_keyboard.append([InlineKeyboardButton(text=product['name'],
                                                     callback_data=f"product:{product['name']}")])
    update.callback_query.message.reply_html(text='Choose a phone',
                                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))
    


def contact(update: Update, context: CallbackContext):
    update.message.reply_html("connact us")

def about(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup([
        ['📝 About Us'],['📝 About the bot'],
        ['Main menu']
    ])
    update.message.reply_html("About us",reply_markup=keyboard)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    updater.dispatcher.add_handler(CommandHandler('start',start))
    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('🛍 Shop'), callback=brands))
    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('📞 Contact'), callback=contact))
    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('📝 About'), callback=about))
    dp.add_handler(handler=CallbackQueryHandler(callback=products, pattern='brand'))
    dp.add_handler(handler=CallbackQueryHandler(callback=products, pattern='product'))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()