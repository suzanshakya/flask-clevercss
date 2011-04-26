"""
flask-clevercss
----------

A small Flask extension that makes it easy to use clevercss with your Flask
application.

Links
`````

* `documentation <https://github.com/suzanshakya/flask-clevercss>`_
* `development version
  <https://download.github.com/suzanshakya-flask-clevercss-401a017.tar.gz#egg=flask-clevercss-dev`_


"""
from setuptools import setup


setup(
    name='flask-clevercss',
    version='0.9.1',
    url='https://github.com/suzanshakya/flask-clevercss',
    license='MIT',
    author='Sujan Shakya',
    author_email='suzan.shakya@gmail.com',
    description='A small Flask extension that adds clevercss support to Flask.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
