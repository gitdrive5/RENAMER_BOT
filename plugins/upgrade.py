"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 50GB
	Price Rs 50 โน  ๐ฎ๐ณ per Month ๐
	
	**VIP 2 **
	Daily Upload limit 200GB
	Price Rs 100 โน ๐ฎ๐ณ per Month ๐
	
	
	Pay Using Upi I'd ```tgnvs@axisbank```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN ๐",url = "https://t.me/tgnvspaymentbot")], 
        			[InlineKeyboardButton("VIP 1",url = "https://upier.vercel.app/pay/tgnvs@axisbank?am=50"),
        			InlineKeyboardButton("VIP 2",url = "https://upier.vercel.app/pay/tgnvs@axisbank?am=100")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free User Plan**
	Daily ๐บ Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily ๐บ Upload  limit 50GB
	Price Rs 50  ๐ฎ๐ณ per Month ๐
	
	**VIP 2 **
	Daily ๐บ Upload limit 200GB
	Price Rs 100  ๐ฎ๐ณ per Month ๐
	
	
	Pay Using Upi I'd ```tgnvs@axisbank```
	
	After Payment Send ๐ฒScreenshots Of 
        Payment To Admin ๐งโโ๏ธ"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN ๐",url = "https://t.me/tgnvspaymentbot")], 
        			[InlineKeyboardButton("VIP 1",url = "https://upier.vercel.app/pay/tgnvs@axisbank?am=50"),
        			InlineKeyboardButton("VIP 2",url = "https://upier.vercel.app/pay/tgnvs@axisbank?am=100")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
