'''
/core/lib/engine.py
By @python3lover (GitHub and GitLab)
'''
from check import *
class engine():
  def __init__(self,configpath,path,command):
    self.configpath = configpath
    self.path = path
    self.command = command
    self.quit = False
  def engine(self):
    print('PythonCI')
    while not self.quit:
      