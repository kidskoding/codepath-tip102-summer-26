import pytest
from prob05 import prob05

CONNECTIONS = [
    ["Amber Gill", "Greg O'Shea"],
    ["Amber Gill", "Molly-Mae Hague"],
    ["Greg O'Shea", "Molly-Mae Hague"],
    ["Greg O'Shea", "Tommy Fury"],
    ["Molly-Mae Hague", "Tommy Fury"],
    ["Tommy Fury", "Ovie Soko"],
    ["Curtis Pritchard", "Maura Higgins"],
]


def test_prob05_example():
    assert prob05(CONNECTIONS, 7, "Amber Gill") == {
        "Amber Gill": (1, 10),
        "Greg O'Shea": (2, 9),
        "Molly-Mae Hague": (3, 8),
        "Tommy Fury": (4, 7),
        "Ovie Soko": (5, 6),
        "Curtis Pritchard": (-1, -1),
        "Maura Higgins": (-1, -1),
    }


def test_prob05_start_mid_chain():
    # edges are directed: nobody points back to Amber or Greg
    result = prob05(CONNECTIONS, 7, "Molly-Mae Hague")
    assert result["Molly-Mae Hague"] == (1, 6)
    assert result["Tommy Fury"] == (2, 5)
    assert result["Ovie Soko"] == (3, 4)
    assert result["Amber Gill"] == (-1, -1)
    assert result["Greg O'Shea"] == (-1, -1)
