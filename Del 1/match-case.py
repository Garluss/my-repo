# simple match case statement
def runMatch():
    num = int(input("Enter a number between 1 and 3: "))
    
    # match case
    match num:
        # pattern 1
        case 1:
            print("One")
        # pattern 2
        case 2:
            print("Two")
        # pattern 3
        case 3:
            print("Three")
        # default pattern
        case _:
            print("Number not between 1 and 3")
            
runMatch()

# python match case with OR operator
def runMatch():
    num = int(input("Enter a number between 1 and 6: "))
    
    # match case
    match num:
        # pattern 1
        case 1 | 2:
            print("One or Two")
        # pattern 2
        case 3 | 4:
            print("Three or Four")
        # pattern 3
        case 5 | 6:
            print("Five or Six")
        # default pattern
        case _:
            print("Number not between 1 and 6")
            
runMatch()

# python match case with if condition
def runMatch():
    num = int(input("Enter a number: "))
    
    # match case
    match num:
        # pattern 1
        case num if num > 0:
            print("Positive")
        # pattern 2
        case num if num < 0:
            print("Negative")
        # default pattern
        case _:
            print("Zero")
            
runMatch()

# match case to check a character in a string
def runMatch():
    myStr = "Hello World"
     
    # match case
    match (myStr[6]):
        case "w":
            print("Case 1 matches")
        case "W":
            print("Case 2 matches")
        case _:
            print("Character not in the string")
            
runMatch()

# python match case with list
def runMatch(mystr):
    
    # match case
    match mystr:
        # pattern 1
        case ["a"]:
            print("a")
        # pattern 2
        case ["a", *b]:
            print(f"a and {b}")
        # pattern 3
        case [*a, "e"] | (*a, "e"):
            print(f"{a} and e")
        # default pattern
        case _:
            print("No data")
            
runMatch([])
runMatch(["a"])
runMatch(["a", "b"])
runMatch(["b", "c", "d", "e"])

# match case with python dictionaryu
def runMatch(dictionary):
    # match case
    match dictionary:
        # pattern 1
        case {"name": n, "age": a}:
            print(f"Name:{n}, Age:{a}")
        # pattern 2
        case {"name": n, "salary": s}:
            print(f"Name:{n}, Salary:{s}")
        # default pattern
        case _ :
            print("Data does not exist")

runMatch({"name": "Jay", "age": 24})
runMatch({"name": "Ed", "salary": 25000})
runMatch({"name": "Al", "age": 27})
runMatch({})