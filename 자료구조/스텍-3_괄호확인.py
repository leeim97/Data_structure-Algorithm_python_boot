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

def peek():
    global SIZE, stack, top
    if isStackEmpty():
        return
    return stack[top]

def checkBracket(ex):
    for i in ex:
        if i == '(':
            push('(')
        elif i == ')':
            data = pop()
            if data == '(':
                pass
            else:
                return False
    if top == -1: # 스텍이 깔끔하게 비었냐
        return True
    else:
        return False

## 변수부
SIZE = 50 # 전역상수, 대문자.
stack = [None for _ in range(SIZE)]
top = -1

## 메인
expr='(())(())(a+b)()'
retTF=checkBracket(expr)

print(expr)
if retTF:
    print('success')
else:
    print('wrong')