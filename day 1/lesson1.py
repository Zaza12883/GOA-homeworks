from turtle import *
speed ( 30 )

#we want to paint a house

#step 1:   draw a square
width ( 5 )

pensize ( 5 )
     
color ("brown")

       
forward ( 200 )
left ( 90 )

forward ( 200 )
left ( 90 )
forward ( 200 )
left ( 90 )
forward ( 200 )
left ( 90 )
#end of square
#drawing a door

forward ( 70 )
color ( "red" )

begin_fill()


left ( 90 )

forward ( 120 ) #height of the door
right ( 90 )
forward ( 60 )
right ( 90 )

forward ( 120 )
end_fill()



penup ( )

goto ( 201, 201 )

pendown ( )




color ("black")
begin_fill ( )
right ( 120 )

forward ( 129 )

left(66)

forward ( 111 )
end_fill()

penup()
pensize(3)
goto(200,150)
pendown()
color("blue")
begin_fill()
right(36)



forward(50)

left(90)


forward(36)



right(270)

forward(50)



left(90)

forward(40)
end_fill()


penup()
pensize(3)
goto(0,113)
pendown()
color("blue")
begin_fill()
right(90)
pensize(5)
forward(50)
left(90)
forward(30)
left(90)

forward(50)
left(90)

forward(30)
end_fill()
exitonclick()

