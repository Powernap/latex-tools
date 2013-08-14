#Script to clean up a directory tree!
import os,subprocess

#browse the directory
for dirname, dirnames, filenames in os.walk('.'):
	for filename in filenames:
		#Check every file for:
		filepath = os.path.join(dirname, filename)
		#hidden file
		if filename.startswith('.'):
			print 'remove hidden file ' + filepath
			os.remove(filepath)
		#backup file
		elif filename.endswith('~'):
			print 'remove backup file ' + filepath
			os.remove(filepath)
		#log file
		elif filename.endswith('.log'):
			print 'remove log file ' + filepath
			os.remove(filepath)
		elif filename.endswith('.fls') or filename.endswith('.fls') or filename.endswith('.bbl') or filename.endswith('.blg') or filename.endswith('.pdf') or filename.endswith('.aux'):
			print 'remove log file ' + filepath
			os.remove(filepath)