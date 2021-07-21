from time import sleep
import requests
class General:
  def printt(string, speed):
    if speed <= 50:
      delay = 100 - speed
      delay = delay / 100
      print(delay)
    else:
      raise ValueError(f"maximum speed is 50, you put {speed}, which resulted in a delay of {(100 - speed) / 100}s")
    for i in str(string):
      print(i, end="", flush = True)
      sleep(delay)
    print('')
  class Math:
    square = lambda x: x**2
    cube = lambda x: x**3
  Maths = Math
class Hastebin:
  def __init__(self, text):
    '''eg.
    data = Hastebin(input("Whats your name? "))
    print(f'Hello {data.text}!')
    debug = False
    if debug:
      print(data.data)
    print(data.url)'''
    self.text = str(text)
    self.data = requests.post("https://hastebin.com/documents", data=self.text)
    if self.data.text.startswith('<!DOCTYPE html>'):
      print('hastebin API is currently down')
    self.url = "https://hastebin.com/" + self.data.json()["key"]
class Fun:
  class Character:
    def __init__(self,name: str, script: list):
      self.chrname = name
      self.curline = 0
      self.lines = script
    def nextline(self):
      '''Go to next line'''
      self.curline += 1
    def getline(self):
      '''Return current line'''
      return f'{self.chrname}:{self.lines[self.curline]}'
    def sendnext(self):
      '''Does both getline() and nextline()'''
      line = getline(self)
      nextline(self)
      return line
    