from multiprocessing import Process
import imutils
import os
import cv2
import numpy
import face_recognition


def db_images_load():
    encoding_face_image = []
    id_face_image = []
    
    db_faces = imutils.paths.list_images(os.path.join("static","persons"))
    
    
    for image_file in db_faces:
        i_path, i_filename = os.path.split(image_file)
        file_name, file_extension = os.path.splitext(i_filename)

        image = face_recognition.load_image_file(image_file)
        encode_image = face_recognition.face_encodings(image)[0]
        encoding_face_image.append(encode_image)
        id_face_image.append(file_name)

     

