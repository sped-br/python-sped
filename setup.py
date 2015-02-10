from setuptools import setup, find_packages
from sped import __version__

setup(
    name='sped',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    version=__version__,
    description='Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para Python.',
    author='Sergio Garcia',
    author_email='sergio@ginx.com.br',
    url='https://github.com/sped-br/python-sped',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='sped fiscal contábil contabilidade receita federal',
)
