"""
通常情况下，data中的数据按照一个参数传递给测试用例，
如果data中含有多个数据，以元组，列表，字典等数据，
需要自行在脚本中对数据进行分解或者使用unpack分解数据

"""

"""
 1. data以data('zhangsan', 30, '男')
 这种方式排列，则会执行三次用例，每次都会把数据赋给第一个参数，后面的参数不会赋值
 这种方式就不能用到unpack，unpack只能对序列进行分解
 2. data以data(['zhangsan', 30, '男'])或data(('zhangsan', 30, '男'))
 这种方式，元组或列表，必须用unpack装饰器分解数据，否则会当成一个参数
 unpack分解后，序列中的三个元素，会分别对应用例中的三个参数
 3. 如果用例只有一个参数，就不用unpack，多个参数就需要unpack分解数据
 4. file_data中使用unpack没有意义

 """
import unittest
import ddt


# 对测试类要使用ddt装饰器
@ddt.ddt
class TestDdt(unittest.TestCase):

    def setUp(self):
        print("我是初始化方法!")



    @ddt.data('zhangsan', 'lisi', 'wangwu')
    def test_ddt_data_simple(self, name):
        print("test_ddt获取的参数 \n name: %s" % (name))


    # @ddt.data(['zhangsan', 30, '男'],
    #           ['lisi', 25, '男'],
    #           ['wangwu', 41, '女'])
    #@ddt.unpack
    # @ddt.data(['zhangsan', 30, '男'])
    # @ddt.unpack
    # def test_ddt_data(self, name='', age=0, sex=''):
    #     print("------------------")
    #     print("test_ddt获取的参数 \n name: %r \n age: %r \n sex: %r" % (name, age, sex))
    #     print("------------------")

    # @ddt.data({'name':'zhangsan', 'age':30, 'sex':'男'})
    # @ddt.unpack
    # def test_ddt_data_dict(self, **kw):
    #     def print_person(name='', age=0, sex=''):
    #         print("test_ddt获取的参数 \n name: %r \n age: %r \n sex: %r" % (name, age, sex))
    #     print_person(**kw)

    # @ddt.file_data(r'E:\工作\海德\附件\person_list.json')
    # def test_ddt_file(self, data):
    #     # def print_person(name='', age=0, sex=''):
    #     #     print("test_ddt获取的参数 \n name: %r \n age: %r \n sex: %r" % (name, age, sex))
    #     # print_person(**data)
    #     print(data)

    # @ddt.file_data(r'E:\工作\海德\附件\person_list.json')
    # def test_ddt_file_list(self, args):
    #     def print_person(name, age, sex):
    #         print("test_ddt获取的参数 \n name: %r \n age: %r \n sex: %r" % (name, age, sex))
    #     print_person(*args)

    # @ddt.file_data(r'E:\工作\海德\附件\person_dict.json')
    # def test_ddt_file_dict(self, name='', age=0, sex=''):
    #     print("test_ddt获取的参数 \n name: %r \n age: %r \n sex: %r" % (name, age, sex))

    # @ddt.file_data(r'E:\工作\海德\附件\name.yml')
    # def test_ddt_yml_file(self, args):
    #     def print_person(name, age, sex):
    #         print("test_ddt获取的参数 \n name: %r \n age: %r \n sex: %r" % (name, age, sex))
    #     print(args)

    def tearDown(self):
        print("我是清理方法!")