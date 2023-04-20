import asyncio
import os
import logging
from pyrogram import Client, filters, enums
from Script import script
from info import CHANNELS, ADMIN, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL, PM, ADMINS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



from pyrogram import Client, filters 
from plugins.helpers.config import ADMINS, DOWNLOAD_LOCATION
import os


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)




dir = os.listdir(DOWNLOAD_LOCATION)

# dir = "./DOWNLOADS"

@Client.on_message(filters.private & filters.photo)                            
async def set_tumb(bot, message):       
    if len(dir) == 0:
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        return await bot.send_message(chat_id=ADMINS, message=message.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")            

            
    else:    
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await bot.download_media(message=message.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")               
        return await bot.send_cached_media(chat_id=ADMINS, message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")            





@Client.on_message(filters.command("chat") & filters.media)
async def pm_text(client: Client, message):
    try:
        if message.from_user.id == ADMIN:
            await reply_text(client, message)
            return
        info = await client.get_users(user_ids=message.from_user.id)
        reference_id = int(message.chat.id)
        k = await client.send_message(
            chat_id=ADMIN,
            text=script.PM_TXT_ATT.format(reference_id, info.first_name, message.text),
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
        
        await client.send_message(            
            chat_id=PM,
            text=script.PM_TXT_ATT.format(reference_id, info.first_name, message.text),
            parse_mode=enums.ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
        await asyncio.sleep(3000)
        await k.delete()

    except Exception as e:
        logger.exception(e)    








    


@Client.on_message(filters.private & filters.user(ADMIN) & filters.text & filters.reply)
async def reply_text(client: Client, message):
    try:
        reference_id = True
        if message.reply_to_message is not None:
            file = message.reply_to_message
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
            await client.send_message(
                caption=message.text,
                chat_id=int(reference_id),
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
    except Exception as e:
        logger.exception(e)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.media & filters.reply)
async def replay_media(client: Client, message):
    try:
        reference_id = True
        if message.reply_to_media is not None:
            file = message.reply_to_media
            try:
                reference_id = file.text.split()[2]
            except Exception:
                pass
            try:
                reference_id = file.caption.split()[2]
            except Exception:
                pass
            await client.copy_photo(
                chat_id=int(reference_id),
                from_chat_id=message.chat.id,
                message_id=message.id,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton('🎁𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬🎁', url="http://t.me/nasrani_bot?startgroup=true")
                            ],
                            [
                                InlineKeyboardButton('📩𝐑𝐄𝐐𝐔𝐀𝐒𝐓 𝐆𝐑𝐎𝐔𝐏📩', url="https://t.me/NasraniMovies"),
                                InlineKeyboardButton('☘𝐍𝐄𝐖 𝐌𝐎𝐕𝐈𝐄𝐒☘', url="https://t.me/HDAZmovies")
                            ]                            
                        ]
                    )
                )        
    except Exception as e:
        logger.exception(e)
