# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from setuptools.command.test import test as test_command
from sped import __version__

class PyTest(test_command):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # doctest
        import sys
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='python-sped',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    include_package_data=True,
    package_data={
        'sped': ['leiautes/*'],
    },
    version=__version__,
    description='Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para Python.',
    long_description='Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para '
                     'Python.',
    author='Sergio Garcia',
    author_email='sergio@ginx.com.br',
    url='https://github.com/Trust-Code/python-sped',
    download_url='https://github.com/Trust-Code/python-sped/releases',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='sped fiscal contábil contabilidade receita federal',
    install_requires=['six','cchardet','xlsxwriter'],
    tests_require=['pytest'],
    extras_require={
        'dev': ['pylint>=1.9.1'],
        'leiaute': [
            'jupyter>=1.0.0',
            'pyquery>=1.4.0',
        ]
    },
    cmdclass={'test': PyTest},

    # https://stackoverflow.com/questions/4840182/setup-py-and-adding-file-to-bin
    # scripts=['sped/relatorios/efd_relatorios'],

    entry_points = {
        'console_scripts': ['efd_relatorios=sped.relatorios.efd_relatorios:main']
    },
)
