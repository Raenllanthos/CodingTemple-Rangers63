########################
# CULLEN WENZLICK
# CODING QUESTIONS
# DATE: MAY 20 2021
########################

def seeTheAnswer():
    x = input("Enter an input to move on: ")

######################## Question 1
print("Question 1:")
def hello(name):
    print(f"Hello, {name}!")
name = input("What is your name? ")
hello(name)

seeTheAnswer()
######################## Question 2
print("\nQuestion 2:")
def oddNumbers():
    numbers = 0
    while numbers < 101:
        numbers += 1
        if numbers % 2 == 0:
            continue
        else:
            print(numbers)

oddNumbers()
seeTheAnswer()
####################### Question 3
print("\nQuestion 3:")
def maxNumInList(aList):
    print(f"Given list is: {aList}")
    maxNum = max(aList)
    print(f"{maxNum} is the max number in list.")
numberList = [1, 2, 4, 5, 6, 7, 10, 20]
maxNumInList(numberList)

seeTheAnswer()
###################### Question 4
print("\nQuestion 4:")
def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
year = int(input("Enter a leap year: "))
isLeapYear(year)

seeTheAnswer()
############################ Question 5
print("\nQuestion 5:")
def isConsecutive(aList):
    sortedList = sorted(aList)
    print(f"Original list: {aList}")
    print(f"Sorted List: {sortedList}")
    return sortedList == list(range(min(sortedList), max(sortedList)+1))
sortThru = [7, 2, 1 ,5]
print(isConsecutive(sortThru))
sortThru2 = [1, 2, 3, 4, 5, 6, 7]
print(isConsecutive(sortThru2))