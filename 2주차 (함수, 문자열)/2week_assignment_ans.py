# 1번
def sum(a, b):
    # your code
    return a+b

# 2번
def sub(a, b):
    # your code
    return a-b

# 3번
def mul(a, b):
    # your code
    return a*b

# 4번
def div(a, b):
    # your code
    return a/b

# 5번
def distance(x1, y1, x2, y2):
    # your code
    return ((x1-y1)**2 + (x2-y2)**2)**0.5

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    # your code
    return lylics[21:31]

# 7번
def reverseStr(string):
    # your code
    return string[::-1]

# 8번
def introduce():
    name = input("이름을 입력하세요 : ")
    hobby = input("취미를 입력하세요 : ")
    univ = input("재학 중인 학교를 입력하세요 : ")
    birth = input("생일을 입력하세요 : ")
    selfint = "제 이름은 {0}입니다. 취미는 {1}입니다. 저는 {2}를 다니고 있습니다. 제 생일은 {3}월 {4}일 입니다.".format(name, hobby, univ, birth[2:4], birth[4:])
    print(selfint)
    return selfint

# 9번
def calc():
    a = int(input("첫 번째 수를 입력하세요 : "))
    b = int(input("두 번째 수를 입력하세요 : "))
    result = "두 수의 합 : {0}\n두 수의 차 : {1}\n두 수의 곱 : {2}\n두 수의 몫 : {3}".format(a+b, a-b, a*b, a//b)
    print(result)
    return result