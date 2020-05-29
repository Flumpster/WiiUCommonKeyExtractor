from tkinter import Tk, Button, filedialog, Label
import tkinter.font as tkFont
import binascii


def UploadAction(event=None):
    input_file = filedialog.askopenfile(mode ='rb', filetypes =[('bin Files', '*.bin')])
    txt = input_file.read()
    input_file.seek(224, 0)
    raw_key = input_file.read(16)
    common_key = (binascii.hexlify(raw_key))
    common_key = common_key.decode()
    if common_key[:2] == "d7" and len(common_key) == 32:
        lbl3.configure(text=common_key)
        button2 = Button(window, text='Copy', command=CopyClipboard)
        button2.grid(ipadx=1, padx=7, column=2, row=1, sticky="w")
    else:
        lbl3.configure(text="Invalid otp.bin")

def CopyClipboard(event=None):
    window.clipboard_clear()
    window.clipboard_append(lbl3.cget("text"))

window = Tk()
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(family='Arial', size=11)
window.title("Wii U Common Key Extractor")
window.resizable(0,0)
window.minsize(width=325, height=84)
lbl = Label(window, text="Select otp.bin")
lbl.grid(pady=7, padx=7, column=0, row=0)
lbl2 = Label(window, text="Common Key:")
lbl2.grid(pady=3, column=0, row=1)
lbl3 = Label(window, text="No otp.bin")
lbl3.grid(pady=3, column=1, row=1)
button = Button(window, text='Open', command=UploadAction)
button.grid(ipadx=1, pady=7, column=1, row=0, sticky="w")
window.mainloop()