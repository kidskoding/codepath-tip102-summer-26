def prob03(character: str) -> str:
    # 1. Store the valid catchphrases
    # 2. Check if the character string has a valid catchphrase
    #   2.1. If so , simply return the catchphrase
    #   2.2. Otherwise, just return the sorry message
    
    # Time: O(n)
    # Space: O(1)

    catchphrases = {
        "Pooh": "Oh bother!",
        "Tigger": "TTFN: Ta-ta for now!",
        "Eeyore": "Thanks for noticing me.",
        "Christopher Robin": "Silly old bear.",
    }

    if character in catchphrases:
        return catchphrases[character]
    else:
        return f"Sorry! I don't know {character}'s catchphrase!"
