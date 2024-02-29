from random import randint,choice
## 함수
def binSearch(ary,fdata):
    pos = -1

    start=0; end=len(ary)-1

    while start <= end:
        mid =( start + end ) //2
        if fdata > ary[mid]:
            start =mid+1
        elif fdata < ary[mid]:
            end = mid-1
        elif ary[mid]==fdata:
            return mid


    return pos
## 변수
dataAry = [randint(30,190) for _ in range(8)]#가족
findData= choice(dataAry) # 누나키
dataAry.sort()

## 메인
print('배열 -->',dataAry)
position = binSearch(dataAry,findData)
if position != -1:
    print(findData,'는',position,'위치에 있어요')
else:
    print(findData, '는', position, '없어요 ㅜㅜ')