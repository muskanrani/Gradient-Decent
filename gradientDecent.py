#Function to calculate error at current m and b

def calculate_error(X,Y,m,b):
    error=0
    for x,y in zip(X,Y):
        error = error + (m*x+b-y)**2
    error/=2
    return error

def update_weights(m_current,b_current,X,Y,learning_rate):
    dssem=0
    dsseb=0
    for x,y in zip(X,Y):
        yp=m_current * x+b_current
        dssem = dssem- (y-yp)* x
        dsseb = dsseb -(y-yp)
    m_new = m_current - learning_rate * dssem
    b_new = b_current - learning_rate * dsseb
    return [b_new,m_new]

def run_(X,Y, m_current, b_current, learning_rate,steps):
    stepcount = 0
    olderror = calculate_error(X,Y,m_current,b_current)
    while(stepcount <= steps or newerror - olderror >= .001):
        b_current, m_current = update_weights(m_current, b_current, X, Y, learning_rate)
        newerror = calculate_error(X,Y, m_current, b_current)
        if stepcount % 10== 0:
            print("{0:5d}{1:10.2f}{2:10.2f}{3:10.2f}".format(stepcount, b_current, m_current, newerror))
        stepcount += 1
    return [b_current, m_current]
X=[0.00,0.22, 0.24, 0.33, 0.37, 0.44, 0.44, 0.57, 0.93, 1.00]
Y=[0.00,0.22, 0.58, 0.20, 0.55, 0.39, 0.54, 0.53, 1.00, 0.61]

m_current = 0.45
b_current = 0.75

print("String")
print("{0:10.2f}{1:10.2f}{2:10.2f}".format(b_current,m_current,calculate_error(X,Y, m_current, b_current)))
learning_rate = 0.01
steps =300
b_current, m_current = run_(X,Y, m_current, b_current, learning_rate, steps)
print("running...")
print("After {0} iterations: m is {1:10.2f} and b is {2:10.2f} with error {3:10.2f}".format(steps, m_current, b_current, calculate_error(X, Y, m_current, b_current)))
