from setuptools import setup, find_packages

setup(
    name='ret2retro',
    version='0.1',
    description='CTF ret2retro web',
    author='Arseny Lezin',
    author_email='arseny.lezin@gmail.com',
    url='https://www.netangels.ru',
    install_requires=[
        'aiohttp-jinja2 == 1.1.0',
        'aiohttp == 3.4.4',
        'pyyaml == 3.13',
        'uvloop == 0.11.3'
    ],
    extras_require={
        'dev': [
            'ipython',
            'ipdb',
        ]
    },
    entry_points={
        'console_scripts': [
            'ret2retro = ret2retro.__main__:main',
        ]
    }
)
