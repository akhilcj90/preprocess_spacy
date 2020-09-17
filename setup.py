import setuptools

with open('readme.md') as file:
	long_description = file.read()

setuptools.setup(
	name = 'preprocess_akhilcj90', # this must be unique
    version = '0.1', # any number can provide
    author = 'akhil cj',
    author_mail = 'akhilcj@ymail.com',
    description = 'preprocessing_package',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    classifiers = ['Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    "Operating System :: OS Independent"],
    python_requires = '>=3.5')
