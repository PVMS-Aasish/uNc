
import cv2
import time
import dropbox
import random

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
        return img_name 
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = 'sl.AyZD68SkdVpgMv3v2CEKn5yKq4FMuq7RAIDT3FCesu61zAzXcSE6iPYXxAR7hhvkQsSvyaVPgvdOGCfcOyQJOiWMmD7VwMNhytEAaI4WVfpWbe4scjQJVyU7CL7vTMVy_B6ecv9-rF8'
    file=img_name
    file_from=file
    file_to="/cNu/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=18):
            name=take_snapshot()
            upload_file(name)
        
main()
