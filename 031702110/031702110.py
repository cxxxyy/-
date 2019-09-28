import re
import json

def getph(message):
    a=re.findall(r'\d{11}',message)
    number=''.join(a)
    return number

def getname(message):
    (name,a)=message.split(',')
    return name

def getaddress(messsage):
    
    #先把信息中姓名，电话号码删去
    address=re.sub(r'\d{11}','',message)
    name=getname(message)
    address=re.sub(name,'',message)
    address=re.sub(',','',message)
