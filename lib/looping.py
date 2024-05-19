#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0 :
        print(i)
        i -= 1
        print("Happy New Year!")
      
       
      
    pass

def square_integers(int_list):
    # code goes here!
    square_list = []
    for num in int_list:
        square_list.append(num*num)
    return square_list

    pass

def fizzbuzz():
    # code goes here!
    for i in range (1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)       

    pass
