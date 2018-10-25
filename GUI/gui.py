import Tkinter as tk
import tkMessageBox

root = tk.Tk()

def helloCallBack():
	
	mymessage = E1.get() + E2.get()
	tkMessageBox.showinfo( "Hello Python", mymessage)

	
L1 = tk.Label(root, text="Input Variable here:")
L1.pack()

E1 = tk.Entry(root, bd =5)
E1.pack()

L2 = tk.Label(root, text="Input Variable here:")
L2.pack()

E2 = tk.Entry(root, bd =5)
E2.pack()
	
B1 = tk.Button(root, text ="Hello", command = helloCallBack)
B1.pack()


root.mainloop()
