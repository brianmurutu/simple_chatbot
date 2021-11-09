def greet(bot_name, birth_year):
    print("\n Hello! My name is {0}.".format(bot_name))
    print("\n I was created by AI Group 6 in {0}.".format(birth_year))


def remind_name():
    print('\n Please, remind me your name.')
    name = input()
    print("\n What a great name you have, {0}!".format(name))


def guess_age():
    print('\n Let me guess your age.')
    print('\n Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("\n Your age is {0}; that's a good age to start programming!".format(age))


def count():
    print('\n Now I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1


def test():
    print("\n Let's test your programming knowledge.")
    print("\n Why do we use methods?")
    print("\n 1. To repeat a statement multiple times.")
    print("\n 2. To decompose a program into several small subroutines.")
    print("\n 3. To determine the execution time of a program.")
    print("\n 4. To interrupt the execution of a program.")

    answer = 2
    guess = int(input())
    while guess != answer:
        print("\n Please, try again.")
        guess = int(input())

    print('\n Completed, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')


def end():
    print('\n Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()
    
greet('Zuhura', '2021')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
