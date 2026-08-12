
class KBC:
    def __init__(self):
        print("=======Welcome to KBC Game========")
    def start(self):
        print("\n")
        user=input("What is your Name Sir: ")
        print("\n")
        print(f"welcome sir {user} may wish you will win: \n")


        Questions=["Who was the first Mughal emperor in India?:","Who win the T20 Wc of 2009?","total number of planet on solar system?:","which planet is known as Red Planet?","Which day is observed as world environment day?","Which is the largest continent in the world?","Which is the largest ocean in the world?","Which is the largest desert in the world?","Which is the largest river in the world?","Which is the largest country in the world?"]
        Ans=["babur","pakistan","8","mars","5 june","asia","pacific ocean","sahara desert","nile river","russia"]

        Lv1=100000
        Lv2=200000
        Lv3=300000
        Lv4=400000
        Lv5=500000
        Lv6=600000
        Lv7=700000
        Lv8=900000
        Lv9=1200000
        Lv10=1600000

        Q1=input(Questions[0]+"\n1: Akbar \n2: Babur \n3: Humayun \n4: Shahjahan\n Ans: ")

        if Q1.lower()==Ans[0]:
            print("\n 🎉Correct answer:you have won Rs.",Lv1,"\n")
    

            Q2=input(Questions[1]+"\n1: India \n2: Pakistan \n3: Bangladesh \n4: Sri Lanka\n Ans: ")

            if Q2.lower()==Ans[1]:

                print("\n 🎉Correct answer you have won Rs.",Lv2,"\n")

                Q3=input(Questions[2]+"\n1: 7 \n2: 8 \n3: 9 \n4: 10\n Ans: ")

                if Q3.lower()==Ans[2]:

                    print("\n 🎉Correct you have won Rs.",Lv3,"\n")

                    Q4=input(Questions[3]+"\n1: Venus \n2: Mars \n3: Jupiter \n4: Saturn\n Ans: ")

                    if Q4.lower()==Ans[3]:

                        print("\n 🎉Correct you have won price: ",Lv4,"\n")

                        Q5=input(Questions[4]+"\n1: 5 June \n2: 6 June \n3: 7 June \n4: 8 June\n Ans: ")

                        if Q5.lower()==Ans[4]:

                            print("\n 🎉Correct you have won price: ",Lv5,"\n")

                            Q6=input(Questions[5]+"\n1: Asia \n2: Africa \n3: Europe \n4: Australia\n Ans: ")

                            if Q6.lower()==Ans[5]:

                                print("\n 🎉Correct you have won price: ",Lv6,"\n")

                                Q7=input(Questions[6]+"\n1: Atlantic Ocean \n2: Indian Ocean \n3: Pacific Ocean \n4: Arctic Ocean\n Ans: ")

                                if Q7.lower()==Ans[6]:

                                    print("\n 🎉Correct you have won price: ",Lv7,"\n")

                                    Q8=input(Questions[7]+"\n1: Gobi Desert \n2: Kalahari Desert \n3: Sahara Desert \n4: Arabian Desert\n Ans: ")

                                    if Q8.lower()==Ans[7]:

                                        print("\n 🎉Correct you have won price: ",Lv8,"\n")

                                        Q9=input(Questions[8]+"\n1: Amazon River \n2: Nile River \n3: Yangtze River \n4: Mississippi River\n Ans: ")

                                        if Q9.lower()==Ans[8]:

                                            print("\n 🎉Correct you have won price: ",Lv9,"\n")

                                            Q10=input(Questions[9]+"\n1: China \n2: USA \n3: Russia \n4: Canada\n Ans: ")

                                            if Q10.lower()==Ans[9]:

                                                print("\n 🎉Correct you have won price:",Lv10,"\n")

                                            else:

                                                print("wrong answer, you can take money",Lv9)

                                        else:

                                            print("wrong answer, you can take money",Lv8)

                                    else:

                                        print("wrong answer, you can take money",Lv7)

                                else:

                                    print("wrong answer, you can take money",Lv6)

                            else:

                                print("wrong answer, you can take money",Lv5)

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