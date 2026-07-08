"""

Write a function nanana_batman() that accepts an integer x
and prints the string "nanana batman!" where "na" is repeated x times.
Do not use the * operator.

UNDERSTAND:
    * Input: integer x
    * Output: string "nanana batman!" where "na" is repeated x times

    * questions about the problem?

    * edge cases?
    - x < 0 (negative numbers), null, None, invalid data type (string) --> print("error: invalid input")
    - x = 0     (should print "batman!")
    - large numbers


MATCH:    * similar problems?

PLAN
1. validate input
2. initialize result as empty string
3. init a for loop that runs x times and adds "na" to result in each iteration
4. check if x is 0, if so return "batman!"
5. add " batman!" to result and return result

IMPLEMENT:
- see below

REVIEW:
- will do next class

EVALUATE:
    * runtime and complexity? (will do next class)


"""


## IMPLEMENT
# PATTERN: build a string by ACCUMULATING in a loop (the "accumulator" pattern).
# Start empty, add a piece each iteration, return the result at the end.
def nanana_batman(x):
    result = ""              # accumulator: starts empty, grows each loop.

    if x < 0:                # GUARD CLAUSE: handle the bad input first and bail,
        return("error!")     # so the main logic below can assume x >= 0.

    # range(x) yields x times; `_` means "we don't use the loop variable, only
    # the repetition." Each pass concatenates "na" onto result.
    for _ in range(x):
        result += "na"       # x=3 -> "" -> "na" -> "nana" -> "nanana"

    if result:               # a non-empty string is "truthy"; "" is "falsy".
        return(result+ " batman!")   # x >= 1 case
    else:
        return("batman!")    # x == 0 case: loop ran zero times, result is still ""
    # NOTE: this builds the whole thing with the loop, avoiding the "na" * x
    # shortcut the prompt forbids. The final if/else handles the x=0 edge case.


## TESTS
print(nanana_batman(-10))   # try also nanana_batman(0) and nanana_batman(3) to see each branch