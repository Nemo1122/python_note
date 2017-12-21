from django.db import models


class Test(models.Model):
    """
    考试科目，如自动化考试、数据库考试等
    """
    FIRST = 'F'
    SECOND = 'S'
    THIRD = 'T'
    Q_STAGE = (
        (FIRST, '第一阶段'),
        (SECOND, '第二阶段'),
        (THIRD, '第三阶段')
    )

    INVALID = 'I'
    VALID = 'V'
    STATUS = (
        (INVALID, '无效'),
        (VALID, '有效')
    )
    course = models.CharField('考试科目', max_length=20)
    total_score = models.IntegerField('总分', blank=True, null=True)
    intro = models.TextField('科目简介', default='')
    stage = models.CharField('阶段', blank=True, choices=Q_STAGE, max_length=10)
    order = models.IntegerField('顺序', blank=True, null=True)
    status = models.CharField('状态', choices=STATUS, default='V', max_length=10)

    def __str__(self):
        return  self.course

    def q_stage(self):
        if self.stage == 'F':
            return '第一阶段'
        elif self.stage == 'S':
            return '第二阶段'
        elif self.stage == 'T':
            return '第三阶段'

    class Meta:
        verbose_name = '考试科目'
        verbose_name_plural = '考试科目'
        ordering = ['order']


class TestDetail(models.Model):
    """
    具体的考题内容及标准答案。
    """
    CHOICE = 'C'
    FILLING = 'F'
    TRUE_OR_FALSE = 'T'
    SHORT_ANSWER = 'S'
    Q_TYPE = (
        (CHOICE, '选择题'),
        (FILLING, '填空题'),
        (TRUE_OR_FALSE, '判断题'),
        (SHORT_ANSWER, '简答题')
    )

    INVALID = 'I'
    VALID = 'V'
    STATUS = (
        (INVALID, '无效'),
        (VALID, '有效')
    )
    course = models.ForeignKey(Test, verbose_name='科目编号', null=True, blank=True, on_delete=models.SET_NULL)
    serial_number = models.IntegerField('题目序号', blank=True, null=True)
    questions = models.TextField('题目内容', default='')
    score = models.IntegerField('分值', blank=True, null=True)
    questions_type = models.CharField('题目类型', choices=Q_TYPE, max_length=10)
    answer = models.TextField('标准答案', blank=True, default='')
    # 一个大题中有几个小题，第一级大题等级为1，第二级为2，以此类推
    level = models.IntegerField('试题等级', default=1)
    # 2级以上的标题，都应该有个父ID，就是上一级大题的ID
    parent = models.IntegerField('父级ID', default=0)
    status = models.CharField('状态', choices=STATUS, default='V', max_length=10)

    def __str__(self):
        return  self.questions

    def q_type(self):
        if self.questions_type == 'C':
            return '选择题'
        elif self.questions_type == 'F':
            return '填空题'
        elif self.questions_type == 'T':
            return '判断题'
        elif self.questions_type == 'S':
            return '简答题'

    class Meta:
        verbose_name = '考题'
        verbose_name_plural = '考题'
        ordering = ['course_id', 'level', 'serial_number']


class UserAnswer(models.Model):
    """
    参考人员在考试过程中写的答案。
    """
    question = models.ForeignKey(TestDetail, verbose_name='题目编号', blank=True, null=True, on_delete=models.SET_NULL)
    user_answer = models.TextField('答案', blank=True, null=True, default='')
    create_time = models.DateTimeField('答题时间')
    update_time = models.DateTimeField('修改时间', blank=True, null=True)
    create_user = models.CharField('答题者', blank=True, default='', max_length=20)
    update_user = models.CharField('修改者', blank=True, default='', max_length=20)
    course = models.ForeignKey(Test, verbose_name='科目编号', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user_answer

    class Meta:
        verbose_name = '答案'
        verbose_name_plural = '答案'
        ordering = ['update_user', 'question', 'course']

"""
异常：
author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='作者')
TypeError: __init__() missing 1 required positional argument: 'on_delete'

给ForeignKey增加属性，

on_delete=models.SET_NULL

即可。

该属性还有其他值可选：

CASCADE: 默认的，级联删除

PROTECT: 通过抛出django.db.models.ProtectedErrordjango.db.models.ProtectedError错误来阻止删除关联的对象

SET_NULL: 设置ForeignKey 为 null; 这个只有设置了null 为 True的情况才能用

SET_DEFAULT: 设置 ForeignKey 为默认值; 默认值必须预先设置

SET(): 设置为某个方法返回的值

DO_NOTHING: 什么都不做，如果数据库设置必须关联则会报IntegrityError错。
"""
