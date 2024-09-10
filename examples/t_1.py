import asyncio
import json
import websockets

# 定义发送消息的数据
d2 = {
    "sender": "cwb",
    "type": "message",
    "content": "你好 灰喵",
    "time": "2024-8-5-17-17",
}

async def receive_messages(websocket):
    """接收并处理服务器消息"""
    while True:
        try:
            response = await websocket.recv()
            response = json.loads(response)

            print(f"\n{response['sender']}:{response['content']}")


        except websockets.ConnectionClosed:
            print("Connection with server closed")
            break

async def send_messages(websocket):
    """处理用户输入并发送消息到服务器"""
    while True:
        user_input = await asyncio.to_thread(input, "You: ")
        message = {
            "sender": "cwb",
            "type": "message",
            "content": user_input,
            "time": "2024-8-5-17-17",  # 可以根据需要动态生成时间
        }
        await websocket.send(json.dumps(message))

async def client():
    p_ad = "ws://106.53.104.224:2048"
    s_ad = "ws://127.0.0.1:2048"
    uri = p_ad
    headers = {
        "X-Auth-Key": "caixukun66"  # 连接密钥
    }

    async with websockets.connect(uri, extra_headers=headers) as websocket:
        # 启动接收消息的任务
        receive_task = asyncio.create_task(receive_messages(websocket))
        # 启动发送消息的任务
        send_task = asyncio.create_task(send_messages(websocket))

        # 等待任务完成
        await asyncio.gather(receive_task, send_task)

if __name__ == "__main__":
    asyncio.run(client())