 
# (1) Write a function that takes in a list of numbers and returns a list with every number doubled.


def double(numbers):
  doubled = []
  for i in range(len(numbers)):
    doubled.append(numbers[i] * 2)
  
  return doubled
  
print(double([1, 2, 3, 4, 5]))
  


# (2) Write a function that takes in a list of words and returns a list of only the words that start with the letter 'a.'


def a(words):
  aWords = []
  for i in range(len(words)):
    if words[i][0] == "a":
      aWords.append(words[i])
  return aWords
  
print(a(["apple", "africa", "food", "salt"]))
      


# (3) Write a function that takes in a list of numbers and returns the number of even numbers in the list.


def even(numbers):
  y = 0
  for i in range(len(numbers)):
    if (numbers[i] % 2) == 0:
      y += 1
  return y
  
print(even([1, 2, 4, 7, 12, 11, 102, 132, 143]))


# (4) Write a function that takes in a list of numbers and returns the sum of the list.


def sumOfList(numbers):
  return sum(numbers)
  
print(sumOfList([1, 2, 3, 100, 201, 210, 502]))


# (5) Write a function that takes in a list of distinct numbers and returns the index of the largest number in the list.


def largest(numbers):
  y = numbers[0]
  for number in numbers:
    if number > y:
      y = number
  return numbers.index(y)
  
print(largest([1, 2, 3, -5, 12, 7]))


# (6) For a given integer N, print all perfect squares less than or equal to N.


def squaresCalc(n):
  squares = []
  x = 1
  while (x*x) <= n:
    squares.append(x)
    x += 1
  return squares
  
print(squaresCalc(100))


# (7) Write a function that takes in an integer N and returns the greatest integer x for which 2^x is less than or equal to N.


def highestSquare(n):
  x = 1
  while (2**x) <= n:
    x += 1
  return x
  
print(highestSquare(100))



# (8) Write a function that takes in an integer N and returns the sum of 1! + 2! + ... + N!.


def factorial(n):
  fact = 1
  sum_facts = 0
  for j in range(1, n+1):
    for i in range(1, j+1):
      fact = i*fact
    sum_facts += fact
    fact = 1
  return sum_facts 
  
print(factorial(5))

# (9) Write a function that takes in a positive integer N and returns its largest divisor less than N.

def divisor(n):
  div = 1
  for i in range(1, n):
    if n % i == 0:
      div = i
  return div

print(divisor(15))
    

# (10) Write a function that takes in a list of integers (positive or negative) and returns the largest product that can be made with any two numbers from the list.
sorted
def largestProduct(list1):
  x = sorted(list1)
  num1 = x[0] * x[1]
  num2 = x[-0] * x[-1]
  if num1 > num1:
    return num1
  else:
    return num2
    
print(largestProduct([1, 2, 3, 4, 10]))
  
# (11) Write a function that takes in a list of integers (positive or negative) and return True if any pair of the numbers in the list sum to 0, Otherwise, return False.


def sum0(list1):
  for i in range(0, len(list1)):
    for j in range(i, len(list1)):
      sum1 = list1[i] + list1[j]
      if sum1 == 0:
        return True
  return False

sum0([1, 2, 3, 4, 14, 5 , 10, 11, -4])

# (12) Write a function that takes in a list of integers and returns a list of the most commonly occurring integers in the list. For example, if the list is [3, 6, 2, 2, 6], the function should return [2,6].

def count(list1):
  counter = 1
  numbers = {}
  returnedNumbers = []
  for num in list1:
    numbers[num] = list1.count(num)
    if list1.count(num) > counter:
      counter = list1.count(num)
      
  for pair in numbers:
    if numbers[pair] == counter:
      returnedNumbers.append(pair)
  return returnedNumbers
  
print(count([1, 2, 3, 6, 5, 7, 10, 2, 10]))



# (13) Write a function that takes in a string and returns the string in reverse order.

def reverse(string):
  newString = ""
  for i in range(4, -1, -1):
    newString += str(string[i])
  return newString
  
print(reverse("hello"))

# (14) Write a function that takes in a string and returns the number of vowels in the string.


def allVowels(string):
  vowels = ["a", "e", "i", "o", "u"]
  vowelCount = 0
  for i in range(len(string)):
    if string[i] in vowels:
      vowelCount += 1
  return vowelCount

print(allVowels("aeiouksjfksjdfkjdsaf"))
        

# (15) Write a function that takes in a list of numbers and returns the number of numbers that appear twice in the list.

def twice(List):
  dictionary = {}
  returns = []
  for number in List:
    if number in dictionary:
      dictionary[number] += 1
    else:
      dictionary[number] = 1
  for number in dictionary:
    if dictionary[number] == 2:
      returns.append(number)
  return len(returns)

print(twice([1, 2, 3, 4, 5, 6, 6, 7, 7, 1]))


# (16) Write a function that takes in a list of distinct numbers and return the list with the smallest and largest numbers swapped.

def swap(List):
  largestNum = max(List)
  smallestNum = min(List)
  for i in range(len(List)):
    if List[i] == largestNum:
      List.insert(i, smallestNum)
      List.remove(List[i]+1)
    elif List[i] == smallestNum:
      List.insert(i, largestNum)
      List.remove(List[i+1])
  return List
      
  
print(swap([1, 2, 3, 4, 5, 6, 4, 5, 10, 2, 1]))