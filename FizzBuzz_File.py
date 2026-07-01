import numpy as np

def FizzBuzz(start, finish):
    numbers = np.arange(start, finish + 1)

    result = numbers.astype(object)

    result = np.where((numbers % 3 == 0) & (numbers % 5 == 0), 'fizzbuzz', result)
    result = np.where((numbers % 3 == 0) & (numbers % 5 != 0), 'fizz', result)
    result = np.where((numbers % 5 == 0) & (numbers % 3 != 0), 'buzz', result)

    return result.tolist()
