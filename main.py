from tkinter import *
from tkinter.messagebox import *
import os
import cv2
import uuid
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

class ai:
    def main(self):
        root = Tk()
        root.geometry('550x600')
        root.title('Hand Gesture Detection Application')
        
        # Title in the center
        Label(root, text="Hand Gesture Detection Application", font=('arial',18 , 'bold')).grid(row=0, column=0,columnspan=500,pady=20)

        def destroy1():
            root.destroy()
            self.desc()
        def destroy2():
            root.destroy()
            self.helpp()
        def destroy3():
            root.destroy()
            self.start()

        #Label(root,text=" ").grid(row=2,column=0)
        #Label(root,text=" ").grid(row=2,column=1)

        handImage = PhotoImage(file='hand_home.png')
        Label(root, image=handImage).grid(row=2, column=2,columnspan=10,padx=60)

        fr=Frame(root)
        fr.grid(row=4,column=0,columnspan=7,padx=95)
        Button(fr, text='Description', command=destroy1, font=('arial' , 11), bg='Sky blue1').grid(row=4, column=2)
        Label(fr, text=" ").grid(row=4,column=3,padx=100)
        Button(fr, text='Help', command=destroy2,font=('arial' , 11),width=6, bg='Sky blue1').grid(row=4, column=5)
        Button(fr, text="Let's try!!", command=destroy3, font=('arial' , 11),height=2,width=12, bg='orange').grid(row=5, column=3,pady=40)
        
        root.mainloop()

    def desc(self):
        root = Tk()
        root.title('Description')
        root.geometry('420x370')
        Label(root, text="Description",font=('arial',10,'bold')).grid(row=0, column=0,padx=10, pady=5)
        Label(root, text="The project is a real-time hand gesture emoji detection application",font=('arial',9)).grid(row=1,column=0,padx=10)
        Label(root, text="and developed using Python. It utilizes computer vision and machine",font=('arial',9)).grid(row=2, column=0,padx=10 )
        Label(root, text="learning techniques to detect and recognize hand gestures captured",font=('arial',9)).grid(row=3, column=0,padx=10 )
        Label(root, text="by webcam in real-time. The application employs libraries such as",font=('arial',9)).grid(row=5, column=0,padx=10)
        Label(root, text="OpenCV, MediaPipe and TensorFlow to process video input,detect hand",font=('arial',9)).grid(row=6, column=0,padx=10 )
        Label(root, text="landmarks, and classify gestures. A pre-trained deep learning model",font=('arial',9)).grid(row=8, column=0,padx=10 )
        Label(root, text="is used to predict the gesture classes, which are then mapped to",font=('arial',9)).grid(row=9, column=0,padx=10 )
        Label(root, text="corresponding emojis. The emojis are displayed on the screen along",font=('arial',9)).grid(row=10, column=0,padx=10 )
        Label(root, text="with the live video feed, providing users with visual representation",font=('arial',9)).grid(row=12, column=0,padx=10 )
        Label(root, text="of their hand gestures.This project enables interactive communication",font=('arial',9)).grid(row=13, column=0,padx=10 )
        Label(root, text="through hand gestures, enhancing user experience and offering a novel",font=('arial',9)).grid(row=15, column=0,padx=10 )
        Label(root, text="way to express emotions and messages.",font=('arial',9)).grid(row=16, column=0,padx=10 )

        def back():
            root.destroy()
            self.main()
        
        Button(root, text='Back', command=back,font=('arial',9,'bold')).grid(row=18,column=0,pady=10)
        root.mainloop()

    def helpp(self):
        root = Tk()
        root.title('Help')
        root.geometry('400x420')
        Label(root, text="Here are few hand gestures which can be detected:",font=('arial',10,'bold')).grid(row=0,column=0,pady=5,padx=20)

        Label(root, text="* Okay ,V (Peace), Thumbs up, Thumbs down, Call me,",font=('arial',9)).grid(row=1, column=0,padx=20)
        Label(root, text="Stop, Rock, Live Long, Fist, Smile.",font=('arial',9)).grid(row=2, column=0,padx=20)
        Label(root, text="* To quit the webcam screen enter 'q'.",font=('arial',9)).grid(row=3, column=0,padx=20)
        # Image on the right-hand side in the middle
        helpImage = PhotoImage(file='helpp.png')
        Label(root, image=helpImage).grid(row=4, column=0,pady=20,padx=20)
        
        def back():
            root.destroy()
            self.main()
        
        Button(root, text='Back', command=back,font=('arial',10)).grid(row=5,column=0,padx=20)
        root.mainloop()

    def start(self):
        root = Tk()
        root.title('Start Hand Gesture Detection')
        
        #Initialize Mediapipe
        mp_drawing=mp.solutions.drawing_utils
        mp_hands=mp.solutions.hands

        #Load the gesture recognizer model
        model = load_model('mp_hand_gesture')

        #Load Class Names
        file = open('hand_gestures.names', 'r')
        class_names = file.read().split('\n')
        file.close()
        print(class_names)

        #Initialize the Webcam
        cap=cv2.VideoCapture(0)

        with mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
            while cap.isOpened():

                #Read each frame from the webcam
                ret,frame=cap.read()

                x,y,c=frame.shape

                #BGR 2 RGB
                image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

                #Flip on horizontal
                image=cv2.flip(image,1)

                #Set flag
                image.flags.writeable=False

                #Detections
                results=hands.process(image)

                #Set flag to true
                image.flags.writeable=True

                #RGB 2 BGR
                image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

                #Detections
                ##print(results)

                class_name = ''
                
                #Post process the results
                if results.multi_hand_landmarks:
                    landmarks=[]
                    for num,hand in enumerate(results.multi_hand_landmarks):
                        for i in hand.landmark:
                            ##print(id,i)
                            lm_x=int(i.x * x)
                            lm_y=int(i.y * y)

                            landmarks.append([lm_x,lm_y])

                        #Drawing landmarks on frames
                        ##mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS)
                        mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS,mp_drawing.DrawingSpec(color=(0,0,0),thickness=1,circle_radius=4),mp_drawing.DrawingSpec(color=(0,165,255),thickness=2,circle_radius=2))

                        #Predict gesture
                        prediction=model.predict([landmarks])
                        ##print(prediction)
                        class_id=np.argmax(prediction)
                        class_name=class_names[class_id]
                            
                #Show the prediction on the frame
                cv2.putText(image,class_name,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,0),1,cv2.LINE_AA)

                #Show the final output
                cv2.imshow("Hand-Gesture-Detection-Application",image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        #Release the webcam and destroy all active windows
        cap.release()
        cv2.destroyAllWindows()

        Label(root, text="Thank You!!").pack(pady=20)
        def back():
            root.destroy()
            self.main()
        
        Button(root, text='Back', command=back).pack(pady=10)
        root.mainloop()

a = ai()
a.main()
