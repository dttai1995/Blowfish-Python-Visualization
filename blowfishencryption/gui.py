from tkinter import Entry, END, Button, Tk, Label, messagebox, Toplevel, mainloop

from blowfish import BlowfishCipher
from const import DEFAULT_ENCODING


class Window:
    def __init__(self):
        root = Tk()
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry('%sx%s' % (width, height))
        root.wm_title("Blowfish Algorithm Demonstration")

        label_1 = Label(root, text="Plaintext")
        label_1.grid(row=0, column=0, padx=(0, 10))
        label_2 = Label(root, text="Key")
        label_2.grid(row=1, column=0, padx=(0, 10))
        label_3 = Label(root, text="Result (HexaDecimal)")
        label_3.grid(row=2, column=0, padx=(0, 10))
        label_4 = Label(root, text="Cipher Text")
        label_4.grid(row=0, column=2, padx=(0, 10))
        label_5 = Label(root, text="Plaintext")
        label_5.grid(row=1, column=2, padx=(0, 10))
        self.e1 = Entry()
        self.e1.grid(row=0, column=1)
        self.e2 = Entry()
        self.e2.grid(row=1, column=1)
        self.e3 = Entry()
        self.e3.grid(row=2, column=1)
        self.cipherentry = Entry()
        self.cipherentry.grid(row=0, column=3)

        self.e4 = Entry()
        self.e4.grid(row=1, column=3)
        self.buttons = {}
        button = Button(root, text="Initialize Blowfish", height=1, width=20,
                        command=self.change)
        decrypt_button = Button(root, text="Decrypt", height=1, width=20,
                                command=self.decrypt)
        b1 = Button(root, text="S1", height=1, width=10, command=lambda idx=0: self.show_s_box(idx),
                    state="disabled")
        b2 = Button(root, text="S2", height=1, width=10, command=lambda idx=1: self.show_s_box(idx),
                    state="disabled")
        b3 = Button(root, text="S3", height=1, width=10, command=lambda idx=2: self.show_s_box(idx),
                    state="disabled")
        b4 = Button(root, text="S4", height=1, width=10, command=lambda idx=3: self.show_s_box(idx),
                    state="disabled")

        self.buttons["change"] = button
        self.buttons["1"] = b1
        self.buttons["2"] = b2
        self.buttons["3"] = b3
        self.buttons["4"] = b4

        button.grid(row=10, column=0, padx=(0, 100), pady=(0, 0))
        b1.grid(row=11, column=0, padx=(0, 100), pady=(0, 0))
        b2.grid(row=11, column=1, padx=(0, 100), pady=(0, 0))
        b3.grid(row=12, column=0, padx=(0, 100), pady=(0, 0))
        b4.grid(row=12, column=1, padx=(0, 100), pady=(0, 0))
        decrypt_button.grid(row=10, column=2, padx=(0, 100), pady=(0, 0))
        self.root = root

    def change_level(self, *agrs):
        pass

    def change(self):
        try:
            key = self.e1.get()
            plaintext = self.e2.get()
            blowfish = BlowfishCipher(bytes(key, DEFAULT_ENCODING))
            self.s_box = [blowfish.S1, blowfish.S2
                , blowfish.S3
                , blowfish.S4]
            print(blowfish.S1)
            self.change_entry_text(self.e3, blowfish.encrypt_block(bytes(plaintext, DEFAULT_ENCODING)).hex())
            self.buttons["change"].config(state="disabled")
            self.buttons["1"].config(state="active")
            self.buttons["2"].config(state="active")
            self.buttons["3"].config(state="active")
            self.buttons["4"].config(state="active")
            self.blowfish = blowfish
        except ValueError as e:
            messagebox.showinfo("Value Error", str(e))

    def decrypt(self):
        try:
            cipher = self.cipherentry.get()
            self.change_entry_text(self.e4, self.blowfish.decrypt_block(bytes(cipher, DEFAULT_ENCODING)).hex())
            pass
        except:
            messagebox.showinfo("Blowfish not initialize yet")

    def show_s_box(self, idx):
        box = Toplevel(self.root)
        box.wm_title("S" + str(idx + 1))
        data = self.s_box[idx]

        for i in range(0, 16):
            for j in range(0, 16):
                print(str(data[i * 16 + j]))
                b = Entry(box, font=("Calibri", 8), width=8, text=str(data[i * 16 + j]))
                self.change_entry_text(b, '{0:08X}'.format(data[i * 16 + j]))
                b.grid(row=i, column=j)

        print(len(data))

        # b5 = Button(s_box, text="S2", height=1, width=10, command=lambda sbox=s_box: show_s_box(sbox), state="disabled")

    @staticmethod
    def change_entry_text(entry: Entry, content):
        entry.delete(0, END)
        entry.insert(0, str(content))


main_window = Window()
mainloop()
