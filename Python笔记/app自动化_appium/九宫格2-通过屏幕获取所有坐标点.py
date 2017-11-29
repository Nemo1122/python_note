def gesture(action, driver, s):
    """
    九宫格解锁
    :param action: TouchAction对象
    :param driver: 当前的driver对象
    :param s: 将解锁过程需要经过的点组成一个集合传入, e.g.“s = [7, 4, 1, 5, 9, 6, 3]”
    :return:
    """
    # 取得所有坐标点
    p = [[110, 275], [285, 275], [463, 275],
         [110, 455], [285, 455], [463, 455],
         [110, 630], [285, 630], [463, 630]]
    # 基准的屏幕长宽为 576, 1024, 如果获取到的屏幕坐标不是这两个值
    # 得出相对比值后计算新屏幕下的xy值,size['width']/576 *x, size['height']/1024 * y,
    size = driver.get_window_size()
    if size['height'] == 1024 and size['width'] == 576:
        p = p
    else:
        x_offset = size['width']/576
        y_offset = size['height']/1024
        p = [[i[0] * x_offset, i[1] * y_offset] for i in p]

    print('当前屏幕的九宫格坐标为：', p)

    # 按下传入的坐标点的列表
    action.press(x=p[s[0] - 1][0], y=p[s[0] - 1][1])
    for i in range(1, len(s)):
        # 判断当前点在上一个点的位置, 然后通过减法计算相对于上一个位置的偏移量
        # 如果是负数, 则表示往左上角移动, 如果是正数, 则表示向右下角移动
        x = p[s[i] - 1][0] - p[s[i-1] - 1][0]
        y = p[s[i] - 1][1] - p[s[i-1] - 1][1]
        # 根据偏移量移动
        action.move_to(x=x, y=y)
        # 稍作等待
        action.wait(300)

    # 释放按下动作
    action.release()
    # 将所有的操作提交
    action.perform()