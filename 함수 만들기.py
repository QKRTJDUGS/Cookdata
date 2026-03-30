def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

while True: 
    a = 0
    b = 0
    hap = 0

    a = int(input("숫자를 입력하세요"))
    b = int(input("숫자를 입력하세요"))

    hap = plus(a, b)
    print("함수 결과는 %d" % hap)
