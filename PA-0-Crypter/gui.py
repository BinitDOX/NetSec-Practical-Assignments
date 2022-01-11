import tkinter as tk  # For GUI
import threading  # For multithreading
from time import sleep  # For adding delay
from tkvideomod import TKVideo # For adding a load video

class GUI(threading.Thread):
    def __init__(self, crypter):
        super(GUI, self).__init__()
        self.crypter = crypter  # Ref to crypter object
        self.btn_states = ['normal', 'disabled']  # Button states
        self.start()  # Start the GUI thread

    def callback(self):  # For clean and elegant exit
        print('(+) Stopped')
        self.root.quit()

    def run(self):
        self.root = tk.Tk()  # Create tkinter object
        self.root.protocol("WM_DELETE_WINDOW", self.callback)  # Call callback on exit window
        self.root.title('Encrypt-Decrypt-Assignment-0')  # Window title
        self.root.geometry("670x400")  # Set window size
        self.root.resizable(0, 0)  # Make it un-resizable

        def splash_screen():  # Play a micro load vid in a label widget
            player = TKVideo('./splash/load.mp4', splash, loop=0, size=(658, 20), start_after=0, delay=0.02)
            player.play()

        def crypt(state):  # Enc / Dec depending on arg
            message = message_ent.get()  # Get user input from text field
            cyper =  self.crypter.encrypt(message) if state else self.crypter.decrypt(message)  # Enc / Dec depending on arg
            if cyper is not None:  # If success
                text_var.set(cyper)  # Set it to screen
            encrypt_btn['state'] = self.btn_states[self.crypter.c_state]   # Map crypter state to enc button state
            decrypt_btn['state'] = self.btn_states[not self.crypter.c_state]  # Map crypter state to dec button state
            message_lbl['text'] = 'Cypher Text:  ' if self.crypter.c_state else 'Message Text:  '  # Change label based on crypter state
            error_lbl['text'] = self.crypter.error  # Update error label based on crypter error state

        def encrypt():
            crypt(True)

        def decrypt():
            crypt(False)

        frame = tk.Frame(self.root, bg="#3B3B3B")  # Define a frame in window
        splash = tk.Label(frame)  # Create GUI label
        text_var = tk.StringVar()  # Create GUI string var
        title_txt = tk.Label(frame, text='Network Security Assignment-0: Crypter', width=40, height=2, font=("Helvetica", 13), bg="#464342", fg="white")
        message_lbl = tk.Label(frame, text='Message Text:  ', font=("Helvetica", 11), bg="#464342", fg="white")
        error_lbl = tk.Label(frame, text='', font=("Helvetica", 9), bg="#3B3B3B", fg="red")
        message_ent = tk.Entry(frame, textvariable = text_var, borderwidth=5, bg="#464342", width=15, font=("Helvetica", 12), fg="white")  # Create text field
        encrypt_btn = tk.Button(frame, text='Encrypt', command=encrypt, width=8, font=("Helvetica", 11), bg="#464342", fg="white")  # Create GUI Encrypt button and set it t call encrypt function
        decrypt_btn = tk.Button(frame, text='Decrypt', command=decrypt, state='disabled', width=8, font=("Helvetica", 11), bg="#464342", fg="white")  # Create Decrypt button and set it t call decrypt function
        destroy_btn = tk.Button(frame, text='Exit', width=25, command=self.callback, font=("Helvetica", 11), bg="#464342", fg="white")  # Create Exit button and set it t call callback exit function

        frame.pack(fill='both', expand=True, padx=2, pady=2)  # Not needed, removable, used for grid layout
        # Use absolute placement
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
