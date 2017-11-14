Conference Scheduler

Assumptions:

	1) Timings are mentioned in 24 hour clock format.
	2) No. of tracks are calculated dynamically depending on the number of proposals for conference.
	3) Lightning sessions are taken for 5 min.
	4) Presenters will be very punctual and there is no gap between sessions.


Constants:
 
	1) Conference session timings are from 9:00 - 12:00 and 13:00 - 17:00
	2) Lunch is at 12:00
	3) Networking may be started 60 min earlier (i.e. at 16:00). 


Input File:
 
	1) input.txt (in the same folder where program file is).
	2) Each line is composed of Talk Title followed by Talk Time in minutes at the end.
	3) Talk Title should not have any numbers except for the Talk Time.


Output:
 
	1) Conference talks are scheduled under multiple tracks.
	2) Each line under respective track mentions talk time followed by talk title.


Implementation:

	1) Language: Python
	2) CLI: python conference_scheduler.py
	3) Input: File Reading
	4) Output: STDOUT