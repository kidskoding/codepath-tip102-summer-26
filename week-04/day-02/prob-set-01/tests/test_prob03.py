from prob03 import prob03


def test_prob03():
    assert prob03([("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
                   ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]) == (
        {'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}, 'Accommodation')
    assert prob03([("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
                   ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]) == (
        {'Entertainment': 25.0, 'Food': 40.0, 'Transport': 10.0, 'Accommodation': 40.0}, 'Food')
    assert prob03([("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
                   ("Utilities", 50.0), ("Food", 25.0)]) == (
        {'Utilities': 150.0, 'Food': 75.0, 'Transport': 75.0}, 'Utilities')
