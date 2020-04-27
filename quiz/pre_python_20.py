"""20. 1부터 100까지 369 게임을 하려고 한다.
3,6,9가 들어가는 부분에는 '짝' 을 출력하고, 
5의 배수에는 '아자' 를 출력,
그외에는 수를 출력하는 프로그램을 만드시오.


<출력>-일렬로 출력

1  2  짝 4  아자  짝 7  8  짝 아자  11  12  짝 14  아자  짝 17  18  짝 아자  21  22  짝 24  아자  짝 27  28  
짝 짝 짝 짝 짝 짝 짝 짝 짝 짝 짝 아자  41  42  짝 44  아자  짝 47  48  짝 아자  51  52  짝 54  아자  짝 57  58
짝 짝 짝 짝 짝 짝 짝 짝 짝 짝 짝 아자  71  72  짝 74  아자  짝 77  78  짝 아자  81  82  짝 84  아자  짝 87  88  
짝 짝 짝 짝 짝 짝 짝 짝 짝 짝 짝 아자

"""

numbers = []
i = range(1, 101)

for i in range(1, 101):
    s = str(i)
    try:
        if (int(s[0]) % 3 == 0) or (int(s[1]) % 3 == 0) or (int(s[2]) % 3 == 0):
            s = "짝"
            numbers.append(s)
        elif i % 5 == 0:
            s = "아자"
            numbers.append(s)
        else:
            numbers.append(s)
    except:
        try:
            if (int(s[0]) % 3 == 0) or (int(s[1]) % 3 == 0):
                s = "짝"
                numbers.append(s)
            elif i % 5 == 0:
                s = "아자"
                numbers.append(s)
            else:
                numbers.append(s)
        except:
            if (int(s[0]) % 3 == 0):
                s = "짝"
                numbers.append(s)
            elif i % 5 == 0:
                s = "아자"
                numbers.append(s)
            else:
                numbers.append(s)

print(",".join(numbers))