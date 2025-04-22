from tkinter import*
from time import*
from threading import*
from tkinter import messagebox

#변수설정
repeat_check = 0
h_1 = 0
m_1 = 0
s_1 = 0
window = Tk()
main_label_value = StringVar()

#타이머 메인로직
def main_loop():
    global repeat_check
    repeat_check = timer.time_cal()
    if repeat_check == 1:
        messagebox.showinfo("타이머 종료", "타이머가 종료되었습니다.")
        window.quit()  # 루프 종료
    else:
        window.after(1000, main_loop)  # 1초 후 재호출

#엔트리 초기값 설정
def on_click(entry, default_value="0"):
    if entry.get() == default_value:
        entry.delete(0, "end")
        entry.config(fg="black")

def off_click(entry, default_value="0"):
    if entry.get() == "":
        entry.insert(0, default_value)
        entry.config(fg="gray")

# 기존 함수들을 축약
def on_click_h(event): on_click(time_entry_h)
def off_click_h(event): off_click(time_entry_h)
def on_click_m(event): on_click(time_entry_m)
def off_click_m(event): off_click(time_entry_m)
def on_click_s(event): on_click(time_entry_s)
def off_click_s(event): off_click(time_entry_s)

def num_check(event):
    if event.isdigit() or event == "":
        return True
    return False

class timer():
    @staticmethod
    def create_time_entry(window, label_text, x, y, on_click, off_click):
        num_check_func = (window.register(num_check), "%P")
        time_label = Label(window, text=label_text, font=("맑은 고딕", 13))
        time_entry = Entry(window, width=5, font=("맑은 고딕", 10), fg="gray", justify="center", validate="key", validatecommand=num_check_func)
        time_entry.insert(0, "0")
        time_entry.bind("<FocusIn>", on_click)
        time_entry.bind("<FocusOut>", off_click)
        time_entry.place(x=x, y=y)
        time_label.place(x=x + 40, y=y - 5)
        return time_entry

    def start_GUI():
        global main_label, window, main_label_value, time_entry_h, time_entry_m, time_entry_s, h_1, m_1, s_1, repeat_check
        # 시간 라벨 표시
        main_label = Label(window, textvariable=main_label_value, font=("맑은 고딕", 25))
        main_label_value.set(f"{h_1}H{m_1}M{s_1}S")
        main_label.pack(side="top", fill="x")
        
        # 시간, 분, 초 엔트리 생성
        time_entry_h = timer.create_time_entry(window, "H", 20, 50, on_click_h, off_click_h)
        time_entry_m = timer.create_time_entry(window, "M", 80, 50, on_click_m, off_click_m)
        time_entry_s = timer.create_time_entry(window, "S", 140, 50, on_click_s, off_click_s)

    def live_time_GUI():
        main_label_value.set(str(h_1) + "H" + str(m_1)+ "M" + str(s_1) + "S")
        window.after(500, timer.live_time_GUI)

    def time_cal():
        global h_1, m_1, s_1
        if s_1 > 0:
            s_1 -= 1
        elif m_1 > 0:
            m_1 -= 1
            s_1 = 59
        elif h_1 > 0:
            h_1 -= 1
            m_1 = 59
            s_1 = 59
        else:
            return 1
        return 0  # 타이머가 종료되지 않음을 반환
    def timer_start_bt_press():
        main_loop()  # 메인 루프 시작
        thread_1 = Thread(target=timer.live_time_GUI, daemon=True)
        thread_1.start()

# 메인 스레드
window.title("타이머")
window.geometry("240x160")
timer.start_GUI()



window.mainloop()