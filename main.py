# #pip3 install requests;
import similar_text;
import requests;
import math;
import random;

from similar_text import similar_text;


response= requests.get("http://jservice.io/api/clues?category=139").json()
#print(response)

#store a random dictionary with id and questions and answer
ranQuest = response[random.randint(0,len(response)) ]#['question']
userScore = 0;
computerScore =0;

#print(response)
#print(ranQuest)
print("##############################################")

#made a function with question from random dictionary
def askQuestion():
  print(ranQuest['question'])
  myAnswer = input("Whats your answer ")
  #return that answer to be used later return doesnt store anything so when i call the function make sure i store the return value in a variable ex:
  # vanilla = iceCream()
  return myAnswer
  
#THis is a function that takes in the answer the user score and computer score and checks if the answer is correct and changes the score accordingly
def checkAnswer(myAnswer,userScore,computerScore):
  #if myAnswer in ranQuest.values():
  if myAnswer.lower()==ranQuest["answer"].lower():
    print("Your right")
    userScore= userScore + 1;
    #return userScore
    

  else:
    print("cmon bro")
    print("The correct answer was "+ranQuest['answer'] )
    computerScore= computerScore + 1;
  
  return(userScore,computerScore)

  #returned user score and cp score to be used in while loop
  
 

while userScore <=3 and computerScore <=3:
  ranQuest = response[random.randint(0,len(response)) ]
  answer = askQuestion() #set answer to equal to return of ask question
  userScore,computerScore= checkAnswer(answer,userScore,computerScore)#updates thes scores
  print(userScore)
  print(computerScore)




#plan
#while score is less that or equal to 3 print
#print(response[0]['answer'])

#ask the user question
#if the question and answer are in the dictionary print you got it right
#if the user input matches value in dictionary your right



