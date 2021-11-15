import pytsk3, sys
import shutil
from distutils.dir_util import copy_tree
import time

#start = time.time()  # 시작 시간 저장

class Extract_File:

    def __init__(self):
        self.volume='\\\\.\\'+ str(sys.argv[1]) #드라이브
        self.img=pytsk3.Img_Info(self.volume) #드라이브 파일 핸들 생성
        self.fs=pytsk3.FS_Info(self.img) #파일 핸들 이용해서 드라이브 내부 정보

    # $MFT, $LogFile
    def Extract(self,filename,output_name):
        f=self.fs.open(filename)
        with open(output_name,'wb') as o:
            offset=0
            size=f.info.meta.size
            while offset<size:
                available_to_read=min(1024*1024,size-offset)
                buf = f.read_random(0,available_to_read)
                if not buf: break
                o.write(buf)
                offset+=len(buf)

    # $UsnJrnl 
    def Extract_UsnJrnl(self):
        f=self.fs.open('/$Extend/$UsnJrnl')
        found=False
        
        for attr in f:
            if attr.info.name == b'$J':
                found=True
                break
        if not found:
            sys.exit(0)
        
        with open('$UsnJrnl','wb') as o:
            offset=0
            size=attr.info.size
            while offset < size:
                available_to_read=min(1024*1024,size-offset)
                buf=f.read_random(offset,available_to_read,attr.info.type,attr.info.id) #attr.info.type,attr.info.id
                if not buf:
                    break
                o.write(buf)
                offset+=len(buf)

def main():
    Ext=Extract_File()
    Ext.Extract('/$MFT','$MFT')
    Ext.Extract('/$LogFile','$LogFile')
    Ext.Extract_UsnJrnl()

if __name__ == '__main__':
    main()

#print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
