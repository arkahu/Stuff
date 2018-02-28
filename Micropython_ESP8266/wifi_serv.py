"""
ESP8266 code for running a webserver on the MCU. Data input from the form is
displayed in a TFT.
"""

import socket, text2display

def inputHandler(message):
    text2display.reset()
    text2display.drawtext(str(message), scaling = 3)


def simpleserver():


    html = """<!DOCTYPE html>
    <html>
        <head> <title>ESP8266</title> </head>
        <body> <h1>ESP8266</h1>
               <form>
               Enter input:<br>
               <input type="text" name="myinput"><br><br>
               <input type="submit" value="Submit">

               </form> 
            
        </body>
    </html>
    """

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            #print (line)
            if line[:37] == b'Referer: http://192.168.4.1/?myinput=':
                #print('refererri found')
                #print(line[37:])
                inputHandler(line[37:-2])
            if not line or line == b'\r\n':
                break
        response = html 
        cl.send(response)
        cl.close()

