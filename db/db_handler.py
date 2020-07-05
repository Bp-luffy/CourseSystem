# coding=utf-8
'''
用于保存对象与获取对象
'''

import os
import pickle
from conf import settings


# 保存数据
def save_data(obj):
    # 1.获取对象的保存文件夹路径
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(settings.DB_PATH, class_name)

    # 2.判断文件夹是否存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 3.拼接当前当前用户的pickle文件路径，以用户名作为文件名
    user_path = os.path.join(user_dir_path, obj.user)  # 当前用户名字

    # 4.打开文件保存对象，通过pickle处理
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)


# 查看数据
def select_data(cls, username):
    # 1.获取对象的保存文件夹路径
    class_name = cls.__name__
    user_dir_path = os.path.join(settings.DB_PATH, class_name)

    # 2.判断文件夹是否存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 3.拼接当前当前用户的pickle文件路径，以用户名作为文件名
    user_path = os.path.join(user_dir_path, username)  # 当前用户名字

    # 4.判断文件如果存在，再打开，并返回，若不存在，则代表用户不存在
    if os.path.exists(user_path):
        with open(user_path, 'rb') as f:
            obj = pickle.load(f)
            return obj