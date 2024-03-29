import re
import json
import os

city_0=['石家庄','秦皇岛','张家口','葫芦岛','哈尔滨','齐齐哈尔','牡丹江','佳木斯' ,'双鸭山','七台河','连云港','马鞍山','景德镇','平顶山','三门峡','驻马店','张家界','攀枝花','六盘水','嘉峪关','呼和浩特','鄂尔多斯','呼伦贝尔','巴彦淖尔','乌兰察布','防城港','日喀则','石嘴山','乌鲁木齐','克拉玛依','吐鲁番']
person={
    '姓名':'',
    '手机':'',
    '地址':[],
    }

def getph(message): 
    a=re.findall(r'\d{11}',message)
    number=''.join(a)
    return number


def getname(message):
    (name,q)=message.split(',')
    return name

def divide(i,address):
    a=re.sub(i,' ',address)
    (b,q)=a.split(' ',1)
    z=b+i
    return z


def getaddress(messsage):

   #先把信息中姓名，电话号码删去
    address=re.sub(r'\d{11}','',message)
    name=getname(message)
    address=re.sub(name,'',address)
    address=re.sub(',','',address)
    address=address.replace('.','',1)
    
   #直辖市 自治区 省  
    if '北京' in address or'天津' in address or'上海' in address or'重庆' in address:
        for i in ['北京','天津','上海','重庆']:
            if i in address:
                a=i
                break
        address=re.sub(a,'',address)
        if address[0]=='市':
            address=re.sub(address[0],'',address)
        
    elif '自治区' in address:
        a=divide('自治区',message)
        address=re.sub(a,'',address)
        
    elif '省' in address:
        a=divide('省',address)
        address=re.sub(a,'',address)
        
    else:
        if address[0:3]=='黑龙江':
            a='黑龙江省'
            address=re.sub('黑龙江','',address)
        else:
            a=address[0:2]+'省'
            address=re.sub(address[0:2],'',address)
            
   #市，地区，自治州，盟
    city_1=['市','地区','自治区','盟']
    b=''
    for i in ['北京','天津','上海','重庆']:
        if a==i:
            b=i+'市'
            
    if b=='':
        for i in city_1:
            if i in address:
                b=divide(i,address)
                address=re.sub(b,'',address)
                break
            
    if b=='':
        for i in city_0:
            if i in address:
                address=re.sub(i,'',address)
                b=i+'市'
                break

    if b=='':
        b=address[0:2]+'市'
        address=re.sub(address[0:2],'',address)

   #市辖区、县级市、县、自治县、旗、自治旗、林区
    county_1=['区','市','县','自治县','旗','自治旗','林区']
    c=''
    for i in county_1:
        if i in address:
            c=divide(i,address)
            address=re.sub(c,'',address)
            break

            
   #街道、镇、乡、民族乡、苏木、民族苏木、县辖区
    town_1=['街道','镇','乡','苏木','民族苏木']
    d=''
    for i in town_1:
        if i in address:
            d=divide(i,address)
            address=re.sub(d,'',address)
            break

   #路，街，村
    road_1=['路','街','村']
    e=''
    for i in road_1:
        if i in address:
            e=divide(i,address)
            address=re.sub(e,'',address)

   #号
    f=''
    i='号'
    if i in address:
        f=divide(i,address)
        address=re.sub(f,'',address)

    g=address
    
    return [a,b,c,d,e,f,g]
        
        
message=input()
person['姓名']=getname(message)
person['手机']=getph(message)
person['地址'].extend(getaddress(message))
Json=json.dumps(person,ensure_ascii=False)
print(Json)
