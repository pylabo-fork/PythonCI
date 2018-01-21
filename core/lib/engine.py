'''
/core/lib/engine.py
By @python3lover (GitHub and GitLab)
'''
from check import *
from subprocess import Popen, STDOUT, STDERR
from time import wait
class engine():
  def __init__(self,configpath,outputpath,delay=10000):
    self.configpath = configpath
    self.outputpath = outputpath
    self.quit = False
    self.check = check(path)
    self.delay = delay/1000
  def engine(self):
    print('PythonCI')
    while not self.quit:
      if self.check.check():
        stdout,stderr = Popen(self.command,stdout=STDOUT,stderr=STDERR).communicate()
<<<<<<< HEAD
<<<<<<< HEAD
      wait(self.delay)
=======
      wait(self.delay)
>>>>>>> 0104f07452b45f511b5ac6c49f9c0cdeee6dc592
=======
      wait(self.delay)
>>>>>>> 0104f07452b45f511b5ac6c49f9c0cdeee6dc592
