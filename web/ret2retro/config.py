import os

PROJECT_NAME = 'ret2retro'

PROJECT_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TEMPLATES_PATH = os.path.join(PROJECT_PATH, 'ret2retro', 'views')

RET2RETRO_ENV = os.getenv('RET2RETRO_ENV', 'development')