def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    result = 1      #k=0,输出1
    while k > 0:
        result = result * n 
        n -= 1
        k -= 1
    return result
   
    "*** YOUR CODE HERE ***"


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    data=k
    time=0   #n以内能被k整除个数
    while data <= n:
        if data % k == 0:
            print(data)        #n以内k的倍数
            time += 1

        data += 1

    return time


    "*** YOUR CODE HERE ***"


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    data=0
    while y > 0:
        data = data + y % 10    #取余，对余数进行累加
        y = y // 10           #右移一位
    return data

    "*** YOUR CODE HERE ***"


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    time=0
    while time < 2 and n > 0:    #若判断出两个连续8，跳出循环，否则继续直到所有数字判断完全
        data = n % 10       #取余判断
        if data == 8:
            time += 1
        else:
            time = 0
        n = n // 10           #右移一位
    if time == 2:
        return True
    else:
        return False


    "*** YOUR CODE HERE ***"



