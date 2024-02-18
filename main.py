from tkinter import *
from tkinter.messagebox import *
class ai:
    def main(self):
        root = Tk()
        root.title('Hand Gesture Emoji Detection Application')
        Label(root, text="Hand Gesture Emoji Detection Application").grid(row=0,column=3)
        Label(root, text='').grid(row=1,column=1)
        Label(root, text='').grid(row=2,column=1)
        Label(root, text='').grid(row=3,column=1)
        def destroy1():
            root.destroy()
            self.desc()
        def destroy2():
            root.destroy()
            self.helpp()
        def destroy3():
            root.destroy()
            self.start()
        Button(root, text='Description', command=destroy1).grid(row=4, column=1)
        Button(root, text='Help', command=destroy2).grid(row=5, column=1)
        Button(root, text="Let's try!!", command=destroy3).grid(row=6, column=1)
        root.mainloop()


    def desc(self):
        root = Tk()
        root.title('Description')
        Label(root, text="Description").grid(row=0,column=3)
        def back():
            root.destroy()
            self.main()
        Button(root, text='Back', command=back).grid(row=11, column=1)
        root.mainloop()


    def helpp(self):
        root = Tk()
        root.title('Help')
        Label(root, text="Here are few hand gestures which can be detected").grid(row=0,column=3)
        def back():
            root.destroy()
            self.main()
        Button(root, text='Back', command=back).grid(row=11, column=1)
        root.mainloop()

    def start(self):
        root = Tk()
        root.title('Start')
        root.mainloop()
        
        
        

        

a=ai()
a.main()
