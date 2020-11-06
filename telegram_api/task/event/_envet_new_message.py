# checks whether there's a 'joinchat' in the msg text?
@client.on(events.NewMessage(outgoing=False, pattern=r'(?i).*joinchat/'))
async def my_event_handler(event):
    # extracts the hash of that link
    hash = re.search('(?<=joinchat\/)(\w+[-]?\S\w+)', event.raw_text).group(0)
    checked = await client(CheckChatInviteRequest(hash=hash))
    if checked.megagroup and checked.broadcast == False:
        updates = await client(ImportChatInviteRequest(hash))

client.start()
client.run_until_disconnected()