import tkinter

class FightManager:
    # コンストラクタ
    def __init__(self):
        self.dialog = tkinter.Frame(width=820, height=434)
        self.dialog.place(x=10, y=10)
        canvas = tkinter.Canvas(self.dialog, width=820, height=434)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0, 0, 620, 434, fill="black")
        # ボタン作成
        winbutton = tkinter.Button(self.dialog, text="勝った")
        winbutton.place(x=180, y=340)
        losebutton = tkinter.Button(self.dialog, text="負けた")
        losebutton.place(x=320, y=340)
        # 非表示
        self.dialog.place_forget()
        
