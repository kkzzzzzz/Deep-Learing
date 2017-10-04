#coding:utf-8 
# 感知器 y  = f(Wn * x + b)
# 代码实现的是一个逻辑AND操作，输入最后一项一直为1，代表我们可以理解偏置项b的特征值输入一直为1 
# 这样就是 y = f(Wn+1*[x,1])， Wn+1就是b
# https://www.zybuluo.com/hanbingtao/note/433855
from numpy import array, dot, random
from random import choice


def fun_1_or_0(x): return 0 if x < 0 else 1



training_data = [(array([0, 0, 1]), 0), (array([0, 1, 1]), 0),
                 (array([1, 0, 1]), 0), (array([1, 1, 1]), 1)]

weights = random.random(3)
print("before traning, weights:",weights)

learning_rate = 0.2
num_iteratios = 100
for i in range(num_iteratios):
    input, truth = choice(training_data)
    result = dot(weights, input)
    error = truth - fun_1_or_0(result)
    
    weights += learning_rate * error * input

print("after traning, weights:",weights)

for x, _ in training_data:
    result = dot(x, weights)
    print("{}:{}->{}".format(x[:2], result, fun_1_or_0(result)))


