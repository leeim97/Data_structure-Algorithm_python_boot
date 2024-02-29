from random import randint


## 함수
def selectSort(ary):
    n = len(ary)

    for i in range(n - 1):  # 사이클(3회)
        minIdx = i
        for j in range(i + 1, n):
            if ary[minIdx] > ary[j]:
                minIdx=j
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary

## 변수
dataAry = [randint(30, 190) for _ in range(8)]

## 메인
print('정렬전-->', dataAry)
dataAry = selectSort(dataAry)
print('정렬후-->', dataAry)



