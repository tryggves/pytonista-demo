# This feature was introduced in python 3.10

x = 5
match x:
    case 0:
        print("Case 0")
    case 5:
        print("Case 5")
    case 10:
        print("Case 10")
    case _:
        print("No match")
    
    
t = "Hello world"
match t:
    case "Hello world":
        print("Got match")
    case _:
        print("No match")
    