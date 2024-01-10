# -*- coding: utf-8 -*-
import tkinter

# ウインドウ作成
root = tkinter.Tk()
root.title("勇者求む！")
root.minsize(640, 480)
root.option_add("*font", ["メイリオ", 14])

# 画像読み込み
img1 = tkinter.PhotoImage(file="img4/chap4-1-1.png")
img2 = tkinter.PhotoImage(file="img4/chap4-1-2.png")
img3 = tkinter.PhotoImage(file="img4/chap4-1-3.png")

# キャンバス作成
canvas = tkinter.Canvas(root, width=640, height=480)
canvas.place(x=0, y=0)
canvas.create_image(320, 240, image=img1, tag="illust")

# テキスト表示
serifu_text = tkinter.Label(text="王様「魔王を倒したら褒美をやるぞ！」")
serifu_text.place(x=160, y=10)
sys_text = tkinter.Label(text="褒美はいくらあげますか？", fg="red")
sys_text.place(x=180, y=380)

# テキストボックス表示
entry = tkinter.Entry(width=12)
entry.place(x=180, y=420)
gold_text = tkinter.Label(text="ゴールド")
gold_text.place(x=330, y=420)

# ボタン表示
button = tkinter.Button(text="決定")
button.place(x=420, y=420)

# ボタンイベントクリック関数
def btn_click():
    gold = float(entry.get())
    if gold >= 5000:
        canvas.delete("illust")
        canvas.create_image(320, 240, image=img2, tag="illust")
        serifu_text["text"] = "勇者「よーし、私に任せなさい！」"
    else:
        serifu_text["text"] = "志願者は誰も来ませんでした。"
    
button["command"] = btn_click

root.mainloop()
