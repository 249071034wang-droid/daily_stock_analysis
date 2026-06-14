import requests
import json

APP_ID = "cli_aaa7dc7b4878dbd6"
APP_SECRET = "v74btPQlsRsuFWFhx9mJZbq7NpAahXZS"

print("正在获取 tenant_access_token ...")
resp = requests.post(
    "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
    json={"app_id": APP_ID, "app_secret": APP_SECRET}
)
data = resp.json()
if data.get("code") != 0:
    print("获取 token 失败：", data)
    exit(1)
token = data["tenant_access_token"]
print("token 获取成功\n")

print("正在获取群列表 ...")
resp2 = requests.get(
    "https://open.feishu.cn/open-apis/im/v1/chats",
    headers={"Authorization": f"Bearer {token}"},
    params={"page_size": 20}
)
result = resp2.json()
print(json.dumps(result, ensure_ascii=False, indent=2))

if result.get("code") == 0:
    chats = result.get("data", {}).get("items", [])
    if chats:
        print("\n=== 找到以下群聊 ===")
        for c in chats:
            print(f"群名：{c.get('name')}  |  chat_id：{c.get('chat_id')}")
    else:
        print("\n未找到群聊，请先把机器人拉进群，然后再运行此脚本")
else:
    print("\n获取群列表失败：", result)
    print("错误码：", result.get("code"), result.get("msg"))
