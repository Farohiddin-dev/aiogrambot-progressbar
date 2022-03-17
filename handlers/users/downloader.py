import asyncio
import os
from tqdm import tqdm
from aiogram import types
from loader import dp, bot
from pytube import YouTube
from utils.misc.ydownasync import download_video
from aiogram.utils.exceptions import FileIsTooBig

# where to save
SAVE_PATH = "export/"  #to_do


# @dp.message_handler()
# async def video_down(message: types.Message):
#     yt = YouTube(message.text)
#     userid = str(message.from_user.id)
#     msg = await message.reply(text="Video yuklab olinmoqda...")
#     title = yt.title
#     views = yt.views
#     path = 'export/'
#     # yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
#     try:
#         # downloading the video
#         with tqdm(total=100, bar_format="{l_bar}{bar}|") as progressbar:
#             for i in range(4):
#                 progressbar.update(25)
#                 yt.streams.filter(progressive=True,
#                                   file_extension='mp4').order_by('resolution')[-1].download(output_path=path,
#                                                                                             filename=f"{userid}.mp4")
#                 await bot.edit_message_text(text=f"**Yuklab olinmoqda...**\n{progressbar}",
#                                             chat_id=message.from_user.id,
#                                             message_id=msg.message_id, parse_mode="Markdown")
#             await types.ChatActions.upload_video()
#             await bot.edit_message_text(text=f"**Yuklab olindi ✅**\n{progressbar}",
#                                         chat_id=message.from_user.id,
#                                         message_id=msg.message_id, parse_mode="Markdown")
#             try:
#                 await message.reply_video(video=types.InputFile(path_or_bytesio=f"export/{userid}.mp4"),
#                                           caption=f"<b>{title}</b>\n\n{views}")
#             except FileIsTooBig:
#                 await message.answer("Video hajmi katta, uni sizga yubora olmayman")
#     except Exception as e:
#         print(f"Some Error!\n{e}")


@dp.message_handler()
async def down2(message: types.Message):
    task = asyncio.create_task(download_video(link=message.text, name=message.from_user.id))
    await task
    await message.answer("BOshlandi")