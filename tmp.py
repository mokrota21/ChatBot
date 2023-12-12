from typing import Any
import discord
from unibot import UniBot
from ConversationTree import ConversationTree
from ConversationTree import Node
import pandas as pd
import csv
with open("unilife.csv", 'r') as file:
  csvreader = csv.reader(file)
  data = list(csvreader)
sports_list = [row[0] for row in data[1:]]
associations_list = [row[1] for row in data[1:]]
events_list = [row[2] for row in data[1:]]
def str_csv_table(path: str):
        """
        Converts csv table in easy to read message and returns it as a string
        path - path to a file
        """
        df = pd.read_csv(path)
        table_str = '```\n' + df.to_string(index=False) + '\n```'
        return table_str
# Discord properties of our bot
client = discord.Client(intents=discord.Intents.all())
TOKEN = 'MTE4Mzc3NDI1NDY0NzQ4MDM5MA.GObune.mBUpjjKyo8ZviY_xMwhV0m29cCRM48KvKHUwO4'
# Conversation rules for bot
conversation = ConversationTree()
# Greeting 
greet1 = str_csv_table('unilife.csv')
greet2 = 'Hello! Nice to meet you. What topic would you like to discuss?'
greet3 = '1 - Study advice \n2 - Sports \n3 - Social acticities'
greet = Node([greet1, greet2, greet3])
# study
study01 = 'Are you struggling with any aspect of your studies or just looking for practical information?'
study02 = '1 - I am struggling with something \n2 - I am looking for practical information'
study = Node([study01,study02])
greet['1'] = study
study10 = 'Would you like to share this with other students in a study group, or would you prefer to talk to a student advisor?'
study101 = '1 - Share in a study group \n2 - Talk to a student advisor'
study1 = Node([study10, study101])
study['1'] = study1
study111 = 'Joining a study group can be a great way to overcome challenges. You can find more information about study groups on the university\'s student portal.'
study112 = 'Talking to a student advisor can provide personalized help. You can book an appointment with a student advisor through the university website.'
study1['2']
study11 = Node([study111])
study12 = Node([study112])
study1['1'] = study11
study1['2'] = study12
study20 = 'For practical information about studying, including resources and tips, you can visit the Student Desk\'s contact page on the university website.'
study2 = Node([study20])
study['2'] = study2
# sport
sport01 = 'Do you want to search for a certain sport\'s club you are interested in joing or do you want to explore what is available at VU Amsterdam?'
sport02 = '1 - I am looking for something specificic \n2 - I would like to explore the options '
sport = Node([sport01,sport02])
greet['2'] = sport
sport10 = 'What are you looking for?'
sport1 = Node([sport10])
sport['1'] = sport1
sport110 = 'Sorry, we don\'t have any clubs for what you listed, but let\'s see if there is anything else you would like.'
sport11 = Node([sport110])
sport1.set_neg(sport11)
sport_present = 'We have sport club related to this, you can join it on our university website'
sport_present_node = Node([sport_present])
for s in sports_list:
    sport1[s] = sport_present_node
sport20 = 'Do you like team sports? \n1 - Yes \n2 - No'
sport2 = Node([sport20])
sport['2'] = sport2
sport210 = 'Are you looking for watersports?  \n1 - Yes \n2 - No'
sport21 = Node([sport210])
sport2['1'] = sport21
sport2110 = 'I recommend you to join our waterpolo team.'
sport211 = Node([sport2110])
sport21['1'] = sport211
sport2120 = 'In that case, I can recommend football and basketball.'
sport212 = Node([sport2120])
sport21['2'] = sport212
sport220 = 'Are you interested in joining a martial arts club? \n1 - Yes \n2 - No'
sport22 = Node([sport220])
sport2['2'] = sport22
sport2210 = 'You can join our aikido or karate sports club.'
sport221 = Node([sport2210])
sport22['1'] = sport221
sport2220 = 'Are you looking for watersports?  \n1 - Yes \n2 - No'
sport222 = Node([sport2220])
sport22['2'] = sport222
sport22210 = 'I recommend you to join our swimming team.'
sport2221 = Node([sport22210])
sport222['1'] = sport2221
sport22220 = 'In that case, I can recommend tennis, yoga or zumba.'
sport2222 = Node([sport22220])
sport222['2'] = sport2222
# social
social00 = 'Are you interested in joining an association? \n1 - Yes \n2 - No'
social0 = Node([social00])
greet['3'] = social0
social10 = 'You can reach for associations or help you find a good fit based on your interest after answering a few questions about you. \n 1 - Search for associations \n - I need help to find out what would be suitable'
social1 = Node([social10])
social0['1'] = social1
social110 = 'What are you looking for?'
social11 = Node([social110])
social1['1'] = social11
social120 = 'Which of these aligns with your area of interest the most? \n1 - Humanities \n2 - Arts \n3 - Sciences \n4 - Community service \n5 - Sports'
social12 = Node([social120])
social1['2'] = social12
social1210 = 'Poetry Pals, Debate Club and Language Club could be suitable for you.'
social121 = Node([social1210])
social12['1'] = social121
social1220 = 'Poetry Pals, Painting and Pottery are suitable associations for you.'
social122 = Node([social1220])
social12['2'] = social122
social1230 = ''
social123 = Node([social1230])
conversation.expand_answers({'l': greet})
UniBot(0.1, conversation, TOKEN, client)