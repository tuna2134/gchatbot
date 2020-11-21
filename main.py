import discord
import json

# 読み込み
with open("data.json", mode="r") as f:
    data = json.load(f)

client = discord.Client()

@client.event
async def on_ready():
    print("ログイン完了")

@client.event
async def on_message(message):
# もし文字の最初がt!gc add なら
 if message.content.startswith("t!gc add "):
    # 名前をt!gc add を消して取り出す
    name = message.content.replace("t!gc add ","")
    # gcの中にグロチャと言う名前でこのコマンド実行ﾁｬﾝﾈﾙIDが入ったリストを入れる
    data["gc"][name] = [message.channel.id]
    # データ書き込み
    with open("data.json", mode="r") as f:
        json.dump(data,f,indent=4)
    await message.channel.send("作成")


client.run("NzY4MDEwOTY3NjM5NTIzMzI5.X46P8w.2eh_sOWinFKjwBR_2q_kvZTpDDs")
