a=input("What is your name: ")
print("welcome sir ",a,"may wish you won:")


b=["Who was the first Mughal emperor in India?:","Who win the T20 Wc of 2009","total number of planet on solar system:","which planet is known as Red Planet."]
c=["babur","pakistan","8","mars"]

g=100000
h=200000
j=300000
k=400000000

a1=input(b[0])

if a1.lower()==c[0]:
    print("Correct answer:you have won Rs.",g)
    

    a2=input(b[1])
    if a2.lower()==c[1]:
        print("Correct answer you have won Rs.",h)

        a3=input(b[2])
        if a3.lower()==c[2]:
            print("Correct you have won Rs.",j)
            a4=input(b[3])
            if a4.lower()==c[3]:
                print("Correct you have win Bumper price '7 crore'",k)
            else:
                print("wrong answer, you can take money",k)
        else:
            print("wrong answer: you can take money",j)
    else:
        print("wrong answer, you can take money ",h)
else:
    print("tumse na ho payegaa baccha:" )