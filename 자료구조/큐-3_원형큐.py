## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear+1)%SIZE == front:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front ,rear
    if isQueueFull() :
        return print('꽉찬큐')
    rear = (rear+1)%SIZE
    queue[rear]=data

def deQueue():
    global SIZE, queue, front ,rear
    if isQueueEmpty() :
        return print('큐가빔')
    else:
        front = (front+ 1)%SIZE
        data=queue[front]
        queue[front]=None
        return data
def isQueueEmpty():
    global SIZE, queue, front ,rear
    if front == rear:
        return True
    else:
        return False

def peek():
    global SIZE, queue, front ,rear
    if isQueueEmpty():
        return print('큐가빔')
    return queue[(front +1)%SIZE ]


## 변수


## 메인
SIZE = 5
queue = [None for _ in range(SIZE)]
front =rear = 0

enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')

retData = deQueue()
print('손님 이리로 :',retData)
# print('**준비하세요==>',peek())
retData = deQueue()
print('손님 이리로 :',retData)

enQueue('재남')
print('출구<--',queue,'<--입구')
enQueue('정국  ')
print('출구<--',queue,'<--입구')
enQueue('길동')
print('출구<--',queue,'<--입구')