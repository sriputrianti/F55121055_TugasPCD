import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps, ImageFilter, ImageEnhance

class ImageEditor:
    def __init__(self, master):
        self.master = master
        master.title("Aplikasi Perbaikan Citra")

        # membuat Label untuk menampilkan nama
        self.label_nama = tk.Label(master, text="Sri Putrianti Mateka F55121055")
        self.label_nama.pack()

        # membuat tombol untuk memilih file citra
        self.button1 = tk.Button(master, text="Pilih Gambar", command=self.open_image)
        self.button1.pack()

        # membuat tombol untuk reduksi noise
        self.button3 = tk.Button(master, text="Reduksi Noise", command=self.reduce_noise)
        self.button3.pack()

        # membuat tombol untuk peningkatan kontras
        self.button4 = tk.Button(master, text="Peningkatan Kontras", command=self.enhance_image)
        self.button4.pack()

        # membuat tombol untuk menampilkan citra yang telah diperbaiki
        self.button5 = tk.Button(master, text="Tampilkan Hasil", command=self.show_image)
        self.button5.pack()

        # membuat label untuk menampilkan citra asli
        self.label1 = tk.Label(master)
        self.label1.pack()

        # membuat label untuk menampilkan citra yang telah diperbaiki
        self.label2 = tk.Label(master)
        self.label2.pack()

    def open_image(self):
        # membuka jendela dialog untuk memilih file citra
        file_path = filedialog.askopenfilename()

        # membuka citra dan menampilkan citra asli pada label1
        self.image = Image.open(file_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label1.config(image=self.photo)

    def reduce_noise(self):
        # mengurangi noise pada citra dan menampilkan citra yang telah diperbaiki pada label2
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius=2)) 
        self.photo2 = ImageTk.PhotoImage(self.image)
        self.label2.config(image=self.photo2)

    def enhance_image(self):
        # meningkatkan kontras citra dan menampilkan citra yang telah diperbaiki pada label2
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(2) 
        self.photo2 = ImageTk.PhotoImage(self.image)
        self.label2.config(image=self.photo2)

    def show_image(self):
        # menampilkan citra yang telah diperbaiki pada jendela baru
        self.image.show()

root = tk.Tk()
editor = ImageEditor(root)
root.mainloop()