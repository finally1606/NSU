import turtle as T

t = T.Turtle()
t.up()
#x, y - координаты
#rotate - поворот в градусах
#color - цвет
#scale - увеличение размера
def square(x, y, rotate, color, scale):
    t.goto(x, y)
    t.down()
    t.pencolor('white')
    t.speed(1000)
    t.right(rotate)
    t.fillcolor(f'{color}')
    t.begin_fill()
    t.forward(30*scale)
    t.right(90)
    t.forward(30*scale)
    t.right(90)
    t.forward(30*scale)
    t.right(90)
    t.forward(30*scale)
    t.end_fill()
    t.right(90)
    t.left(rotate)
    t.up()

def triangle(x, y, rotate, color, scale):
    t.goto(x, y)
    t.down()
    t.pencolor('white')
    t.speed(1000)
    t.right(rotate)
    t.fillcolor(f'{color}')
    t.begin_fill()
    t.forward(30*scale)
    print(t.pos())
    t.right(225)
    t.forward((30*scale)*(2**0.5))
    print(t.pos())
    t.right(225)
    t.forward(30*scale)
    t.end_fill()
    t.right(-rotate-90)
    t.up()


def parallelogram(x, y, rotate, color, scale):
    t.goto(x, y)
    t.down()
    t.pencolor('white')
    t.speed(1000)
    t.left(45+rotate)
    t.fillcolor(f'{color}')
    t.begin_fill()
    t.forward(30*scale)
    t.right(45)
    t.forward(42.42641*scale)
    t.right(135)
    t.forward(30*scale)
    t.end_fill()
    t.right(45)
    t.forward(42.42641*scale)
    t.up()

def finish(x,y):
    t.goto(x,y)


#central square
def central_square():
    triangle(2, 32, -45, 'red', 2)
    triangle(2, 32, 225, 'yellow', 2)
    parallelogram(-40, -10, 0, 'green', 1)
    triangle(44, -10, 90, 'blue', 1.45)
    triangle(2, 32, -45, 'pink', 1)
    triangle(23, 53, 225, 'violet', 1)
    square(23,11,45,'orange',1)

#fish
def fish():
    triangle(0, 200, 0, 'red', 1)
    triangle(0, 140, 90, 'yellow', 1)
    square(-13,160,45,'orange',0.5)
    triangle(16, 170, 45, 'blue', 0.75)
    parallelogram(-53, 186, 135,'green', 0.5)
    triangle(-37, 171, -135, 'violet', 0.5)
    triangle(-37, 156, 45, 'pink', 0.5)

#chiken
def chicken():
    triangle(100, 180, -45, 'red', 1)
    triangle(85, 196, -90, 'blue', 0.75)
    parallelogram(82, 147, -45, 'green', 0.5)
    triangle(100, 165, 0, 'yellow', 1)
    square(128,180,0,'orange',0.5)
    triangle(122,189, 45, 'pink', 0.5)
    triangle(111, 144, -45, 'violet', 0.5)

#rabbit
def rabbit():
    triangle(-110, 160, 180, 'red', 1)
    triangle(-140, 160, 0, 'yellow', 1)
    square(-95,190,0,'orange',0.5)
    parallelogram(-100, 190, 225,'green', 0.5)
    triangle(-117, 132, 225, 'blue', 0.75)
    triangle(-98, 155, 180, 'pink', 0.5)
    triangle(-117, 132, -45, 'violet', 0.5)

#human left
def human_left():
    square((-117+(-100))//2 - 10,65,0,'orange',0.5)
    triangle((-117+(-120))//2 - 10, 45, 45, 'red', 1)
    parallelogram((-117+(-150))//2 - 10, 16, 90, 'green', 0.5)
    triangle(-110, 2, 135, 'yellow', 1)
    triangle(-145, 10,  -45, 'pink', 0.5)
    triangle(-93, -5, 90, 'blue', 0.75)
    triangle(-120, -20, -90, 'violet', 0.5)

#boat
def boat():
    triangle(-115, -70, -135, 'violet', 0.5)
    triangle(-93, -90, 90, 'red', 1)
    triangle(-115, -105, 135, 'yellow', 1)
    square(-82,-101,0,'orange',0.5)
    triangle(-104, -100, 0, 'pink', 0.49)
    parallelogram(-137, -110, 90, 'green', 0.5)
    triangle(-105, -126, 90, 'blue', 0.75)

#whale
def whale():
    triangle(42, -100, 0, 'red', 1)
    triangle(0, -100, 180, 'yellow', 1)
    parallelogram(52, -70, 45, 'green', 0.5)
    triangle(12, -70, 135, 'blue', 0.5)
    square(-28,-83, 45,'orange',0.5)
    triangle(-12, -110,-45, 'pink', 0.5)
    triangle(-1, -100, 135, 'violet', 0.5)

#rocket
def rocket():
    triangle(120, -91, 45, 'red', 1)
    triangle(139, -71, 225, 'yellow', 1)
    triangle(140, -50, 180, 'blue', 0.75)
    triangle(130, -40, 135, 'pink', 0.5)
    parallelogram(152, -123, 90, 'green', 0.5)
    square(131,-103, 45,'orange',0.5)
    triangle(120, -114, 135, 'violet', 0.5)

#human right
def human_right():
    triangle(130, 45, 90, 'red', 1)
    triangle(130, 45, 0, 'yellow', 1)
    square(140,55, 50,'orange',0.5)
    triangle(130, -5, 270, 'blue', 0.75)
    parallelogram(115, -10, 135, 'green', 0.5)
    triangle(158, -5, 45, 'violet', 0.5)
    triangle(122, -18, 135, 'pink', 0.5)

central_square()
fish()
chicken()
rabbit()
human_left()
boat()
whale()
rocket()
human_right()

finish(1000, 1000)
t.hideturtle()  

T.done()
