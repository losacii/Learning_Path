# -*- coding: UTF-8 -*-
import smtplib  
from email.mime.text import MIMEText

mail_host="smtp.163.com"  #设置服务器
mail_user="losacii"       #发件人
senderNameSet = "LosaHere"
mail_postfix="163.com"    #发件箱后缀名
mail_pass="XXXXXXXXX"      #口令 

to_list = ["1423089007@qq.com"] #收件人
  
def send_mail(to_list,sub,content):
    
    mailSender="%s<%s@%s>" %(senderNameSet, mail_user, mail_postfix) # 发件箱格式化字符串
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')      # MIMText对象设置
    msg['Subject'] = sub  
    msg['From'] = mailSender
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()                 # server 定义登录
        server.connect(mail_host)  
        server.login(mail_user, mail_pass)      
        server.sendmail(mailSender, to_list, msg.as_string())  # 发送
        server.close()                                         # 关闭
        return True
    except Exception, e:
        print str(e)  
        return False

if __name__ == '__main__':  
    print "Sending mail..."
    if send_mail(to_list, "Subject Here!", "Ok!\nHello world！ \nthis is just a testing message!"):
        print "发送成功!"
    else:  
        print "发送失败!"
