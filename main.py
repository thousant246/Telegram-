from telethon import TelegramClient, events
import os
from keep_alive import keep_alive

# ✅ Get your API credentials from environment variables
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

# ✅ List of source channel usernames
source_channels = ['@loot2', '@genuineworkgroup']

# ✅ Target channel username
target_channel = '@earnbyhustler'

# ✅ Initialize Telegram client session
client = TelegramClient('forward_session', api_id, api_hash)

# ✅ Event handler for new messages in any of the source channels
@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    # ❌ Skip voice or audio messages
    if event.message.voice or event.message.audio:
        return
    # ✅ Forward message to target channel
    await client.send_message(target_channel, event.message)

# ✅ Start and keep the bot alive
print("🤖 Bot is running... Waiting for messages.")
client.start()
keep_alive()
client.run_until_disconnected()