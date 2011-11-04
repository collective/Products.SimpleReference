import unittest
import doctest

#from zope.testing import doctestunit
#from zope.component import testing, eventtesting

from Testing import ZopeTestCase as ztc

from Products.SimpleReference.tests import base


def test_suite():

    filenames = ['content/simplereference.txt', ]
    tests = []

    for filename in filenames:
        tests.append(ztc.ZopeDocFileSuite(
            filename, package='Products.SimpleReference',
            test_class=base.FunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS))

    return unittest.TestSuite(tests)


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
