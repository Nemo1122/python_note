import logging
import logging.handlers


# basicConfig一次性的简单配置工具使，也就是说只有在第一次调用该函数时会起作用，
# 后续再次调用该函数时完全不会产生任何操作的，多次调用的设置并不是累加操作。
logging.basicConfig(level=logging.DEBUG)

"""
怎样得到一个Logger对象呢？一种方式是通过Logger类的实例化方法创建一个Logger类的实例，
但是我们通常都是用第二种方式--logging.getLogger()方法。
logging.getLogger()方法有一个可选参数name，该参数表示将要返回的日志器的名称标识，
如果不提供该参数，则其值为'root'。若以相同的name参数值多次调用getLogger()方法，
将会返回指向同一个logger对象的引用。
"""
logger = logging.getLogger('test_log')

# 输出文件到文件，默认情况下文件大小会无限增长
handler = logging.FileHandler("log.log", encoding='utf-8')
# 按时间分割日志文件
"""
TimedRotatingFileHandler(filename [,when [,interval [,backupCount]]])
filename 是输出日志文件名的前缀
when 是一个字符串的定义如下：
“S”: Seconds
“M”: Minutes
“H”: Hours
“D”: Days
“W”: Week day (0=Monday)
“midnight”: Roll over at midnight
interval 是指等待多少个单位when的时间后，Logger会自动重建文件，当然，这个文件的创建
取决于filename+suffix，若这个文件跟之前的文件有重名，则会自动覆盖掉以前的文件，所以
有些情况suffix要定义的不能因为when而重复。
backupCount 是保留日志个数。默认的0是不会自动删除掉日志。若设10，则在文件的创建过程中
库会判断是否有超过这个10，若超过，则会从最先创建的开始删除。
"""
handler = logging.handlers.TimedRotatingFileHandler('time_log.log', 'D', 1)

# 设置handle的level
# handler.setLevel(logging.INFO)
handler.setLevel(logging.DEBUG)

# 日志输出格式
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Start logging")

records = {'name': 'Nemo', 'url': 'http://www.jianshu.com/u/ea364f9b9048'}
logger.debug('记录数据： %s' % records)
# logger.info('修改记录 ...')
# # update records here
# logger.info('修改完成 ...')
# logger.warning('这是一个警告！')
# logger.debug('这是一个debug信息！！')
try:
    open('oo', 'r')
except Exception as e:
    # 使用参数 exc_info=true 调用 logger 方法, traceback 会输出到 logger 中
    logger.error(e, exc_info=True)
    # 不使用参数exc_info=true, 则只会输出[Errno 2] No such file or directory: 'oo'
    # logger.error(e)
    # 你也可以调用logger.exceptioen(msg, _args)，它等价于 logger.error(msg, exc_info=True, _args)。
    # logger.exception(e)



