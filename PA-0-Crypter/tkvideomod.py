from time import sleep
import threading
import imageio
from PIL import Image, ImageTk

class TKVideo():
    def __init__(self, path, label, loop = 0, size=(640,360), start_after=0, delay=0):
        self.path = path
        self.label = label
        self.loop = loop
        self.size = size
        self.delay = delay
        self.start_after = start_after

    def load(self, path, label, loop, start_after, delay):
        frame_data = imageio.get_reader(path)
        sleep(start_after)

        if loop == 1:
            while True:
                for image in frame_data.iter_data():
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                    label.config(image=frame_image)
                    label.image = frame_image
        else:
            for image in frame_data.iter_data():
                    sleep(delay)
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                    label.config(image=frame_image)
                    label.image = frame_image
        label.destroy()

    def play(self):
        thread = threading.Thread(target=self.load, args=(self.path, self.label, self.loop, self.start_after, self.delay))
        thread.daemon = 1
        thread.start()
