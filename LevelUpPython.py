# Lessons from the Level Up: Python LinkedIn Learning Series
# https://www.linkedin.com/learning/level-up-python
import re
import time
import random
import pickle
import sched
import smtplib
import collections
from random import randint
from collections import Counter

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


def schedule_function(event_time, function, *args):
    """schedule a function"""
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
    s.run()

"""
>>> import time
>>> from LevelUpPython import schedule_function
>>> schedule_function(time.time() +1, print, 'Howdy!')
print() scheduled for Wed Mar 29 09:21:55 2023
Howdy!
"""

"""
>>> import time
>>> from LevelUpPython import schedule_function
>>> schedule_function(time.time() +1, print, 'Howdy!', 'How are you?')
print() scheduled for Wed Mar 29 09:21:55 2023
Howdy! How are you?
"""


SENDER_EMAIL = 'example@gmail.com'
SENDER_PASSWORD = 'emailPASSWORD'
# receiver_email = 'bobBlahLawBlog@gmail.com'
# subject = "Hey, Buddy"
# body = "Long time no see. Send me a reply when you get back to your office."

def send_email(receiver_email, subject, body):
    """send an email"""
    # may require security configurations to allow privileged access to email client
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        # replace 'smtp.office365.com' with your email server name
        # replace 587 with your server's port number
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)


def roll_dice(*dice, num_trials=1_000_000):
    """simulate dice"""
    counts = Counter()
    for _ in range(num_trials):
        counts[sum((randint(1, sides) for sides in dice))] += 1
    
    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice) + 1):
        print(f'{outcome}\t{counts[outcome] * 100 / num_trials :0.2f}%')

"""
>roll_dice(4, 6, 6)

OUTCOME PROBABILITY
3       0.69%
4       2.08%
5       4.17%
6       6.97%
7       9.67%
8       12.46%
9       13.85%
10      13.86%
11      12.53%
12      9.76%
13      6.96%
14      4.18%
15      2.11%
16      0.70%
"""
"""
>roll_dice(6,8)

OUTCOME PROBABILITY
2       2.06%
3       4.18%
4       6.26%
5       8.31%
6       10.45%
7       12.46%
8       12.50%
9       12.47%
10      10.47%
11      8.31%
12      6.27%
13      4.18%
14      2.07%
"""


def count_words(filepath):
    """count unique words"""
    with open(filepath, 'r', encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\nTotal Words: {len(all_words)}')

        word_counts = collections.Counter(all_words)

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')

"""
>count_words("Sample.txt")

Total Words: 255

Top 20 Words:
THE     16
OF      13
IN      9
TO      7
DISNEY  6
A       6
IGER    5
COMPANY 5
WILL    5
000     5
S       5
SAID    4
LAYOFFS 4
AND     4
7       3
JOBS    3
ROUND   3
CNN     2
BOB     2
HIS     2
"""


def generate_passphrase(num)
"""generate a password"""


"""merge csv files"""


"""solve a sudoku"""


"""build a zip archive"""


"""download sequential files"""

def main():
    """ main function """
    count_words("Sample.txt")

if __name__ == '__main__':
    main()