import os
import socket
import platform
import datetime
import shutil

from distutils.dir_util import copy_tree


def hostinfo():
    try:
        print("\n=== Host PC info ===")
        print("OS Version:", platform.system(),platform.version())
        print("Host name:", socket.gethostname())
        winid = os.getlogin()  # 사용자 이름 가져오기
        print("Login Account:", winid)
    except Exception as ex:  # ex는 발생한 에러의 이름을 받아오는 변수
        print(ex)
    return winid

def log():
    print("123")

def create(path):
    print("Create Directory Path:",path+"/Desktop/Art")
    try:
        # 디렉터리 생성
        
        #지속실행 등록 저장 폴더 
        os.makedirs(path +"/Desktop/Art/continuous execution", exist_ok=True)
        os.makedirs(path +"/Desktop/Art/continuous execution/Startup", exist_ok=True)
        os.makedirs(path +"/Desktop/Art/continuous execution/Scheduler", exist_ok=True)
        os.makedirs(path +"/Desktop/Art/continuous execution/System Time", exist_ok=True)


        #파일 열기 및 생성 저장 폴더
        os.makedirs(path +"/Desktop/Art/File_create_open", exist_ok=True)        
        os.makedirs(path +"/Desktop/Art/File_create_open/RecentDocs", exist_ok=True)        
        os.makedirs(path +"/Desktop/Art/File_create_open/HWPRecentFiles", exist_ok=True)        
        os.makedirs(path +"/Desktop/Art/File_create_open/OfficeRecentFiles", exist_ok=True)        
        os.makedirs(path +"/Desktop/Art/File_create_open/LNKFiles", exist_ok=True)        
        os.makedirs(path +"/Desktop/Art/File_create_open/Jumplist", exist_ok=True)        


        #프로그램 실행저장 폴더
        os.makedirs(path +"/Desktop/Art/program_start", exist_ok=True)        
        os.makedirs(path +"/Desktop/Art/program_start/prefetch", exist_ok=True)      
        os.makedirs(path +"/Desktop/Art/program_start/PowerShell Event", exist_ok=True)      
        os.makedirs(path +"/Desktop/Art/program_start/Amcache", exist_ok=True)


        #계정 사용 저장 폴더
        os.makedirs(path +"/Desktop/Art/user_account", exist_ok=True)      
        os.makedirs(path +"/Desktop/Art/user_account/Succes Fail Logons", exist_ok=True)      
        os.makedirs(path +"/Desktop/Art/user_account/RDP Usage", exist_ok=True)      
        os.makedirs(path +"/Desktop/Art/user_account/RDP Usage/Cache", exist_ok=True)      
        
        
        #메모리 오류 저장 폴더
        os.makedirs(path +"/Desktop/Art/WER", exist_ok=True)

        #로컬 F/W
        os.makedirs(path +"/Desktop/Art/Windows Defender", exist_ok=True)

        #휴지통
        os.makedirs(path +"/Desktop/Art/RecycleBin", exist_ok=True)

        #타임라인
        os.makedirs(path +"/Desktop/Art/TimeLine", exist_ok=True)
        
        #레지스트리
        os.makedirs(path +"/Desktop/Art/Registry", exist_ok=True)
        
    except Exception as ex:
        print(ex)


 # 권한으로 인한 작동 안됨
def Registry(path):  #레지스트리 내용 수집(SAM, SECURITY, SOFTWARE, SYSTEM, DEFAULT, NTUSER.DAT)
    try:
        print("\n\n-------------------------------------------------------------------\n")
        print("[*] Registry artifact Collecting...")
        registry_path = "C:\Windows\System32\config"
        check = os.path.isdir(registry_path)
        if check == False :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ check)
        else :
            print("[!] Registry Directory Path : "+registry_path)
        print("[+] Registry Copying...")

        shutil.copy2(registry_path+"\SAM", "/Desktop/Art/Registry")
        shutil.copy2(registry_path+"\SECURITY", "/Desktop/Art/Registry")
        shutil.copy2(registry_path+"\SOFTWARE", "/Desktop/Art/Registry")
        shutil.copy2(registry_path+"\SYSTEM", "/Desktop/Art/Registry")
        shutil.copy2(registry_path+"\DEFAULT", "/Desktop/Art/Registry")
        shutil.copy2(path+"\\NTUSER.DAT", "/Desktop/Art/Registry")
                 
    except Exception as ex:
        print(ex)



def File_create_open(path): # 파일 열기 및 생성 관련 아티팩트 
    try:
        print("\n\n-------------------------------------------------------------------\n")
        print("[*] File_create_open artifact Collecting...")
        
        RecentDocs_path = path+"\AppData\Roaming\Microsoft\Windows\Recent"
        HWPRecentFiles_path = path+"\AppData\Roaming\HNC\Office\Recent"
        OfficeRecentFiles_path = path+"\AppData\Roaming\Microsoft\Office\Recent"
        LNKFiles_path = path+"\AppData\Roaming\Microsoft\Windows\Recent"
        Jumplist_path = path+"\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations"


        RecentDocs_check = os.path.isdir(RecentDocs_path)
        HWPRecentFiles_check = os.path.isdir(HWPRecentFiles_path)
        OfficeRecentFiles_check = os.path.isdir(OfficeRecentFiles_path)
        LNKFiles_check = os.path.isdir(LNKFiles_path)
        Jumplist_check = os.path.isdir(Jumplist_path)

        #아티팩트 경로 체크
        if RecentDocs_check == True :
            print("[!] RecentDocs Directory Path : "+RecentDocs_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ RecentDocs_path)

        if HWPRecentFiles_check == True :
            print("[!] OfficeRecentFiles Event Directory Path : "+OfficeRecentFiles_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ OfficeRecentFiles_path)

        if OfficeRecentFiles_check == True :
            print("[!] HWPRecentFiles Directory Path : "+HWPRecentFiles_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ HWPRecentFiles_path)

        if LNKFiles_check == True :
            print("[!] LNKFiles Directory Path : "+LNKFiles_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ LNKFiles_path)

        if Jumplist_check == True :
            print("[!] Jumplist Directory Path : "+Jumplist_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ Jumplist_path)


        print("[+] File_create_open Copying...")
              
        copy_tree(RecentDocs_path, path+"/Desktop/Art/File_create_open/RecentDocs") # 폴더 통채로 복사 , shutil.copy2()는 파일 한개 복사
        copy_tree(OfficeRecentFiles_path, path+"/Desktop/Art/File_create_open/OfficeRecentFiles") 
        copy_tree(HWPRecentFiles_path, path+"/Desktop/Art/File_create_open/HWPRecentFiles") 
        copy_tree(LNKFiles_path, path+"/Desktop/Art/File_create_open/LNKFiles") 
        copy_tree(Jumplist_path, path+"/Desktop/Art/File_create_open/Jumplist") 
         
    except Exception as ex:
        print(ex)

   
    
def program_start(path) : # 프로그램 실행
    try:
        print("\n\n-------------------------------------------------------------------\n")
        print("[*] program_start artifact Collecting...")
        
        prefetch_path = "C:\Windows\Prefetch"
        psevent_ptah = "C:\Windows\System32\winevt\Logs"
        Amcache_path = "C:\\Windows\\appcompat\\Programs"


        prefetch_check = os.path.isdir(prefetch_path)
        psevent_check = os.path.isdir(psevent_ptah)
        Amcache_check = os.path.isdir(Amcache_path)
       
 
        if prefetch_check == True :
            print("[!] Prefetch Directory Path : "+prefetch_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ prefetch_path)

        if psevent_check == True :
            print("[!] PowerShell Event Directory Path : "+psevent_ptah)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ psevent_ptah)

        if Amcache_check == True :
            print("[!] Amcache Directory Path : "+Amcache_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ Amcache_path)


        print("[+] program_start Copying...")
              
        copy_tree(prefetch_path, path+"/Desktop/Art/program_start/prefetch") # 폴더 통채로 복사 , shutil.copy2()는 파일 한개 복사
        shutil.copy2(psevent_ptah+"\Microsoft-Windows-PowerShell%4Operational.evtx", path+"/Desktop/Art/program_start/PowerShell Event") 
        shutil.copy2(Amcache_path+"\Amcache.hve", path+"/Desktop/Art/program_start/Amcache") 
 
         
    except Exception as ex:
        print(ex)




def user_account(path) : # 계정 사용 
    try:
        print("\n\n-------------------------------------------------------------------\n")
        print("[*] user account artifact Collecting...")
        
        SuccesEvt_path = "C:\Windows\System32\winevt\Logs"
        RDPEvt_path = "C:\Windows\System32\winevt\Logs"  # System.evtx 찾기 위한 경로
        RDPEvtcache_path = path+"\AppData\Local\Microsoft\Terminal Server Client\Cache" #Microsoft\Terminal Server Client\Cache 경로

        SuccesEvt_check = os.path.isdir(SuccesEvt_path)
        RDPEvt_check = os.path.isdir(RDPEvt_path)
        RDPEvtcach_check = os.path.isdir(RDPEvtcache_path)
       
        
        if SuccesEvt_check == True :
            print("[!] Succes/Fail Logons Directory Path : "+SuccesEvt_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ SuccesEvt_path)
        if RDPEvt_check == True :
            print("[!] RDP Usage Directory Path : "+RDPEvt_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ RDPEvt_path)
        if RDPEvtcach_check == True :
            print("[!] RDP Usage cache Directory Path : "+RDPEvtcache_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ RDPEvtcache_path)

                
        print("[+] user account Copying...")
        
        shutil.copy2(SuccesEvt_path+"\Security.evtx", path+"/Desktop/Art/user_account/Succes Fail Logons") # 폴더 통채로 복사 , shutil.copy2()는 파일 한개 복사
        shutil.copy2(RDPEvt_path+"\System.evtx", path+"/Desktop/Art/user_account/RDP Usage") 
        copy_tree(RDPEvtcache_path, path+"/Desktop/Art/user_account/RDP Usage/Cache") 
 
         
    except Exception as ex:
        print(ex)


def continuous_execution(path) : # 지속실행 등록
    try:
        print("\n\n-------------------------------------------------------------------\n")
        print("[*] Continuous Executiont artifact Collecting...")
        
        Startup_path = path+"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"  # 시작 프로그램 경로
        Scheduler_path = "C:\Windows\System32\Tasks"  # 스케줄러 폴더 경로(Tasks)
        SystemTime_path = "C:\Windows\System32\winevt\Logs"  # System.evtx 찾기 위한 경로

        Startup_check = os.path.isdir(Startup_path)
        Scheduler_check = os.path.isdir(Scheduler_path)
        SystemTime_check = os.path.isdir(SystemTime_path)
       
        
        if Startup_check == True :
            print("[!] Startup Directory Path : "+Startup_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ Startup_path)
        if Scheduler_check == True :
            print("[!] Scheduler Directory Path : "+Scheduler_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ Scheduler_path)
        if SystemTime_check == True :
            print("[!] SystemTime Directory Path : "+SystemTime_path)
        else :
            print("[!] Not Found Prefetcg Path.... Default Path is "+ SystemTime_path)

                
        print("[+] Continuous Executiont Copying...")
        
        copy_tree(Startup_path, path+"/Desktop/Art/continuous execution/Startup") 
        copy_tree(Scheduler_path, path+"/Desktop/Art/continuous execution/Scheduler") 
        shutil.copy2(SystemTime_path+"\Security.evtx", path+"/Desktop/Art/continuous execution/System Time") 
        shutil.copy2(SystemTime_path+"\System.evtx", path+"/Desktop/Art/continuous execution/System Time")
 
    except Exception as ex:
        print(ex)


def TimeLine(path) :
    try:
        print("\n\n-------------------------------------------------------------------\n")
        print("[*] TimeLine artifact Collecting...")
        timeline_path = path+"\AppData\Local\ConnectedDevicesPlatform\388c4b714cf9ab22"
        check = os.path.isdir(timeline_path)

        if check == False :
            print("[!] Not Found Prefetcg Path.... Default Path is "+check)
        else :
            print("[!] TimeLine Directory Path : "+timeline_path)
        print("[+] TimeLine Copying...")
              
        copy_tree(timeline_path, path+"/Desktop/Art/TimeLine") # 폴더 통채로 복사 , shutil.copy2()는 파일 한개 복사
                
    except Exception as ex:
        print(ex)



def  WindowsDefender(path) : # Windows Defender 수집
    try:
        print("\n\n-------------------------------------------------------------------\n")
        print("[*] Windows Defender artifact Collecting...")

        WinDefender_path = "C:\ProgramData\Microsoft\Windows Defender\Scans\History\Service\DetectionHistory"  # Windows Defender 관련 폴더 경로
        
        check = os.path.isdir(str(WinDefender_path))
        if check == False :
            print("[!] Not Found Prefetcg Path.... Default Path is "+check)
        else :
            print("[!] Windows Defender Directory Path : "+WinDefender_path)
        print("[+] Windows Defender Copying...")
              
        copy_tree(WinDefender_path, path+"/Desktop/Art/Windows Defender") # 폴더 통채로 복사 , shutil.copy2()는 파일 한개 복사
                
    except Exception as ex:
        print(ex)      

  

def WER(path) : #WER(Windows Error Reporting) 수집
    try:
        print("\n\n-------------------------------------------------------------------\n")
        print("[*] WER artifact Collecting...")

        WER_path = "C:\ProgramData\Microsoft\Windows\WER"  # System.evtx 찾기 위한 경로

        check = os.path.isdir(WER_path)
        if check == False :
            print("[!] Not Found Prefetcg Path.... Default Path is "+check)
        else :
            print("[!] WER Directory Path : "+WER_path)
        print("[+] WER Copying...")
              
        copy_tree(WER_path, path+"/Desktop/Art/WER") 
                
    except Exception as ex:
        print(ex)      


def Recycle(path) : #Recycle 수집
    try:
        print("\n\n-------------------------------------------------------------------\n")
        print("[*] Recycle artifact Collecting...")

        Recycle_path = "C:\$Recycle.Bin"  

        check = os.path.isdir(Recycle_path)
        if check == False :
            print("[!] Not Found Prefetcg Path.... Default Path is "+check)
        else :
            print("[!] Recycle Directory Path : "+Recycle_path)
        print("[+] Recycle Copying...")
              
        copy_tree(Recycle_path, path+"/Desktop/Art/RecycleBin") 
                
    except Exception as ex:
        print(ex)      



def main():

    print("----------artifact parsing module Test --------")
    runtime = datetime.datetime.now()
    print("[+] Run Time:", runtime)
    info = hostinfo()
    path = "C:/Users/{}".format(info)
    create(path)

    Registry(path)
    TimeLine(path) 

    File_create_open(path)
    program_start(path) 
    user_account(path)
    continuous_execution(path)
    
    WindowsDefender(path)
    WER(path)
    Recycle(path)


    

    print("\n\n-------------------  END  --------------------------------------------\n")
    lasttime = datetime.datetime.now()
    print("[-] Last Time :", lasttime)    
    print("걸린 시간 : ", (lasttime-runtime), "초 \n\n")

if __name__=="__main__":
    main()
    
    
    
    
