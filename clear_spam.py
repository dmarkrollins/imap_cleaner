import datetime
from configuration import Configuration

config = Configuration()

config.login()

b = "INBOX.spam"

config.imap.select(mailbox=b)

typ, data = config.imap.select(mailbox=b, readonly=False)

if typ == "OK":
    resp_code, results = config.imap.search(None, "ALL")

    print(resp_code)

    mail_ids = results[0].decode().split()
    print(
        "Total Mail IDs in scope for {box}: {count}\n".format(
            box=b, count=len(mail_ids)
        )
    )
    i = 0
    for id in mail_ids:
        i += 1
        print("Deleting from {box} - {idx}".format(idx=i, box=b), end="\r")
        resp_code, response = config.imap.store(id, "+FLAGS", "\\Deleted")
        # print(resp_code)

    try:
        resp_code, data = config.imap.expunge()  # delete each item
    except Exception as e:
        print(e.args[0])
    finally:
        print("\n\nExpunge code", resp_code)
