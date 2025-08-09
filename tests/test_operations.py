from src.maths_operations import add,sub


def test_test():
    assert add(2,5) ==7
    assert add(-2,-5) == -7
    
def test_sub():
    assert sub(2,5) == 3