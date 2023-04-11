import discord
import sys
sys.path.append('/home/pi/HowLoudIsSilence/synthMidi')
sys.path.append('/home/pi/HowLoudIsSilence/synthSeq')
import midiControl

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return        

    if message.content.startswith('!send'):
        #split the message into a list
        messageList = message.content.split()
        #check if the message is the correct length
        if len(messageList) != 4:
            await message.channel.send("Invalid command! Please use the format !send <octave> <note> <length>")
            return
        await message.channel.send(midiControl.sendNote(int(messageList[1]),messageList[2], int(messageList[3]), 1))

    if message.content.startswith('!cv'):
        #split the message into a list
        messageList = message.content.split()
        #check if the message is the correct length
        if len(messageList) != 4:
            await message.channel.send("Invalid command! Please use the format !cv <control output [0 or 1]> <static/ramp_up/ramp_down> <length>")
            return
        await message.channel.send(midiControl.sendNote(int(messageList[1]),messageList[2], int(messageList[3]), 1))


#sendNote(octave,note,delay, channel)

client.run('MTA5Mzk5MDY0MDQxMDQ0MzgxNw.GcrpId.V97EbOaxrAFCDrxIbWdV_o035cOssXgRJVFUeA')