import tkinter

# 解読関数
def decord_line(event):
    print("クリックされた")

# ウインドウ作成
root = tkinter.Tk()
root.title("よろしくアドベンチャー")
root.minsize(900, 460)
root.option_add("*font", ["メイリオ", 14])
# キャンバス作成
canvas = tkinter.Canvas(width=900, height=460)
canvas.place(x=0, y=0)
# メッセージエリア
message = tkinter.Label(width=70, height=5, wraplength=840, bg="white", justify="left", anchor="nw")
message.place(x=28, y=284)
message["text"] = "あいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえおあいうえお"

# ファイル読み込み
scenario = []
file = open("img/scenario.txt", "r", encoding="utf-8")
while True:
    line = file.readline()
    scenario.append(line)
    if not line:
        file.close()
        break
    
# 現在の行数
current_line = 0
# イベント設定
message.bind("<Button-1>", decord_line)

root.mainloop()
