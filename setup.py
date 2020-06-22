from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_chameleon',
    'formencode',
    'pyramid_tm',
    'SQLAlchemy',
    'passlib',
    'itsdangerous',
    'waitress',
     "bcrypt",

    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'transaction',
    'zope.sqlalchemy',
    'wtforms==2.1',  # form library
    'WTForms-SQLAlchemy',
    'webhelpers2==2.0',
    'zope',
    'gnupg',
    'pyramid_simpleform',
    'termcolor',
    'pyramid_sacrud',
    'pystan==2.17.1.0', # for 'fbprophet' 0.6
    'fbprophet', 'openpyxl', 'numpy', 'pandas', 'matplotlib', 'pyqrcode', 'pypng'  # various web building related helpers


    ]
tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
]
setup(name='whereikeepinfo',
      version='0.0.1',
      description='whereikeepinfo',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Alexander Gusak',
      author_email='',
      url='http://whereikeep.info',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='whereikeepinfo',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = whereikeepinfo:main
      [console_scripts]
      init_whereikeepinfo_db = whereikeepinfo.scripts.initializedb:main
      """,


      )
