# coding=utf-8
'''
Created on 2016年6月1日
@author: lyxw
'''

import requests

def APIKEY():
    apikey='*********************'       #your baidu apikey
    return apikey

headers={'apikey':APIKEY()}

def Phone(value):
    url='http://apis.baidu.com/apistore/mobilenumber/mobilenumber'
    payload={'phone':value}
    r=requests.get(url,params=payload,headers=headers)
    try:
        s=r.json()
        print s['retMsg']
        print '手机号码: '+s['retData']['phone']
        print '类型: '+s['retData']['suit']
        print '手机号前7位: '+s['retData']['prefix']
        print '运营商: '+s['retData']['supplier']
        print '省份: '+s['retData']['province']
        print '城市: '+s['retData']['city'] 
    except:
        pass
    
def IP(value):
    url='http://apis.baidu.com/apistore/iplookupservice/iplookup'
    payload={'ip':value}
    r=requests.get(url,params=payload,headers=headers)
    try:
        s=r.json()
        print s['errMsg']
        print 'ip地址: '+s['retData']['ip']
        print '国家: '+s['retData']['country']
        print '省份: '+s['retData']['province']
        print '城市: '+s['retData']['city']
        print '地区: '+s['retData']['district']
        print '运营商: '+s['retData']['carrier']
    except:
        pass

def IP_info(value):
    url='http://apis.baidu.com/bdyunfenxi/intelligence/ip'
    payload={'ip':value}
    r=requests.get(url,params=payload,headers=headers)
    try:
        s=r.json()
        print s['Description']
        print 'ip地址: '.encode('gbk')+value
        print '国家: '+s['Base_info']['country']
        print '省份: '+s['Base_info']['province']
        print '城市: '+s['Base_info']['city']
        print '地区: '+s['Base_info']['county']
        print '运营商: '+s['Base_info']['isp']
        if s['Net_info']:
            if s['Net_info']['Is_ntp']==1:
                print 'ntp端口号: '+s['Net_info']['Ntp_port']
            if s['Net_info']['Is_dns']==1:
                print 'ntp端口号: '+s['Net_info']['Dns_port']
            if s['Net_info']['Is_proxy']==1:
                print 'ntp端口号: '+s['Net_info']['Proxy_port']
            if s['Net_info']['Is_vpn']==1:
                print 'ntp端口号: '+s['Net_info']['Vpn_port'] 
    except:
        pass

def IDCard(value):
    url='http://apis.baidu.com/chazhao/idcard/idcard'
    payload={'idcard':value}
    r=requests.get(url,params=payload,headers=headers)
    try:
        s=r.json()
        print s['msg']
        print '身份证号码: '+s['data']['idcard']
        print '性别: '+s['data']['gender']
        print '生日: '+s['data']['birthday']
        print '生肖: '+s['data']['zodiac']
        print '星座: '+s['data']['constellation']
        print '身份证归属地: '+s['data']['address']
    except:
        pass

def Card(value):
    url='http://apis.baidu.com/datatiny/cardinfo/cardinfo'
    payload={'cardnum':value}
    r=requests.get(url,params=payload,headers=headers)
    try:
        s=r.json()
        print s
        print '归属银行: '+s['data']['bankname']
        print '银行卡类型: '+s['data']['cardtype']
        print '银行卡名称: '+s['data']['cardname']
        print '银行卡前缀: '+s['data']['cardprefixnum']
        print '内部结算代码: '+s['data']['banknum']
        print '银行卡长度: '+s['data']['cardlength']
        #print s['retMsg']
        print s['data']['mess']
    except:
        pass  

def Wooyun(value):
    url='http://apis.baidu.com/apistore/wooyun/unclaim'
    payload={'limit':value}
    r=requests.get(url,params=payload,headers=headers)
    try:
        s=r.json()
        #print s
        for i in range(0,value):
            print i
            print '漏洞编号： '+s[i]['id']
            print '漏洞标题: '+s[i]['title']
            print '漏洞作者: '+s[i]['author']
            if s[i]['status']==0:
                print '漏洞状态: 待厂商确认处理'.encode('gbk')
            elif s[i]['status']==1:
                print '漏洞状态: 厂商已经确认'.encode('gbk')
            elif s[i]['status']==2:
                print '漏洞状态: 漏洞通知厂商但厂商忽略'.encode('gbk')
            elif s[i]['status']==3:
                print '漏洞状态: 未联系到厂商或厂商忽略'.encode('gbk')
            else:
                print '漏洞状态: 正在联系厂商并等待认领'.encode('gbk')
            print '用户定义危害等级: '+s[i]['user_harmlevel']
            print '厂商定义危害等级: '+s[i]['corp_harmlevel']
            print 'rank: '+s[i]['corp_rank']
            print '评论数：  '+s[i]['comment']
            print '发布日期：  '+s[i]['data']
            print '发布时间戳： '+s['timestamp']
            print '漏洞链接： '+s[i]['link']
    except:
        pass

def Md5(value):
    url='http://apis.baidu.com/chazhao/md5decod/md5decod'
    payload={'md5':value}
    r=requests.get(url,params=payload,headers=headers)
    try:
        s=r.json()
        print 'md5: '+s['data']['md5']
        print 'md5_src: '+s['data']['md5_src']
    except:
        pass  
