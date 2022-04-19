import requests
import json
from time import sleep
import time
red_color = "\033[1;31m"
info_color = "\033[1;33m"
detect_color = "\033[1;34m"
end_banner_color = "\33[00m"

print (red_color+"""

┌────────────┐
│  @0xFaLaH  │
└────────────┘
       │
       └── Submit a Twitter report ──┐
                                     ▼
                               ┌──────────┐
┌──────────────────────────────┤    api   ├──┐
│                              └──────────┘  │
│              write your report     │       │
│                 then send          │       │
│          ┌──────/python3 ──────────┘       │
│ ┌────────┼───────────────────────────────┐ │
│ │Twitter │                               │ │
│ │┌───────▼──┐ ┌──────────┐ ┌──────────┐  │ │
│ ││ support  │ │ username │ │ Mediator │  │ │
│ │└──────────┘ └──────────┘ └──────────┘  │ │
│ └────────────────────────────────────────┘ │
└────────────────────────────────────────────┘


""")

falah = input (detect_color+ '''
1 - My account has been hacked 
2 - Post unauthorized photos

-> ''')

if falah == "1":
    hack = input("you User : ")
    hack_Email = input("you Email : ")
    headers = {
        "Accept-Encoding": "gzip, deflate",
		"Accept-Language": "ar",	
        "Cookie": "auth_token=3f588867f2e67a5aff0d84f88e70797865ed79f3;ct0=2c7d8fa28b2ae255bbbae52104eef0237e466b201e0ff77a77d7a41f557c4033798343d49d7a5fbbf4edfdd51c3320511f4aba7c3f2df9d035922d1dd7e598fde1799e13505de71c5e881a27952db5c6",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18D61 Twitter for iPhone/8.78.1",
        "Accept": "*/*",
		"Content-Type": "text/plain;charset=UTF-8",
		"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAACHguwAAAAAAaSlT0G31NDEyg%2BSnBN5JuyKjMCU%3Dlhg0gv0nE7KKyiJNEAojQbn8Y3wJm1xidDK7VnKGBP4ByJwHPb",
        "Host": "api.twitter.com",
		"X-Csrf-Token": "2c7d8fa28b2ae255bbbae52104eef0237e466b201e0ff77a77d7a41f557c4033798343d49d7a5fbbf4edfdd51c3320511f4aba7c3f2df9d035922d1dd7e598fde1799e13505de71c5e881a27952db5c6",
        "X-Twitter-Auth-Type": "OAuth2Session",
		"Referer": "https://help.twitter.com/ar/forms/account-access/regain-access/hacked-or-compromised"
    }
    data = ""

    request_object = requests.get('https://api.twitter.com/1.1/strato/column/None/()/cms/prod/user/generateToken',  headers=headers ,data=json.dumps(data ,ensure_ascii=False).encode('utf-8'))
    print(info_color+"Token-You : "+request_object.text)
    TokenYou = input("Token ? : ")
    

#جاري ارسال البلاغ 


    headers = {
        "Accept-Encoding": "gzip, deflate",
		"Accept-Language": "ar",	
        "Cookie": "auth_token=3f588867f2e67a5aff0d84f88e70797865ed79f3;ct0=2c7d8fa28b2ae255bbbae52104eef0237e466b201e0ff77a77d7a41f557c4033798343d49d7a5fbbf4edfdd51c3320511f4aba7c3f2df9d035922d1dd7e598fde1799e13505de71c5e881a27952db5c6",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18D61 Twitter for iPhone/8.78.1",
        "Accept": "*/*",
		"Content-Type": "text/plain;charset=UTF-8",
		"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAACHguwAAAAAAaSlT0G31NDEyg%2BSnBN5JuyKjMCU%3Dlhg0gv0nE7KKyiJNEAojQbn8Y3wJm1xidDK7VnKGBP4ByJwHPb",
        "Host": "api.twitter.com",
		"X-Csrf-Token": "2c7d8fa28b2ae255bbbae52104eef0237e466b201e0ff77a77d7a41f557c4033798343d49d7a5fbbf4edfdd51c3320511f4aba7c3f2df9d035922d1dd7e598fde1799e13505de71c5e881a27952db5c6",
        "X-Twitter-Auth-Type": "OAuth2Session",
		"Referer": "https://help.twitter.com/ar/forms/account-access/regain-access/hacked-or-compromised"
    }
    data = {
    "stringEntries": {
        "_Regarding": "regain-access,hacked-or-compromised",
        "_FormPath": "/content/help-twitter/ar/forms/account-access/regain-access/hacked-or-compromised/jcr:content/root/responsivegrid/ct16_columns_spa_cop_807803376/col2/f200_form",
		"Subject": "Regain access - Hacked or compromised",
		"Source_Form__c": "login",
		"Type_of_Issue__c": "Not Available\t",
		"Category__c": "Hacked",
		"Referral_Source__c": "",
		"Referral_Client__c": "",
		"Screen_Name__c": "@"+hack+"",
		"Form_Email__c": ""+hack_Email+"",
		"DescriptionText": "My account has been hacked please help me I want to recover it",
		"formVerificationToken": ""+TokenYou+""
    }
}

    request_objectf = requests.put('https://api.twitter.com/1.1/strato/column/None/()/cms/submit_form',  headers=headers ,data=json.dumps(data ,ensure_ascii=False).encode('utf-8'))
    print(request_objectf)
    exit()




###############################################



if falah == "2":


    you_user = input("you User : ")
    you_Email = input("you Email : ")
    user_report = input("user report : ")
    url_report = input("url report : ") 
    headers = {
        "Accept-Encoding": "gzip, deflate",
		"Accept-Language": "ar",	
        "Cookie": "auth_token=3f588867f2e67a5aff0d84f88e70797865ed79f3;ct0=2c7d8fa28b2ae255bbbae52104eef0237e466b201e0ff77a77d7a41f557c4033798343d49d7a5fbbf4edfdd51c3320511f4aba7c3f2df9d035922d1dd7e598fde1799e13505de71c5e881a27952db5c6",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18D61 Twitter for iPhone/8.78.1",
        "Accept": "*/*",
		"Content-Type": "text/plain;charset=UTF-8",
		"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAACHguwAAAAAAaSlT0G31NDEyg%2BSnBN5JuyKjMCU%3Dlhg0gv0nE7KKyiJNEAojQbn8Y3wJm1xidDK7VnKGBP4ByJwHPb",
        "Host": "api.twitter.com",
		"X-Csrf-Token": "2c7d8fa28b2ae255bbbae52104eef0237e466b201e0ff77a77d7a41f557c4033798343d49d7a5fbbf4edfdd51c3320511f4aba7c3f2df9d035922d1dd7e598fde1799e13505de71c5e881a27952db5c6",
        "X-Twitter-Auth-Type": "OAuth2Session",
		"Referer": "https://help.twitter.com/ar/forms/account-access/regain-access/hacked-or-compromised"
    }
    data = ""

    request_object = requests.get('https://api.twitter.com/1.1/strato/column/None/()/cms/prod/user/generateToken',  headers=headers ,data=json.dumps(data ,ensure_ascii=False).encode('utf-8'))
    print(info_color+"Token-You : "+request_object.text)
    with open ('Token.txt', 'a') as x:
                  x.write ('\n'+request_object.text)
    TokenYou = input("Token ? :")


#جاري ارسال البلاغ 

def falah2():   
    headers = {
        "Accept-Encoding": "gzip, deflate",
		"Accept-Language": "ar",	
        "Cookie": "auth_token=3f588867f2e67a5aff0d84f88e70797865ed79f3;ct0=2c7d8fa28b2ae255bbbae52104eef0237e466b201e0ff77a77d7a41f557c4033798343d49d7a5fbbf4edfdd51c3320511f4aba7c3f2df9d035922d1dd7e598fde1799e13505de71c5e881a27952db5c6",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18D61 Twitter for iPhone/8.78.1",
        "Accept": "*/*",
		"Content-Type": "text/plain;charset=UTF-8",
		"Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAACHguwAAAAAAaSlT0G31NDEyg%2BSnBN5JuyKjMCU%3Dlhg0gv0nE7KKyiJNEAojQbn8Y3wJm1xidDK7VnKGBP4ByJwHPb",
        "Host": "api.twitter.com",
		"X-Csrf-Token": "2c7d8fa28b2ae255bbbae52104eef0237e466b201e0ff77a77d7a41f557c4033798343d49d7a5fbbf4edfdd51c3320511f4aba7c3f2df9d035922d1dd7e598fde1799e13505de71c5e881a27952db5c6",
        "X-Twitter-Auth-Type": "OAuth2Session",
		"Referer": "https://help.twitter.com/ar/forms/account-access/regain-access/hacked-or-compromised"
    }
    data = {
    "stringEntries": {
		"information-is-accurate[0]": "yes",
		"i-am-authorized[0]":"yes",
		"Communicate_Reported_Content__c[0]":"true",
        "_FormPath": "/content/help-twitter/ar/forms/safety-and-sensitive-content/private-information/somebody-else/jcr:content/root/responsivegrid/ct16_columns_spa_cop_807803376/col2/f200_form",
		"Subject": "Private info is being posted about somebody",
		"Source_Form__c": "private_information",
		"Type_of_Issue__c": "Others",
		"Category__c": "Private Information",
		"Screen_Name__c": "@"+you_user+"",
		"Form_Email__c": ""+you_Email+"",
		"Reported_Screen_Name__c":"@"+user_report+"",
		"reported-content[0]":""+url_report+"",
		"country":"SA",
		"DescriptionText":"Content that causes harm to someone that is not appropriate to be on Twitter",
		"media-concerns[0]":"It is an intimate and/or unauthorized image of me, or somebody else",
		"Private_info_posted_what__c[0]":"Image",
		"signature":"توقيع",
		"formVerificationToken": ""+TokenYou+""
    }
}

    request_objectf = requests.put('https://api.twitter.com/1.1/strato/column/None/()/cms/submit_form',  headers=headers ,data=json.dumps(data ,ensure_ascii=False).encode('utf-8'))
    print(request_objectf)
    if request_objectf.status_code == 200:
       print (info_color + "[ok] تم ارسال البلاغ{}".format (user_report))

    else:
       print (red_color + "[Error] فشل الارسال")
       request_object = requests.get('https://api.twitter.com/1.1/strato/column/None/()/cms/prod/user/generateToken',  headers=headers ,data=json.dumps(data ,ensure_ascii=False).encode('utf-8'))
       print(info_color+"Token-You : "+request_object.text)
       Token = input ("Rest-Token  ? : ")
       print ("")
       print (" -" * 15)




while True:
 start = falah2()
 time.sleep(15)
