import turtle as trt

def Ex_1():
    trt.shape('turtle')
    trt.forward(50)
    trt.left(90)
    trt.forward(50)
    trt.left(90)
    trt.forward(50)
    trt.right(90)
    trt.forward(50)
    trt.right(90)
    trt.forward(50)

def Ex_3():
    # Draw square
    trt.shape('turtle')
    trt.forward(50)
    trt.left(90)
    trt.forward(50)
    trt.left(90)
    trt.forward(50)
    trt.left(90)
    trt.forward(50)

def Ex_4(angle = 10, acc = 10 ):
    """
    :param angle:
    angle of rotate a turtle
    :param acc:
    accuracy of draw circle ( angle rotate )
    :return:
    draw the circle with module turtle
    """
    # Draw circle
    trt.shape('turtle')

    steps = int(360/acc)
    for _ in range(steps):
        trt.forward(acc)
        trt.left(angle)

def Ex_5(num_square = 5, step_sq = 10):
    """
    :param num_square:
    :param step_sq:
    :return:
    """
    square = 10
    trt.shape('turtle')

    for _ in range(num_square):
        trt.forward(square)
        trt.left(90)
        trt.forward(square)
        trt.left(90)
        trt.forward(square)
        trt.left(90)
        trt.forward(square)

        trt.penup()
        trt.forward(step_sq)
        trt.right(90)
        trt.forward(step_sq)
        trt.left(90)
        trt.left(90)
        square += step_sq *2
        trt.pendown()


def Ex_6(num_of_paw = 12,lenght_puw = 70):
    """
    :param num_of_paw:
    :param lenght_puw:
    :return:
    draw paw of
    """
    trt.shape('turtle')
    # calculate angle of rotate paw
    angle = 360 / num_of_paw
    for i in range(num_of_paw):
        trt.forward(lenght_puw)
        trt.stamp()
        trt.backward(lenght_puw)
        trt.right(angle)


def Ex_7():
    trt.shape('turtle')
    # p = k * angle
    l = 1 # bias
    angle = 10

    for i in range(400):
        trt.forward(l)
        trt.left(angle)
        l = l + 0.05






Ex_7()

