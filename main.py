from tkinter import *
from tkinter.messagebox import *

class ai:
    def main(self):
        root = Tk()
        root.geometry('600x600')
        root.title('Hand Gesture Emoji Detection Application')

        # Title in the center
        Label(root, text="Hand Gesture Emoji Detection Application", font=('arial',18 , 'bold')).grid(row=0, column=0,columnspan=5,padx=14,pady=20,sticky='n')

        def destroy1():
            root.destroy()
            self.desc()
        def destroy2():
            root.destroy()
            self.helpp()
        def destroy3():
            root.destroy()
            self.start()
        # Buttons on the left
        Button(root, text='Description', command=destroy1).grid(row=6, column=0, pady=10, padx=5)
        Button(root, text='Help', command=destroy2).grid(row=7, column=0, pady=10, padx=5)
        Button(root, text="Let's try!!", command=destroy3).grid(row=8, column=0, pady=10, padx=5)

        # Frame for image on the right
        fr = Frame(root)
        fr.grid(row=2, column=1,rowspan=13)
        
        # Image on the right-hand side in the middle
        handImage = PhotoImage(file='hand_home.png')
        Label(fr, image=handImage).grid(row=2, column=1)

        root.mainloop()

    def desc(self):
        root = Tk()
        root.title('Description')
        root.geometry('400x370')
        Label(root, text="Description").grid(row=0, column=0,padx=10, pady=5)
        Label(root, text="The project is a real-time hand gesture emoji detection application").grid(row=1,column=0,padx=10)
        Label(root, text="and developed using Python. It utilizes computer vision and machine").grid(row=2, column=0,padx=10 )
        Label(root, text="learning techniques to detect and recognize hand gestures captured").grid(row=3, column=0,padx=10 )
        Label(root, text="by webcam in real-time. The application employs libraries such as").grid(row=5, column=0,padx=10)
        Label(root, text="OpenCV, MediaPipe and TensorFlow to process video input,detect hand").grid(row=6, column=0,padx=10 )
        Label(root, text="landmarks, and classify gestures. A pre-trained deep learning model").grid(row=8, column=0,padx=10 )
        Label(root, text="is used to predict the gesture classes, which are then mapped to").grid(row=9, column=0,padx=10 )
        Label(root, text="corresponding emojis. The emojis are displayed on the screen along").grid(row=10, column=0,padx=10 )
        Label(root, text="with the live video feed, providing users with visual representation").grid(row=12, column=0,padx=10 )
        Label(root, text="of their hand gestures.This project enables interactive communication").grid(row=13, column=0,padx=10 )
        Label(root, text="through hand gestures, enhancing user experience and offering a novel").grid(row=15, column=0,padx=10 )
        Label(root, text="way to express emotions and messages.").grid(row=16, column=0,padx=10 )

        def back():
            root.destroy()
            self.main()
        
        Button(root, text='Back', command=back).grid(row=18,column=0,pady=10)
        root.mainloop()

    def helpp(self):
        root = Tk()
        root.title('Help')
        root.geometry('400x370')
        Label(root, text="Here are few hand gestures which can be detected").grid(row=0,column=0,columnspan=6,pady=5)

        # Image on the right-hand side in the middle
        helpImage = PhotoImage(file='helpp.png')
        Label(root, image=helpImage).grid(row=2, column=0)
        
        def back():
            root.destroy()
            self.main()
        
        Button(root, text='Back', command=back).grid(row=4,column=0)
        root.mainloop()

    def start(self):
        root = Tk()
        root.title('Start Hand Gesture Detection')
        
        Label(root, text="This is where the hand gesture detection will happen.").pack(pady=20)
        
        def back():
            root.destroy()
            self.main()
        
        Button(root, text='Back', command=back).pack(pady=10)

        root.mainloop()


a = ai()
a.main()
