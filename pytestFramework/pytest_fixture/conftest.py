import pytest

@pytest.fixture(scope="class")
def setup():
    print("\nThis is dharnish dp what are you guys doing")
    yield "\nfixture return value"
    print("\nend of the fixture method")
    
    