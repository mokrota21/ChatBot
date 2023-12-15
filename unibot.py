from typing import Any
from ConversationTree import ConversationTree, Node
from asyncio import sleep


class UniBot:
     """
     Authorize bot in discord and gives instructions via discrod API. For simplicity we represent conversation inside as ConversationTree. Since this
     bot can be used on server with a lot of people we also need create unique ConversationTree for each user by their userid. Due to how Python
     works, we don't create new tree over and over again, we just create a lot of pointers to existing nodes, which means that our bot doesn't consume
     tremendous amounts of memory
     """
     def __init__(self, TOKEN, client, delay: float, tree_root: Node, attributes: dict[str, str] = {}) -> None:
          self.tree_root = tree_root # root of predetermined conversation tree
          self.conversations = {}
          
          # necessary info for running bot
          self.TOKEN = TOKEN 
          self.client = client

          self.id = client.user # id of bot
          self.delay = delay # delays in messages
          self.attributes = attributes # attributes for formating
    
     async def get_conversation(self):
          userid = self.attributes['userid']

          if userid not in self.conversations.keys():
               self.conversations[userid] = ConversationTree(self.tree_root)
          return self.conversations[userid]
     
     async def handle_messages(self): 
           conversation = await self.get_conversation()
           user_reply = self.attributes['user_message']

           return conversation.get_answer(user_reply, self.attributes)
    
     async def send_messages(self):
            try:
                messages = await self.handle_messages()
                channel = self.attributes['channel']

                for message in messages:
                    await channel.send(message)
                    await sleep(self.delay)
            except Exception as e:
                 print(e)
        
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
            
            # Storing all esential attributes
            self.attributes['username'] = str(message.author).split('#')[0]
            self.attributes['user_message'] = message.content.lower()
            self.attributes['userid'] = str(message.author)
            self.attributes['channel'] = message.channel
            print(f"{self.attributes['username']}: {self.attributes['user_message']}")

            if message.author == self.client.user:
                return

            await self.send_messages()

        self.client.run(self.TOKEN)