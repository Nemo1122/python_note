import csv


# csv 读

file_path = "E:\\工作\\海德\\附件\\user.csv"

with open(file_path, "r") as f:
    # 生成csv读对象
    data = csv.reader(f)
    all_user = []
    for user in data:
        all_user.append(user)

print(all_user)
# reader(csvfile, dialect='excel', **fmtparams)
# 参数说明：
# csvfile，必须是支持迭代(Iterator)的对象，可以是文件(file)对象或者列表(list)对象，如果是文件对
# 象，打开时需要加"b"标志参数。
# dialect，编码风格，默认为excel的风格，也就是用逗号（,）分隔，dialect方式也支持自定义，
# 通过调用register_dialect方法来注册，下文会提到。
# fmtparam，格式化参数，用来覆盖之前dialect对象指定的编码风格。


# csv 写

# windows系统中每加一行，都会自动在行尾加\r\n导致会产生一个新行，因此打开是必须用newline=''，
# 否则每添加一次会有一个空行
file_path = "E:\\工作\\海德\\附件\\user.csv"
with open(file_path, 'a', newline='') as csv_file:
    user = ['zhaoqi','3344']
    all_user = [['wangwu2','1212'],['hanliu', '1311']]
    # csv 写对象
    my_writer = csv.writer(csv_file)
    # 写入一行
    my_writer.writerow(user)
    # 写入多行
    my_writer.writerows(all_user)





