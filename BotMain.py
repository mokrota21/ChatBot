from typing import Any
import discord
from unibot import UniBot
from ConversationTree import ConversationTree, Node
import pandas as pd
from datetime import date
from datetime import datetime
import csv

def seperate_event_date(text):
  """
  Seperates events from dates by given string
  """
  tmp = text.split('(')
  event = tmp[0].strip()
  date = tmp[1].strip(')')
  return event, date

def str_csv_table(path: str):
        """
        Converts csv table in easy to read message and returns it as a string
        
        path - path to a file
        """
        df = pd.read_csv(path)
    
        table_str = '```\n' + df.to_string(index=False) + '\n```'
        return table_str

# Adjusted associations function
def association_nodes():
  study111 = 'Joining a study group can be a great way to overcome challenges. You can find more information about study groups on the university\'s student portal.'
  association01 = 'You can reach for associations or help you find a good fit based on your interest after answering a few questions about you.'
  association02 = '\n1 - Search for associations \n2 - I need help to find out what would be suitable \nBack'
  association = Node([study111, association01, association02])

  association1 = Node(['What are you looking for?'])

  association1_neg = Node(["Sorry, we don't have any clubs for {user_message}."])
  association1_pos = Node(["We have study group related to {user_message}, you can join it on our university website"])

  association021 = 'Which of these aligns with your area of interest the most?'
  association022 = '\n1 - Humanities \n2 - Arts \n3 - Sciences \n4 - Community service \n5 - Sports \nBack'
  association2 = Node([association021, association022])

  association21 = Node(['Poetry Pals, Debate Club and Language Club could be suitable for you.'])

  association22 = Node(['Poetry Pals, Painting and Pottery are suitable associations for you.'])

  association23 = Node(['Science Society and Debate Club could be suitable options for you.'])

  association24 = Node(['Students for Sustainability and Animal Shelter Volunteers are suitable associations for you.'])

  association25 = Node(['Bunch of Backpackers could be a good fit to you. Additionally, you could take a look at our sports club options.'])

  global social
  social['1'] = association

  association1.set_neg(association1_neg)
  make_edges(associations_list, association1, association1_pos)
  association['1'] = association1

  association['2'] = association2
  association2['1'] = association21
  association2['2'] = association22
  association2['3'] = association23
  association2['4'] = association24
  association2['5'] = association25 

  return association

# Adjusted version of study() function
def study_nodes():
   study01 = 'Are you struggling with any aspect of your studies or just looking for practical information?'
   study02 = '1 - I am struggling with something \n2 - I am looking for practical information \nBack'
   study = Node([study01,study02])

   study10 = 'Would you like to share this with other students in a study group, or would you prefer to talk to a student advisor?'
   study101 = '1 - Share in a study group \n2 - Talk to a student advisor \nBack'
   study1 = Node([study10, study101])

   study112 = 'Talking to a student advisor can provide personalized help. You can book an appointment with a student advisor through the university website.'

   study12 = Node([study112])

   study20 = 'For practical information about studying, including resources and tips, you can visit the Student Desk\'s contact page on the university website.'
   study2 = Node([study20])

   study['1'] = study1
   study1['2'] = study12
   study['2'] = study2

   study1['1'] = association_nodes()

   return study

# Adjusted version of sport() function
def sports_nodes():
  sport01 = 'Do you want to search for a certain sport\'s club you are interested in joing or do you want to explore what is available at VU Amsterdam?'
  sport02 = '1 - I am looking for something specificic \n2 - I would like to explore the options \nBack'
  sport = Node([sport01,sport02])

  sport10 = 'What are you looking for?'
  sport1 = Node([sport10])

  sport110 = 'Sorry, we don\'t have any clubs for what you listed, but let\'s see if there is anything else you would like.'
  sport11 = Node([sport110])

  sport_present = 'We have sport club related to {user_message}, you can join it on our university website'
  sport_present_node = Node([sport_present])

  sport20 = 'Do you like team sports? \n1 - Yes \n2 - No \nBack'
  sport2 = Node([sport20])

  sport210 = 'Are you looking for watersports?  \n1 - Yes \n2 - No \nBack'
  sport21 = Node([sport210])

  sport2110 = 'I recommend you to join our waterpolo team.'
  sport211 = Node([sport2110])

  sport2120 = 'In that case, I can recommend football and basketball.'
  sport212 = Node([sport2120])

  sport220 = 'Are you interested in joining a martial arts club? \n1 - Yes \n2 - No \nBack'
  sport22 = Node([sport220])

  sport2210 = 'You can join our aikido or karate sports club.'
  sport221 = Node([sport2210])

  sport2220 = 'Are you looking for watersports?  \n1 - Yes \n2 - No \nBack'
  sport222 = Node([sport2220])

  sport22210 = 'I recommend you to join our swimming team.'
  sport2221 = Node([sport22210])

  sport22220 = 'In that case, I can recommend tennis, yoga or zumba.'
  sport2222 = Node([sport22220])


  sport['1'] = sport1
  sport1.set_neg(sport11)
  global sports_list
  make_edges(sports_list, sport1, sport_present_node)

  sport['2'] = sport2
  sport2['1'] = sport21
  sport21['1'] = sport211
  sport21['2'] = sport212
  sport2['2'] = sport22
  sport22['1'] = sport221
  sport22['2'] = sport222
  sport222['1'] = sport2221
  sport222['2'] = sport2222

  return sport
   
def social_nodes(top3):
  social00 = 'Are you interested in joining an association? \n1 - Yes \n2 - No \nBack'
  social = Node([social00])

  social021 = 'In that case, I can tell you about the upcoming events.'
  social022 = top3
  social2 = Node([social021, social022])

  social['2'] = social2

  return social

# Current date
current_date = date.today()

# Reading 'unilife' file
with open("unilife.csv", 'r') as file:
  csvreader = csv.reader(file)
  data = list(csvreader)

# Creating sports and associations lists
sports_list = [row[0] for row in data[1:]]
associations_list = [row[1] for row in data[1:]]

# Making pandas dataframe for events and their corresponding date
raw_events_list = [row[2] for row in data[1:]]
events_list = []
events_date_list = []

for event in raw_events_list:
  event_str, event_date_str = seperate_event_date(event)
  events_list.append(event_str)
  events_date_list.append(event_date_str)

events_df = {
  'Event': events_list,
  'Date': events_date_list
}
events_df = pd.DataFrame(events_df)

# changing date from string to datetime
date_format = '%d %b'
events_df['Date'] = events_df['Date'].apply(lambda x: datetime.strptime(x, date_format).date())
current_year = current_date.year
events_df['Date'] = events_df['Date'].apply(lambda x: x.replace(year=current_year))

events_df['Date_dif'] = events_df['Date'] - current_date
events_df = events_df.sort_values(by='Date_dif', ascending=False)

top3 = events_df[events_df['Date_dif'] > current_date - current_date].head(3)
top3 = top3[['Event', 'Date']]
top3 = '```\n' + top3.to_string(index=False) + '\n```'

def make_edges(l, parent, target):
    for s in l:
      parent[s] = target

# Discord properties of our bot
client = discord.Client(intents=discord.Intents.all())
TOKEN = 'MTE4Mzc3NDI1NDY0NzQ4MDM5MA.GObune.mBUpjjKyo8ZviY_xMwhV0m29cCRM48KvKHUwO4'

# Greeting 
greet1 = str_csv_table('unilife.csv')
greet2 = 'Hello {username}! Nice to meet you. My name is UniBot, I\'m chat bot specifically designed to provide students useful information.'
greet3 =  'What topic would you like to discuss?'
greet4 = '1 - Study advice \n2 - Sports \n3 - Social acticities \nBack'
greet = Node([greet1, greet2, greet3, greet4])

# social
social = social_nodes(top3)
greet['3'] = social

# Study nodes
study = study_nodes()
greet['1'] = study

# sport
sport = sports_nodes()
greet['2'] = sport

bot = UniBot(TOKEN, client, 0.1, greet)
bot.run_bot()