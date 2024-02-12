from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Input-Armor',
    packages=['input_armor'],
    version='1.1.3',
    license='BSD',

    description='This library provides protection from SQL-injections, DOM-manipulation (HTML injections), CMD injections, and almost all types of injections.',

    author='Armen-Jean Andreasian',
    author_email='armen_andreasian@proton.me',

    url='https://github.com/Armen-Jean-Andreasian',
    keywords=['security', 'injection protection', 'python'],

    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
    ],

    python_requires='>=3.8',

    long_description=long_description,  # Comma added here
    long_description_content_type='text/markdown',
)
