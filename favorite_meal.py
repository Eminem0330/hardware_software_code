def meal_test(answer):
     if answer == 1:
          print ("Fried chicken Yummy!")
     elif answer == 2:
          print ("burger")
     elif answer == 3:
          Print ("pizza")
     else:
         print("That is not an option")

def main():
     print ("which is your favorite meal?")
     print ("1.chicken")
     print ("2.burger")
     print ("3.pizza")
     answer = int (input())
     meal_test (answer)

if __name__ == "__main__":
     main()
