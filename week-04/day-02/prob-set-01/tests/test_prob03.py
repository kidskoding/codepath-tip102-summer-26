import pytest
from prob03 import prob03


@pytest.mark.parametrize("expenses, expected", [
    ([("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
      ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)],
     ({'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}, 'Accommodation')),
    ([("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
      ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)],
     ({'Entertainment': 25.0, 'Food': 40.0, 'Transport': 10.0, 'Accommodation': 40.0}, 'Food')),
    ([("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
      ("Utilities", 50.0), ("Food", 25.0)],
     ({'Utilities': 150.0, 'Food': 75.0, 'Transport': 75.0}, 'Utilities')),
    ([("Food", 20.0)], ({'Food': 20.0}, 'Food')),  # single expense -> that category is also the max
])
def test_prob03(expenses, expected):
    assert prob03(expenses) == expected
