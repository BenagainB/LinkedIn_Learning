#Lessons from the Level Up: Python LinkedIn Learning Series
#https://www.linkedin.com/learning/level-up-python
import re

#find prime factors
def get_prime_factors(number):
  factors = []
  divisor = 2
  while divisor <= number:
    if number % divisor == 0:
      factors.append(divisor)
      number = number // divisor
    else:
      divisor += 1
  return factors

#identify a plindrome
def is_palindrome(phrase):
  #'Go hang a salami - I'm a lasanga hog' will evaluate True
  forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
  backwards = forwards[::-1]
  return forwards == backwards

#sort a string
def sort_words(input):
  #sorts 'apple ORANGE banana' as 'apple banana ORANGE' ignoring case for sort but preserving for output
  words = input.split()
  words = [w.lower() + w for w in words]
  words.sort()
  words = [w[len//2:] for w in words]
  return ' '.join(words)

#find all list items
def index_all(search_list, item):
  #searching 'example = [[[1,2,3], 2, [1,3]], [1,2,3]]' for presence of 'example, 2' resutls in '[[0,0,1], [0,1], [1,1]]'
  #searching 'example = [[[1,2,3], 2, [1,3]], [1,2,3]]' for presence of 'example, [1,2,3]' resutls in '[[0,0], [1]]'
  for index, value in enumerate(search_list):
    if value == item:
      index_list.append([index])
    elif isinstance(search_list[index], list):
      for i in index_all(searchlist[index], item):
        index_list.append([index] + i)
  return index_list




