num = input("Enter a number: ")
int_num = int(num)

def invert_number(num):
    a = []
    y = []
    for i in num:
        y.append(i)
    actual_length = len(y) - 1
    for i in range(actual_length, -1, -1):
        a.append(y[i])
    inverted_num = "".join(a)
    inverted_int = int(inverted_num)
    return inverted_int
inverted_num = invert_number(num)
if int_num == inverted_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

