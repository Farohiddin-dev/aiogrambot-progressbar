import os
from tqdm import tqdm
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from aiogram.utils.exceptions import FileIsTooBig


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n\n"
                         f"Menga video yuboring.\n\n")


@dp.message_handler(content_types='video')
async def video_handler(message: types.Message):
    videoid = message.video.file_unique_id
    if message.video.file_size / 2**20 <= 20:
        msg = await message.reply("<b>Video yuklab olinmoqda...</b>")
        destination = f"export/videos/" \
                      f"{videoid}.mp4".format(os.path.dirname(os.path.realpath(__file__)))
        # Siz uchun kerakli  bo'lgan joy 👇🏻
        with tqdm(total=100, bar_format="{l_bar}{bar}|") as progressbar:
            for i in range(4):
                progressbar.update(25)
                await message.video.download(destination_file=destination)
                await bot.edit_message_text(text=f"**Yuklab olinmoqda...**\n{progressbar}", chat_id=message.from_user.id,
                                            message_id=msg.message_id, parse_mode="Markdown")
        await message.reply("Video qabul qilindi\n"
                            f"file_id = {message.video.file_id}")
    else:
        await message.reply("<b>Kechirasiz video hajmi katta bo'lgani uchun uni yuklay olmayman\n\n"
                            "Limit 20mb</b>")
