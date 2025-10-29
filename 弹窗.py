import tkinter as tk
import random
import threading
import time
def dow():
    # 1. 修正TK()拼写错误，补充括号
    window = tk.Tk()
    # 2. 修正获取屏幕尺寸的语法，补充括号
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0,width)
    b = random.randrange(0,height)
    window.title('亲爱的小秦宝宝：')
    # 3.修正引号、加号拼接语法错误，统一中文/英文符号
    window.geometry("330x75" + "+"+ str(a) + "+" + str(b))
    #4.修正字体参数的逗号、引号错误，调整Label尺寸(原height=4会超出窗口)
    tk.Label(window,
             text='我爱你❤',
             bg='pink',
             font=('楷体', 45),
             width=10,  # 适配文字长度
             height=1   #避免文字溢出
             ).pack()
    window.mainloop()
    # 5. 修正列表命名错误 (threads_三 → threads)
threads = []
    # 创建200个线程 (原range(200)逻辑正确，此处保留)
for i in range(200):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.01)
    # 6. 修正start()方法的括号错误
    threads[i].start()
