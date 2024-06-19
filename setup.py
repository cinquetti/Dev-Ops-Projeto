from setuptools import setup, find_packages

setup(
    name='minha_calculadora',
    version='1.0.0',
    description='Uma calculadora simples em Python',
    author='Lucas Cinquetti e Carl Betsa',
    author_email='lucas.cinquetti@ges.inatel.br',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'minha_calculadora = minha_calculadora.main:main',
        ],
    },
)
