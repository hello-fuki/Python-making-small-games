import tkinter

# 解読関数
def decord_line(event):
    global current_line, bgimg, lcharimg, ccharimg, rcharimg
    if current_line >= len(scenario):
        return;
    # 1行読み込み
    line = scenario[current_line]
    current_line = current_line + 1
    line = line.replace("\\n", "\n").strip()
    params = line.split(" ")
    # 分岐
    if line[0] != "#":
        message["text"] = line
        return
    elif params[0] == "#back":
        canvas.delete("all")
        bgimg = tkinter.PhotoImage(file=params[1])
        canvas.create_image(450, 230, image=bgimg)
    elif params[0] == "#putChar":
        if params[2] == "L":
            canvas.delete("left")
            lcharimg = tkinter.PhotoImage(file=params[1])
            canvas.create_image(200, 160, image=lcharimg, tag="left")
        elif params[2] == "R":
            canvas.delete("right")
            rcharimg = tkinter.PhotoImage(file=params[1])
            canvas.create_image(700, 160, image=rcharimg, tag="right")
        else:
            canvas.delete("center")
            ccharimg = tkinter.PhotoImage(file=params[1])
            canvas.create_image(450, 160, image=ccharimg, tag="center")
    elif params[0] == "#branch":
        message.unbind("<Button-1>")
        btn = tkinter.Button(text=params[2], width=20)
        branch.append(btn)
        btn.place(x=300, y=60+int(params[1])*60)
        jumplabel.append(params[3])
        if params[4] == "n":
            return
    # 再帰呼び出し
    decord_line(None)   # 命令文でないときはreturnで関数を抜け出す仕組み

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
message["text"] = "クリックしてスタート"

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
# 画像
bgimg = None
lcharimg = None
ccharimg = None
rcharimg = None
# 選択肢
branch = []
jumplabel = []

root.mainloop()
