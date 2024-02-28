## 함수부
def isStackFull():
    global SIZE, stack, top
    if top == SIZE -1:
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def push(data):
    global SIZE,stack, top
    if isStackFull() :
        return print('overflow')
    else:
        top+=1
        stack[top]=data

def pop():
    global SIZE, stack, top
    if isStackEmpty():
        return print('Empty')

    data = stack[top]
    stack[top] = None
    top -= 1
    return data

## 변수부
SIZE = 5 # 전역상수, 대문자.
stack = [None for _ in range(SIZE)]
top = -1

## 메인
push('커피')
push('녹차')
# push('꿀물')
# push('콜라')
# push('환타')
print('바닥 :',stack)

# push('게토레이')
# print('바닥 :',stack)
retData = pop()
print('팝 데이터 -->',retData)
retData = pop()
print('팝 데이터 -->',retData)
