#coding:utf-8 
#通过组合最小二乘法和梯度下降法，可以得到线性回归

wheat_and_bread =  [[1, 6], [2, 5], [3, 7], [4, 10]]


def step_gradient(b_current, m_current, points, learingRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0,len(points)):
        x  = points[i][0]
        y  = points[i][1]
        # 损失函数，对b求导
        b_gradient += -(2/N) * (y - ((m_current * x + b_current)))
        # 损失函数，对m求导
        m_gradient += -(2/N) * x * (y - (m_current * x) + b_current)
    new_b = b_current - (learingRate * b_gradient)
    new_m = m_current - (learingRate * m_gradient)
    return [new_b, new_m]


def gradient_descent_runner(points, start_b, start_m, learing_rate, num_iterations):
    b = start_b
    m = start_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, points, learing_rate)
        print [b,m]
    return [b, m]


s = gradient_descent_runner(wheat_and_bread, 1, 1, 0.01, 1000)
print s
