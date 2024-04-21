import smtplib
import imaplib


class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        if not '@' in self.username:
            from_email = "{}@{}".format(self.username, self.host)
        else:
            from_email = self.username

        message = ("From: {0}\r\n"
                   "To: {1}\r\n"
                   "Subject: {2}\r\n\r\n{3}"
                   ).format(from_email, to_email, subject, message)
        smtp = smtplib.SMTP(self.host)
        smtp.login(self.username, self.password)
        smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login(bytes(self.username, 'utf-8'), bytes(self.password, 'utf-8'))
        mailbox.select()
        x, data = mailbox.search(None, 'ALL')
        messages = []
        for num in data[0].split():
            x, message = mailbox.fetch(num, '(RFC822)')
        messages.append(message[0][1])
        return messages


if __name__ == '__main__':
    facade = EmailFacade('localhost','ummiesmelimh05@gmail.com','112345')
    facade.send_email('ummiesmelimh05@gmail.com','text',"hello world")
    facade.get_inbox()
