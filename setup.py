from setuptools import setup
import os

fPath = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(fPath, "README.md")) as rFile:
	long_des = rFile.read()

setup(name='mp3wav',
	version='0.1',
	description='MP3 to Wav Converter',
	long_description = long_des,
	url='',
	author='Kapil Garg',
	author_email='kapilgarg1996@gmail.com',
	license='MIT',
	classifiers=[
		'Development Status :: 0.1-Beta',
		'Topic :: Audio Format Converter'
	],
	scripts = ['mp3wav/bin/mp3wav'],
	keywords='mp3 wav converter',
	packages=['mp3wav', 'mp3wav/exceptions'],
        test_suite='py.test',
        tests_require=['pytest']
	zip_safe=False)
