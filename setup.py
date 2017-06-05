from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='language_detection',
      version='0.1',
      description='The fast language detection module',
      url='https://github.com/salarmohtaj/language_detection',
      author='Salar Mohtaj',
      author_email='salar.mohtaj@aut.ac.ir',
      license='MIT',
	packages=['language_detection'],
	package_data={'language_detection': ['data//*.MODEL']},
	include_package_data=True,
      install_requires=['sklearn'],
      zip_safe=False)
