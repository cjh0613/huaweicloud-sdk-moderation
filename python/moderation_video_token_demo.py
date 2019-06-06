# -*- coding:utf-8 -*-
from moderation_sdk.gettoken import get_token
from moderation_sdk.moderation_video import moderation_video
from moderation_sdk.utils import init_global_env

if __name__ == '__main__':
    # Services currently support North China-Beijing(cn-north-1,cn-north-4), Asia Pacific-Hong Kong(ap-southeast-1)
    init_global_env('cn-north-1')

    #
    # access asr, long_sentence，post data by token
    #
    user_name = '******'
    password = '******'
    account_name = '******'  # the same as user_name in commonly use

    demo_data_url = 'https://obs-test-llg.obs.cn-north-1.myhuaweicloud.com/bgm_recognition'
    token = get_token(user_name, password, account_name)

    # call interface use the url
    result = moderation_video(token, demo_data_url, 1)
    print(result)