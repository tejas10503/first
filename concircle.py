import turtle

turtle.penup()
for i in range(1, 500, 50):
    turtle.right(90)    
    turtle.forward(i)   
    turtle.right(270)   
    turtle.pendown()    
    turtle.circle(i)    
    turtle.penup()      
    turtle.home()  
