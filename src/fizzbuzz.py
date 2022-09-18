def fizzbuzz(number):
    mylist = []
    if number % 3 == 0:
        mylist.append('Fizz')
        if number % 5 == 0:
            mylist.append('Buzz')
        elif number % 9 == 0:
            mylist.append('Fizz')
    elif number % 5 == 0:
        mylist.append('Buzz')
        if number % 25 == 0:
            mylist.append('Buzz')

    return ''.join(mylist)
