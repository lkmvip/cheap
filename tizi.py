import requests ,json ,random ,re ,time ,selenium ,os #line:1
from selenium import webdriver #line:2
from selenium .webdriver .common .by import By #line:3
from selenium .webdriver .support import expected_conditions as EC #line:4
from selenium .webdriver .support .ui import WebDriverWait #line:5
TG_USER_ID =''#line:6
def get_email ():#line:7
    OOO00O0OOOO0OOO00 =random .randint (11 ,9999 )#line:8
    OO00OO0OOOOO00O00 =random .randint (0 ,2000 )#line:9
    OOO0OOOO000O0000O ='varytmp+{}uu{}d@gmail.com'.format (OOO00O0OOOO0OOO00 ,OO00OO0OOOOO00O00 )#line:10
    return OOO0OOOO000O0000O #line:11
def send (OOOOO0O0O0O00O0OO ):#line:12
    OOOO0OOO0OO0O0O0O ={'email':OOOOO0O0O0O00O0OO }#line:15
    OOOOO00OOO0OOOO00 =requests .post (url ='https://cv2.cheap/auth/send',data =OOOO0OOO0OO0O0O0O ).text #line:16
def get_num (OO000OO0OOO0OOOO0 ):#line:18
    global Driver #line:19
    OO0OOO00OOOO000O0 ={'Cookie':'csrf_gmailnator_cookie=9283eccf4672e233327c1d07cbde2fbe; __gads=ID=808c92a03a3667c7-2268f1463cc6007d:T=1614844196:RT=1614845007:S=ALNI_MaEB-hZfUPTo6kHkEmOBLzPe4nqTQ; cto_bundle=AGHOXV9XSVpTNzY3TlRHbldjMDY5RFhQTlU4Y2J1cUpIWGNLVU0xa3ZiWGRKV1duNHo5cXpJYSUyQm5mZ0ROVDJBRFlIa211cG85JTJCOElMV0ZGQUIzVCUyRjg4NTdQZmZSSW9xMzZmMVY5dXdXeDViUUFYeG51SWNibEhqZGxqWGU5NjBQZHpxMg; _ga=GA1.2.1618068840.1614844229; _gid=GA1.2.103981802.1614844229; ci_session=15d382f04f7b998cecd0f9158bfe3db2c8f32629; __cfduid=d1f9a21dd34e5060cfd24ea55f37149961614844181'}#line:22
    OOOOO0O00O0OO0OOO ={'csrf_gmailnator_token':'9283eccf4672e233327c1d07cbde2fbe','action':'LoadMailList','Email_address':OO000OO0OOO0OOOO0 }#line:24
    try :#line:25
        O00O000OOOOOO00O0 =requests .post (url ='https://www.gmailnator.com/mailbox/mailboxquery',data =OOOOO0O00O0OO0OOO ,headers =OO0OOO00OOOO000O0 ).text #line:26
        OO00OOOO0O0O00OOO =re .findall (r'(?<=messageid\\/#).+(?=\\">\\n\\t\\t\\t\\t\\t<table class=\\"message_container)',O00O000OOOOOO00O0 )[0 ]#line:27
        OO0O0O0O000OOOOOO ={'csrf_gmailnator_token':'9283eccf4672e233327c1d07cbde2fbe','action':'get_message','message_id':OO00OOOO0O0O00OOO ,'email':'varytmp'}#line:29
        OO0O00O0O00OO00O0 =requests .post (url ='https://www.gmailnator.com/mailbox/get_single_message/',headers =OO0OOO00OOOO000O0 ,data =OO0O0O0O000OOOOOO ).text #line:30
        O00OOOO00OO0O00OO =re .findall (r'(?<=\\uff1a\\r\\n\\r\\n).+(?=\\r\\n \\r\\n\\u795d\\u987a\\)',OO0O00O0O00OO00O0 )[0 ].replace ('\\','')#line:32
        Driver .get (O00OOOO00OO0O00OO )#line:35
        time .sleep (2 )#line:36
        telegram_bot ("梯子",'邀请成功！')#line:37
        Driver .quit ()#line:38
    except Exception as O0OO0O0OO0000OO00 :#line:39
        print (O0OO0O0OO0000OO00 )#line:40
        Driver .close ()#line:41
def register (O0OO00O0O0O00O000 ,O0O0OO000OOO000OO ):#line:42
    global Driver #line:43
    O0O000O000O0O00OO =webdriver .ChromeOptions ()#line:44
    O0O000O000O0O00OO .add_argument ('--headless')#line:45
    O0O000O000O0O00OO .add_argument ('--disable-gpu')#line:46
    O0O000O000O0O00OO .add_argument ('--window-size=1366,768')#line:47
    O0O000O000O0O00OO .add_argument ("--no-sandbox")#line:48
    Driver =webdriver .Chrome (options =O0O000O000O0O00OO )#line:49
    try :#line:50
        Driver .get (O0O0OO000OOO000OO )#line:52
        time .sleep (2 )#line:54
        Driver .find_element_by_xpath ('//*[@id="header"]/div[2]/div[1]/div/div[2]/a').click ()#line:55
        WebDriverWait (Driver ,10 ).until (EC .element_to_be_clickable ((By .ID ,'register')))#line:57
        Driver .find_element_by_xpath ('//*[@id="id_username"]').send_keys (O0OO00O0O0O00O000 )#line:58
        Driver .find_element_by_xpath ('//*[@id="id_password1"]').send_keys ('refddr265rt!')#line:59
        Driver .find_element_by_xpath ('//*[@id="id_password2"]').send_keys ('refddr265rt!')#line:60
        Driver .find_element_by_xpath ('//*[@id="register"]/div/div/div/div[2]/form/div[5]/button').click ()#line:61
        time .sleep (2 )#line:62
        Driver .find_element_by_xpath ('/html/body/div[11]/div/div[4]/div/button').click ()#line:63
        time .sleep (1 )#line:64
        Driver .find_element_by_xpath ('//*[@id="send-confirm-email"]').click ()#line:65
        time .sleep (5 )#line:66
    except Exception as OOOO0OOO0OO00000O :#line:67
        
        telegram_bot ("梯子",'邀请失败！')#line:69
def telegram_bot (O0OOO000O0OOOOO00 ,O0OOO00OOOO00O00O ):#line:70
    
    OOO00O000OOO0OOOO =TG_USER_ID #line:72
    if "TG_USER_ID"in os .environ :#line:73
        OO000O000O0O0O0OO =os .environ ["TG_BOT_TOKEN"]#line:74
        OOO00O000OOO0OOOO =os .environ ["TG_USER_ID"]#line:75
    if not OO000O000O0O0O0OO or not OOO00O000OOO0OOOO :#line:76
        
        return #line:78
    
    OOO0OO00O000OO000 ={"chat_id":OOO00O000OOO0OOOO ,"text":O0OOO000O0OOOOO00 +'\n\n'+O0OOO00OOOO00O00O ,"disable_web_page_preview":"true"}#line:80
    OO00O0O00O00OO00O =requests .post (url ='https://api.telegram.org/bot%s/sendMessage'%(OO000O000O0O0O0OO ),data =OOO0OO00O000OO000 )#line:82
    
def main (OO00O0000000O0O00 ):#line:86
    OOOOO00O00OO00OO0 =get_email ()#line:87
    register (OOOOO00O00OO00OO0 ,OO00O0000000O0O00 )#line:88
    time .sleep (5 )#line:89
    get_num (OOOOO00O00OO00OO0 )#line:90
    return True #line:91
if __name__ =="__main__":#line:92
    invite =os .environ ["INVITECODE"]#line:93
    print (invite )#line:94
    if "START"in os .environ and os .environ ["START"]=='584UFTGB888':#line:95
        main (invite )#line:96
    else :#line:97
        
        telegram_bot ("梯子",'没有启动码!')
