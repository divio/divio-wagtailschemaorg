# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from divio_wagtailschemaorg import __version__


setup(
    name='divio-wagtailschemaorg',
    version=__version__,
    description=open('README.rst').read(),
    author='Divio AG',
    author_email='info@divio.com',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[
        'wagtail-schema.org==0.3.0',
    ],
    include_package_data=True,
    zip_safe=False,
)
