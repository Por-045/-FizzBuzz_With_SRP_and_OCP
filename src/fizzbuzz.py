def fizzbuzz(number):
    mylist = []
    if number % 3 == 0:
        mylist.append('Fizz')
        if number % 9 == 0: # must above mod 5 condition if then it will conflict with mod 9 and 25 condition
            mylist.append('Fizz')
            if number % 25 == 0:
                mylist.append('BuzzBuzz')
        elif number % 5 == 0:
            mylist.append('Buzz')
    elif number % 5 == 0:
        mylist.append('Buzz')
        if number % 25 == 0:
            mylist.append('Buzz')
    else:
        mylist.append('NoFizzBuzz')

    return ''.join(mylist)
