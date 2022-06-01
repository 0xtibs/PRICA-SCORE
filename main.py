print("**************************************************************************"
      "\nPersonal Report of Intercultural Communication Apprehension (PRICA)"
      "\n************************************************************************"
      "\n"
      "\n"
      "The 14 statements below are comments frequently made by people with "
      "\nregard to communication with people from other cultures."
      "\nPlease indicate how much you agree with these statements by marking"
      "\na number representing your response to each statement using the following choices:"
      "\n"
      "++++++++++++++++++++++++++++++"
      "\nStrongly Disagree = 1      +"
      "\nDisagree = 2               +"
      "\nNeutral = 3                +"
      "\nAgree = 4                  +"
      "\nStrongly Agree = 5         +"
      "\n+++++++++++++++++++++++++++")


Q1 = int(input("1. Generally, I am comfortable interacting with a group of people from different cultures: "))
Q2 = int(input("2. I am tense and nervous while interacting with people from different cultures: "))
Q3 = int(input("3. I like to get involved in group discussion with others who are from different cultures: "))
Q4 = int(input("4. Engaging in a group discussion with people from different cultures makes me nervous: "))
Q5 = int(input("5. I am calm and relaxed with interacting with a group of people who are from different cultures:  "))
Q6 = int(input("6. While participating in a conversation with a person from a different culture, I get nervous: "))
Q7 = int(input("7. I have no fear of speaking up in a conversation with a person from a different culture: "))
Q8 = int(input("8. Ordinarily I am very tense and nervous in a conversation with person from a different culture: "))
Q9 = int(input("9. Ordinarily I am very calm and relaxed in conversations with a person from a different culture: "))
Q10 = int(input("10. While conversing with a person from a different culture, I feel very relaxed: "))
Q11= int(input("11. I am afraid to speak up in conversations with a person from a different culture: "))
Q12= int(input("12. I face the prospect of interacting with people from different cultures with confidence:  "))
Q13= int(input("13. My thoughts become confused and jumbled when interacting with people from different cultures: "))
Q14= int(input("14. Communicating with people from different cultures makes me fee uncomfortable: "))

Step1 = Q1 + Q3 + Q5 + Q7 +Q9 + Q10 + Q12
Step2 = Q2 + Q4 + Q6 + Q8 + Q11 + Q13 + Q14
Step3 = 42 - (int(Step1) + int(Step2))

print("Your PRICA score is " + str(Step3) + "!")
print("Scores can range from 14 to 70. Scores below 32 indicate low intercultural CA. "
      "\nScores above 52 indicate high intercultural CA. Scores ranging between 32 and 52 indicate a "
      "\nmoderate level of intercultural CA. ")