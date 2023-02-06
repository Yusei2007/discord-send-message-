import requests

token="" #ここにtoken
payload={
    'content': f"hello"#ここに送りたいメッセージ
}
header={
    'authorization':f"{token}"
}
channel=""#送りたいチャンネルのID

sendmessage = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages",data=payload,headers=header)

