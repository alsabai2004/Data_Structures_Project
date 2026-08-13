from .queue_Array import Queue
from .queue_linkd import QueueLinked
def Queue_oprea():    
    
    while True:
        choice_implement = input("Enter your choice: " \
        "1- to choice the Array implemention" \
        "2- to choice the linkedlist implemntion: ")
        match choice_implement:
            case "1":
                queue_ch = Queue(int(input("Enter the size of the stack: ")))
                while True:
                    print("1- adding an element")
                    print("2- delete an element")
                    print("3- to display")
                    print("4- to show the front")
                    print("5- to show the rear")
                    print("6- to delete specifice item")
                    print("7- exit")
                    choice_Array = input("Enter your choice: ")
                    #print("\n"*100)
                    match choice_Array:
                        case "1":
                            queue_ch.Enequeue(int(input("Enter integer only: ")))
                        case "2":
                            queue_ch.dequeue()
                        case "3":
                            queue_ch.display()
                        case "4":
                            print(queue_ch.get_fron())
                        case "5":
                            print(queue_ch.get_rear())
                        case "6":
                            queue_ch.deletitem(int(input("Enter the item that you want to delete it: ")))
                        case "7":
                            break
            case "2":
                    qulinked = QueueLinked()
                    while True:
                        print("1- adding an element (Node)")
                        print("2- delete an element (Node)")
                        print("3- to show all Node")
                        print("4- to show Front")
                        print("5- to show Rear")
                        print("6- exit")
                        choice_linked = input("Enter your choice: ")
                        #print("\n"*100)
                        match choice_linked:
                            case "1":
                                qulinked.Enequeue(input("Eneter your data: "))
                            case "2":
                                qulinked.Dequeue()
                            case "3":
                                qulinked.display()
                            case "4":
                                print(qulinked.getFront())
                            case "5":
                                print(qulinked.getRear())
                            case "6":
                                break
            case "3":
                break

