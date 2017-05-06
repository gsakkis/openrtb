from setuptools import setup
import codecs

try:
    from Cython.Build import cythonize
except ImportError:
    ext_modules = []
else:
    ext_modules = cythonize('openrtb/base.py')


def readme(fn):
    with codecs.open(fn, encoding='utf-8') as f:
        return f.read()


setup(name='openrtb',
      version='0.2.0',
      packages=[
          'openrtb',
      ],
      ext_modules=ext_modules,
      author='Pavel Anossov',
      author_email='anossov@gmail.com',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Libraries',
      ],
      install_requires=[
          'six',
          'tox'
      ],
      url='https://github.com/anossov/openrtb',
      license='BSD',
      description='A set of classes implementing OpenRTB 2.2 and OpenRTB Mobile specifications',
      long_description=readme('README.rst'),
)
