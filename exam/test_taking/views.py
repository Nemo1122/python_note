from django.shortcuts import render, redirect, reverse
from .models import *
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import time

def index(request):
    return render(request, 'test_taking/index.html')

def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user:
        auth.login(request, user)
        request.session['user'] = username
        response = HttpResponseRedirect('/test/')
        return response
    else:
        return render(request, 'test_taking/index.html', {"error": '用户名或密码错误，请重新输入！'})

@login_required
def testing(request):
    all_test_list = Test.objects.filter(status='V').order_by('order')
    return render(request, 'test_taking/testing.html',
                  {'all_test_list': all_test_list})

@login_required
def test_detail(request, course_id):
    """试卷页面"""

    # 展示试题
    # 标题取科目名称
    start = time.time()
    test_title = Test.objects.filter(status='V', id=course_id)
    questions_level_1_list = TestDetail.objects.filter(status='V', level=1, course_id=course_id)
    question_list = []

    user = request.session['user']
    # 获取已保存的答案
    for q1 in questions_level_1_list:
        # 获取该大题下面的所有小题
        questions_level_2_list = TestDetail.objects.filter(status='V',
                                                           level=2,
                                                           parent=q1.id)
        if questions_level_2_list:
            for q2 in questions_level_2_list:
                # 获取每一道题的答案
                answer = UserAnswer.objects.filter(create_user=user, course_id=course_id, question_id=q2.id)
                if answer:
                    setattr(q2, 'user_answer', answer[0].user_answer)
            setattr(q1, 'q2', questions_level_2_list)
        else:
            answer = UserAnswer.objects.filter(create_user=user, course_id=course_id, question_id=q1.id)
            if answer:
                setattr(q1, 'user_answer', answer[0].user_answer)
        question_list.append(q1)
    end = time.time()
    print('{0} 查询数据时间：{1}'.format(user, end - start))

    return render(request, 'test_taking/test_detail.html',
                  {'test_title': test_title[0].course,
                   'question_list': question_list,
                   })

@login_required
# 在页面提交答案后，需要保存答案
def test_answer(request, qid):
    # answer = request.POST.get('answer')
    # question = TestDetail.objects.get(id=qid)
    # question.answer = answer
    # question.save()
    # course_id = question.course_id.id
    # 重定向到考卷页面
    # return HttpResponseRedirect('/test_paper/{0}/'.format(course_id))
    start = time.time()
    answer = request.POST.get('answer')
    user = request.session['user']
    question = TestDetail.objects.get(id=qid)
    course_id = question.course.id
    try:
        user_answer = UserAnswer.objects.get(question_id=qid, create_user=user, course_id=question.course_id)
    except ObjectDoesNotExist:
        user_answer = None
    if user_answer:
        user_answer.user_answer = answer
        now = datetime.now().strftime("%Y-%m-%d %X.%f")
        user_answer.update_time = now
        user_answer.update_user = user
        # 外键必须在字段名后面加id，否则格式必须是外键的对象
        user_answer.course_id = course_id
        user_answer.question_id = qid
        user_answer.save()
    else:
        user_answer = UserAnswer()
        user_answer.question_id = qid
        user_answer.user_answer = answer
        user_answer.create_user = user
        now = datetime.now().strftime("%Y-%m-%d %X.%f")
        user_answer.create_time = now
        user_answer.course_id = course_id
        user_answer.save()
    end = time.time()
    print('{0} 保存数据时间：{1}'.format(user, end - start))
    return HttpResponseRedirect('/test_paper/{0}/'.format(course_id))

