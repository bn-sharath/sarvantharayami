import random

def createOTP():
    otp=""
    for i in range(4):
        otp+=str(random.randint(0,9))
    # otp=random.randint(0000,9999)
    return otp


def createKEY(permission,name,uniqueNO):
    key=str(permission)+"_"+str(uniqueNO)+"@"+str(name)
    return key
    
if __name__ == '__main__':
    print("working fine")