from .array import Arrays
def array_oprea():
    while True:
        print("1-to play array")
        print("2-exit")
        choice_array = input("Enter your choice: ")
        match choice_array:
            case "1":
                array_play = Arrays(int(input("enter the size of your array: ")))
                while True:
                    print("1-to insert")
                    print("2-to display all element")
                    print("3-to delete items")
                    print("4-to delete all items")
                    print("5-to delete all items except the last one")
                    choice_playarray = input("enter your choice: ")
                    match choice_playarray:
                        case "1":
                            array_play.insert()
                        case "2":
                            array_play.display()
                        case "3":
                            array_play.deleteitem(int(input("enter the element ")))
                        case "4":
                            array_play.deleteALLItem(int(input("enter the element ")))
                        case "5":
                            array_play.notfirst(int(input("enter the element ")))
            case "2":
                break
                

