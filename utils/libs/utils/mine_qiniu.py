# -*- coding: utf-8 -*-

import uuid
from qiniu import Auth, put_data


# 需要填写你的 Access Key 和 Secret Key
access_key = 'OztWMC0DK77aVCqExkSZl6zCIwJM7dgNMQ9_Rh7G'
secret_key = '7eaeCFSDOIrVAOuEis_IipZqMnya6dHKvRPwrHr1'
domain_prefix = 'http://oss.dongyeshengxue.com/'


def upload_data(filestream, bucket_name):
    # 生成上传凭证
    q = Auth(access_key, secret_key)
    suffix = filestream.name.split('.')[-1]  # 后缀(jpg, png, gif)

    filename = uuid.uuid4().hex + '.' + suffix.lower()
    token = q.upload_token(bucket_name, filename)
    # 上传文件
    retData, respInfo = put_data(token, filename, filestream)

    return filename, domain_prefix + filename
