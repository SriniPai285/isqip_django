from percentage import perc

def test_perc():
    percentage=perc(100,10)
    assert percentage==float(10)
    a="10"
    b="0"
    percentage=perc(b,a)
    assert percentage == "invalid"
    printer()
