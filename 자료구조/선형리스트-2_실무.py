## 함수
def add_data(friend):
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 추가한 빈칸에 친구 넣기
    katok[kLen-1]=friend

def insert_data(position,friend):
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 한칸씩 뒤로 이동(마지막 친구~ 바로 다음)
    for i in range(kLen-1,position,-1):
        katok[i]=katok[i-1]
    # 3단계 : 포지션 자리에 친구 넣기
    katok[position]=friend
## 변수
katok= []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)
add_data('모모')
print(katok)

insert_data(3,'미나')
print(katok)