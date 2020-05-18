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

def Ex_3(angle = 10, acc = 10 ):
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

