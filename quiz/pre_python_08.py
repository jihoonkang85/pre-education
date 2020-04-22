"""8. 정수를 입력했을 때 짝수인지 홀수인지 핀별하는 코드를 작성하시오

예시
<입력>
정수를 입력하세요 : 14

<출력>
짝수입니다.
"""


def enter():
    num = input("정수를 입력하세요 : ")
    try:
        val = int(num)
        if (val % 2) == 0:
            print("짝수입니다.")
        else:
            print("홀수입니다.")

    except ValueError:
        print("정수가 아닙니다.")
        return enter()


enter()