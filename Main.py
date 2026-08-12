user=input("What is your name: ")
print("welcome sir ",user,"may wish you won:")


Questions=["Who was the first Mughal emperor in India?:","Who win the T20 Wc of 2009","total number of planet on solar system:","which planet is known as Red Planet."]
Ans=["babur","pakistan","8","mars"]

Lv1=100000
Lv2=200000
Lv3=300000
Lv4=400000000

a1=input(Questions[0])

if a1.lower()==Ans[0]:
    print("Correct answer:you have won Rs.",Lv1)
    

    a2=input(Questions[1])
    if a2.lower()==Ans[1]:
        print("Correct answer you have won Rs.",Lv2)

        a3=input(Questions[2])
        if a3.lower()==Ans[2]:
            print("Correct you have won Rs.",Lv3)
            a4=input(Questions[3])
            if a4.lower()==Ans[3]:
                print("Correct you have win Bumper price '7 crore'",Lv4)
            else:
                print("wrong answer, you can take money",Lv4)
        else:
            print("wrong answer: you can take money",Lv3)
    else:
        print("wrong answer, you can take money ",Lv2)
else:   
    print("tumse na ho payegaa baccha:" )