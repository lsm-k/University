import time as t
import tkinter
from tkinter import messagebox

#시간 변수
h_1 = 0
m_1 = 0
s_1 = 0
tk=tkinter.Tk()
h = tkinter.StringVar()

#타이머 시간 확인창
def timer_check():
    global h_1, m_1, s_1
    h.set(str(h_1)+"시간" + str(m_1)+"분" + str(s_1)+"초")


#엔트리 값 불러오기
def get_entry():
    global h_1, m_1, s_1
    h_1 = int(timer_h.get())
    m_1 = int(timer_m.get())
    s_1 = int(timer_s.get())
    timer_check()
#타이머 종료시 창 호출
def timer_end():
    messagebox.showinfo("타이머 종료", "타이머가 종료되었습니다.")
#타이머 시작시 실행되는 함수
def timer_start():
    global h_1, m_1, s_1
    while True:
        timer_check()
        if s_1 == 0 and m_1 == 0 and h_1 == 0:
            timer_end()
            break
        elif s_1 == 0 and m_1 != 0:
            m_1 -= 1
            s_1 = 59
        elif s_1 == 0 and m_1 == 0 and h_1 != 0:
            h_1 -= 1
            m_1 = 59
            s_1 = 59
        else:
            s_1 -= 1
        t.sleep(1)
    

#타이머 창 설정
tk.title("타이머")
tk.geometry("600x400")
timer_check()
timer_main=tkinter.Label(tk, textvariable=h, font=("맑은 고딕", 20))
timer_main.place(x=240, y=1)
#타이머 시간 설정창
timer_h=tkinter.Entry(tk, font=("맑은 고딕", 10), width=7)
timer_h.place(x=180, y=60)
timer_h_label=tkinter.Label(tk, text="H", font=("맑은 고딕", 16))   
timer_h_label.place(x=235, y=50)
#타이머 분 설정창
timer_m=tkinter.Entry(tk, font=("맑은 고딕", 10), width=7)
timer_m.place(x=270, y=60)
timer_m_label=tkinter.Label(tk, text="M", font=("맑은 고딕", 16))
timer_m_label.place(x=325, y=50)
#타이머 초 설정창
timer_s=tkinter.Entry(tk, font=("맑은 고딕", 10), width=7)
timer_s.place(x=370, y=60)
timer_s_label=tkinter.Label(tk, text="S", font=("맑은 고딕", 16))
timer_s_label.place(x=425, y=50)
#값 입력 버튼
timer_bt = tkinter.Button(tk, text="값 입력", font=("맑은 고딕", 10), command=get_entry)
timer_bt.place(x=490, y=60)
#타이머 시작 버튼
timer_start_bt = tkinter.Button(tk, text="타이머 시작", font=("맑은 고딕", 10), command=timer_start)
timer_start_bt.place(x=290, y=100)



tk.mainloop()