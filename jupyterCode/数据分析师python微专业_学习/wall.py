import turtle as t
t.up()
t.bk(400)
t.rt(90)
t.fd(170)
t.lt(90)
t.down()
t.pencolor("black")
t.fillcolor("red")
t.pensize(5)

i = 1
t.begin_fill()
while i<= 7: 
	t.fd(80)
	t.lt(90)
	t.fd(40)
	t.rt(90)
	t.fd(30)
	t.rt(90)
	t.fd(40)
	t.lt(90)
	t.bk(30)
	t.fd(30)
	i += 1
t.fd(80)

t.rt(90)
t.fd(50)
t.rt(90)

def draw_wall(count,size):	
	j = 1
	while j <= count:
		t.fd(size)
		t.rt(90)
		t.fd(50)
		t.bk(50)
		t.lt(90)
		j += 1

draw_wall(8,106.25)
t.bk(850)
t.lt(90)
t.fd(50)
t.rt(90)

draw_wall(1,53.125)
draw_wall(7,106.25)
draw_wall(1,53.125)
t.bk(850)
t.lt(90)
t.fd(50)
t.rt(90)
draw_wall(8,106.25)
t.end_fill()

t.up()
t.bk(425)
t.rt(90)
t.fd(200)
t.down()

t.pensize(20)
t.pencolor("grey")
t.fd(300)
t.pencolor("red")
t.fillcolor("red")
t.pensize(1)

t.begin_fill()
for i in range(4):
	if i in [1,3]:
		t.rt(90)
		t.fd(75)
	else:
		t.rt(90)
		t.fd(100)
t.end_fill()

#t.up()
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(25)
t.lt(90)
#t.down()

t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()

def draw_5(length):
	for i in range(5):
		t.fd(length)
		t.rt(144)

draw_5(20)


t.end_fill()

t.up()
t.lt(90)
t.fd(30)
t.down()
	
t.hideturtle()
t.write("The Picture of Wall!",align="center",font=("Time Romance",26,"bold"))
t.exitonclick()
