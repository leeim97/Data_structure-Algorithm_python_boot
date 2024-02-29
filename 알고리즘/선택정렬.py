from random import randint
## 함수
def findMinIndex(ary) :
    minIdx=0
    for i in range(1,len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i

    return minIdx

## 변수
testAry=[randint(0,100) for _ in range (30)]


## 메인
print(testAry)
minPos= findMinIndex(testAry)
print('제일 작은값 : ',testAry[minPos])
