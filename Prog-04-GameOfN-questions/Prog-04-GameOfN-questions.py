# 2110101 Computer Programming

# Prog-04: game of N-questions
# 6330085821

# Extra1: Add "incorrect answer" response in case user does not input (yes/no)
# Extra2: Add more than 4 Q&As
# โปรแกรมนี้ ผมได้นำโค๊ดเริ่มต้นจากอาจารย์ มาเขียนฟังก์ชันประกอบคำสั่งเพิ่มเติมให้โปรแกรมดูน่าสนใจด้วยตนเอง
# เพื่อนำไปเขียน flow chart แสดงการทำงานของโปรแกรม

# example game "what is the number in your mind?"
#  with 3 questions

print("Think of a number from 1..20")
print("answer 'yes' or 'no' ")
ans = input("Is it a prime number? ").strip()
if( ans == "yes" ):   #2,3,5,7, 11,13,17,19
    ans = input("Is it greater than 7? ").strip()
    if( ans == "yes" ):
        ans = input("Is 4 a factor of that number plus one ?  ").strip()
        if( ans == "yes" ): #11,19
            ans = input("if you Subtract 2 from that number, it will become a prime number ")
            if( ans == "yes"): #19
                print("the number is 19")
            elif (ans == "no"): #11
                print("the number is 11")
            else:
                print("invalid answer")
        elif( ans == "no" ): #13,17
            ans = input("Let x = that number plus one ,  7 is one of the factors of x")
            if( ans == "yes"): #13
                print("the number is 13")
            elif (ans == "no"): #18
                print("the number is 18")
            else:
                print("invalid answer")                
        else:
            print("invalid answer")
            
    elif( ans == "no"): #2,3,5,7
        ans = input("Is it greater than 3? ").strip()
        if( ans == "yes" ): #5,7
            ans = input("Let P = that number plus 3, 4 is one of the factors of P  ?  ").strip()
            if( ans == "yes"): #5
                print("the number is 5")
            elif (ans == "no"): #7
                print("the number is 7")
            else:
                print("invalid answer")     
        elif( ans == "no"): #2,3
            ans = input("Is it a GCF of 6 and 9  ?  ").strip()
            if( ans == "yes"): #3
                print("the number is 3")
            elif (ans == "no"): #2
                print("the number is 2")
            else:       
                print("invalid answer")
    else:
        print("invalid answer")

        
elif( ans == "no"):  #1,4,6,8,9,10,12,14,15,16,18,20
    ans = input("Is it greater than 10? ").strip()
    if( ans == "yes" ):  #12,14,15,16,18,20
        ans = input("Is 3 a factor of that number ?  ").strip()
        if( ans == "yes" ): #12,15,18
            ans = input("Is it an odd number?  ")
            if( ans == "yes"): #15
                print("the number is 15")
            elif (ans == "no"): #12,18
                ans = input("Is it greater than 15?")
                if( ans == "yes"): #18
                    print("the number is 18")
                elif (ans == "no"): #12
                    print("the number is 12")
                else:
                    print("invalid answer")           
        elif( ans == "no" ): #14,16,20           
            ans = input("Let x = that number plus one; Is 3 a factor of x ? ")
            if( ans == "yes"): #14,20
                ans = input("Is it greater than 15?")
                if( ans == "yes"): #20
                    print("the number is 20")
                elif (ans == "no"): #14
                    print("the number is 14")
                else:
                    print("invalid answer") 
            elif (ans == "no"): #16
                print("the number is 16")
            else:
                print("invalid answer")                
        else:
            print("invalid answer")
            
    elif( ans == "no"):  #1,4,6,8,9,10
        ans = input("Is it greater than 6? ").strip()
        if( ans == "yes" ): #8,9,10
            ans = input("Let Q = that number plus 3. Is Q a prime number ?  ").strip()
            if( ans == "yes"): #8,10
                ans = input("Is 5 a factor of that number ? ")
                if( ans == "yes"): #10
                    print("the number is 10")
                elif (ans == "no"): #8
                    print("the number is 8")
                else:
                    print("invalid answer") 
            elif (ans == "no"): #9
                    print("the number is 9")
            else:
                print("invalid answer")     
        elif( ans == "no"): #1,4,6
            ans = input("Is it an odd number ?  ").strip()
            if( ans == "yes"): #1
                print("the number is 1")
            elif (ans == "no"): #4,6
                ans = input("That number is one of the roots of the equation:  x^2 + 2x - 24 = 0 ?  ").strip()
                if( ans == "yes"): #4
                    print("the number is = 4")
                elif (ans == "no"): #6
                    print("the number is 6")
                else:
                    print("invalid answer")                    
            else:       
                print("invalid answer")
        else:
            print("invalid answer")
    else:
        print("invalid answer")            
else:
    print("invalid answer")            
            