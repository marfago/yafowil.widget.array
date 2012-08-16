from setuptools import setup, find_packages
import sys, os

version = '1.2htug1'
shortdesc = 'Array Widget for YAFOWIL'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()
tests_require = ['yafowil[test]']
fanstatic_require = ['js.jquery']

setup(name='yafowil.widget.array',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Environment :: Web Environment',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'License :: OSI Approved :: BSD License',                    
      ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      license='Simplified BSD',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['yafowil', 'yafowil.widget'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'yafowil>1.99',
      ],
      tests_require=tests_require,
      extras_require = dict(
          test=tests_require,
          fanstatic=fanstatic_require,
      ),
      test_suite="yafowil.widget.array.tests.test_suite",
      entry_points={
          'yafowil.plugin': [
              'register = yafowil.widget.array:register',
              'example = yafowil.widget.array.example:get_example'
          ],
          'fanstatic.libraries': [
              'yafowil.widget.array = yafowil.widget.array:library',
          ],
      },
      )
