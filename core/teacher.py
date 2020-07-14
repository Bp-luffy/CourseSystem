'''老师视图'''

from lib import common
from interface import common_interface
from interface import teacher_interface

teacher_info = {'user': None}


# 老师登录
def login():
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        flag, msg = common_interface.login_interface(username, password, user_type='teacher')
        if flag:
            print(msg)
            teacher_info['user'] = username
            break
        else:
            print(msg)


# 老师查看教授课程
@common.auth('teacher')
def check_course():
    while True:
        # 1.先打印所有学校，并选择
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break

        for index, school_name in enumerate(school_list):
            print(f'编号：{index}   学校名：{school_name}')

        choice = input('请输入选择的学校编号：').strip()
        if not choice.isdigit():
            print('输入有误')
            continue

        choice = int(choice)

        if choice not in range(len(school_list)):
            print('编号输入有误！')
            continue

        # 获取选择的学校名称
        school_name = school_list[choice]

        # 2.从选择的学校中获取所有的课程
        flag2, course_list = common_interface.get_course_in_school_interface(school_name)

        if not flag2:
            print(course_list)
            break
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}   学校名：{course_name}')

        choice2 = input('请输入选择的课程编号：').strip()

        if not choice2.isdigit():
            print('输入错误')
            continue
        choice2 = int(choice2)

        if choice2 not in range(len(course_list)):
            print('输入编号有误！')
            continue

        # 获取课程的名称
        course_name = course_list[choice2]

        # 3.调用选择教授课程接口，将该课程添加到老师课程列表中
        flag3, msg = teacher_interface.add_course_interface(course_name, teacher_info.get('user'))
        if flag3:
            print(msg)
            break
        else:
            print(msg)


# 老师选择教授课程
@common.auth('teacher')
def choose_course():
    while True:
        # 1.先打印所有学校，并选择
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break

        for index, school_name in enumerate(school_list):
            print(f'编号：{index}  学校名：{school_name}')

        choice = input('请输入选择的学校编号：').strip()

        if not choice.isdigit():
            print('输入错误，请重新输入')
            continue

        choice = int(choice)
        if choice not in range(len(school_list)):
            print('输入超出范围，请重新输入')
            continue
        # 获取选择的学校名称
        school_name = school_list[choice]

        # 2.从选择的学校中获取所有的课程
        flag2, course_list = common_interface.get_course_in_school_interface(school_name)
        if not flag2:
            print(course_list)
            break
        for index, course_name in enumerate(school_list):
            print(f'编号：{index}   课程名：{school_name}')

        choice2 = input('请输入选择的课程编号：').strip()
        if not choice2.isdigit():
            print('输入有误')
            continue
        choice2 = int(choice2)

        if choice2 not in range(len(course_list)):
            print('输入有误')
            continue
        course_name = course_list[choice2]

        # 3.调用选择教授课程接口，将该课程添加到老师课程列表中
        teacher_interface.add_course_interface(course_name, teacher_info.get('user'))


# 查看课程下的学生
@common.auth('teacher')
def check_stu_from_course():
    while True:
        # 1.先获取当前老师下所有的课程
        flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not flag:
            print(course_list)
            break

        # 2.打印所有课程，并让老师选择
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}    课程名：{course_name}')

        choice = input('请输入选择的课程编号：').strip()

        if not choice.isdigit():
            print('输入有误')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入编号有误！')
            continue

        # 3.获取选择的课程名称
        course_name = course_list[choice]

        # 4.利用当前课程名称获取所有学生
        flag2, studemt_list = teacher_interface.get_student_interface(course_name, teacher_info.get('user'))

        print(studemt_list)
        break


# 修改学生分数
@common.auth('teacher')
def change_score_from_stu():
    '''
     1.先获取老师下所有的课程，并选择
     2.获取选择的课程下所有的学生，并选择修改的学生
     3.调用修改学生分数接口修改分数
    '''
    while True:
        # 1.先获取当前老师下所有的课程
        flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not flag:
            print(course_list)
            break

        # 2.打印所有课程，并让老师选择
        for index, course_name in enumerate(course_list):
            print(f'编号：{index}    课程名：{course_name}')

        choice = input('请输入选择的课程编号：').strip()

        if not choice.isdigit():
            print('输入有误')
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print('输入编号有误！')
            continue

        # 3.获取选择的课程名称
        course_name = course_list[choice]

        # 4.利用当前课程名称获取所有学生
        flag2, student_list = teacher_interface.get_student_interface(course_name, teacher_info.get('user'))

        if not flag2:
            print(student_list)
            break

        # 5.打印所有学生让老师选择
        for index, student_name in enumerate(student_list):
            print(f'编号：{index}   学生名：{student_name}')

        choice2 = input('请输入学生编号：').strip()

        if not choice2.isdigit():
            print('输入错误')
            continue

        choice2 = int(choice2)

        if choice2 not in range(len(course_list)):
            print('输入编号有误')
            continue

        # 6.获取选择的课程名称
        course_name = course_list[choice2]

        # 7.老师输入需要修改的分数
        score = input('请输入需要修改的成绩：').strip()
        if not score.isdigit():
            print('输入错误')
            continue

        score = int(score)

        flag3, msg = teacher_interface.change_score_interface(course_name, student_name, score,
                                                              teacher_info.get('user'))

        if flag3:
            print(msg)
            break


func_dict = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_score_from_stu,
}


def teacher_view():
    while True:
        print('''
            1、登录    
            2、查看教授课程
            3、选择教授课程
            4、查看课程下学生
            5、修改学生分数
        ''')

        choice = input('请输入功能编号:  ').strip()

        if choice == 'q':
            break

        if choice not in func_dict:
            print('输入错误，请重新输入')
            continue
        func_dict.get(choice)()
