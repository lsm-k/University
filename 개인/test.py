import threading as th
import time

# Lock 객체 생성
lock = th.Lock()

def thread1():
    for _ in range(5):
        with lock:
            print("1")  # 줄바꿈 추가
        time.sleep(0.1)

def thread2():
    for _ in range(5):
        with lock:
            print("2")  # 줄바꿈 추가
        time.sleep(0.1)

def thread3():
    for _ in range(5):
        with lock:
            print("3")  # 줄바꿈 추가
        time.sleep(0.1)

t1 = th.Thread(target=thread1)
t2 = th.Thread(target=thread2)
t3 = th.Thread(target=thread3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print()  # 줄바꿈 추가
