import math
import csv
import pandas as pd
import tempfile

# Name: Owen Bochner
# Panther ID: 002-27-6910
# Qustion 1
#------------------------------------------------
print('Question 1')
def fizzBuzz():
    for i in range(1,101):
        if(i % 3 == 0 and i % 5 ==0):
            print("i : " , i , "FizzBuzz")
        elif(i % 3 == 0): 
            print("i : " , i , "Fizz")
        elif(i % 5 == 0):
            print("i : " , i , "Buzz")
        else:
            print("i : " , i)
fizzBuzz()
print('')

# Question 2
#------------------------------------------------
print('Question 2')
def sphereVolume(r):
    x = pow(r, 1)
    y = math.pi
    z = 4/3 * y * x
    return print(z)
print('')
print('The volume is: ')
sphereVolume(10)
print('')

#Question 3
#------------------------------------------------
print('Question 3')
sort = ['Title','Author','ISBN13', 'Page']
dict = [
       {"Title": "1984","Author": "George Orwell", "ISBN13":"987298", "Page":"321" },
       {"Title": "Zenser","Author": "Peter Gabriel", "ISBN13":"156489", "Page":"234" },
       {"Title": "Thidicous","Author": "Barack Obama", "ISBN13":"123548", "Page":"968" },
       {"Title": "Vulten","Author": "Alexander Hoffman", "ISBN13":"945231", "Page":"789" },
       {"Title": "Good Times","Author": "Nathan Depot", "ISBN13":"111945", "Page":"654" } 
       ]

name = "authors.csv"
with open('authors.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = sort)
    writer.writeheader()
    writer.writerows(dict)

print('file name: ', name)
print('')

#Question 4
#------------------------------------------------
print('Question 4')
dictToCSV = pd.read_csv('authors.csv', index_col = 0).to_dict()
print(dictToCSV)
print('file name: ', name)
print('')

#Question 5
#------------------------------------------------
print('Question 5')
def createAndDelete():
    
    temp_file = tempfile.TemporaryFile(delete = False)
    
    sort = ['Title','Author','ISBN13', 'Page']
    dict = [
        {"Title": "1984","Author": "George Orwell", "ISBN13":"987298", "Page":"321" },
        {"Title": "Zenser","Author": "Peter Gabriel", "ISBN13":"156489", "Page":"234" },
        {"Title": "Thidicous","Author": "Barack Obama", "ISBN13":"123548", "Page":"968" },
        {"Title": "Vulten","Author": "Alexander Hoffman", "ISBN13":"945231", "Page":"789" },
        {"Title": "Good Times","Author": "Nathan Depot", "ISBN13":"111945", "Page":"654" } 
        ]

    with open(temp_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = sort)
        writer.writeheader()
        writer.writerows(dict)

    newDictionary = pd.read_csv(temp_file, index_col = 0).to_dict()
    print(newDictionary)

    temp_file.close()

createAndDelete()
    






    
