'''管理注册接口'''

from db import models


# 管理员注册接口
def admin_register_interface(username, password):
    # 1.判断用户是否存在
    admin_obj = models.Admin.select(username)

    # 1.1 若存在不允许注册，返回用户已存在给视图层
    if admin_obj:
        return False, '用户已存在'

    # 1.2 若不存在则允许注册，调用类实力化对象并保存
    admin_obj = models.Admin(username, password)
    admin_obj.save()
    return True, '注册成功'


# 管理员登录接口
def admin_login_interface(username, password):
    # 1.判断用户是否存在
    admin_obj = models.Admin.select(username)

    # 2.若不存在，则证明用户不存在并返回给视图层
    if not admin_obj:
        return False, '用户名不存在'

    # 3.若用户存在，则校验密码
    if password == admin_obj.pwd:
        return True, '登录成功'
    else:
        return False, '密码错误'


# 管理员创建学校接口
def create_school_interface(school_name, school_addr, admin_name):
    # 1.查看当前学校是否已存在
    # school_obj ---> 对象 or None
    school_obj = models.School.select(school_name)
    # 2.若学校存在，则返回False，告知用户学校已存在
    if school_obj:
        return False, '学校已存在'
    # 3.若不存在，则创建学校，注意（由管理员对象来创建）
    admin_obj = models.Admin.select(admin_name)
    # 由管理员来调用创建学校方法，并传入学校的名字与地址
    admin_obj.create_school(school_name, school_addr)

    # 4.返回创建学校成功给视图层
    return True, f'[{school_name}]学校创建成功！'
