import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'waitress',
    'PIL',
    'pycrypto',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'zope.sqlalchemy',
    'docutils',
    'WebHelpers==1.3',
    'pyramid_jinja2',
    'pyramid_handlers',
    'pyramid_beaker',
    'WebError',
    'pyramid_simpleform',
    'tw.forms == 0.9.9',
    'jsonpickle',
    'velruse',
    'redis',
    'mock',
    'alembic',
    'pandas',
    'matplotlib',
    'gunicorn',
    'Paste',
    ]

setup(name='bmwcrm',
      version='0.0',
      description='bmwcrm',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="bmwcrm",
      entry_points="""\
      [paste.app_factory]
      main = bmwcrm:main
      """,
      paster_plugins=['pyramid'],
      )
