import pytest
from time import sleep
run_slow_tests = False

@pytest.mark.order(2)
def test_first_testcase():
    print('This is first testcase')
    assert 1 == 1

@pytest.mark.order(1)
def test_second_testcase():
    print('This is second testcase')
    assert 2 == 2
    
@pytest.mark.xfail()
def test_third_testcase():
    print('This is third testcase')
    assert 2 == 3

@pytest.mark.skip('not required')
def test_fourth_testcase():
    print('This is fourth testcase')
    assert 2 == 2

@pytest.mark.skipif(not run_slow_tests, reason="Skipping slow tests unless enabled")
def test_fifth_testcase():
    print('This is fifth testcase')
    assert 2 == 2

# Check the method is taking less then 2 sec or not, if yes then pass else fail even if pass
@pytest.mark.timeout(2)
def test_sixth_testcase():
    sleep(6)
    print('This is sixth testcase')
    assert 2 == 2

@pytest.mark.integration
def test_integration_scenario():
    print('This is integration test')
    assert True

@pytest.mark.smoke
def test_smoke_scenario():
    print('This is smoke test')
    assert True
