from linked import Linkedlist
from DLinkedList import DLinkedList

def Linked_oprea():
    
    
    while True:
        print("1-single linkedlist")
        print("2-Double linkedlist")
        print("3-exit")
        choice_implement = input("Enter your choice: ")
        match choice_implement:
            case "1":
                mlinked = Linkedlist()
                while True:
                    print("1- adding an element (Node)")
                    print("2- to add after data")
                    print("3- to add at index")
                    print("4- to delete data")
                    print("5- to delete at index")
                    print("6- to know how many node do you have")
                    print("7- to find element that you want to check if it's existe")
                    print("8- to find index that you want to check if it's existe")
                    print("9- to display all element")
                    print("10-exit")
                    choice_linked = input("Enter your choice: ")
                   # print("\n"*100)
                    match choice_linked:
                        case "1":
                            mlinked.append(input("Eneter your data: "))
                        case "2":
                            mlinked.addafter(input("Enter your element: "),input("enter the data: "))
                        case "3":
                            mlinked.addat(input("Enter your element: "),int(input("enter an index: ")))
                        case "4":
                            mlinked.delete_Data(input("Enter the data that you want to delete it: "))
                        case "5":
                            mlinked.delete_index(int(input("Enter an indext that you want to delete it: ")))
                        case "6":
                            print(mlinked.get_length())
                        case "7":
                            mlinked.find(input("Enter the element that you want to find it: "))
                        case "8":
                            mlinked.findAt(input("Enter an indext that you want to find it: "))
                        case "9":
                            #print("\n"*100)
                            mlinked.display()
                            

                        case "10":
                            break
            case "2":
                Dlinked = DLinkedList()
                while True:
                    print("1- adding first")
                    print("2- adding last")
                    print("3- deleteFirst")
                    print("4- deleteLast")
                    print("5- deleteItem")
                    print("6- deleteAt")
                    print("7- addAt")
                    print("8- addAfter")
                    print("9-addBefore")
                    print("10- deleteBefore")
                    print("11- display_recursive")
                    choice_linked = input("Enter your choice: ")
                    #print("\n"*100)
                    match choice_linked:
                        case "1":
                            Dlinked.addFirst(input("Eneter your data: "))
                        case "2":
                            Dlinked.addLast(input("Enter your element: "))
                        case "3":
                            Dlinked.deleteFirst()
                        case "4":
                            Dlinked.deleteLast()
                        case "5":
                            Dlinked.deleteItem(int(input("Enter the value that you want to delete: ")))
                        case "6":
                            Dlinked.deleteAt(int(input("Enter the index: ")))
                        case "7":
                            Dlinked.addAt(input("enter the data: "),int(input("Enter the index: ")))
                        case "8":
                            Dlinked.addAfter(input("enter your element: "), int(input("enter the data that you want to add after it: ")))
                        case "9":
                            Dlinked.addBefore(input("enter your element: ") ,int(input("enter the data that you want to add befor it: ")))
                        case "10":
                            Dlinked.deleteBefore(int(input("enter the data that you want to delete befor it: ")))
                        case "11":
                            #print("\n"*100)
                            Dlinked.display()
                            
                        case "12":
                            break
            case "3":
                break
                

