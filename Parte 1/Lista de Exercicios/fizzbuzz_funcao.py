def fizzbuzz(valor):
    if valor % 3 == 0 and valor % 5 != 0:
        return "Fizz"
    if valor % 5 == 0 and valor % 3 != 0:
        return "Buzz"
    if valor % 5 == 0 and valor % 3 == 0:
        return "FizzBuzz"
    else:
        return valor