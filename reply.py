import socket
import asyncio

SERVER_IP = ""
SERVER_PORT = 5005

clients = set()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))
sock.setblocking(False)

async def relay():
    loop = asyncio.get_event_loop()
    while True:
        try:
            data, addr = await loop.sock_recvfrom(sock, 4096)
            clients.add(addr)
            for c in clients:
                if c != addr:
                    sock.sendto(data, c)
        except:
            await asyncio.sleep(0.001)

asyncio.run(relay())