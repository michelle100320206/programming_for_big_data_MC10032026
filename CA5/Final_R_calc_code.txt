#Write a scientfic calc in R 

rm(list=ls()) 

add <- function(x, y) {
  return(x + y)
}

print(add(4,44))

subtract <- function(x, y) {
  return(x - y)
}

print(subtract(4,44))

multiply <- function(x, y) {
  return(x * y)
}

print(multiply(4,44))

divide <- function(x,y) {
  if(y == 0){
    return ("error")
  } else {
    return(x/y)
  }
}

print(divide(4,44))

squareroot <-function(x) {
  return (sqrt(x))
}

print (squareroot(1000))



square <-function(x) {
  return (x*x)
}

print (square(1000))

getfactorial <- function(num) {
  if(num < 0) {
    print("Error: factorial does not exist for neg numbers")
  } else if(num == 0) {
    print("The factorial of 0 is equal to 1")
  } else {
    factorial = 1
    for(i in 1:num) {
      factorial = factorial * i
    }
    print(paste("The factorial of", num ,"is equal to",factorial))
  }
}

print (getfactorial(4))

cosine <- function(x) {
  return(cos(x*pi/180))
}

print (cosine(120))


sine <- function(x) {
  return(sin(x*pi/180))
}

print (sine(120))



tangent <- function(x) {
  if(x %% 180 ==0){
    return (0)
  } else if(x%% 90 ==0){
    return ("error")
  } else {
    return (tan(x*pi/180))
  }
}

print (tangent(90))

#handling user input using readline() in R - couldnt get this to work all the time 

getnumberinputs <- function() 
{ 
  numinputs = as.numeric(readline("Enter num [1 or 2]: "))
  if (numinputs == 1) {
    print("Select a number to carry out operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = as.integer(readline(prompt="Enter choice[1/2/3/4]: "))
    
    num1 = as.integer(readline(prompt="Enter first number: "))
    num2 = as.integer(readline(prompt="Enter second number: "))
    
    operator <- switch(choice,"+","-","*","/")
    result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2))
    
    print(paste(num1, operator, num2, "=", result))
  } else if (numinputs == 2) {
    print("select a number to carry out operation.")
    print("1.Sine")
    print("2.Cosine")
    print("3.Tan")
    print("4.SquareRoot")
    print("5.Square")
    print("6.Factorial")
    choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6]: "))
    
    uinput = as.integer(readline(prompt="Enter input: "))
    operator <- switch(choice,"Sine","Cosine","Tan","SquareRoot","Square","Factorial")
    result <- switch(choice, sine(uinput), cosine(uinput), tangent(uinput), squareroot(uinput), square(uinput), getfactorial(uinput))
    print(paste(operator, uinput, "=", result))
  } else {print("error invalid")}
} 

#handling user input using readline() in R - couldnt get this to work all the time 
print("Select Number of inputs:")
print("1. For Add, Subtract, Multiply or Divide")
print("2. For SQRT and square")
inptnumber <-getnumberinputs()
#~print (inptnumber)


if(inptnumber==1){
  print("select a number to carry out operation.")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  choice = as.integer(readline(prompt="Enter choice[1/2/3/4]: "))
  
  num1 = as.integer(readline(prompt="Enter first number: "))
  num2 = as.integer(readline(prompt="Enter second number: "))
  
  operator <- switch(choice,"+","-","*","/")
  result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2))
  
  print(paste(num1, operator, num2, "=", result))
  
} else if(inputnumber == 2){
  print ("B")
} else {
  print ("Invalid Input")
}










if(choice==1){
  print ("A")
} else if(choice == 2){
  print ("B")
} else {
  print ("C")
}


#handling user input using readline() in R - couldnt get this to work all the time 
print("select a number to carry out operation.")
print("1.Sine")
print("2.Cosine")
print("3.Tan")
print("4.SquareRoot")
print("5.Square")
print("6.Factorial")
choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6]: "))

uinput = as.integer(readline(prompt="Enter input: "))
operator <- switch(choice,"Sine","Cosine","Tan","SquareRoot","Square","Factorial")
result <- switch(choice, sine(uinput), cosine(uinput), tangent(uinput), squareroot(uinput), square(uinput), getfactorial(uinput))
print(paste(operator, uinput, "=", result))