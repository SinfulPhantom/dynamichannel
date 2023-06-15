import voltage
from voltage.ext import commands


class DynamiClient(commands.CommandsClient):
    async def on_ready(self):
        await self.set_status(text="Ready to serve", presence=voltage.PresenceType.online)
        print(f"Client started...")
