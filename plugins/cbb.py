#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ pemilik 💱 : <a href='https://t.me/cieemarah'>KING CH🪙</a>\n○ 💱: <code>monubot3</code>\n○ asupan 2 : <a href='https://T.ME/donasiBUAS/'>Pyrogram mon {__version__}</a>\n○ asupan: <a href='https://t.me/asupanbuas'>Click here</a>\n○ asupan 3 : @gulalibuas\n○ Support Group : @ohbabysini</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("repo 💱", callback_data = "close")
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
