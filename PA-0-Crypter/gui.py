import tkinter as tk
import threading
import cv2
from time import sleep
from tkvideomod import TKVideo

class GUI(threading.Thread):
    def __init__(self, crypter):
        super(GUI, self).__init__()
        self.capture = cv2.VideoCapture('load.mp4')
        self.crypter = crypter
        self.btn_states = ['normal', 'disabled']
        self.start()

    def callback(self):
        print('(+) Stopped')
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title('Encrypt-Decrypt-Assignment-0')
        self.root.geometry("670x400")
        self.root.resizable(0, 0)

        def splash_screen():
            player = TKVideo('./splash/load.mp4', splash, loop=0, size=(658, 20), start_after=0, delay=0.02)
            player.play()

        def crypt(state):
            message = message_ent.get()
            cyper =  self.crypter.encrypt(message) if state else self.crypter.decrypt(message)
            if cyper is not None:
                text_var.set(cyper)
            encrypt_btn['state'] = self.btn_states[self.crypter.c_state]
            decrypt_btn['state'] = self.btn_states[not self.crypter.c_state]
            message_lbl['text'] = 'Cypher Text:  ' if self.crypter.c_state else 'Message Text:  '
            error_lbl['text'] = self.crypter.error

        def encrypt():
            crypt(True)

        def decrypt():
            crypt(False)

        frame = tk.Frame(self.root, bg="#3B3B3B")
        splash = tk.Label(frame)
        text_var = tk.StringVar()
        title_txt = tk.Label(frame, text='Network Security Assignment-0: Crypter', width=40, height=2, font=("Helvetica", 13), bg="#464342", fg="white")
        message_lbl = tk.Label(frame, text='Message Text:  ', font=("Helvetica", 11), bg="#464342", fg="white")
        error_lbl = tk.Label(frame, text='', font=("Helvetica", 9), bg="#3B3B3B", fg="red")
        message_ent = tk.Entry(frame, textvariable = text_var, borderwidth=5, bg="#464342", width=15, font=("Helvetica", 12), fg="white")
        encrypt_btn = tk.Button(frame, text='Encrypt', command=encrypt, width=8, font=("Helvetica", 11), bg="#464342", fg="white")
        decrypt_btn = tk.Button(frame, text='Decrypt', command=decrypt, state='disabled', width=8, font=("Helvetica", 11), bg="#464342", fg="white")
        destroy_btn = tk.Button(frame, text='Exit', width=25, command=self.callback, font=("Helvetica", 11), bg="#464342", fg="white")

        frame.pack(fill='both', expand=True, padx=2, pady=2)
        splash.place(x=2, y=70)
        title_txt.place(x=130, y=10)
        message_lbl.place(x=280, y=100)
        message_ent.place(x=260, y=140)
        error_lbl.place(x=240, y=185)
        encrypt_btn.place(x=220, y=220)
        decrypt_btn.place(x=370, y=220)
        destroy_btn.place(x=220, y=300)

        splash_screen()
        sleep(1.2)
        self.root.mainloop()
