import math

import inline as inline
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model

df=pd.read_csv('l.csv')
median_bedrooms=math.floor((df.bedrooms.median()))

def gradient_descent(x,y):
    m_curr=b_curr=0
    iterations=10000
    learning_rate=0.08
    n=len(x)
    for i in range(iterations):
        y_predicted = m_curr*x+b_curr
        cost=(1/n)*sum([val**2 for val in (y-y_predicted)])
        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        print("m {}, b {},cost {} iteration {}".format(m_curr,b_curr,cost,i))
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])


if __name__ == '__main__':
    gradient_descent(x,y)

