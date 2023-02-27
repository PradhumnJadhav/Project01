import pyttsx3
engine=pyttsx3.init("sapi5")
voice=engine.getProperty('voices')
engine.setProperty('voices' , voice[0].id)
 
class greet():
 def __init__(self,name,gender):
      self.name=name
      self.gender=gender
       
 def say(self):
    if self.gender in ['male','Male'] :
        engine.say('hello mister ' + self.name) 
        engine.runAndWait()
        
    if self.gender in ['female','Female'] :
        engine.say('hello madam ' + self.name)     
        engine.runAndWait()
name=input("enter Your Name :")
gender=input("Enter Your Gender: ")
I=greet(name,gender)

I.say()