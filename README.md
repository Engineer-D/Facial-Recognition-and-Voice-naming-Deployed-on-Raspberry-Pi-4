# Facial Recognition and Voice naming with Raspberry Pi 4 using OpenCV and Facial Recognition Library and Flask for Real Time Web Stream of Pi camera.

Facial recognition is the process of identifying or verifying the identity of a person using their face. It captures, analyzes, and compares patterns based on the person's facial details. The face detection process is an essential step in detecting and locating human faces in images and videos.
Facial recognition could be done in some ways such as:
 * Model Training

 * Face Verification

 Considering the latter which is what I used. The major difference between the two mentioned method is model Training. I don't need to compulsorily train a model before performing face Verification I can just use pretrained model and I will be just fine.

 ## How does Face Verification perform Face Recognition
 There is a database where variety of image faces are stored. hence to perform face recognition we can give each face a label and using Face Verification technique we check for similarity between faces. If there is a match then the system picks that match with its label and calls out the name of the person through the earphone jack. Real time streaming of the Pi camera has been done using flask and hosted on a Local server (Therefore to view you have to be on the same network as the Raspberry Pi).

 ## How to operate
 * Clone this repository into the Raspberry Pi

 * Go to directory where repo is save and open directory Dataset

 * Include Image of yourself correctly labelled

 * Open terminal in Raspberry and cd to the directory of this repo

 * Run command python3 main.py

 * Go to your favorite browser

 * insert: "IP Addresses of your Pi on network:5000" e.g. 192.123.88.137:5000

 * Stream Pi camera
 Remember to insert earphones to the audio output jack so you can hear the name of the recognized Face

 Default Faces in Dataset:
 This faces used were selected from the web and were selected based on my likeness towards them
* Bella

* Davido

* Elon Musk

* Engineer_D (Myself)

* H E R

* Jay Z

* Messi

* Post Malone

* Rihanna

* Ronaldo

* Stormzy

* Tiwa Savage

* Tony Stark

* Vee

* Wizkid

Feel free to add yours and enjoy using this application

Special Thanks to (EbenKouao)
