def test_always_passes():
    print "This is first test case..."
    a = 10
    b = 20
    print a+b
    assert True

def test_always_fails():
    print "This is second test case..."
    assert True
