# Ваша задача в этом ката - реализовать функцию, которая вычисляет сумму целых чисел внутри строки.
# Например, в строке "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog" сумма целых чисел равна 3635.
# Примечание: будут проверяться только положительные целые числа.

# Task2 Test example
# test.describe("Example test cases")
#
# exampleTests = (
# ("12.4", 16),
# ("h3ll0w0rld", 3),
# ("2 + 3 = ", 5),
# ("Our company made approximately 1 million in gross revenue last quarter.", 1),
# ("The Great Depression lasted from 1929 to 1939.", 3868),
# ("Dogs are our best friends.", 0),
# ("C4t5 are 4m4z1ng.", 18),
# ("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 3635)
# )
#
# for testString, correctAnswer in exampleTests:
#     test.assert_equals(sum_of_integers_in_string(testString), correctAnswer)

# Start resolving! Good luck!
def sum_of_integers_in_string(s):
    number = []
    sum = 0
    for i in s:
        if i.isdigit():
            if not number or last_isalpha:
                number.append(i)
            else:
                number[-1] += i
        last_isalpha = i.isalpha()
    for i in number:
        sum += int(i)
    print(number)
    return sum
print(sum_of_integers_in_string("12.4"))