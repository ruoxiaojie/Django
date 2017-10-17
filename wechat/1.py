#!/usr/bin/python3.4
#--coding:utf-8--
import os
import tarfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


deallog_dir = "/space/build_deal_core/logs/deal-core/"
namelist = [
    "liujie",
    "yuepengyuan",
    "huangyahao"]
#deal-core.log

def Mail_send ():
    name_input = input("place input name: ")
    if name_input in namelist:
        sender = 'service@xmjr.com'
        mailto = '{0}@xmjr.com'.format(name_input)
    else:
        print("the {0} os wrong.".format(name_input))
        name_input = input("place input name, once again: ")

    msg = MIMEMultipart()
    att1 = MIMEText(open('/space/build_deal_core/logs/deal-core/deal-core.log.tar.gz', 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename=deal-core.log.tar.gz'
    msg.attach(att1)

    msg['to'] = mailto
    msg['from'] = sender
    msg['subject'] = 'deal_core日志'

    try:
        server = smtplib.SMTP()
        server.connect('smtp.exmail.qq.com')
        server.login("service@xmjr.com","9Z4Io3EFEcaI4HHT")
        server.sendmail(sender,mailto,msg.as_string())
        server.quit()
        print ('发送成功')
    except Exception as e:
        print(str(e))


os.chdir(deallog_dir)
log_name = "deal-core.log"
tar_log = tarfile.open("deal-core.log.tar.gz","w:gz")
tar_log.add(log_name)
tar_log.close()
Mail_send()
print('send mail successfully')





