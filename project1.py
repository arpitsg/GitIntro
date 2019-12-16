def fib(number_for_fibonacci):
    
	if number_for_fibonacci==1 or number_for_fibonacci==0:
	    return 1
	    
	return (fib(number_for_fibonacci-1)+fib(number_for_fibonacci-2))


def is_prime(number_to_check):
    
    return #boolean value


def reverse_string(string_to_be_reversed):
	# Add code here
    return string_to_be_reversed[::-1]
	# return reversed_string

#Take input for fib in variable a
k=int(input())

print(fib(k))


#Take input for is_prime in variable b

print(is_prime(b))


#Take input for reverse in variable c 

print(reversed_string(c))
