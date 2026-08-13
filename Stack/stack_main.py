from .stack_Array import Stack
from .stack_linkedlist import Stack_linkedlist 
def Stack_oprea():
    
    
    while True:
        choice_implement = input("Enter your choice: " \
        "\n1- to choice the Array implemention" \
        "\n2- to choice the linkedlist implemntion: ")
        #print("\n"*100)
        match choice_implement:
            case "1":
                st1 = Stack(int(input("Enter the size of the stack: ")))
                while True:
                    print("1- adding an element")
                    print("2- delete an element")
                    print("3- to see the top element")
                    print("4- show all element")
                    print("5- break")
                    choice_Array = input("Enter your choice: ")
                    #print("\n"*100)
                    match choice_Array:
                        case "1":
                            st1.push(int(input("Enter integer only: ")))
                        case "2":
                            st1.pop()
                        case "3":
                            #print("\n"*100)
                            print(st1.peek())
                        case "4":
                            #print("\n"*100)
                            st1.display()
                            
                        case "5":
                            print("invalid choice")
                            break
            case "2":
                stlinked = Stack_linkedlist()
                while True:
                    print("1- adding an element (Node)")
                    print("2- delete an element (Node)")
                    print("3- to see the top element (Node)")
                    print("4-exit")
                    choice_linked = input("Enter your choice: ")
                    #print("\n"*100)
                    match choice_linked:
                        case "1":
                            stlinked.push(input("Eneter your data: "))
                        case "2":
                            stlinked.pop()
                        case "3":
                            #print("\n"*100)
                            print(stlinked.peek())
                    
                        case "4":
                            print("invalid choice")
                            break
            case "3":
                break

