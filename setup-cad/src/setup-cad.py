#!/usr/bin/python
"""
   This python script allows you to open the Cadence Virtuoso directly without having to type in setup commands everytime you login

   To Get the latest version of this script:
    Open the terminal window, enter command:
    wget -P ~/Desktop http://www.people.virginia.edu/~hz9xa/setup-cad.py
    The file should be downloaded to your desktop
    
   To Execute in terminal: 
    1.Open terminal
    2.Change to the directory where your 'setup-cad.py' file is located. Eg. 'cd ~/Desktop' if the file is on your desktop
    3.Type in 'python setup-cad.py' in command line. This will open the Cadence for you.
   
   To Execute using double click: 
    1.Open terminal
    2.Change to the directory where your 'setup-cad.py' file is located. Eg. 'cd ~/Desktop' if the file is on your desktop
        3.Type in 'chmod 755 setup-cad.py'
    4.Double click the file, and click 'Run in Terminal'.This will open the Cadence for you.    
        5.NOTE: You only need to do steps 1-3 once:)

   To Exit:  Save all your work, close Candence windows

   @Author Hang (Eric) Zhang
       PhD student, Computer Engineering
   @Email hz9xa@virginia.edu
   
   Please email me if you have any questions.

"""

import os,subprocess
home = os.path.expanduser('~')
cadencedir= home + '/cadence'
os.chdir(cadencedir)
print('Changed directory')
os.system('. cadence-mmsim')
print('cadence-mmsim executed')
print('To exit, press "Ctrl+C"')

r,w = os.pipe()

pid = os.fork()
if pid: #parent
    os.write(w,'source %s/setup-cadence\n' % cadencedir)
    os.write(w,'virtuoso &\n')
    os.write(w,'exit\n')
    os.wait()
else:    #child
    subprocess.call('tcsh -s', stdin=r,shell=True)