from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/7f1402824c0c70c91fd81.jpg")
START_IMG = getenv("START_IMG", "lhttps://graph.org/file/7f1402824c0c70c91fd81.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/W_4_M")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DEV_MIX")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5693859462").split()))


FAILED = "https://graph.org/file/7f1402824c0c70c91fd81.jpg"
