# Lessons from the Level Up: Python LinkedIn Learning Series
# https://www.linkedin.com/learning/level-up-python
import re
import time
import random
import pickle

def get_prime_factors(number):
    """find prime factors"""
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors


def is_palindrome(phrase):
    """identify a palindrome"""
    #'Go hang a salami - I'm a lasagna hog.' will evaluate True
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


def sort_words(input):
    """sort a string"""
    #sorts 'apple ORANGE banana' as 'apple banana ORANGE' ignoring case for sort but preserving for output
    words = input.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)


def index_all(search_list, item):
    """find all list items"""
    #searching 'example = [[[1,2,3], 2, [1,3]], [1,2,3]]' for presence of 'example, 2' results in '[[0, 0, 1], [0, 1], [1, 1]]'
    #searching 'example = [[[1,2,3], 2, [1,3]], [1,2,3]]' for presence of 'example, [1,2,3]' results in '[[0,0], [1]]'
    index_list = []
    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item):
                index_list.append([index] + i)
    return index_list


def waiting_game(input):
    """play the waiting game"""
    target = random.randint(2,4) #target seconds to wait
    print(f'\nYour target time is {target} seconds.')

    input(' ---Press Enter to begin--- ')
    start = time.perf_counter()

    input(f'\n...Press Enter again after {target} seconds...')
    elapsed = time.perf_counter() - start

    print(f'\nElapsed Time: {elapsed :.3f} seconds')
    if elapsed == target:
        print('(Unbelievable! Perfect timing!)')
    elif elapsed < target:
        print(f'({target - elapsed :.3f} seconds too fast)')
    else:
        print(f'({target - elapsed :.3f} seconds too slow)')


def save_dict(dict_to_save, filepath):
    """save a dictionary"""
    with open(filepath, 'wb') as file:
        pickle.dump(dict_to_save, file)

def load_dict(filepath):
    """load a dictionary"""
    with open(filepath, "rb") as file:
        return pickle.load(file)

"""
test_dict = {1: 'a', 2: 'b', 3: 'c'}
    save_dict(test_dict, "test.pickle")
    recovered = load_dict('test.pickle')
    print(recovered)
"""


def schedule_function():
    """schedule a function"""


def main():
    """ main function """
    test_dict = {1: 'a', 2: 'b', 3: 'c'}
    save_dict(test_dict, "test.pickle")
    recovered = load_dict('test.pickle')
    print(recovered)

if __name__ == '__main__':
    main()