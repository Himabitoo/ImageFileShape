from pathlib import Path
from tkinter import filedialog,messagebox

import os
import cv2
import sys
import shutil

#ディレクトリを選択させる
messagebox.showinfo('確認', '仕分けしたいディレクトリを選択して下さい。')
SELECTED_DIR = filedialog.askdirectory()

if SELECTED_DIR :
    print("続行")
else:
    messagebox.showinfo('通知', 'ディレクトリの選択がなかったため処理を終了します。')
    sys.exit()


messagebox.showinfo('確認', '保存先のディレクトリを選択してください。')
SAVE_DIR = filedialog.askdirectory()

if SAVE_DIR :

    path = Path(SELECTED_DIR)

    for i, file in enumerate(path.glob('*.png')):

        #ファイル名に使う文字列用の変数
        img = cv2.imread(str(file))
        w,h,c = img.shape
        TARGET_DIR = str(h)+" x "+str(w)
        
        # ディレクトリが存在しない場合、ディレクトリを作成する
        if not os.path.exists(SAVE_DIR + '/' + TARGET_DIR):
            
            os.makedirs(SAVE_DIR + '/' + TARGET_DIR)

        #move(元ファイル,ファイル先)
        shutil.move (file,SAVE_DIR + '/' + TARGET_DIR)

        print(file)
        print("w:",w)
        print("h",h)
        print(TARGET_DIR)
    
    messagebox.showinfo('通知', '無事処理は完了しました。')

else:
    messagebox.showinfo('通知', 'ディレクトリの選択がなかったため処理を終了します。')
    sys.exit()
