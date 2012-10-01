from testrunner import HqTestSuiteRunner
from django.core.management.commands import test
from south.management.commands import patch_for_test_db_setup
import sys

SELENIUM_TEST_MODULE = 'tests.selenium'

class TestSuiteRunner(HqTestSuiteRunner):

    def build_suite(self, test_labels, *args, **kwargs):
        import django.test.simple
        orig_test_module = django.test.simple.TEST_MODULE
        django.test.simple.TEST_MODULE = SELENIUM_TEST_MODULE

        try:
            return super(TestSuiteRunner, self).build_suite(test_labels,
                                                            *args, **kwargs)
        except:
            raise

        finally:
            django.test.simple.TEST_MODULE = orig_test_module


class Command(test.Command):
    help = 'Runs the selenium test suite for the specified applications, or the entire site if no apps are specified.'
    args = '[appname ...]'

    def handle(self, *test_labels, **options):
        verbosity = int(options.get('verbosity', 1))
        interactive = options.get('interactive', True)
        failfast = options.get('failfast', False)

        patch_for_test_db_setup()

        test_runner = TestSuiteRunner(verbosity=verbosity,
                                      interactive=interactive,
                                      failfast=failfast)

        failures = test_runner.run_tests(test_labels)

        if failures:
            sys.exit(bool(failures))
