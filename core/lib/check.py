'''
/core/lib/check.py
By @python3lover (GitHub and GitLab)
'''
from hashlib import sha512
class check():
  def __init__(self,path):
    self.path = path
    self.file = None
    self.oldhash = None
  def check(self):
    self.file = open(self.path,'r')
    if hashlib.sha512(self.file.read()).hexdigest() != self.oldhash:
      self.file.close()
      return True
    else:
      self.file.close()
      return False
