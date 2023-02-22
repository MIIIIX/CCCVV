from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/a6d73fc7ae299f173e69a.jpg")
START_IMG = getenv("START_IMG", "lhttps://telegra.ph/file/a6d73fc7ae299f173e69a.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/W_4_M")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DEV_MIX")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5693859462").split()))


FAILED = "https://telegra.ph/file/a6d73fc7ae299f173e69a.jpg"
