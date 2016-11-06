import imapclient
import pyzmail
import webbrowser
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('yourmail@gmail.com ', 'applicationspecificpassword')
while True:
 imapObj.select_folder('INBOX', readonly=False)
 UID = imapObj.search(['FROM secondmail@gmail.com'])
 if len(UID) != 0:
    webbrowser.open('https://www.youtube.com/watch?v=9f06QZCVUHg')
    imapObj.delete_messages(UID)
    imapObj.expunge()
 
  
  
  
 
 
