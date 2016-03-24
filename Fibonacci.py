#A class that accepts a number as input and prints out the corresponding
#Fibonacci number

class fibo:

    #Constructor function which sets the data member num 
    def __init__(self, num):
        self.num = num

    def fibo(self, number):
        if (number == 1 or number == 0):
            return 1
        else:
            x = self.fibo(number-1) + self.fibo(number-2)
            return x
		
number = int(input("Enter a number: "))

fib = fibo(number)
print "The", number, "th number of the fibonacci sequence is:", fib.fibo(number-1)
