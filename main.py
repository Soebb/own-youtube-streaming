import os
from pyromod import listen
from stream import create_stream_url
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
default_thumb = "https://github.com/Soebb/own-utube-stream-link-gen/raw/main/default_thumbnail.jpg"

Bot = Client(
    "Own-ST-Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

START_TXT = """
Hi {},
I'm Own YouTube Stream URL Generator Bot.

Send a YouTube URL to get started.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/Soebb/own-utube-stream-link-gen'),
        ]]
    )


@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.text)
async def gen_st_url(bot, m):
    yt_url = m.text
    title = await bot.ask(m.chat.id,'`Send the Title name`', filters=filters.text, parse_mode='Markdown')
    thumbnail = default_thumb
    own_stream_url = create_stream_url(yt_url, title.text, thumbnail)
    await m.reply(own_stream_url + "\n\nCopy and paste it to your web browser.")
    #import webbrowser
    #webbrowser.open(own_stream_url)


Bot.run()
