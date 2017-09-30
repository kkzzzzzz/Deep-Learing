#  http://www.taodabai.com/68228096.html
#  最小二乘法通过最小化误差的平方和寻找数据的最佳函数匹配
#  一般两个变量，斜率和常数
#  对这两个变量求偏导，得到两个方程，然后就可以算出两个未知量了
#  y = mx + b
#  m is slope , b is y-intercept

def compute_error_for_line_given_poinst(b,m,cordinates):
    totalError = 0
    for i in range(0,len(cordinates)):
        x = cordinates[i][0]
        y = cordinates[i][1]
        totalError += (y - (m * x + b))**2

    return totalError / float(len(cordinates))

# example


points = [[1, 6], [2, 5], [3, 7], [4, 10]]
minError = 1000
m = 0
b = 0
for i in range(1,50):
  for j in range(1,50):
      error = compute_error_for_line_given_poinst(i / 10.0, j / 10.0, points)
      if(minError > error):
          minError = error
          m = i/10.0
          b = j/10.0

print m
print b
