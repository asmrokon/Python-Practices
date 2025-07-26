score = float(input("Enter your score: "))

if score >= 90 <= 100:
    print("You got an A.")  
    
elif score >= 80 <= 89:   
    print("You got a B.")

elif score >= 70 <= 79 :
    print("You got a C.")

elif score >= 60 <= 69 :
    print("You got a D.")

elif score >= 50 <= 59:
    print("You got an E.")

elif score < 50:
    print("You got an F.")