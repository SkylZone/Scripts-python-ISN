from turtle import *
color('black','blue')
pensize(2)
home()
begin_fill()
while True:
	forward(100)
	left(60)
	if abs(pos()) < 1:
		break
end_fill()
done()