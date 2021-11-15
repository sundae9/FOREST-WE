import os, subprocess
import socket
import platform
import datetime
import shutil
from distutils.dir_util import copy_tree
import sys
import time

#start = time.time()  # 시작 시간 저장

# Host PC 정보 (OS 버전, Host 이름, Login 계정)
def hostinfo():
    try:
        print("\n=== Host PC info ===")
        print("OS Version:", platform.system(),platform.version())
        print("Host name:", socket.gethostname())
        winid = os.getlogin()
        print("Login Account:", winid)
    except Exception as ex:
        print(ex)
    return winid

# 아티팩트 수집 폴더 생성
def create(path):
    print("\nCreate Directory Path:",path+"/Desktop/Art")
    try:
        os.makedirs(path+"/Desktop/Art/Chrome",exist_ok=True)
        os.makedirs(path +"/Desktop/Art/Edge", exist_ok=True)
        os.makedirs(path +"/Desktop/Art/IE", exist_ok=True)  
    except Exception as ex:
        print(ex)

# 크롬 아티팩트 수집
def chrome(path):
    try:
        print("[*] Chrome Browser artifact Collecting...")
        check = os.path.isdir(path+"/AppData/Local/Google")
        if check == False:
            print("[!] Not Found Chrome Path... Default Path is "+str(check))
        else:
            print("[!] Chrome Directory Path: "+path+"/AppData/Local/Google")
        print("[+] Chrome History, Cache, Cookies, Download List Copying...")

        history = path+"/AppData/Local/Google/Chrome/User Data/Default/History"
        cookies = path+"/AppData/Local/Google/Chrome/User Data/Default/Cookies"
        cache = path+"/AppData/Local/Google/Chrome/User Data/Default/Cache/"

        shutil.copy2(history, path+"/Desktop/Art/Chrome/History")
        shutil.copy2(cookies, path + "/Desktop/Art/Chrome/Cookies")
        copy_tree(cache, path + "/Desktop/Art/Chrome/Cache")
    except Exception as ex:
        print(ex)

# 엣지 아티팩트 수집
def edge(path):
    try:
        print("\n[*] Edge Browser artifact Collecting...")
        check = os.path.isdir(path+"/AppData/Local/Microsoft/Edge")
        if check == False:
            print("[!] Not Found Edge Path... Default Path is"+check)
        else:
            print("[!] Edge Directory Path: "+path+"/AppData/Local/Microsoft/Edge")
        print("[+] Edge History, Cache, Cookies, Download List Copying...")

        history = path+"/AppData/Local/Microsoft/Edge/User Data/Default/History"
        cookies = path+"/AppData/Local/Microsoft/Edge/User Data/Default/Cookies"
        cache = path+"/AppData/Local/Microsoft/Edge/User Data/Default/Cache/"

        shutil.copy2(history, path+"/Desktop/Art/Edge/History")
        shutil.copy2(cookies, path + "/Desktop/Art/Edge/Cookies")
        copy_tree(cache, path + "/Desktop/Art/Edge/Cache")
    except Exception as ex:
        print(ex)

# 익스플로어 아티팩트 수집 (Permission denied)
def ie(path,user):
    try:
        print("\n[*] IE Browser artifact Collecting...")
        check = os.path.isdir(path+"/AppData/Local/Microsoft/Windows")
        if check == False:
            print("[!] Not Found IE Path... Default Path is"+check)
        else:
            print("[!] IE Directory Path: "+path+"/AppData/Local/Microsoft/Windows")
        print("[+] IE History, Cache, Cookies, Download List Copying...")

        history = 'C:\\Users\\{}\\AppData\\Local\\Microsoft\\Windows\\WebCache\\WebCacheV*.dat'.format(user)
        cookies = path+"/AppData/Local/Microsoft/Windows/INetCookies/"
        cache = path+"/AppData/Local/Microsoft/Windows/INetCache/IE/"
        downlist = path+"/AppData/Local/Microsoft/Windows/IEDownloadHistory/"

        copy_tree(cookies, path + "/Desktop/Art/IE/Cookies")
        copy_tree(cache, path + "/Desktop/Art/IE/Cache")    
        copy_tree(downlist, path + "/Desktop/Art/IE/DownloadList")

        # WebCacheV*.dat 파일 COPY
        os.system('taskkill /f /im taskhostw.exe')
        os.system('taskkill /f /im dllhost.exe')   
        copyPath = 'C:\\Users\\{}\\Desktop\\Art\\IE\\History'.format(user)
        command = 'xcopy /s /h /i /y "{0}" {1}'.format(history,copyPath) 
        os.system(command)
    except Exception as ex:
        print(ex)

def main():
    print("[*] Browser artifact parsing module")
    runtime = datetime.datetime.now()
    print("[+] Run Time:", runtime)
    
    users = os.listdir(r'C:\Users')
    
    for user in users:
        try:
            if os.path.isdir('C:\\Users\\'+user):
                path = 'C:/Users/'+user
                create(path)
                chrome(path)
                edge(path)
                ie(path,user) 
        except PermissionError:
            print('[!] Permission denied')
            break

    print("End")


if __name__=="__main__":
    main()

#print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


