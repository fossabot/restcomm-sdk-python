from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='Restcomm_Python_SDK',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    #  https://packaging.python.org/en/latest/single_source_version.html

      version='0.1',
      description='Restcomm SDK for Python user',
      long_description=readme(),
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
    # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
    #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
    # Pick your license as you wish (should match "license" below)
        'License :: OSI Approved :: MIT License',
    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
      ],

    # What does your project relate to?

      keywords='Restcomm SDK for python',
    # The project's main homepage.
      url='http://github.com/',
    # Author details
      author='MD Sharique',
      author_email='nukles1.07@gmail.com',
      license='MIT',
      test_suite='nose.collector',
      tests_require=['nose'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.

      entry_points = {'console_scripts': ['Restcomm_Python_SDK=Restcomm_Python_SDK.command_line:main']},
      packages=['Restcomm_Python_SDk'],
      install_requires=[
          'requests','xml.etree.ElementTree'
      ],
      include_package_data=True,
      zip_safe=False)