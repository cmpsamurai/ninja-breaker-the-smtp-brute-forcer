#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SMTPConnection.py
#  
#  Copyright 2013 Moustafa <Moustafa@LAPTOP>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from smtplib import SMTP,SMTPAuthenticationError,SMTPConnectError
import datetime
debuglevel = 0
import traceback
import socket
socket.setdefaulttimeout(1800)

class SMTPConnection:
	''' 
	Class that Handles Connection to a SMTP server and tests Username/Password on it , it is initialized with the Server and Port,
	:param server : Server to connect to
	:param port   : Port to connect to usually 537
	'''
	def __init__(self,server,port):
		self.server=server
		self.port=port
		self.smtp = SMTP()
		
	def isConnected(self):
		''' 
		Checks that we are still connected ( The served didnt kick us out )
		'''
		try:
			status = self.smtp.docmd('NOOP')[0]
		except:  # smtplib.SMTPServerDisconnected
			status = -1
		return True if status == 250 else False
	
	def Connect(self):
		'''
		Connect to The Server / Reconnect
		'''
		self.smtp = SMTP()
		self.conn=self.smtp.connect(self.server, self.port)	
		self.smtp.starttls()
		
	def Test_Credentials(self,user,password):
		''' 
		The main Function, Takes username ,password , and tries to log them in the currennt connectopm
		:param user : the username (email)
		:param password : the password 
		returns True if password is correct / False if not 
		'''
		done=False
		while 1:
			try:
				if not self.isConnected():
					self.Connect()
				self.smtp.login(user, password)
				self.smtp.close()
				return True
			except SMTPAuthenticationError: 
				return False
			except:
				continue

	def Check_Server(self,server,port):
		try:
			_smtp=SMTP()
			_smtp.connect(self.server, self.port)	
			return True
		except:
			return False
			

def main():
	
	return 0

if __name__ == '__main__':
	main()

