from random import randint
## 함수
def findMinIndex(ary) :
    minIdx=0
    for i in range(1,len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i

    return minIdx
## 변수
before=[randint(30,190) for _ in range (8)]
after = []

## 메인
print('정렬전-->',before)
for _ in range(len(before)):
    minPos=findMinIndex(before)
    after.append(before[minPos])
    del (before[minPos])
print('정렬후-->',after)
