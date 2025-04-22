from threading import*

def print_num():
    for i in range(1, 11):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

thread_1 = Thread(target=print_num)
thread_2 = Thread(target=print_letters)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()