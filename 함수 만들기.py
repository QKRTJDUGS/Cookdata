def plus(v1, v2, v3):
    result = 0
    if v3 =='+':
        result = v1 + v2
    elif v3 == '-':
        resul = v1 - v2
    elif v3 == '*':
        result = v1 * v2
    elif v3 == '/':
        result = v1 / v2
        
        return result

while True: 
    a = 0
    b = 0
    c = 0

    a = int(input("숫자를 입력하세요"))
    b = int(input("숫자를 입력하세요"))
    c = input("사칙연산==> ")
    hap = plus(a, b, c)

    print("함수 결과는 %d" % hap)
