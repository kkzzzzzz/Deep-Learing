# coding:utf-8
# 用最小二乘法，找误差的时候，如果每次迭代的步长确定，会导致找最小误差的时长特别长
# 因此用梯度下降法，找到误差下降最快的方式
# 参考资料http://www.cnblogs.com/pinard/p/5970503.html

# 这里的值可能影响到最终的最优解，可能只是一个局部最优
current_x = 1.5

# 这里的技巧是learning_rate。（步长）学习速度，速度越大下降越大，但是可能错过极值点
learning_rate = 0.09
# 学习次数
num_iterations = 1000

# 误差函数求导，也就是斜率
def slope_at_given_x_value(x):
    return 5 * x**4 - 6 * x**2


for i in range(num_iterations):
    previous_x = current_x
    # 这里的负号是关键，斜率的相反方向下降
    current_x += -learning_rate * slope_at_given_x_value(previous_x)
    print(previous_x)

print("The loacl minimum occurs at %f" % current_x)

# 梯度下降法的缺点包括：
# 靠近极小值时速度减慢。
# 直线搜索可能会产生一些问题。
# 可能会“之字型”地下降。