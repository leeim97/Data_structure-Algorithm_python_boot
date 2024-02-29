## 함수
def openBox():
    global count
    print('상자 열기~~')
    count -= 1
    if count == 0:
        return print('선물!!')
    openBox()
    print('상자닫기')
## 메인
count= 10
openBox()