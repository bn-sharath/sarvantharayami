import os

def folder_create(folder_path,name):
    cpath =os.path.join(folder_path,name)
    try:
        os.mkdir(cpath)
        print("success")
    except:
        print("can not create folder")
        exit()
    
def folder_delete(name):
    pass
    
    
    
    
if __name__ == "__main__":
    folder_create("sharath")