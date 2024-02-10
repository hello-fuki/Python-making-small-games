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
        winbutton["command"] = self.fight_win
        losebutton = tkinter.Button(self.dialog, text="負けた")
        losebutton.place(x=320, y=340)
        # 非表示
        self.dialog.place_forget()
    
    # 戦闘開始
    def fight_start(self, map_data, x, y):
        self.dialog.place(x=10, y=10)
        self.map_data = map_data
        self.brave_x = x
        self.brave_y = y
    
    # 勝利
    def fight_win(self):
        self.map_data[self.brave_y][self.brave_x] = 0   # ミュータブル型の性質を利用して勇者を移動
        self.dialog.place_forget()
