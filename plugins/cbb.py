#(Β©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>β pemilik π± : <a href='https://t.me/cieemarah'>KING CHπͺ</a>\nβ π±: <code>monubot3</code>\nβ asupan 2 : <a href='https://T.ME/donasiBUAS/'>Pyrogram mon {__version__}</a>\nβ asupan: <a href='https://t.me/asupanbuas'>Click here</a>\nβ asupan 3 : @gulalibuas\nβ Support Group : @ohbabysini</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("repo π±", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
