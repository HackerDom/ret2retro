from setuptools import setup

setup(
    name='ret2retro_bot',
    version='0.1',
    description='CTF ret2retro bot',
    author='Arseny Lezin',
    author_email='arseny.lezin@gmail.com',
    install_requires=[
        'python-telegram-bot == 11.1.0',
        'PySocks == 1.6.8'
    ],
    entry_points={
        'console_scripts': [
            'ret2retro_bot = ret2retro_bot.__main__:main',
        ]
    }
)
