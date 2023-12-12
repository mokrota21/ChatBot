from typing import Any
from ConversationTree import ConversationTree
from asyncio import sleep

class UniBot:
    def __init__(self, delay: float, conversation: ConversationTree, TOKEN: str, client) -> None:
        
        # keep track of conversation
        self.conversation = conversation

        # required variables
        self.TOKEN: str = TOKEN
        self.client = client

        # delay between messages
        self.delay = delay

        # starting bot
        self.run_bot()
    

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