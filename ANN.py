import math

def cal(net):
    return 1/(1+math.e**(-net))

def Farward(net, V, W, theta):
    net[3] = V[1] * W[1][3] + V[2] * W[2][3] + theta[3]
    V[3] = cal(net[3])
    print("net3:", net[3], "V[3]:", V[3])
    net[4] = V[1] * W[1][4] + V[2] * W[2][4] + theta[4]
    V[4] = cal(net[4])
    print("net4:", net[4], "V[4]:", V[4])
    net[5] = V[1] * W[1][5] + V[2] * W[2][5] + theta[5]
    V[5] = cal(net[5])
    print("net5:", net[5], "V[5]:", V[5])

    net[6] = V[3] * W[3][6] + V[4] * W[4][6] + V[5] * W[5][6] + theta[6]
    V[6] = cal(net[6])
    print("net6:", net[6], "V[6]:", V[6])
    net[7] = V[3] * W[3][7] + V[4] * W[4][7] + V[5] * W[5][7] + theta[7]
    V[7] = cal(net[7])
    print("net7:", net[7], "V[7]:", V[7])
    return net, V

def Backward(T, L, V, W, theta):
    de_6 = (T[2] - V[6]) * V[6] * (1 - V[6])
    print("de_6:", de_6)
    de_7 = (T[3] - V[7]) * V[7] * (1 - V[7])
    print("de_7:", de_7)

    dW36 = L * de_6 * V[3]
    W[3][6] += dW36 
    print("dW36:", dW36, "W[3][6]:", W[3][6])
    dW37 = L * de_7 * V[3]
    W[3][7] += dW37 
    print("dW37:", dW37, "W[3][7]:", W[3][7])
    dW46 = L * de_6 * V[4]
    W[4][6] += dW46 
    print("dW46:", dW46, "W[4][6]:", W[4][6])
    dW47 = L * de_7 * V[4]
    W[4][7] += dW47 
    print("dW47:", dW47, "W[4][7]:", W[4][7])
    dW56 = L * de_6 * V[5]
    W[5][6] += dW56 
    print("dW56:", dW56, "W[5][6]:", W[5][6])
    dW57 = L * de_7 * V[5]
    W[5][7] += dW57
    print("dW57:", dW57, "W[5][7]:", W[5][7])

    dthe6 = L * de_6
    theta[6] += dthe6
    print("dthe6:", dthe6, "theta[6]:", theta[6])
    dthe7 = L * de_7
    theta[7] += dthe7
    print("dthe7:", dthe7, "theta[7]:", theta[7])

    de_3 = V[3] * (1 - V[3]) * (W[3][6] * de_6 + W[3][7] * de_7)
    print("de_3:", de_3)
    de_4 = V[4] * (1 - V[4]) * (W[4][6] * de_6 + W[4][7] * de_7)
    print("de_4:", de_4)
    de_5 = V[5] * (1 - V[5]) * (W[5][6] * de_6 + W[5][7] * de_7)
    print("de_5:", de_5)

    dW13 = L * de_3 * V[1]
    W[1][3] += dW13
    print("dW13:", dW13, "W[1][3]:", W[1][3])
    dW23 = L * de_3 * V[2]
    W[2][3] += dW23
    print("dW23:", dW23, "W[2][3]:", W[2][3])
    dW14 = L * de_4 * V[1]
    W[1][4] += dW14
    print("dW14:", dW14, "W[1][4]:", W[1][4])
    dW24 = L * de_4 * V[2]
    W[2][4] += dW24
    print("dW24:", dW24, "W[2][4]:", W[2][4])
    dW15 = L * de_5 * V[1]
    W[1][5] += dW15
    print("dW15:", dW15, "W[1][5]:", W[1][5])
    dW25 = L * de_5 * V[2]
    W[2][5] += dW25
    print("dW25:", dW25, "W[2][5]:", W[2][5])

    dthe3 = L * de_3
    theta[3] += dthe3
    print("dthe3:", dthe3, "theta[3]:", theta[3])
    dthe4 = L * de_4
    theta[4] += dthe4
    print("dthe4:", dthe4, "theta[4]:", theta[4])
    dthe5 = L * de_5
    theta[5] += dthe5
    print("dthe5:", dthe5, "theta[5]:", theta[5])

    return W, theta

W = [[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0.1, 0, 0.3, 0, 0],
[0, 0, 0, -0.2, 0.2, -0.4, 0, 0],
[0, 0, 0, 0, 0, 0, -0.4, 0.2],
[0, 0, 0, 0, 0, 0, 0.1, -0.1],
[0, 0, 0, 0, 0, 0, 0.6, -0.2],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]]

theta = [0, 0, 0, 0.1, 0.2, 0.5, -0.1, 0.6]
V = [0] * 8
net = [0] * 8
L = 0.1
T_1 = [0.6, 0.1, 1, 0]
V[1], V[2] = T_1[0], T_1[1]

net, V = Farward(net, V, W, theta)
print("net:", net, "V", V)
W, theta = Backward(T_1, L, V, W, theta)
print("W", W, "theta", theta)

T_2 = [0.2, 0.3, 0, 1]
V[1], V[2] = T_2[0], T_2[1]

net, V = Farward(net, V, W, theta)
print("net:", net, "V", V)
W, theta = Backward(T_2, L, V, W, theta)
print("W", W, "theta", theta)