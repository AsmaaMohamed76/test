#function to draw pyramid
def pyramid(height):
    print("===============================================")    
    for i in range(0, height):
        for j in range(0, height-i-1):
            print(end=" ")
        for j in  range(0, i+1):
            print("*", end=" ")
        print()     
 #function to draw right triangle       
def rightTriangle(height) :
    print("===============================================")    
    k = 1
    for i in range(0, height):
        for j in range(0, k):
            print("* ", end="")
        k = k + 1
        print()       
 #function to draw square        
def square(height):
    print("===============================================")   
    for i in range(height):
      print("* " * height) 
 #function to draw circle              
def circle(height): 
    print("===============================================")    
    for row in range(height):  
        for col in range(height):     
           if(row == 0 and (col != 0 and col != height-1)) or (row == height - 1 and (col != 0 and col != height-1)) or (col == 0 and (row != 0 and row != height-1)) or (col == height -1 and (row != 0 and row != height-1)) :
               print("* ",end='')
           else:
                print("  ",end='')
        print() 
#function to chose the shape name         
def choose(shape,height) :
    match shape :
        case "pyramid" :
            pyramid(height)
        case "right triangle" :
            rightTriangle(height)
        case "square" :
            square(height)
        case "circle" :
            circle(height)
        case _:
            print("Invalid Input")  

    
                   
print("Shapes list:\n *pyramid\n *right Triangle\n *square\n *circle")
shape1 = input("Enter Shape Name: ")
height1 = int(input("Enter Shape Height: "))

first = (shape1, height1)
shape2 = input("Enter Shape Name: ")
height2 = int(input("Enter Shape Height: "))
second = (shape2, height2)

shape3 = input("Enter Shape Name: ")
height3 = int(input("Enter Shape Height: "))
third = (shape3, height3)

shape4 = input("Enter Shape Name: ")
height4 = int(input("Enter Shape Height: "))
fourth = (shape4, height4)

shapes = [first, second, third, fourth]
shapes.sort(key=lambda y: y[1])
print(shapes)
choose(shapes[0][0],shapes[0][1])
choose(shapes[1][0],shapes[1][1])
choose(shapes[2][0],shapes[2][1])
choose(shapes[3][0],shapes[3][1])   
            
        
          