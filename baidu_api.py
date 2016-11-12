# coding=utf-8
'''
Created on 2016年6月20日
@author: lyxw
'''

import base64
import requests
import json
import time
import hmac
import hashlib
from randstr import randstr

def build_sign(secret_key, params):
    '''
    通过HMAC-SHA1构造签名串
    Args:
        secret_key: HMAC-SHA1所使用的key
        params: 待签名的参数dict
    '''
    try:
        ks = params.keys()
        ks.sort()
        base_str = '&'.join(['%s=%s' % (k, str(params[k])) for k in ks])
        return base64.b64encode(hmac.new(str(secret_key), base_str, hashlib.sha1).digest())
    except Exception as e:
        import traceback
        print traceback.format_exc()
        return None

def build_headers(access_key, secret_key, path, get_params={}, post_params={}):
    '''
    根据请求参数构建包含鉴权参数的请求Header
    Args:
        access_key: ak
        secret_key: sk
        get_params: 业务相关的GET参数
        post_params: 业务相关的POST参数
        view_params: url中的restful参数
    Returns:
        params: 添加了鉴权相关参数，并且签名过的参数
    '''
    headers = {}
    headers['X-Auth-Access-Key'] = access_key
    headers['X-Auth-Timestamp'] = str(int(time.time()))
    headers['X-Auth-Signature-Method'] = 'HMAC-SHA1'
    headers['X-Auth-Nonce'] = randstr(32)
    all_params = {}
    all_params.update(get_params)
    all_params.update(post_params)
    all_params.update(headers)
    all_params['X-Auth-Path-Info'] = path.strip('/')
    auth_sign = build_sign(secret_key, all_params)
    headers['X-Auth-Sign'] = auth_sign
    return headers

method = 'post'
ak = 'd7a559051ee0456f9397f78c0b90d747'     #your_access_key
sk = 'd7a559051ee0456f9397f78c0b90d747'     #your_secret_key
url = 'https://api.su.baidu.com/v3/yjs/zones/'
path = 'zones'
get_params = {}
post_params = {"X-User-Id": "5y1sesn8ph",
               "domain": "yjwc.com",
               "type": "ns",
               "plan_bd": "free"}
headers = build_headers(ak, sk, path, get_params, post_params)
'''
     headers = {
    'X-Auth-Access-Key': 'd7a559051ee0456f9397f78c0b90d747',
    'X-Auth-Signature-Method': 'HMAC-SHA1',
    'X-Auth-Sign': 'Xi8JGn7gFTAWw/8oGibC0vioqMk=',
    'X-Auth-Nonce': 'eq2d8qosy5nape7r13qhaykotrsgq0r6',
    'X-Auth-Timestamp': '1413440640'}
'''
resp = requests.request(method, url, params=get_params, data=post_params, headers=headers)
print resp
data = json.loads(resp.text)
