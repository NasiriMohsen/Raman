import SC

with SC.Socket("192.168.1.8",8000) as server:
    server.Server()
    with server.conn:
        while True:
            data = server.SData(server.conn)
            if data != b'':
                print(data)