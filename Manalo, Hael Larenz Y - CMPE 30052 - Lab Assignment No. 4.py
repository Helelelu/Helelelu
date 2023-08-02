elementList = []

def selectionSorting():
      try:
            numberofElements = int(input("How many elements are there on your list?: "))
            elementType = int(input("Enter the type of elements [1] Numbers   [2] Letters : "))
            if elementType == 1:
                  try:
                        sortingMode = int(input("Enter sorting mode [1] Ascending   [2] Descending : "))
                        if sortingMode == 1:
                              print("Enter your {} integers".format(numberofElements))
                              while True:
                                    try:
                                          if len(elementList) <= numberofElements - 1:
                                                elements = int(input())
                                                elementList.append(elements)
                                          else:
                                                ascendingSelectionSort()
                                                print("Sorted elements using Ascending Selection Sort:\n",
                                                      elementList,'\n')
                                                input("======Press Enter to continue======")
                                                elementList.clear()
                                                break
                                    except ValueError:
                                          print("=====Please input whole numbers only=====\n")
                                          elementList.clear()
                                          break
                        elif sortingMode == 2:
                              print("Enter your {} integers".format(numberofElements))
                              while True:
                                    try:
                                          if len(elementList) <= numberofElements - 1:
                                                elements = int(input())
                                                elementList.append(elements)
                                          else:
                                                descendingSelectionSort()
                                                print("Sorted elements using Descending Selection Sort:\n",
                                                      elementList, '\n')
                                                input("======Press Enter to continue======")
                                                elementList.clear()
                                                break
                                    except ValueError:
                                          print("=====Please input whole numbers only=====\n")
                                          elementList.clear()
                                          break
                  except ValueError:
                        print("=====Please input a valid option=====\n")

            elif elementType == 2:
                  try:
                        sortingMode = int(input("Enter sorting mode [1] A to Z   [2] Z to A : "))
                        if sortingMode == 1:
                              print("Enter your {} letters (lowercase only)".format(numberofElements))
                              while True:
                                    if len(elementList) <= numberofElements - 1:
                                          elements = str(input())
                                          elementList.append(elements)
                                          if not elements.isalpha():
                                                print("=====Please input letters only=====\n")
                                                elementList.clear()
                                                break
                                    else:
                                          ascendingSelectionSort()
                                          print("Sorted elements using Ascending Selection Sort:\n",
                                                elementList, '\n')
                                          input("======Press Enter to continue======")
                                          elementList.clear()
                                          break
                        elif sortingMode == 2:
                              print("Enter your {} letters (lowercase only)".format(numberofElements))
                              while True:
                                    if len(elementList) <= numberofElements - 1:
                                          elements = str(input())
                                          elementList.append(elements)
                                          if not elements.isalpha():
                                                print("=====Please input letters only=====\n")
                                                elementList.clear()
                                                break
                                    else:
                                          descendingSelectionSort()
                                          print("Sorted elements using Descending Selection Sort:\n",
                                                elementList, '\n')
                                          input("======Press Enter to continue======")
                                          elementList.clear()
                                          break
                  except ValueError:
                        print("=====Please input a valid option=====\n")

      except ValueError:
            print("=====Please input a valid option=====\n")
def ascendingSelectionSort():
    for i in range(0, len(elementList) - 1):
        minimumIndex = i
        for j in range(i + 1, len(elementList)):
            if elementList[j] < elementList[minimumIndex]:
                minimumIndex = j
        elementList[i], elementList[minimumIndex] = elementList[minimumIndex], elementList[i]
        print("Pass ", i + 1, ":", elementList)
def descendingSelectionSort():
    for i in range(0, len(elementList) - 1):
        minimumIndex = i
        for j in range(i + 1, len(elementList)):
            if elementList[j] > elementList[minimumIndex]:
                minimumIndex = j
        elementList[i], elementList[minimumIndex] = elementList[minimumIndex], elementList[i]
        print("Pass ", i + 1, ":", elementList)

def bubbleSorting():
      try:
            numberofElements = int(input("How many elements are there on your list?: "))
            elementType = int(input("Enter the type of elements [1] Numbers   [2] Letters : "))
            if elementType == 1:
                  try:
                        sortingMode = int(input("Enter sorting mode [1] Ascending   [2] Descending : "))
                        if sortingMode == 1:
                              print("Enter your {} integers".format(numberofElements))
                              while True:
                                    try:
                                          if len(elementList) <= numberofElements - 1:
                                                elements = int(input())
                                                elementList.append(elements)
                                          else:
                                                ascendingBubbleSort()
                                                print("Sorted numbers using Ascending Bubble Sort:\n",
                                                      elementList, '\n')
                                                input("======Press Enter to continue======")
                                                elementList.clear()
                                                break
                                    except ValueError:
                                          print("=====Please input whole numbers only=====\n")
                                          elementList.clear()
                                          break
                        elif sortingMode == 2:
                              print("Enter your {} integers".format(numberofElements))
                              while True:
                                    try:
                                          if len(elementList) <= numberofElements - 1:
                                                elements = int(input())
                                                elementList.append(elements)
                                          else:
                                                descendingBubbleSort()
                                                print("Sorted numbers using Descending Bubble Sort:\n",
                                                      elementList, '\n')
                                                input("======Press Enter to continue======")
                                                elementList.clear()
                                                break
                                    except ValueError:
                                          print("=====Please input whole numbers only=====\n")
                                          elementList.clear()
                                          break
                  except ValueError:
                        print("=====Please input a valid option=====\n")

            elif elementType == 2:
                  try:
                        sortingMode = int(input("Enter sorting mode [1] A to Z   [2] Z to A : "))
                        if sortingMode == 1:
                              print("Enter your {} letters (lowercase only)".format(numberofElements))
                              while True:
                                    if len(elementList) <= numberofElements - 1:
                                          elements = str(input())
                                          elementList.append(elements)
                                          if not elements.isalpha():
                                                print("=====Please input letters only=====\n")
                                                elementList.clear()
                                                break
                                    else:
                                          ascendingBubbleSort()
                                          print("Sorted letters using Ascending Bubble Sort:\n",
                                                elementList, '\n')
                                          input("======Press Enter to continue======")
                                          elementList.clear()
                                          break
                        elif sortingMode == 2:
                              print("Enter your {} letters (lowercase only)".format(numberofElements))
                              while True:
                                    if len(elementList) <= numberofElements - 1:
                                          elements = str(input())
                                          elementList.append(elements)
                                          if not elements.isalpha():
                                                print("=====Please input letters only=====\n")
                                                elementList.clear()
                                                break
                                    else:
                                          descendingBubbleSort()
                                          print("Sorted letters using Descending Bubble Sort:\n",
                                                elementList, '\n')
                                          input("======Press Enter to continue======")
                                          elementList.clear()
                                          break
                  except ValueError:
                        print("=====Please input a valid option=====\n")

      except ValueError:
            print("=====Please input a valid option=====\n")
def ascendingBubbleSort():
    for i in range (len(elementList)):
        for j in range (0, len(elementList) - i - 1):
            if elementList[j] > elementList[j + 1]:
                elementList[j], elementList[j + 1] = elementList[j + 1], elementList[j]
        print("Pass", i + 1, ":", elementList)
def descendingBubbleSort():
    for i in range (len(elementList)):
        for j in range (0, len(elementList) - i - 1):
            if elementList[j] < elementList[j + 1]:
                elementList[j], elementList[j + 1] = elementList[j + 1], elementList[j]
        print("Pass", i + 1, ":", elementList)

def insertionSorting():
      try:
            numberofElements = int(input("How many elements are there on your list?: "))
            elementType = int(input("Enter the type of elements [1] Numbers   [2] Letters : "))
            if elementType == 1:
                  try:
                        sortingMode = int(input("Enter sorting mode [1] Ascending   [2] Descending : "))
                        if sortingMode == 1:
                              print("Enter your {} integers".format(numberofElements))
                              while True:
                                    try:
                                          if len(elementList) <= numberofElements - 1:
                                                elements = int(input())
                                                elementList.append(elements)
                                          else:
                                                ascendingInsertionSort()
                                                print("Sorted numbers using Ascending Insertion Sort:\n",
                                                      elementList, '\n')
                                                input("======Press Enter to continue======")
                                                elementList.clear()
                                                break
                                    except ValueError:
                                          print("=====Please input whole numbers only=====\n")
                                          elementList.clear()
                                          break
                        elif sortingMode == 2:
                              print("Enter your {} integers".format(numberofElements))
                              while True:
                                    try:
                                          if len(elementList) <= numberofElements - 1:
                                                elements = int(input())
                                                elementList.append(elements)
                                          else:
                                                descendingInsertionSort()
                                                print("Sorted numbers using Descending Insertion Sort:\n",
                                                      elementList, '\n')
                                                input("======Press Enter to continue======")
                                                elementList.clear()
                                                break
                                    except ValueError:
                                          print("=====Please input whole numbers only=====\n")
                                          elementList.clear()
                                          break
                  except ValueError:
                        print("=====Please input a valid option=====\n")

            elif elementType == 2:
                  try:
                        sortingMode = int(input("Enter sorting mode [1] A to Z   [2] Z to A : "))
                        if sortingMode == 1:
                              print("Enter your {} letters".format(numberofElements))
                              while True:
                                    if len(elementList) <= numberofElements - 1:
                                          elements = str(input())
                                          elementList.append(elements)
                                          if not elements.isalpha():
                                                print("=====Please input letters only=====\n")
                                                elementList.clear()
                                                break
                                    else:
                                          ascendingInsertionSort()
                                          print("Sorted letters using Ascending Insertion Sort:\n",
                                                elementList, '\n')
                                          input("======Press Enter to continue======")
                                          elementList.clear()
                                          break
                        elif sortingMode == 2:
                              print("Enter your {} letters".format(numberofElements))
                              while True:
                                    if len(elementList) <= numberofElements - 1:
                                          elements = str(input())
                                          elementList.append(elements)
                                          if not elements.isalpha():
                                                print("=====Please input letters only=====\n")
                                                elementList.clear()
                                                break
                                    else:
                                          descendingInsertionSort()
                                          print("Sorted letters using Descending Insertion Sort:\n",
                                                elementList, '\n')
                                          input("======Press Enter to continue======")
                                          elementList.clear()
                                          break
                  except ValueError:
                        print("=====Please input a valid option=====\n")

      except ValueError:
            print("=====Please input a valid option=====\n")
def ascendingInsertionSort():
    for i in range (1, len(elementList)):
        j = i
        while elementList[j - 1] > elementList[j] and j > 0:
            elementList[j - 1], elementList[j] = elementList[j], elementList[j - 1]
            j -= 1
        print("Pass", i, ":", elementList)
def descendingInsertionSort():
    for i in range (1, len(elementList)):
        j = i
        while elementList[j - 1] < elementList[j] and j > 0:
            elementList[j - 1], elementList[j] = elementList[j], elementList[j - 1]
            j -= 1
        print("Pass", i, ":", elementList)

def mergeSorting():
      try:
            numberofElements = int(input("How many elements are there on your list?: "))
            elementType = int(input("Enter the type of elements [1] Numbers   [2] Letters : "))
            if elementType == 1:
                  try:
                        sortingMode = int(input("Enter sorting mode [1] Ascending   [2] Descending : "))
                        if sortingMode == 1:
                              print("Enter your {} integers".format(numberofElements))
                              while True:
                                    try:
                                          if len(elementList) <= numberofElements - 1:
                                                elements = int(input())
                                                elementList.append(elements)
                                          else:
                                                ascendingMergeSort(elementList)
                                                print("Sorted numbers using Ascending Merge Sort:\n",
                                                      elementList, '\n')
                                                input("======Press Enter to continue======")
                                                elementList.clear()
                                                break
                                    except ValueError:
                                          print("=====Please input whole numbers only=====\n")
                                          elementList.clear()
                                          break
                        elif sortingMode == 2:
                              print("Enter your {} integers".format(numberofElements))
                              while True:
                                    try:
                                          if len(elementList) <= numberofElements - 1:
                                                elements = int(input())
                                                elementList.append(elements)
                                          else:
                                                descendingMergeSort(elementList)
                                                print("Sorted numbers using Descending Merge Sort:\n",
                                                      elementList, '\n')
                                                input("======Press Enter to continue======")
                                                elementList.clear()
                                                break
                                    except ValueError:
                                          print("=====Please input whole numbers only=====\n")
                                          elementList.clear()
                                          break
                  except ValueError:
                        print("=====Please input a valid option=====\n")

            elif elementType == 2:
                  try:
                        sortingMode = int(input("Enter sorting mode [1] A to Z   [2] Z to A : "))
                        if sortingMode == 1:
                              print("Enter your {} letters (lowercase only)".format(numberofElements))
                              while True:
                                    if len(elementList) <= numberofElements - 1:
                                          elements = str(input())
                                          elementList.append(elements)
                                          if not elements.isalpha():
                                                print("=====Please input letters only=====\n")
                                                elementList.clear()
                                                break
                                    else:
                                          ascendingMergeSort(elementList)
                                          print("Sorted letters using Ascending Merge Sort:\n",
                                                elementList, '\n')
                                          input("======Press Enter to continue======")
                                          elementList.clear()
                                          break
                        elif sortingMode == 2:
                              print("Enter your {} letters (lowercase only)".format(numberofElements))
                              while True:
                                    if len(elementList) <= numberofElements - 1:
                                          elements = str(input())
                                          elementList.append(elements)
                                          if not elements.isalpha():
                                                print("=====Please input letters only=====\n")
                                                elementList.clear()
                                                break
                                    else:
                                          descendingMergeSort(elementList)
                                          print("Sorted letters using Descending Merge Sort:\n",
                                                elementList, '\n')
                                          input("======Press Enter to continue======")
                                          elementList.clear()
                                          break
                  except ValueError:
                        print("=====Please input a valid option=====\n")

      except ValueError:
            print("=====Please input a valid option=====\n")
def ascendingMergeSort(elementList):
    if len(elementList) > 1:
        mid = len(elementList)//2
        firstArray = elementList[:mid]
        secondArray = elementList[mid:]
        print("First Array: {}  ||  Second Array: {}".format(firstArray, secondArray))
        ascendingMergeSort(firstArray)
        ascendingMergeSort(secondArray)
        print("First Array: {}  ||  Second Array: {}".format(firstArray, secondArray))
        i = 0
        j = 0
        k = 0
        while i < len(firstArray) and j < len(secondArray):
            if firstArray[i] <= secondArray[j]:
                elementList[k] = firstArray[i]
                i += 1
                k += 1
            else:
                elementList[k] = secondArray[j]
                j += 1
                k += 1
        while i < len(firstArray):
            elementList[k] = firstArray[i]
            i += 1
            k += 1
        while j < len(secondArray):
            elementList[k] = secondArray[j]
            j += 1
            k += 1
def descendingMergeSort(elementList):
    if len(elementList) > 1:
        mid = len(elementList)//2
        firstArray = elementList[:mid]
        secondArray = elementList[mid:]
        print("First Array: {}  ||  Second Array: {}".format(firstArray, secondArray))
        ascendingMergeSort(firstArray)
        ascendingMergeSort(secondArray)
        print("First Array: {}  ||  Second Array: {}".format(firstArray, secondArray))
        i = 0
        j = 0
        k = 0
        while i < len(firstArray) and j < len(secondArray):
            if firstArray[i] <= secondArray[j]:
                elementList[k] = firstArray[i]
                i += 1
                k += 1
            else:
                elementList[k] = secondArray[j]
                j += 1
                k += 1
        while i < len(firstArray):
            elementList[k] = firstArray[i]
            i += 1
            k += 1
        while j < len(secondArray):
            elementList[k] = secondArray[j]
            j += 1
            k += 1
        firstArray.reverse()
        secondArray.reverse()
        print("First Array: {}  ||  Second Array: {}".format(firstArray, secondArray))
        elementList.reverse()
      
def interface():
      while True:
            print("||========SORTING ALGORITHM APPLICATION========||\n"
                  "||       Code by: Manalo, Hael Larenz Y.       ||\n"
                  "||                BSCOE 2 - 5                  ||\n"
                  "||                                             ||\n"
                  "||                 MAIN MENU                   ||\n"
                  "||          [1] Selection Sorting              ||\n"
                  "||          [2] Bubble Sorting                 ||\n"
                  "||          [3] Insertion Sorting              ||\n"
                  "||          [4] Merge Sorting                  ||\n"
                  "||          [5] Exit                           ||\n"
                  "||                                             ||\n"
                  "||      Select the number of your desired      ||\n"
                  "||               Sorting Method                ||\n"
                  "||                                             ||\n"
                  "||=============================================||")
            try:
                  option = int(input("Enter an option: "))
                  if option == 1:
                        selectionSorting()
                  elif option == 2:
                        bubbleSorting()
                  elif option == 3:
                        insertionSorting()
                  elif option == 4:
                        mergeSorting()
                  elif option == 5:
                        print("||=========================================||\n"
                              "||  Thank you for using the application!   ||\n"
                              "||=========================================||")
                        break
                  else:
                        print("======Please input a valid option======")
            except ValueError:
                  print("===Please input a valid option===\n")

interface()
