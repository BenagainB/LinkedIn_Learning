#Lessons from the Level Up: Python LinkedIn Learning Series
#https://www.linkedin.com/learning/level-up-python
import re

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

#'Go hang a salami - I'm a lasanga hog' will evaluate True
def is_palindrome(phrase):
  forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
  backwards = forwards[::-1]
  return forwards == backwards




