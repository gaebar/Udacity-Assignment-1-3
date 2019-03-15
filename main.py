#IPND Stage 2 Final Project, Gaetano Barreca
#I took my time to write this Python project because I was intrigued to see how I could express my knowledge through this language. I am a former Italian teacher as a second language, ready to step forward to a new tech career. I am pleased with the results of this Python project and hope you can enjoy it when reviewing. 

class UserContext:
  user_name = "Gaetano"
  user_city = "Boston"
  italian_city = "Rome"
  friend_name = "Alberto"
  italian_name = "Mario"
  attempts = 1
  max_attempts = 3
  difficulty = "easy"
  
  placeholders = ['__1__','__2__','__3__','__4__']
  answers = {'easy': 'Ciao', 'medium':'Ciao, bene, tu, Anche', 'advanced':'Ciao, Anche, chiamo, sono'}
 

#0. Introduction
def display_intro_questions(user_context):
  print("Welcome to the 'Italian Learning fill in the blanks quiz'! At the end of the quiz, you will be ready to introduce yourself in Italian and have a basic conversation.")
  print("\nPlease, type your name below: ")
  user_context.user_name=input()
  print("\nCiao " + user_context.user_name + ", benvenuto!(welcome!)")
  print("Please, type an Italian city you'd love to visit")
  user_context.italian_city=input()
  print("\nGood choice! In the context of this first Italian quiz, you will find yourself travelling on a train to " + user_context.italian_city + ". Who would you like to meet?")
  user_context.friend_name=input()

#1.Italian Learning fill in the blanks quiz
def display_quiz_text(user_context):
  print("\nBene, let's start! You have the first move: ")
  
  quiz_text = {'easy': "\n _1_ " + user_context.friend_name+ ", come stai?  \n Ciao " + user_context.user_name + ". Sto bene, grazie! E tu? \n Anche io! \n\n Hi, " + user_context.friend_name + ", how are you? \n Hi " + user_context.user_name + ". I'm good, thanks! And you? \n Me too!\n", 
  'medium':"\n Ciao " + user_context.friend_name + ", come stai?  \n _1_ " + user_context.user_name + ". Sto _2_, grazie! E tu? \n Anche io! Dove vai? \n Sto andando a " + user_context.italian_city + " e _3_? \n _4_ io! \n\n Hi, " + user_context.friend_name + ", how are you? \n Hi " + user_context.user_name + " I am good, thanks! And you? \n Mee too! Where are you going?\n I am going to " + user_context.italian_city + " and you? \n Me too!\n" ,
  'advanced':"\n Ciao " + user_context.friend_name + ", come stai?  \n _1_ " + user_context.user_name + ". Sto bene, grazie! E tu? \n Anche io! Dove vai? \n Sto andando a" + user_context.italian_city + " e tu? \n _2_ io! \n Lui è un tuo amico? \n Sì, studiamo insieme all’Università. \n Piacere, io mi chiamo " + user_context.user_name +", e tu come ti chiami? \n Piacere, io mi _3_ " + user_context.italian_name + ". Di dove sei? \n Io sono di " + user_context.user_city + " e sono in viaggio in Italia. E tu che cosa fai? \n Anche io _4_ di " + user_context.user_city + " e sono in viaggio in Italia! Quanti anni hai? \n Io ho trentatré anni e tu? Anche io!\n\n Hi, " + user_context.friend_name + ", how are you? \n Hi " + user_context.user_name + " I am good, thanks! And you? \n Mee too! Where are you going?\n I am going to " + user_context.italian_city + " and you? \n Me too!\n Is he one of your friends? \n Yes, we study together at the University. \n Nice to meet you, my name is " + user_context.user_name + ", what’s your name? \n Nice to meet you, my  name is " + user_context.italian_name + "Where are you from? \n I am from " + user_context.user_city + "and I am travelling to Italy. What do you do? \n I am also from" + user_context.user_city + " and I am travelling to Italy too! How old are you? \n I am thirtythree and you? \n Me too!"}
  
  #2. Teacher's notes
  quiz_notes = {
    'easy': "\nDid you know? The Italian Language “Ciao” means either hello and goodbye! When you are in Italy, and you start with a core and standard conversion like “Ciao, come stai?” Italians think you can speak their language correctly and for this reason, they begin to telling you all their life. After few minutes they understand you don't speak any Italian and to explain to you what they said, Italians start to use their favourite body language. It’s funny! Be always warming and friendly with unknown people and tourists is part of our culture. Being in Italy is a blessing!",
    'medium':"\nReread this exercise and practise with your friends. Just a small note to teach you that in the Italian language the \"ch\" sound is strong. We pronounce \"ch\" like the English \"k\". So, when you read \"Anche io\" (Me too), just remember to read with k, Anche io",
    'advanced' : "\nAs in other Latin languages, when Italians say their age, they don't use the verb to be but the verb to have. Check this example: Io sono Gaetano, io ho trentasette anni. (I am Gaetano, I have - not I am - thirty-seven years old.) IMPORTANT! when you learn a new language, you need to understand that every language, like Python, has its own roles. Now, be happy. You can successfully introduce yourself in Italian and have a small conversation. Bravo! For the very best results, repeat the advanced quiz level and take notes of the Italian questions."}
  
  #3. display different messages
  print(quiz_text[user_context.difficulty])
  print("What should go instead of the numbers? Separate your answers with commas: ")
  
  user_answers = input()
  is_input_correct = False
  
  while (is_input_correct == False):
    if(user_answers.lower() == (user_context.answers[user_context.difficulty]).lower()):
      display_win_message(user_context, quiz_notes)
      return
    else:
      print("Mamma Mia! Your answer is not correct. Please try again.")
      user_answers = input()
    
def display_win_message(user_context, quiz_notes):
  if(user_context.difficulty == 'easy' or user_context.difficulty == 'medium'):
    print ("\nBravo! You won. Read the teacher's notes and than try again with a higher difficulty level")
  else:
    print ("\nEccellente! You beat the highest level. Read and try the questions with your friends to practice your italian.")
  print (quiz_notes[user_context.difficulty])
  
#4. select difficulty
def select_difficulty(user_context):
    print("\nGreat, " + user_context.user_name + "! On this quiz use Easy, Medium and Advanced level to learn or revise some Italian words. At the end of each stage, you'll find some tips in the teacher's notes. How exciting it is!")
    user_prompt = "\nPlease type a game difficulty by typing it in!\nPossible choices: easy, medium, advanced:"
    selected_difficulty = input(user_prompt)
    print ("\nYou have selected '" + selected_difficulty + "'.")
    
    is_input_correct = False
    while(is_input_correct == False):
      if selected_difficulty.lower() == 'easy' or selected_difficulty.lower() == 'medium' or selected_difficulty.lower() == 'advanced':
          is_input_correct = True
          user_context.difficulty = selected_difficulty.lower()
      else:
          print("\nMamma mia! '" + selected_difficulty + "' is not a proper level option!\nPlease try again: ")
          selected_difficulty = input(user_prompt)
    
    user_context.difficulty = selected_difficulty.lower()
    
    if selected_difficulty.lower() =='advanced':
      print("\nWhich city are you from?")
      user_context.user_city = input()

def quiz():
  user_context = UserContext()
  display_intro_questions(user_context)
  select_difficulty(user_context)
  display_quiz_text(user_context)

quiz()

