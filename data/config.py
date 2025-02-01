from environs import Env

env = Env()
env.read_env()

TELEGRAM_BOT_TOKEN = env.str('BOT_TOKEN')
WEB_APP_URL = env.str('WEB_APP_URL')