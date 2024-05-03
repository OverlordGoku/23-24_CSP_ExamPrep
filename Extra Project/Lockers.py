#In a high school hallway, there are 100 lockers, all intially closed. A student walks down the hallway and opens every locker. Then another student walks down the hallway and closes every other locker, starting with the second locker. Next, a third student walks down the hallway and changes the state (open if closed, closed if open) of every third locker, starting with the third locker. THis process continues with each subsequent student changing the state of every fourth locker, every fifth locker, and so on, until the 100th studetn changes the state of only the 100th locker.

lockers = []

def swapLocker(locker):
        if lockers[locker] == 0:
            lockers[locker] = 1
        else:
            lockers[locker] = 0

    # Only worried about indexes from 1 - 100
        for elem in range(101):
            lockers.append(0)

        for elem in range(101):
            lockers[elem] = 1


    # Print List
def printList():
        for locker in range(1,101):
            if lockers[locker] ==1:
                print("Locker" + str(locker) + ":" + str(lockers[locker]))

        for elem in range(101):
            if elem % 2 == 0:
                lockers[elem] = 0



        for student in range(3, 101):
                for student > 2:
             if elem % 2 == 0:
                lockers[elem] = 0

    printList()