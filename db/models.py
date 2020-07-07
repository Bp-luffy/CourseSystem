# coding=utf-8

'''
角色：学校，学员、课程、讲师、管理员
'''

from db import db_handler


# 父类，让所有子类都继承select与save方法
class Base:
    @classmethod
    def select(cls, username):  # Admin，username
        # obj:对象 or None
        obj = db_handler.select_data(cls, username)
        return obj

    # 保存数据--->注册、保存、更新数据
    def save(self):
        db_handler.save_data(self)


# 管理员类
class Admin(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    # 创建学校
    def create_school(self, school_name, school_addr):
        '''该方法内部来调用学校类实例化的得到对象，并保存'''
        school_obj = School(school_name, school_addr)
        school_obj.save()

    # 创建课程
    def create_course(self, school_obj, course_name):
        # 1.调用课程类，实例化创建课程
        course_obj = Course(course_name)
        course_obj.save()
        # 2.获取当前学校对象，并将课程添加到课程列表
        school_obj.course_list.append(course_name)
        school_obj.save()

    # 创建讲师
    def create_teacher(self, teacher_name, teacher_pwd):
        # 1.调用老师类，实例化的到老师对象，并保存
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()


# 学校类
class School(Base):
    def __init__(self, name, addr):
        # 必须写：self.user，因为db_handler里面的select_data统一规范
        self.user = name
        self.addr = addr
        # 课程列表:每所学校都应该有相应的课程
        self.course_list = []


# 学生类
class Student(Base):
    pass


# 课程类
class Course(Base):
    def __init__(self, course_name):
        self.user = course_name
        self.student_list = []


class Teacher(Base):
    def __init__(self, teacher_name, pwd):
        self.user = teacher_name
        # self.pwd需要统一
        self.pwd = pwd
        self.course_list_from_teacher = []
