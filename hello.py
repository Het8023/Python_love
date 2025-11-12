import tkinter as tk
import random
import threading
import time
import math

def heart_x(t, size=10):
    """计算爱心形状的x坐标"""
    return size * 16 * (math.sin(t) ** 3)

def heart_y(t, size=10):
    """计算爱心形状的y坐标"""
    return -size * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))

def show_warm_tip(x, y, delay=0):
    """在指定位置显示温馨提醒窗口"""
    if delay > 0:
        time.sleep(delay)
    # 创建窗口
    window = tk.Tk()
    # 设置窗口标题和大小
    window.title('温馨提示')
    window_width = 150  # 减小窗口宽度
    window_height = 40  # 减小窗口高度
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 提示文字列表
    tips = [
        '多喝水哦~', '保持微笑呀', '每天都要元气满满',
        '记得吃水果', '保持好心情', '好好爱自己', '我想你了',
        '梦想成真', '期待下一次见面', '金榜题名',
        '顺顺利利', '早点休息', '愿所有烦恼都消失',
        '别熬夜', '今天过得开心嘛', '天冷了，多穿衣服'
    ]
    tip = random.choice(tips)

    # 多样的背景颜色
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
        'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
    ]
    bg = random.choice(bg_colors)

    # 创建标签并显示文字
    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 12),  # 字体调小
        width=20,
        height=2
    ).pack()

    # 窗口置顶显示
    window.attributes('-topmost', True)
    window.mainloop()

# 获取屏幕尺寸
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

# 只计算爱心轮廓的点，不填充内部
heart_points = []
for i in range(0, 628, 8):  # 步长适中
    t = i / 100
    x = heart_x(t, 15)  # 增大缩放因子，使爱心更大
    y = heart_y(t, 15)
    heart_points.append((x, y))

# 限制窗口数量，只使用轮廓点
max_windows = len(heart_points)  # 使用所有轮廓点

# 创建线程列表
threads = []

# 创建窗口线程，按顺序显示爱心轮廓
for i in range(max_windows):
    x, y = heart_points[i]
    # 将坐标转换为屏幕坐标（爱心居中显示）
    screen_x = int(screen_width / 2 + x)
    screen_y = int(screen_height / 2 + y)
    # 创建线程，每个线程有逐渐增加的延迟
    delay = i * 0.1  # 调整延迟时间
    t = threading.Thread(target=show_warm_tip, args=(screen_x, screen_y, delay))
    threads.append(t)
    t.start()
    time.sleep(0.01)  # 线程启动间隔

# 等待所有线程完成
for t in threads:
    t.join()