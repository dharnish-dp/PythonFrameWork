'''
Explanation of the Code
test_first_method: This test has no dependencies, so it will always run.
test_second_method: This test depends on test_first_method passing. If test_first_method fails, test_second_method will be skipped.
test_third_method: This also depends on test_first_method passing. It will be skipped if test_first_method fails, but since it fails, any test depending on it will also be skipped.
test_fourth_method: This test depends on test_third_method passing. Since test_third_method is expected to fail, test_fourth_method will be skipped as well.
'''

import pytest

class TestDependencyExample:

    @pytest.mark.dependency(name="first")
    def test_first_method(self):
        print("Running test_first_method")
        assert True  

    @pytest.mark.dependency(depends=["first"])
    def test_second_method(self):
        print("Running test_second_method")
        assert True  

    @pytest.mark.dependency(depends=["first"])
    def test_third_method(self):
        print("Running test_third_method")
        assert False  

    @pytest.mark.dependency(depends=["third"])
    def test_fourth_method(self):
        print("Running test_fourth_method")
        assert True  