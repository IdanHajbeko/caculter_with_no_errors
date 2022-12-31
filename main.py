# this function checks if the input given by the user is a valid number.
def checkIfValidNUm(num, shouldContinue):
    numsAreValid = True
    listOfnum = list(num)
    for checkIfValidNum in listOfnum:
        if checkIfValidNum not in "0123456789.":
            numsAreValid = False
            break

    if numsAreValid == False:
        if num != 'N':
            print("use only numbers")
        if num == 'N':
            shouldContinue = False
            print("exiting...")
        return num, shouldContinue, numsAreValid
    
    # we could simply turn every number to a float but that will give less precision to real numbers.
    if '.' in num:
        num = float(num)

    else:
        num = int(num)
    
    return num, shouldContinue, numsAreValid

def makeCalc(operation, firstNum, secondNum, calcToDo, operationToCheck):
    if operation == operationToCheck:
        print(f"the answer is: {calcToDo}")
        print("-----------------------------")

def main():
    shouldContinue = True
    while shouldContinue:
        firstNum = input("enter first number (enter N to exit): ")
        firstNum, shouldContinue, numsAreValid = checkIfValidNUm(firstNum, shouldContinue)
        if shouldContinue == False or numsAreValid == False:
            continue

        secondNum = input("enter second number (enter N to exit): ")
        secondNum, shouldContinue, numsAreValid = checkIfValidNUm(secondNum, shouldContinue)
        if shouldContinue == False or numsAreValid == False:
            continue
        
        while True:
            operation = input("what do you want to do (+, -, *, /): ")
            if operation not in "+-*/":
                print("choose a valid operator")
                continue
            
            if operation == "/" and secondNum == 0:
                print("cannot divide by zero!")
                print("try again pleas")
                print("-----------------------------")
                break

            makeCalc(operation, firstNum, secondNum, calcToDo)
                        
            shouldContinueToNextLoop = input("do you want to continue? (Y/N) ")
            if shouldContinueToNextLoop == 'Y':
                break
            elif shouldContinueToNextLoop == 'N':
                print("exiting...")
                exit()
            else:
                print("not a valid option, continuing anyways")
                break

            break

main()
