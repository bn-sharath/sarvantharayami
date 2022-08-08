import os
import cv2
import numpy as np
import face_recognition
from imutils import paths

# images_in_db = ""
encoding_face_image = []
id_face_image = []
match = None
noMatch = None

face_dir = paths.list_images(os.path.join(os.getcwd(), "database_images"))
testing_face_dir = paths.list_images(os.path.join(os.getcwd(), "test_image"))

for image_file in face_dir:
    i_path, i_filename = os.path.split(image_file)
    file_name, file_extension = os.path.splitext(i_filename)

    image = face_recognition.load_image_file(image_file)
    encode_image = face_recognition.face_encodings(image)[0]
    encoding_face_image.append(encode_image)
    id_face_image.append(file_name)


# print(encoding_face_image)
# print(id_face_image)

for image_test in testing_face_dir:
    i_path, i_filename = os.path.split(image_test)
    file_name, file_extension = os.path.splitext(i_filename)

    image = face_recognition.load_image_file(image_test)
    face_loc = face_recognition.face_locations(image)
    encoding_test_image = face_recognition.face_encodings(image, face_loc)

    for face_encode, location in zip(encoding_test_image, face_loc):
        results = face_recognition.compare_faces(
            encoding_face_image, face_encode)
        # print(results)
        if True in results:
            match = {
                id_face_image[results.index(True)]: file_name
            }
            print(match)
        # else:
        #     noMatch = {
        #         id_face_image[results.index(False)]: file_name
        #     }
        #     print(noMatch)


