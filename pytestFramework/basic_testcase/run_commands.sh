# Be in pytestFramework/basic_testcase dir 
# To run all the test case in all python file under pytestFramework dir 
pytest

# To print verbal statement in terminal
pytest -v

# To output the print statement 
pytest -s

# Combine both verbal and print
pytest -vs

# To run the all test case in basic_test.py
pytest basic_test.py

# To run the test_second_method test case in the basic_test.py
pytest -vs basic_test.py::test_second_method

# To select based on the name matching in basic_test.py
pytest -vs -k testcase basic_test.py

# To run the test_third_method test case which is in TestNew class in the basic_test.py
pytest -vs basic_class_test.py::TestNew::test_third_method


 