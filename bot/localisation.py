#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "𝙃𝙚𝙡𝙡𝙤, \n\n𝙏𝙝𝙞𝙨 𝙞𝙨 𝙖 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 <b>𝙑𝙞𝙙𝙚𝙤 𝙀𝙣𝙘𝙤𝙙𝙚𝙧 𝘽𝙤𝙩</b>. \n\n<b>𝙋𝙡𝙚𝙖𝙨𝙚 𝙨𝙚𝙣𝙙 𝙢𝙚 𝙖𝙣𝙮 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙗𝙞𝙜 𝙫𝙞𝙙𝙚𝙤 𝙛𝙞𝙡𝙚 𝙄 𝙬𝙞𝙡𝙡 𝙘𝙤𝙢𝙥𝙧𝙚𝙨𝙨 𝙞𝙩 𝙖𝙨 𝙨 𝙨𝙢𝙖𝙡𝙡 𝙫𝙞𝙙𝙚𝙤 𝙛𝙞𝙡𝙚!</b> \n\n/help for more details. \n\n๏𝓦Ň𝐞𝓻 : @Anime_State"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "🔻 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙞𝙣𝙜.....\n"
    
    UPLOAD_START = "🔺 𝙐𝙥𝙡𝙤𝙖𝙙𝙞𝙣𝙜.....\n"
    
    COMPRESS_START = "❄️ 𝙏𝙧𝙮𝙞𝙣𝙜 𝙩𝙤 𝙀𝙣𝙘𝙤𝙙𝙚....."
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "𝙀𝙣𝙘𝙤𝙙𝙚𝙙 𝘽𝙮 :- [@𝘼𝙣𝙞𝙢𝙚_𝙎𝙩𝙖𝙩𝙚].mkv"

    COMPRESS_PROGRESS = "🕛 ETA: {} 🚨 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\nSupport Group: @Linux_Repo"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
