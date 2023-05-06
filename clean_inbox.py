import datetime
from configuration import Configuration

config = Configuration()

config.login()

config.imap.select(mailbox="INBOX")

boxes = ["INBOX"]

day = 300
limit = 250

while day > limit:
    today = datetime.date.today() - datetime.timedelta(days=day)
    fdate = today.strftime("%d-%b-%Y")
    today = datetime.date.today() - datetime.timedelta(days=(day - 10))
    tdate = today.strftime("%d-%b-%Y")

    criteria = '(SINCE "{fromDate}" BEFORE "{toDate}" UNDELETED)'.format(
        fromDate=fdate, toDate=tdate
    )

    print("Searching...", criteria)

    for b in boxes:
        print("Processing ", b)

        typ, data = config.imap.select(mailbox=b, readonly=False)

        if typ == "OK":
            resp_code, results = config.imap.search(None, criteria)

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

    day -= 10
