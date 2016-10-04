#/usr/bin/python3.5 
# coding:utf-8

from distutils.core import setup,Extension

module1 =Extension('my_fun',
                    sources=['my_fun.c','output.c'])

setup(name ='my_fun',
        version = '1.0',
        description='This is a test for me ,by Me!',
        ext_modules=[module1])

