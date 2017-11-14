import copy

sessions = []
availableTimes = [['09:00','12:00'],['13:00','17:00']]
lunch = "12:00 Lunch"
networking_gap = 60
time = lambda t: int(filter(str.isdigit, t) or 5)

def parseInputs(fPath): # reading the inputs file
	file = open(fPath,'r')
	for line in file.readlines():
		sessions.append(line.rstrip().rsplit(' ',1)+[0])
	file.close()

def calSessionTime(): # get total time of talks
	total = 0
	for x in sessions:
		total = total + time(x[1])
	return total

def calAvailableTime(): # get total time available per session and sum of session times
	at = []
	atm = []
	for x in availableTimes:
		tmp =[int(a) - int(b) for a, b in zip(x[1].split(':'), x[0].split(':'))]
		atm.append((tmp[0]*60)+tmp[1])
	return atm,sum(atm)

def getMyCeil(s,a): # get ceiling value for the given values s/a 
	t = float(s)/a
	T = int(t)
	if(t-T > 0):
		return T+1
	else:
		return T

def getMyFloor(s,a): # get floor value for the given value s/a
	t = float(s)/a
	return int(t)
	

def getNetworkingSchedule(tracks, tat, ng, tst): # get Timing for networking event
	if ((((tracks*tat)-(ng*tracks))-tst)>0):
		tat = tat - ng;
		n = availableTimes[len(availableTimes)-1][-1].split(':')
		hrs_gap = getMyCeil(ng,60)
		min_gap = ng%60
		n[0] = str(int(n[0])-hrs_gap)
		n[1] = str(int(n[1])-min_gap)
		if(int(n[0])<10): n[0] = '0'+n[0]
		if(int(n[1])<10): n[1] = '0'+n[1]
		net = ':'.join(n)
	else:
		net = availableTimes[len(availableTimes)-1][-1]
	net = net+" Networking Event"
	return net

def getSortedSesssions(): # sort sessions in decreasing order of their timing
	return sorted(sessions, key = lambda s: time(s[1]), reverse=True )

def generateSchedules(sess): # form a list of schedules under session timings
	scheds = []
	for t in xrange(tracks):
		scheds.append([])

	for at in xrange(len(availableTimesMins)):
		for t in xrange(tracks):
			remTime = copy.deepcopy(availableTimesMins[at])
			scheds[t].append([])
			for s in xrange(len(sess)):
				if(time(sess[s][1]) <= remTime and sess[s][2] == 0):
					scheds[t][at].append(sess[s])
					sess[s][2] = 1
					remTime = remTime - time(sess[s][1])
	return scheds

def calSchedTiming(hrs,sess_time): # get Talk Time in 24 hour clock format

	t = hrs.split(':')
	hrs_gap = getMyFloor(sess_time,60)
	min_gap = sess_time%60
	t[0] = int(t[0])+hrs_gap
	t[1] = int(t[1])+min_gap
	if(t[1]>=60):
		t[0] = t[0]+1
		t[1] = t[1]%60
	if( t[0]<10):
		t[0] = '0'+str(t[0])
	else:
		t[0] = str(t[0])
	if( t[1]<10):
		t[1] = '0'+str(t[1])
	else:
		t[1] = str(t[1])

	next_timing = ':'.join(t)

	return hrs,next_timing

def printSchedule(scheds,lunch,networking): # print schedule for conference talks
	for t in xrange(tracks):
		print "Track",t+1,":"
		for at in xrange(len(availableTimes)):
			# print availableTimes[at]
			timing = availableTimes[at][0]
			for session in scheds[t][at]:
				session_time = calSchedTiming(timing,time(session[1]))
				timing = session_time[1]
				print session_time[0],session[0] 
			if(at==0):
				print lunch
			elif(at==len(availableTimes)-1):
				print networking,"\n"



if __name__ == "__main__":
	parseInputs('input.txt')
	totalSessionTime = calSessionTime()
	availableTimesMins,totalAvailableTime = calAvailableTime()
	tracks =  getMyCeil(totalSessionTime,totalAvailableTime)
	networking = getNetworkingSchedule(tracks, totalAvailableTime, networking_gap, totalSessionTime)
	sessions_decr = getSortedSesssions()
	schedules = generateSchedules(sessions_decr)
	printSchedule(schedules,lunch,networking)













