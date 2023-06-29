import SC

with SC.Socket("192.168.1.8",8000) as client:
    client.Client()
    a = 0
    while True:
        a = a + 1
        print(client.CData(str(a)))