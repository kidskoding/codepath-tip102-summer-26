from references import Node


def prob04(events: Node | None):
    if not events:
        return None

    prev = events
    current = events
    while current.next:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return events

'''
    prev - current             
    Potion Brewing -> Spell Casting -> Wand Making -> Dragon Taming -> Broomstick Flying

    Spell Casting -> Potion Brewing -> Wand Making -> Dragon Taming -> Broomstick Flying

    Wand Making -> Spell Casting -> Potion Brewing -> Dragon Taming -> Broomstick Flying
'''