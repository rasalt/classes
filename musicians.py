#!/usr/bin/python

class Musician(object):
  def __init__(self, sounds):
    self.sounds = sounds
  def solo(self, length):
     for i in range(length):
          print self.sounds[i % len(self.sounds)]
      
class Bassist(Musician):
  def __init__(self):
    super(Bassist,self).__init__(["Twang","Thumb","Blong"])
    
    
class Guitarist(Musician):
   def __init__(self):
      super(Guitarist, self).__init__(["Boing","Bow","Boom"])
   def tune(self):
      print "Be with you .. I am tuning "
      
class Drummer(Musician):
  def __init__(self):
    super(Drummer, self).__init__(["Dhish"," Dhash","Dhoom"])
  def combust(self):
    print "I am spontaneously combusting"

class Band(object):
  def __init__(self):
    self.musicianlist =  []
  def hire(self, musician):
    self.musicianlist.append(musician)
  def fire(self, musician):
    self.musicianlist.remove(musician)
  def display(self):
    print "Musician list is {}".format(len(self.musicianlist))
    
    
if __name__ == "__main__":
  
  nigel = Guitarist()
  mike = Drummer()
  eric = Bassist()
  myband = Band()
  
  mike.solo(4)
  eric.solo(3)
  nigel.solo(6)

  print "Hiring 3 musicians "
  
  myband.hire(nigel)
  myband.hire(mike)
  myband.hire(eric)
  myband.display() 
  
  print "Now firing 2 musicians "
  myband.fire(nigel) 
  myband.fire(mike)
  myband.display() 
  
  