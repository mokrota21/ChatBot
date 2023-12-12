import csv
from datetime import date
from datetime import datetime

current_date = date.today()


with open("unilife.csv", 'r') as file:
  csvreader = csv.reader(file)
  data = list(csvreader)

sports_list = [row[0] for row in data[1:]]
associations_list = [row[1] for row in data[1:]]
events_list = [row[2] for row in data[1:]]

events = []
for event_line in events_list[1:]:
    event_info = event_line.split('(')
    event_name = event_info[0].strip()
    event_date = event_info[1].split(')')[0].strip()
    events.append((event_name, event_date))

print(sports_list)
print(associations_list)
print(events_list)
print(events)


name = input("Hello, what is your name?")
print(f"Nice to meet you, {name}, what topic would you like to discuss?")
topic_number = int(input(" 1 - Study advice \n 2 - Sports \n 3 - Social acticities "))

def study():
    print("Are you struggling with any aspect of your studies or just looking for practical information?")
    response = int(input(" 1 - I'm struggling with something \n 2 - I'm looking for practical information \n"))

    if response == 1:
        share = int(input("Would you like to share this with other students in a study group, or would you prefer to talk to a student advisor? \n 1 - Share in a study group \n 2 - Talk to a student advisor \n"))
        if share == 1:
            print("Joining a study group can be a great way to overcome challenges. You can find study groups on the university's student portal.")
        elif share == 2:
            print("Talking to a student advisor can provide personalized help. You can book an appointment with a student advisor through the university website.")
    elif response == 2:
        print("For practical information about studying, including resources and tips, you can visit the Student Desk's contact page on the university website.")






def sports():
  havesport: bool = False
  print("Do you want to search for a certain sport's club you are interested in joing or do you want to explore what is available at VU Amsterdam?")
  x = int(input(" 1 - I am looking for something specificic \n 2 - I would like to explore the options "))

  if x == 2:
    team = int(input("Do you like team sports? \n 1 - Yes \n 2 - No "))
    if team==1:
      water = int(input("Are you looking for watersports?  \n 1 - Yes \n 2 - No "))
      if water == 1:
        print("I recommend you to join our waterpolo team. ")
      else:
          print("In that case, I can recommend football and basketball.")




  if x == 1:
    print("What are you looking for?")


    if havesport == False:
      print("Sorry, we don't have any clubs for what you listed, but let's see if there is anything else you would like.")
      sports()


def social():
  x = int(input("Are you interested in joining an association? \n 1 - Yes \n 2 - No "))




  if x==2:
    print("In that case, I can tell you about the upcoming events.")

    sorted_events = sorted(events, key=lambda x: datetime.strptime(x[1], '%d %b').date())


    #for event, date in sorted_events:



    #print("Upcoming Events:")
    #for event, date_str in upcoming_events:
     # print(f"{event} ({date_str})")



if topic_number == 1:
  study()
if topic_number == 2:
  sports()

if topic_number == 3:
  social()
