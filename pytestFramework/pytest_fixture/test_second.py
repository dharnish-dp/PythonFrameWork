import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    
    @pytest.mark.order(2)
    def test_first_inside_class(self):
        print("\nthis is test_first_inside_class")
    
    @pytest.mark.order(1)
    def test_second_inside_class(self):
        print("\nthis is test_second_inside_class")
    
    
    