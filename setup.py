from setuptools import setup

setup(name='polycircles',
      version='0.1',
      description='Polycircle: Circle approximations using polygons in WGS84',
      url='https://github.com/adamatan/polycircle',
      author='Adam Matan',
      author_email='adam@matan.name',
      license='MIT',
      packages=['polycircle'],
      include_package_data=True,
      install_requires=['geographiclib'],
      tests_require=['geopy >= 0.99', 'nose >= 1.3.0', 'simplekml >= 1.2.3'],
      test_suite='polycircle.test',
      zip_safe=False)