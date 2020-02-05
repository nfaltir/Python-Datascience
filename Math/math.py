#main function
def main():

#function that asks for user name
  def hello_func():
    name = input(str("Enter your name:"))
    return name

#function that asks for user age
  def userAge():
    age = int(input("Please enter your age:"))
    return age

#prints user input of both functions 
  print("Greetings" , hello_func() , " you are " , userAge() , "years old!")

main()

