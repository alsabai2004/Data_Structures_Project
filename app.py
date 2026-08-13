from linkedlist.linked_main import Linked_oprea
from Queue.queue_main  Queue_oprea
from Stack.stack_main import Stack_oprea
from Array.array_main import array_oprea

while True:
    print("1-Array")
    print("2-linkedlist")
    print("3-Stack")
    print("4-Queue")
    print("5-exit")
    your_choice = input("Enter your choice: ")
    match your_choice:
        case "1":
            array_oprea()
        case "2":
            Linked_oprea()
        case "3":
            Stack_oprea()
        case "4":
            Queue_oprea()
        case "5":
            break

