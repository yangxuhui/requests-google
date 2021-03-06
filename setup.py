"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""


from setuptools import setup, find_packages
from os import path
from io import open

REQUIRED = [
    'requests', 'feedparser',
]

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='requests-google',
    version='0.0.7',
    description='A simple google related Parsing Package.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yangxuhui/requests-google',
    author='Xuhui Yang',
    author_email='yangxuhui1992@163.com', 
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='google parse crawler',
    packages=find_packages(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=REQUIRED,
    entry_points={
        'console_scripts': [
            'requests_googlenews=requests_google.cli.requests_googlenews:main',
        ],
    },
)
