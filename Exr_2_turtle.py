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


def Ex_6(num_of_paw = 12,length_puw = 70):
    """
    :param num_of_paw:
    :param length_puw:
    :return:
    draw paw of
    """
    trt.shape('turtle')
    # calculate angle of rotate paw
    angle = 360 / num_of_paw
    for i in range(num_of_paw):
        trt.forward(length_puw)
        trt.stamp()
        trt.backward(length_puw)
        trt.right(angle)


def Ex_7():
    """
    Draw a circular spiral
    """
    trt.shape('turtle')
    l = 1 # bias
    angle = 10

    for i in range(400):
        trt.forward(l)
        trt.left(angle)

        #Increases the length
        l = l + 0.05

        # stop the turtle so you can see the result
    trt.mainloop()


def Ex_8():
    """
    Draw a square spiral
    :return:
    """
    l = 15 # length of line

    trt.shape('turtle')
    for i in range(10):
        trt.forward(l)
        trt.left(90)
        trt.forward(l)
        trt.left(90)
        l += 15  # increases the length of line
        trt.forward(l)
        trt.left(90)
        trt.forward(l)
        trt.left(90)
        l += 15  # increases the length of line


    trt.mainloop()


# FIX THIS!!!!
def n_polygon(num_of_side=5, side_length=30):
    trt.shape('turtle')
    # l = 2*PI*R
    angle = 360 / num_of_side

    for i in range(num_of_side):
        trt.left(angle)
        trt.forward(side_length)

# FIX THIS!!!!!
def Ex_9(num_of_polygon=3):
    for i in range(num_of_polygon):
        n_polygon(3+i,20+i*5)
        trt.penup()
        trt.left(20+i*5)
        trt.forward(20)
        trt.left(20 + i * 5)
        trt.pendown()


import math

def Ex_10():
    # draw_circle(20)
    # # trt.left(180)
    # draw_circle(20,-1)
    # trt.left(90)
    # draw_circle(20)
    # trt.left(180)
    # draw_circle(20)
    trt.circle(30,360)
    trt.circle(-30,360)
    trt.left(60)
    trt.circle(30,360)
    trt.circle(-30,360)
    trt.left(60)
    trt.circle(30, 360)
    trt.circle(-30, 360)


    trt.mainloop()

def draw_circle(raius = 10, dir = 1):
    trt.shape('turtle')
    accur_of_circle = raius  # кол сторон, при рисовании окружности(точность)
    angle = 360/accur_of_circle # угол попорота стороны
    angle_radians = math.radians(angle)
    legth_of_side = math.sin(angle_radians) * 2 * raius

    for _ in range(accur_of_circle):
        trt.forward(legth_of_side)
        trt.left(angle*dir)



Ex_10()



