import imaplib
from  imapclient import IMAPClient

email= "divyanshi1001@gmail.com"
password = "mpvv nyst ipsm bzcy"

imap_server = "imap.gmail.com"
imap_port = 993
with IMAPClient(imap_server,port=imap_port) as client:
    client.login(email,password)
    print ("client=>",client)
    
    client.select_folder("INBOX")
    
    msg = client.search(['SUBJECT','hello'])
    
    for uid, msg_data in client.fetch(msg,['ENVELOPE','BODY[TEXT]']).items():    
     enelope = msg_data[b'ENVELOPE']
     print(enelope)
     body = msg_data[b'BODY[TEXT]']
     breakpoint()
     print(f"From:{enelope.from_[0].name}<{enelope.from_[0].address}>")
     print(f"To:{enelope.to[0].name}<{enelope.to[0].address}")
     print(f"Subject:{enelope.subject}")
     print(f"Content: {body.decode('utf-8')}")
     print("receive mail successfull!")