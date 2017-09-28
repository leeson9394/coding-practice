import socket

pool = ['10.0.0.10', '10.0.0.20', '10.0.0.30', '10.0.0.40']
#assuming BE pool uses port 80, this local server listens on 1081

counter = -1

def rproxy():

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 1081))
    s.listen(1500)
    
    while 1 == 1:
        conn, addr = s.accept()
        print(addr)
        headers = ''
        while 1:
            buf = conn.recv(2048).decode('utf-8')
            headers += buf
            if len(buf) < 2048:
                break

        if counter == 3:
            counter = -1
        counter+=1

        host = pool[counter]
        headers = headers.replace('127.0.0.1:1081', host)\
                         .replace('keep-alive', 'close')\
                         .replace('gzip','')
        print(headers)
        s1 = socket.socket()
        s1.connect((host, 80))
        s1.sendall(headers.encode())

        resp = b''
        
        while 1:
            try:
                buf = s1.recv(2048)
            except socket.timeout as e:
                print(e)
                break

            resp += buf
            if not buf or\
                buf.startswith(b'WebSocket') and buf.endswith(b'\r\n\r\n'):
                break

        bytes_host = bytes(host, encoding='utf-8')

        resp = resp.replace(b'Content-Encoding: gzip\r\n', b'')\
                   .replace(bytes_host, b'localhost:1081')
        print('send to', addr)
        conn.sendall(resp)
        conn.close()


rproxy()

