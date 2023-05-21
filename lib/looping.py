def happy_new_year():
    countdown = ""
    for counter in range(10, 0, -1):
        countdown += str(counter) + "\n"
    countdown += "Happy New Year!"
    return countdown


def fizzbuzz_printer():
    result = ""
    for num in range(1, 101):
        result += fizzbuzz(num) + "\n"
    return result

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def reverse_string(string):
    reversed_str = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_str += string[i]
    return reversed_str

def square_integers(int_list):
    return [num ** 2 for num in int_list]