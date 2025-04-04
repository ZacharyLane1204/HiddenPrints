from setuptools import setup, find_packages

setup(name = 'hidden_prints',
      version = '1.0.0',
      author = 'Zachary G. Lane', 
      author_email = 'zacastronomy@gmail.com', 
      description = 'I hate prints', 
      packages = find_packages(), 
      scripts=['hidden_prints/hidden_prints.py'])