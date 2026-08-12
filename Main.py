
class KBC:
    def __init__(self):
        print("=======Welcome to KBC Game========")
    def start(self):
        user=input("What is your Name Sir: ")
        print("welcome sir ",user,"may wish you will win:")


        Questions=["Who was the first Mughal emperor in India?:","Who win the T20 Wc of 2009?","total number of planet on solar system?:","which planet is known as Red Planet?"]
        Ans=["babur","pakistan","8","mars"]

        Lv1=100000
        Lv2=200000
        Lv3=300000
        Lv4=700000

        Q1=input(Questions[0]+"\n1: Akbar \n2: Babur \n3: Humayun \n4: Shahjahan\n Ans: ")

        if Q1.lower()==Ans[0]:
            print("Correct answer:you have won Rs.",Lv1)
    

            Q2=input(Questions[1]+"\n1: India \n2: Pakistan \n3: Bangladesh \n4: Sri Lanka\n Ans: ")

            if Q2.lower()==Ans[1]:

                print("Correct answer you have won Rs.",Lv2)

                Q3=input(Questions[2]+"\n1: 7 \n2: 8 \n3: 9 \n4: 10\n Ans: ")

                if Q3.lower()==Ans[2]:

                    print("Correct you have won Rs.",Lv3)

                    Q4=input(Questions[3]+"\n1: Venus \n2: Mars \n3: Jupiter \n4: Saturn\n Ans: ")

                    if Q4.lower()==Ans[3]:

                        print("Correct you have win Bumper price '7 crore'",Lv4)

                    else:

                        print("wrong answer, you can take money",Lv4)

                else:

                    print("wrong answer: you can take money",Lv3)

            else:

                print("wrong answer, you can take money ",Lv2)

        else:   

            print("tumse na ho payegaa baccha:" )



obj=KBC()
obj.start()