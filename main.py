from selenium import webdriver
import random
import string

def bot(target,msg,ms):
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')

    input("Enter a button after QR code!")

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(target))
    user.click()

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
    
    if(msg=="random"):
        for i in range(ms):
            msg = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))
            msg_box.send_keys(msg)
            button = driver.find_element_by_css_selector('#main > footer > div._3pkkz.V42si.copyable-area > div:nth-child(3) > button > span')
            button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
            button.click()
    
    else:
        for i in range(ms):
            msg_box.send_keys(msg)
            button = driver.find_element_by_css_selector("#main > footer > div._3pkkz.V42si.copyable-area > div:nth-child(3) > button > span")
            button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
            button.click()        

def menu():
    print("""

           Welcome to WhatsApp Message Spammer 



    Coded by FFH
    """)
    target = input("Please enter a target: ")
    msg = input('Enter your message(enter "random" for random messages) :')
    count = int(input("Counts of messages: "))
    bot(target,msg,count)


menu()
