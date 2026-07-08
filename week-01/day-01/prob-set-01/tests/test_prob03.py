from prob03 import print_catchphrase

def test_prob03():
    assert print_catchphrase("Pooh") == "Oh bother!"
    assert print_catchphrase("Tigger") == "TTFN: Ta-ta for now!"
    assert print_catchphrase("Eeyore") == "Thanks for noticing me."
    assert print_catchphrase("Christopher Robin") == "Silly old bear."
    assert print_catchphrase("Piglet") == (
        "Sorry! I don't know Piglet's catchphrase!"
    )
