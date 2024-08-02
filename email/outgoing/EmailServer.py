from smtpd import SMTPServer


class EmailServer(SMTPServer):
    none = 0
    ip = ""
    port = 0    # your port here
    remote_host = ""

