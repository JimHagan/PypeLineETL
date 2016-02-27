import os
import sys
import unittest
import logging

from config import dimension_configs, _test_source_conn, ETL_LOG_HOME

if not os.path.exists(ETL_LOG_HOME):
    os.makedirs(ETL_LOG_HOME)
logging.basicConfig(filename=os.path.join(ETL_LOG_HOME,"tests.log"),
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))


def test_dimension_source_queries():
    for dim in dimension_configs:
        if dim["etl_active"]:
            if dim["source_sql"] == "CSV":
                logger.debug("Skipping CSV loadable dimension %s", dim["name"])
                continue
            logger.debug("Testing dimension source query for %s", dim["name"])

            source_cursor = _test_source_conn.cursor()
            source_cursor.execute(dim["source_sql"])

class TestDimensionSourceQueries(unittest.TestCase):
    test_dimension_source_queries()

if __name__ == '__main__':
    test_cases = (TestDimensionSourceQueries,)
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)