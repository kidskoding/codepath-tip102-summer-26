from prob08 import prob08


def test_prob08():
    assert prob08([("Paris", "2024-07-15"), ("Tokyo", "2024-08-01"), ("Paris", "2024-08-05"),
                   ("New York", "2024-08-10"), ("Tokyo", "2024-08-15"),
                   ("Paris", "2024-08-20")]) == ('Paris', 3)
    assert prob08([("London", "2024-06-01"), ("Berlin", "2024-06-15"), ("London", "2024-07-01"),
                   ("Berlin", "2024-07-10"), ("London", "2024-07-15")]) == ('London', 3)
    assert prob08([("Sydney", "2024-05-01"), ("Dubai", "2024-05-15"), ("Sydney", "2024-05-20"),
                   ("Dubai", "2024-06-01"), ("Dubai", "2024-06-15")]) == ('Dubai', 3)
