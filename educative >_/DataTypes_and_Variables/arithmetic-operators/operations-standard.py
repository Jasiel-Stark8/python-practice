def floor(int1, int2):
    return int1 // int2

user_str = input("Enter 2 numbers separated by space: ")
numbers = [float(x) for x in user_str.split()]
result = floor(numbers[0], numbers[1])
print(result)