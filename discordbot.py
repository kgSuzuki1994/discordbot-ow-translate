import discord
import settings
import message

TOKEN = settings.AP

client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# 返信する非同期関数を定義
async def reply(ms):
    reply = f'{ms.author.mention} {message.transName(ms.clean_content)}'
    await ms.channel.send(reply)

# メッセージ受領時の動作
@client.event
async def on_message(ms):

    # メッセージ送信者がbotだった場合は無視する
    if ms.author.bot:
        return

    # 話しかけられたかの判定
    if client.user in ms.mentions:
        await reply(ms)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

