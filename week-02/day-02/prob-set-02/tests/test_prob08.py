import pytest
from prob08 import prob08


# answer may be returned in any order, so compare sorted
@pytest.mark.parametrize("tourist_list1, tourist_list2, expected", [
    (["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"],
     ["Colosseum", "Trevi Fountain", "Pantheon", "Eiffel Tower"], ["Eiffel Tower"]),
    (["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Disneyland"],
     ["Disneyland", "Eiffel Tower", "Notre-Dame"], ["Eiffel Tower"]),
    (["beach", "mountain", "forest"], ["mountain", "beach", "forest"], ["mountain", "beach"]),
])
def test_prob08(tourist_list1, tourist_list2, expected):
    assert sorted(prob08(tourist_list1, tourist_list2)) == sorted(expected)
