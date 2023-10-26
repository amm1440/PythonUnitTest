class simple_math_lib:

    def add(*args):
        sum = 0
        for num in args:
            sum += num
        return sum

    def multiply(*args):
        sum = 1
        for num in args:
            sum = sum * num
        return sum