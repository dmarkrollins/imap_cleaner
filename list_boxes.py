import imaplib

from configuration import Configuration

config = Configuration()

config.login()

list = config.imap.list()

for l in list:
    if l != "OK":
        for b in l:
            print(b.decode())
