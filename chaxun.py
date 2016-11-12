# coding=utf-8
'''
Created on 2016年6月1日
@author: lyxw
'''

import argparse
import baidu_api

parse = argparse.ArgumentParser()
#group = parse.add_mutually_exclusive_group()
parse.add_argument('-p','--phone',help='phone number')
parse.add_argument('-s','--shenfenzheng',help='IDCard number')
parse.add_argument('-i','--ip',help='ip address')
parse.add_argument('-I','--IP',help='ip address')
parse.add_argument('-c','--card',help='bank card number')
parse.add_argument('-w','--wooyun',help='wooyun security loophole number')
parse.add_argument('-m','--md5',help='md5 string')

args = parse.parse_args()
print args
try:
    if ('p' or 'phone' in args)and args.phone!=None:
        usefull_api.Phone(args.phone)
    if ('s' or 'shenfenzheng' in args)and args.shenfenzheng!=None:
        usefull_api.IDCard(args.shenfenzheng)
    if ('i' or 'ip' in args)and args.ip!=None:
        usefull_api.IP(args.ip)
    if ('I' or 'IP' in args)and args.IP!=None:
        usefull_api.IP_info(args.IP)
    if ('c' or 'card' in args)and args.card!=None:
        usefull_api.Card(args.card)
    if ('w' or 'wooyun' in args)and args.wooyun!=None:
        usefull_api.Wooyun('args.wooyun')
    
except Exception,e:
    print e
