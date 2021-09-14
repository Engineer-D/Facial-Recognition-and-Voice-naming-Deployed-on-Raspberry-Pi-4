#Modified by Engineer-D
#Date 21.07.2021
#Desc: This script is running a face recognition of a live webcam stream.
#Modified code of the original Ageitgey and EbenKouao (Github) face recognition and SmartCCTV camera
#Simply add your desired 'passport-style' face to the 'profile' folder.

import face_recognition # For Easy face recognition manipulation
import cv2 # for Image processing
import numpy as np # for Matrix calculation and manipulation
import os # for file operation

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
ds_factor = 0.6

# My Own Side of the Code
from num2words import num2words
from subprocess import call

cmd_beg = 'espeak '
cmd_end = ' | aplay /home/pi/Desktop/Name.wav 2>/dev/null' #To play back the stored .wav file
#and to dump the std errors to /dev/null
cmd_out = '--stdout > /home/pi/Desktop/Name.wav ' # To store the voice
#End of mt code

#Store Objects in array
known_person = [] #Name of person
known_image = [] #image object
known_face_encodings = [] #encoding object

#Initialize some variable
face_locations = [] #location of face in image
face_encodings = [] #encoding faces detected
face_names = [] #name of the face recognised
process_this_frame = True #Boolean Do you want to process this frame?

#Loop to add images in friends folder
for file in os.listdir("dataset/"):
    try:
        #Extracting person name from the image filename e.g Alex.jpg in our dataset
        known_person.append(file.replace(".jpg",""))
        file = os.path.join("dataset/",file)
        known_image = face_recognition.load_image_file(file) #loading the image in dataset
        #Encode the face of the celebrities we have saved
        known_face_encodings.append(face_recognition.face_encodings(known_image)[0])

    except Exception as e:
        pass

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0) #Startup the camera for recognition

    def __del__(self):
        self.video.release() #function to end stream
    
    def get_frame(self):
        success, image = self.video.read() #reading in the videos from livestream

        process_this_frame = True #frame read from above process it

        # Resize frame of vidoe to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(image, (0,0), fx=0.25, fy=0.25)

        #convert the image from BGR color to RGB color (openCV style to Face recognition style)
        rgb_small_frame = small_frame[:, :, ::-1]

        #only process every other frame of video to save time
        if process_this_frame:
            #find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            global name_gui
            for face_encoding in face_encodings:
                # Verify face for a match of known faces
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                
                #print(matches)

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_person[best_match_index]

                print(name)
                text = name  ## MINE
                face_names.append(name)

                name_gui = name
                
                #Replacing space with underscore (MINE)
                text = text.replace(' ', '_')
                #call the Espeak TTS Engine to read aloud a text (MINE)
                call([cmd_beg+cmd_out+text+cmd_end], shell = True)

        process_this_frame =  not process_this_frame

# Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(image, (left, top), (right, bottom), (255, 255, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(image, (left, bottom - 35), (right, bottom), (255, 255, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(image, name_gui, (left + 10, bottom - 10), font, 1.0, (0, 0, 0), 1)

        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()