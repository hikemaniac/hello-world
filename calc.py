'''
Author:        hikemaniac
Created:       20.05.2017
Purpose:       Small calculator
'''

knownType = ("number", "decimal", "integer", "string")
knownOperator = ("+", "-", "/", "*")

def getValidInput(aPrompt, expectedType, validList = knownType):

    if not(expectedType in validList):
        print(expectedType, "unknown!")
        inputvalue = None

    else:
        inputvalue = input(aPrompt)

        if expectedType == "number" or expectedType == "decimal":

            while not(inputvalue.isdecimal()):
                print(expectedType.upper()+" expected!")
                inputvalue = input(aPrompt)

        elif expectedType == "string":
            while not(inputvalue.isdecimal()):
                print(expectedType.upper()+" expected!")
                inputvalue = input(aPrompt)

    return int(inputvalue) # not yet correct, only number values are returned, sigh

# operator check function
def getValidOperator(aPrompt, knownOperatorList):

    operator=input(aPrompt)

    while not(operator in knownOperatorList):

        print("OPERATOR expected!")
        operator=input(aPrompt)

    return operator



### MAIN ###

print("Calculator")

zahl1=getValidInput("Enter a number >>> ", "number")

operator=getValidOperator("Enter an operator >>>", knownOperator)

zahl2=getValidInput("Enter the second number >>> ", "number")


if  operator =="+":
    result = zahl1 + zahl2
elif operator == "-":
    result = zahl1 - zahl2
elif operator == "/":
    result = zahl1 / zahl2
elif operator == "*":
    result = zahl1 * zahl2

print(zahl1, operator, zahl2, "=", result)
