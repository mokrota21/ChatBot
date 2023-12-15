import csv
from datetime import date
from datetime import datetime

current_date = date.today()
print(current_date)

#OPENING AND PUTTING THE DIFFERENT KINDS OF ASSOCIATIONS INTO DIFFERENT LISTS
with open("unilife.csv", 'r') as file:
  csvreader = csv.reader(file)
  data = list(csvreader)

  sports_list = [row[0] for row in data[1:]]
  associations_list = [row[1] for row in data[1:]]
  events_list = [row[2] for row in data[1:]]


endbool: bool = False
def end():
  if endbool:
    exit()


name = input("Hello, what is your name?")
print(f"Nice to meet you, {name}!")


#function that determines which of the main functions (study, sports, social) will be called/which topic is discussed
#it is called in the begginning and if the discussion of one of these topics ends
def start():
  end()
  print("Type in the number of topic you would like to discuss")
  topic_number = int(input(" 1 - Study advice \n 2 - Sports \n 3 - Social acticities \n 4 - None of these"))
  if topic_number == 1:
    study()
  if topic_number == 2:
    sports()
  if topic_number == 3:
    social()
  if topic_number == 4:
    print("In that case, have a nice day!")
    endbool
    end()


#A FUNCTION THAT RETURNS THE CLUBS WITHIN A GIVEN CATEGORY OF CLUBS (sports_list or associations_list) THAT CONTAIN A GIVEN KEYWORD
def search_association(list_of_clubs, keyword) -> bool:
  end()
  found: bool = False
  results = []
  for club in list_of_clubs:
    if keyword.lower() in club.lower():
      results.append(club)
      found = True
  if found:
    print("The following club(s) include the given keyword:")
    for result in results:
      print(result)
    start()




def study():
    end()
    print("Are you struggling with any aspect of your studies or just looking for practical information?")
    response = int(input(" 1 - I'm struggling with something \n 2 - I'm looking for practical information \n"))

    if response == 1:
        share = int(input("Would you like to share this with other students in a study group, or would you prefer to talk to a student advisor? \n 1 - Share in a study group \n 2 - Talk to a student advisor \n"))
        if share == 1:
            print("Joining a study group can be a great way to overcome challenges. You can find more information about study groups on the university's student portal.")
            find_association()
        elif share == 2:
            print("Talking to a student advisor can provide personalized help. You can book an appointment with a student advisor through the university website.")
            start()
    elif response == 2:
        print("For practical information about studying, including resources and tips, you can visit the Student Desk's contact page on the university website.")
        start()

#function that finds sports club for student by search or through questions
def sports():
  end()
  havesport: bool = False
  print("Do you want to search for a certain sport's club you are interested in joing or do you want to explore what is available at VU Amsterdam?")
  x = int(input(" 1 - I am looking for something specificic \n 2 - I would like to explore the options "))

  if x == 2:
    team = int(input("Do you like team sports? \n 1 - Yes \n 2 - No "))
    if team==1:
      water = int(input("Are you looking for watersports?  \n 1 - Yes \n 2 - No "))
      if water == 1:
        print("I recommend you to join our waterpolo team. ")
        start()
      else:
        print("In that case, I can recommend football and basketball.")
        start()
    else:
      martial = int(input("Are you interested in joining a martial arts club? \n 1 - Yes \n 2 - No"))
      if martial == 1:
        print("You can join our aikido or karate sports club.")
        start()
      else:
        water = int(input("Are you looking for watersports?  \n 1 - Yes \n 2 - No "))
        if water == 1:
          print("I recommend you to join our swimming team. ")
          start()
        else:
          print("In that case, I can recommend tennis, yoga or zumba.")
          start()
  else:
    keyword = str(input("What are you looking for?"))
    search_association(sports_list, keyword)
    if search_association(sports_list, keyword) == False:
      print(f"Sorry, we don't have any clubs for {keyword}, but let's see if there is anything else you would like.")
      sports()


def social():
  end()
  x = int(input("Are you interested in joining an association? \n 1 - Yes \n 2 - No "))

  if x == 1:
    find_association()
  if x==2:
    print("In that case, I can tell you about the upcoming events.")
  upcoming_events()

#function that finds association for student by search or through questions

def find_association():
  end()
  x = int(input("You can reach for associations or help you find a good fit based on your interest after answering a few questions about you. \n 1 - Search for associations \n 2 - I need help to find out what would be suitable"))
  if x == 1:
    keyword = input("What are you looking for?")
    search_association(associations_list, keyword)
    if search_association(associations_list, keyword) == False:
      print(f"Sorry, we don't have any clubs for {keyword}, but let's see if there is anything else you would like.")
      find_association()

  else:
    interest = input("Which of these aligns with your area of interest the most? \n 1 - Humanities \n 2 - Arts \n 3 - Sciences \n 4 - Community service \n 5- Sports")
    if interest == 1:
      print("Poetry Pals, Debate Club and Language Club could be suitable for you.")
      start()
    elif interest == 2:
      print("Poetry Pals, Painting and Pottery are suitable associations for you.")
      start()
    elif interest == 3:
      print("Science Society and Debate Club could be suitable options for you.")
      start()
    elif interest == 4:
      print("Students for Sustainability and Animal Shelter Volunteers are suitable associations for you.")
      start()
    elif interest == 5:
      print("Bunch of Backpackers could be a good fit to you. Additionally, you could take a look at our sports club options.")
      sports()



#after defining all the necessary functions, we call the start function
start()