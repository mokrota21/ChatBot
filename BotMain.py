from typing import Any
import discord
import csv
from datetime import date
from datetime import datetime
import pandas as pd
from asyncio import sleep
"""
root
edges = 
{greeting: {1: study, 2: sports, 3: social_activity},
study: {1: }}
"""
class Node:
    pass

class Node:
    """
    Node class represents nodes in conversation tree, each node has reply which is designed to be given when we get in this node,
    from each node we can go to next instance of conversation via key in neighbours, where keys are possible replies from user.
    Since we give reply when we get into node, we need root node to point to start of conversation (if we begin at start of conversation we don't print it)
    """
    def __init__(self, reply: list[str] =[''], root: bool = False) -> None:
        self.reply: list[str] = reply
        self.neighbours: dict[str, Node] = {}
        self.root: bool = root
    
    def __getitem__(self, key: str) -> list[str]:
        if self.root:
            assert len(self.neighbours) == 1
            return list(self.neighbours.values())[0]
        else:
            return self.neighbours[key]
    
    def __setitem__(self, key: str, value: Node) -> None:
        # if node is root we want it to point only to one node
        if self.root:
            assert len(self.neighbours) <= 1
            if self.neighbours.keys():
                key = list(self.neighbours.keys())[0]
        self.neighbours[key] = value

class ConversationTree:
    """
    Class to store important info about conversation, it has root of the tree to be able to start conversation over,
    current node to keep track of our position
    """
    def __init__(self) -> None:
        self.root: Node = Node(root=True)
        self.now: Node = self.root
        self.path: list[Node] = [self.root]
    
    def expand_answers(self, expansion) -> None:
        self.now.neighbours = expansion
    
    def __getitem__(self, key) -> Node:
        return self.now[key]
    
    def leaf_now(self) -> bool:
        return len(self.now.neighbours) == 0

    def get_reply(self, key: str) -> None:
        self.now = self[key]
        self.path.append(self.now)

        reply = self.now.reply

        if self.leaf_now():
            self.reset()

        return reply
    
    def revert(self) -> None:
        assert len(self.path) >= 2
        self.now = self.path[-2]
        self.path.pop()

    def reset(self) -> None:
        self.now = self.root
        self.path = [self.root]

class UniBot:
    def __init__(self, delay: float, conversation: ConversationTree, TOKEN: str, client) -> None:
        
        self.conversation = conversation
        self.delay = delay
        
        # required variables
        self.TOKEN: str = TOKEN
        self.client = client

        # starting bot
        self.run_bot()
    
    # making table readable
    
    async def handle_message(self, user_message):
        return self.conversation.get_reply(user_message)
    
    async def send_message(self, message, user_message):
        try:
            replies = await self.handle_message(user_message)

            for reply in replies:
                await message.channel.send(reply)
                await sleep(self.delay)
        except Exception as e:
            print(e)

    # async def greet(self, message):
    #     """
    #     Gets message and sends response

    #     message - message overall, data type from discord API

    #     user_message - content of message, type string
    #     """
    #     try:
    #         greeting = f"Hello {message.author.name}, what topic would you like to discuss?"
    #         choice = f'1 - Study advice \n 2 - Sports \n 3 - Social acticities'

    #         await message.channel.send(await self.str_csv_table())
    #         await sleep(self.delay)

    #         await message.channel.send(greeting)
    #         await sleep(self.delay)

    #         await message.channel.send(choice)

    #         reply = await self.client.wait_for('message')

    #         topic_number = reply.content
    #     except Exception as e:
    #         print(e)


    def run_bot(self):
        """
        Starts bot, after calling our becomes active and answers on questions
        """
        @self.client.event
        async def on_ready():
            print(f'{self.client.user} is running')

        @self.client.event
        async def on_message(message):
            nonlocal self

            username = str(message.author).split('#')[0]
            user_message = message.content
            print(f'{username}: {user_message}')

            if message.author == self.client.user:
                return

            await self.send_message(message, user_message)

        self.client.run(self.TOKEN)


def str_csv_table(path: str):
        """
        Converts csv table in easy to read message and returns it as a string
        
        path - path to a file
        """
        df = pd.read_csv(path)
    
        table_str = '```\n' + df.to_string(index=False) + '\n```'
        return table_str

client = discord.Client(intents=discord.Intents.all())
TOKEN = 'MTE4Mzc3NDI1NDY0NzQ4MDM5MA.GObune.mBUpjjKyo8ZviY_xMwhV0m29cCRM48KvKHUwO4'
conversation = ConversationTree()

greet1 = str_csv_table('unilife.csv')
greet2 = 'Hello! Nice to meet you, what topic would you like to discuss?'
greet3 = '1 - Study advice\n2 - Sports\n3 - Social activity'
Greet = Node([greet1, greet2])
conversation.expand_answers({'l': Greet})

UniBot('unilife.csv', 0.1, conversation, TOKEN, client)