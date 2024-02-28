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

def delete_data(position):
    # 1단계 : 위치 친구 지우기
    katok[position] = None
    Klen = len(katok)
    # 2단계 : 지운 친구 다음부터,마지막친구까지 앞으로 이동
    for i in range(position+1,Klen):
        katok[i-1]=katok[i]
        katok[i]=None

    # 3단계 : 마지막 칸 제거
    del(katok[Klen-1])

katok=[]

select=0
while select != 4:
    select = int(input('"선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->"'))

    if select ==1:
        data=input('추가할 데이터-->')
        add_data(data)
        print(katok)

    elif select ==2:
        pos=int(input('삽입할 위치-->'))
        data=input('추가할 데이터-->')
        insert_data(pos,data)
        print(katok)
    elif select ==3:
        pos = int(input("삭제할 위치-->"))
        delete_data(pos)
        print(katok)
    elif select ==4:
        print(katok)
        exit
    else:
        print('1~4중 하나를 입력하세요')
        continue