# -*- coding: utf-8 -*-
#如果需要在linux系统下执行，请在首行指定要使用的python解释器命令路径
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from Tkinter import *
import tkMessageBox
import smtplib
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))
def send_mail():		
	from_addr = f.tf.get('0.0',END)[:-1]
	password = f.tf2.get('0.0',END)[:-1]
	to_addr = f.tf3.get('0.0',END)[:-1]
	smtp_server = f.tf4.get('0.0',END)[:-1].strip()
	if smtp_server == "":
		smtp_server='smtp.'+from_addr.split("@")[1]
	msg = MIMEText(f.tf6.get('0.0',END)[:-1], 'plain', 'utf-8')
	msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
	msg['To'] = _format_addr(u'admin <%s>' % to_addr)
	msg['Subject'] = Header(f.tf5.get('0.0',END)[:-1], 'utf-8').encode()
	accpet=tkMessageBox.askyesno(u'请确认以下项目后点OK发送',u'我的邮箱地址: %s,收件人邮箱地址:%s,SMTP主机地址: %s' % (from_addr,to_addr,smtp_server))
	if accpet:
		send_mail_agent()
def send_mail_agent():
	server = smtplib.SMTP(smtp_server, 25)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()	
f=Frame()
f.button=Button(text="发送",command=send_mail)

f.lb=Label(text="你的邮箱地址: ")
f.lb2=Label(text="密码: ")
f.lb3=Label(text="收件人邮箱地址: ")
f.lb4=Label(text="SMTP主机地址(可留空): ")
f.lb5=Label(text="主题: ")
f.lb6=Label(text="内容: ")
f.tf=Text(height=1)
f.tf2=Text(height=1)
f.tf3=Text(height=1)
f.tf4=Text(height=1)
f.tf5=Text(height=1)
f.tf6=Text(height=6)
f.lb.pack()
f.tf.pack()
f.lb2.pack()
f.tf2.pack()
f.lb3.pack()
f.tf3.pack()
f.lb4.pack()
f.tf4.pack()
f.lb5.pack()
f.tf5.pack()
f.lb6.pack()
f.tf6.pack()
f.button.pack()

f.mainloop()
