""" Que: 1 """

""" def findLargestValue(values):
    if len(values) < 1:
       return "There is no element found"

    result=values[0]
    for val in values:
        if val > result:
            result=val
    return result



values=[]

print(findLargestValue(values)) """


""" Que: 2 """

""" def findSecondLargestValue(values):

    if len(values) < 1:
       return "There is no element found"
    if len(values) < 2:
       return "There is no second largest exist"

    firstLargest=None
    secondLargest=None
    for val in values:
        if val is None:
            continue

        if firstLargest is None or val > firstLargest:
            secondLargest=firstLargest
            firstLargest=val
        elif val !=firstLargest and (secondLargest is None or val > secondLargest):
            secondLargest=val
    
    if secondLargest is None:
        return "No second largest exists"

    return secondLargest



values=[-1,-2,-3,-4,-5]

print(findSecondLargestValue(values)) """


""" Que: 3 """

""" def determineDecreasingOrder(values):

    for i in range(len(values)-1):
        if values[i] > values[i + 1]:
            return False
    return True

values=[2,1,2,3,4,5]

print(determineDecreasingOrder(values)) """


""" Que: 4 """

""" def rotateLeft(values, k):

    k = k % len(values)

    first_part = values[:k]

    second_part = values[k:]

    return second_part + first_part


values = [1,2,3,4,5]

print(rotateLeft(values, 8)) """


""" Que: 4 """

def moveZeroToEnd(values):

    left=0

    for right in range(len(values)):
        if values[right] !=0:
            values[left],values[right]=values[right],values[left]
            left+=1
    return values

values = [0,0,0,1,2,4,4]

print(moveZeroToEnd(values))