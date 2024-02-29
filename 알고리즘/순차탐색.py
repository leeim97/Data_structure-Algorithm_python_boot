from random import randint,choice
# 순차탐색은 정렬되지 않은 데이터에서 탐색
## 함수
def seqSearch(ary,fdata):
    pos = -1

    for i in range(0,len(ary)):
        if ary[i] == fdata:
            pos = i

    return pos
## 변수
dataAry = [randint(30,190) for _ in range(8)]#가족
findData= choice(dataAry) # 누나ㅣㅋ

## 메인
print('배열 -->',dataAry)
position = seqSearch(dataAry,findData)
if position != -1:
    print(findData,'는',position,'위치에 있어요')
else:
    print(findData, '는', position, '없어요 ㅜㅜ')