import random

pid_keys = {}
pid_peers = {}

def add_pid(pid):
	if pid not in pid_keys:
		pid_keys[pid] = True
	else:
		print pid + " key already exists. Cannot re add this user ID"

def remove_pid(pid):
	if pid in pid_keys:
		del pid_keys[pid]
	else:
		print "Key " + pid + " cannot be deleted as it does not exist!"

def update_peer(pid_1, pid_2):
	if pid_1 not in pid_peers and pid_2 not in pid_peers:
		pid_1[pid1] = pid_2
	elif pid_1 not in pid_peers and pid_2 in pid_peers:
		print "Cannot pair peers " + pid_1 + " & " + pid_2 + " as " + pid_2 + " already has a pair"
	elif pid_2 not in pid_peers and pid_1 in pid_peer:
		print "Cannot paid peers " + pid_2 + " & " + pid_1 + " as " + pid_1 + " already has a pair"
	else pid

def remove_peer(pid_1, pid_2):
	if pid_1 not in pid_peers and pid_2 in peers:
		if pid_peers[pid_2] == pid_1:
			del pid_peers[pid_2]
		else:
			print "Invalid key pair delete"
	elif pid_2 not in pid_peers and pid_1 in peers:
		if pid_peers[pid_1] == pid_2:
			del pid_peer[pid_1]
		else:
			print "Invalid key paid delete"
	else:
		print "Why delete? These peers are not peered"
