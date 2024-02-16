import letters


def test_check_alphabet():
    assert letters.check_alphabet('A') == True


def test_check_digit():
    assert letters.check_digit('5') == False



