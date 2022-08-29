# import os
from multiprocessing import Process
import os
import cv2
import face_recognition

from web_application.main import found_result
# from imutils import paths

Criminal_encodings = []
Criminal_image_path = []
Criminal_obj = []

Missing_encodings = []
Missing_image_path = []
Missing_obj = []

Wanted_encodings = []
Wanted_image_path = []
Wanted_obj = []

Allowed_encodings = []
Allowed_image_path = []
Allowed_obj = []

Not_allowed_encodings = []
Not_allowed_image_path = []
Not_allowed_obj = []


videocapture_cctv =[]
frames=[]

FOUNDED_IMAGE_DIR = os.path.join("static","found")
# def hello():
#     obj = cv2.VideoCapture("http://192.168.0.104:8080/video")
#     while True:
#         try:
#             r, frame = obj.read()
#             cv2.imshow("hello", frame)
#         except:
#             print("breaking")
#             exit()
#             # break
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     obj.release()
#     cv2.destroyAllWindows()
    
    
def collect_person(c_db,m_db,w_db,a_db,n_db):
    for c in c_db:
        Criminal_image_path.append(c.image_path)
        Criminal_obj.append(c)
        # img = cv2.imread(c.image_path)
        img = face_recognition.load_image_file(c.image_path)
        img =  cv2.resize(img, (0,0), None, 0.25,0.25)
        encode_img =face_recognition.face_encodings(img)[0]
        Criminal_encodings.append(encode_img)
        # cv2.imshow("hello",img)
        print(c.image_path)
        # cv2.waitKey(0)
    for c in m_db:
        Missing_image_path.append(c.image_path)
        Missing_obj.append(c)
        img = face_recognition.load_image_file(c.image_path)
        # img = cv2.imread(c.image_path)
        img =  cv2.resize(img, (0,0), None, 0.25,0.25)
        encode_img =face_recognition.face_encodings(img)[0]
        Missing_encodings.append(encode_img)
        print(c.image_path)
        
    for c in a_db:
        Wanted_image_path.append(c.image_path)
        Wanted_obj.append(c)
        img = face_recognition.load_image_file(c.image_path)
        # img = cv2.imread(c.image_path)
        img =  cv2.resize(img, (0,0), None, 0.25,0.25)
        encode_img =face_recognition.face_encodings(img)[0]
        Wanted_encodings.append(encode_img)
        print(c.image_path)
        
    for c in w_db:
        Allowed_image_path.append(c.image_path)
        Allowed_obj.append(c)
        img = face_recognition.load_image_file(c.image_path)
        # img = cv2.imread(c.image_path)
        img =  cv2.resize(img, (0,0), None, 0.25,0.25)
        encode_img =face_recognition.face_encodings(img)[0]
        Allowed_encodings.append(encode_img)
        print(c.image_path)
        
    for c in n_db:
        Not_allowed_image_path.append(c.image_path)
        img = face_recognition.load_image_file(c.image_path)
        Not_allowed_obj.append(c)
        # img = cv2.imread(c.image_path)
        img =  cv2.resize(img, (0,0), None, 0.25,0.25)
        encode_img =face_recognition.face_encodings(img)[0]
        Not_allowed_encodings.append(encode_img)
        print(c.image_path)
 
def show_video(frame):
    frames.append(frame)
    
    
def frame_encoding(f):
    face_loc = face_recognition.face_locations(f)
    encoding_test_image = face_recognition.face_encodings(f, face_loc)
    for face_encode, location in zip(encoding_test_image, face_loc):
        criminal_result = face_recognition.compare_faces(Criminal_encodings, face_encode)
        missing_result = face_recognition.compare_faces(Missing_encodings, face_encode)
        wanted_result = face_recognition.compare_faces(Wanted_encodings, face_encode)
        allowed_result = face_recognition.compare_faces(Allowed_encodings, face_encode)
        not_allowed_result = face_recognition.compare_faces(Not_allowed_encodings, face_encode)
        
        if True in criminal_result:
            obj = Criminal_obj[criminal_result.index(True)]
            ipath =Criminal_image_path[criminal_result.index(True)]
            cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj._id),img=f)
            found_result(person_obj=obj,image_path=ipath, image=FOUNDED_IMAGE_DIR+str(obj._id),type_of_person="criminal")
            
        if True in missing_result:
            obj = Missing_obj[missing_result.index(True)]
            ipath =Missing_image_path[missing_result.index(True)]
            cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj._id),img=f)
            found_result(person_obj=obj,image_path=ipath, image=FOUNDED_IMAGE_DIR+str(obj._id),type_of_person="missing person")
            
        if True in wanted_result:
            obj = Wanted_obj[wanted_result.index(True)]
            ipath =Wanted_image_path[wanted_result.index(True)]
            cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj._id),img=f)
            found_result(person_obj=obj,image_path=ipath, image=FOUNDED_IMAGE_DIR+str(obj._id),type_of_person="wanted person")
                
        if True in allowed_result:
            obj = Allowed_obj[allowed_result.index(True)]
            ipath =Allowed_image_path[allowed_result.index(True)]
            cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj._id),img=f)
            found_result(person_obj=obj,image_path=ipath, image=FOUNDED_IMAGE_DIR+str(obj._id), type_of_person="allowed person")
            
        if True in not_allowed_result:
            obj = Not_allowed_obj[not_allowed_result.index(True)]
            ipath =Not_allowed_image_path[not_allowed_result.index(True)]
            cv2.imwrite(filename=FOUNDED_IMAGE_DIR+str(obj._id),img=f)
            found_result(person_obj=obj,image_path=ipath, image=FOUNDED_IMAGE_DIR+str(obj._id),type_of_person="not allowed person")
        
        
def collect_cctv(cctv_ip):
    
    for ip in cctv_ip:
        cap = "http://" + str(ip.ip)
        videocapture_cctv.append(cv2.VideoCapture(cap))
        print(ip.ip)
    
    while True:
        for i in range(len(videocapture_cctv)):
            _, f = videocapture_cctv[i].read()
            show_video(f)
            cv2.imshow(str(i),frames[i])
            Process(target=frame_encoding, args=(frames[i],)).start()
            
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     exit()    
        for tv in videocapture_cctv:
            tv.release()