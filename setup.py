# -*- coding: utf-8 -*-
"""
This module contains the tool of Products.SimpleReference
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = (
    read('README.md')
    + '\n' +
    read('docs', 'HISTORY.txt')
    + '\n' +
    read('CONTRIBUTORS.txt'))

tests_require = ['zope.testing']

setup(name='Products.SimpleReference',
      version=version,
      description="SimpleReference Content Type for RichDocument to enable Image/File referencing support",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        'Products.RichDocument',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='Products.SimpleReference.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
