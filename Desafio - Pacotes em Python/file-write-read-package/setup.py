from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='file_write_read',
    version='0.0.1',
    author='Jardson',
    description='Escrita e Leitura de Arquivos.txt',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jardsonalan/file-write-read-package',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.13',
)