import requests, json, random, re, time,selenium,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
TG_USER_ID = ''             # telegram 用户ID
def get_email():
    a = random.randint(11, 999)
    b = random.randint(0, 200)
    email = 'varytmp+{}uu{}d@gmail.com'.format(a, b)
    return email
def send(email):
    data = {
        'email': email
    }
    s = requests.post(url='https://cv2.cheap/auth/send', data=data).text
    #print(s)
def get_num(email):
    global Driver
    #print(email)
    head = {
        'Cookie': 'csrf_gmailnator_cookie=9283eccf4672e233327c1d07cbde2fbe; __gads=ID=808c92a03a3667c7-2268f1463cc6007d:T=1614844196:RT=1614845007:S=ALNI_MaEB-hZfUPTo6kHkEmOBLzPe4nqTQ; cto_bundle=AGHOXV9XSVpTNzY3TlRHbldjMDY5RFhQTlU4Y2J1cUpIWGNLVU0xa3ZiWGRKV1duNHo5cXpJYSUyQm5mZ0ROVDJBRFlIa211cG85JTJCOElMV0ZGQUIzVCUyRjg4NTdQZmZSSW9xMzZmMVY5dXdXeDViUUFYeG51SWNibEhqZGxqWGU5NjBQZHpxMg; _ga=GA1.2.1618068840.1614844229; _gid=GA1.2.103981802.1614844229; ci_session=15d382f04f7b998cecd0f9158bfe3db2c8f32629; __cfduid=d1f9a21dd34e5060cfd24ea55f37149961614844181'}
    data = {'csrf_gmailnator_token': '9283eccf4672e233327c1d07cbde2fbe', 'action': 'LoadMailList',
            'Email_address': email}
    try:
        s = requests.post(url='https://www.gmailnator.com/mailbox/mailboxquery', data=data, headers=head).text
        id = re.findall(r'(?<=messageid\\/#).+(?=\\">\\n\\t\\t\\t\\t\\t<table class=\\"message_container)', s)[0]
        #print(id)
        data1 = {'csrf_gmailnator_token': '9283eccf4672e233327c1d07cbde2fbe', 'action': 'get_message', 'message_id': id,'email': 'varytmp'}
        mess = requests.post(url='https://www.gmailnator.com/mailbox/get_single_message/', headers=head, data=data1).text
        #print(mess)
        s_url = re.findall(r'(?<=\\uff1a\\r\\n\\r\\n).+(?=\\r\\n \\r\\n\\u795d\\u987a\\)', mess)[0].replace('\\','')

        #print(s_url)
        Driver.get(s_url)
        time.sleep(2)
        telegram_bot("梯子", '邀请成功！')
        Driver.quit()
    except Exception as e:
        print(e)
        Driver.close()
def register(email,invite):
    global Driver
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--headless')  # 无界面化.
    chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
    chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.
    chrome_opt.add_argument("--no-sandbox")
    Driver = webdriver.Chrome(options=chrome_opt)
    try:
        #Driver = webdriver.Chrome()
        Driver.get(invite)
        #driver.switch_to.frame('//*[@id="register"]/div/div')
        time.sleep(2)
        Driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[1]/div/div[2]/a').click()

        WebDriverWait(Driver,10).until(EC.element_to_be_clickable((By.ID, 'register')))
        Driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(email)
        Driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys('refddr265rt!')
        Driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys('refddr265rt!')
        Driver.find_element_by_xpath('//*[@id="register"]/div/div/div/div[2]/form/div[5]/button').click()
        time.sleep(2)
        Driver.find_element_by_xpath('/html/body/div[11]/div/div[4]/div/button').click()
        time.sleep(1)
        Driver.find_element_by_xpath('//*[@id="send-confirm-email"]').click()
        time.sleep(5)
    except Exception as e:
        print(e)
        telegram_bot("梯子", '邀请失败！')
def telegram_bot(title, content):
    print("\n")
    tg_user_id = TG_USER_ID
    if  "TG_USER_ID" in os.environ:
        tg_bot_token = os.environ["TG_BOT_TOKEN"]
        tg_user_id = os.environ["TG_USER_ID"]
    if not tg_bot_token or not tg_user_id:
        print("Telegram推送的tg_bot_token或者tg_user_id未设置!!\n取消推送")
        return
    print("Telegram 推送开始")
    send_data = {"chat_id": tg_user_id, "text": title +'\n\n'+content, "disable_web_page_preview": "true"}
    response = requests.post(
        url='https://api.telegram.org/bot%s/sendMessage' % (tg_bot_token), data=send_data)
    print(response.text)


def main(invite):
    email = get_email()
    register(email,invite)
    time.sleep(5)
    get_num(email)
    return True
if __name__ == "__main__":
    invite=os.environ["INVITECODE"]
    print(invite)
    if  "START"in os .environ and os .environ ["START"]=='584UFTGB888':#line:13
        main(invite)
    else:
        print('没有启动码！')
        telegram_bot ("梯子",'没有启动码!')
