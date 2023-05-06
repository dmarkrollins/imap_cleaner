import imaplib
import imap_tools
import dotenv
import os
import datetime

dotenv.load_dotenv()


class Configuration:
    def __init__(self):
        self.host = os.getenv("IMAP_SERVER")
        self.user = os.getenv("EMAIL_USER")
        self.password = os.getenv("EMAIL_PASSWORD")

    def login(self):
        print("Connecting...")
        self.imap = imaplib.IMAP4_SSL(host=self.host, port=993, timeout=10000)
        return self.imap.login(self.user, self.password)

    def __del__(self):
        if hasattr(self, "imap"):
            print("Cleaning up...")
            try:
                if self.imap.state == "SELECTED":
                    print("Closing and cleaning up deleted")
                    self.imap.close()
            except Exception as e:
                print(e.args[0])
