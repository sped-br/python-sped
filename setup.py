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
        import sys
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='sped',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    package_data={
        'sped': ['ecd/tabelas/*'],
    },
    version=__version__,
    description='Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para Python.',
    long_description='Biblioteca para geração dos arquivos do Sistema Público de Escrituração Digital (SPED) para '
                     'Python.',
    author='Sergio Garcia',
    author_email='sergio@ginx.com.br',
    url='https://github.com/sped-br/python-sped',
    download_url='https://github.com/sped-br/python-sped/releases',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='sped fiscal contábil contabilidade receita federal',
    install_requires=['six'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
