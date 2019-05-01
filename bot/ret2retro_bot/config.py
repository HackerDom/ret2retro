import os

BOT_TOKEN = os.getenv('RET2RETRO_BOT_TOKEN')

PROXY_SETTINGS = {
    'proxy_url': os.getenv('RET2RETRO_TG_PROXY_URL'),
    'urllib3_proxy_kwargs': {
        'username': os.getenv('RET2RETRO_TG_PROXY_USERNAME'),
        'password': os.getenv('RET2RETRO_TG_PROXY_PASSWORD'),
    }
}
