from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
BOT_USERNAME = int(os.environ.get("BOT_USERNAME", ""))
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    bot_name = BOT_USERNAME
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("⭕ Share Your Link ⭕" ,url=f"https://t.me/share/url?url=https://t.me/{bot_name}?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Refer And Earn Get 1GB Upload Limit\nPer Refer 1GB\n Your Link :- https://t.me/{bot_name}?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
