
# coding: utf-8

# In[1]:


#Import necessary modules
import random
from copy import copy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd  


# In[2]:


#Define the individual class.

#not sure if the list of different phenotypes should be used for individual or population 
#project says each population should have inidividuals with same phenotype 
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

class individual:
    # Add a docstring     
    def __init__(self,id ="1", x= "0",y= "0",colorNumber = 0): # Add default values and color phenotype.
        # Add a docstring
        self.id = id
        self.x = x
        self.y = y
        self.colorNumber = colors[colorNumber]


# In[3]:


#Define the population class.

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

class population:
  #add docstring
  def __init__(self,id ="1",popSize = 20 ,colorNumber = 0): # Add default values and starting population size.
        # Add a docstring
        '''Function to create individuals and apply color'''
        self.id = id
        self.popSize = popSize
        self.colorNumber = colors[colorNumber]
        self.pop=[] #create list of individuals

        for i in range(popSize):
          #this will assign the population color to the individual color
          if(i == 0):
            newInd = individual(colorNumber = colorNumber) 
          else:
            newInd = individual(id = i +1, colorNumber = colorNumber)  
          self.pop.append(newInd) #or can i just call addInd function? 



  def addInd(self,newInd):
      self.pop.append(newInd)
  def removeInd(self,newInd):
      self.pop.remove(newInd)

#calculate and print the frequency of phenotypes among individuals.
#Python program to count the frequency of  
#individuals in a list using a dictionary 
  
  def phenotypeFreq(self): #newPop or population. or self?
    #Add doc string

    #need to create a list to be _list that stores all the individual's colors 

    # Creating an empty dictionary  
    freq = {} 
    for newInd in self.pop: 
        if newInd.colorNumber not in freq: #if color not already in dictionary add it with a count of 1 
          freq.update({newInd.colorNumber:1})
        elif newInd.colorNumber in freq: 
          freq[newInd.colorNumber] += 1 #increase number due to color occuring more than once 
  
    for k, v in freq.items(): 
        print ("% s : % d"%(k, v)) 

    #need to take the values for all the keys and divide by the total number of individuals 
    #value / len(newPop.list)
    for i in freq.keys():
        phenFreq = freq[i] / len(self.pop)
        print("Phenotype Color %s has a frequency of %f" % (i,phenFreq))


# In[4]:


#Define the landscape class.
class landscape:
  #add dosctring
  def __init__(self,landscapeSize=3,dispersalMatrix = None): #Add default values.
    # Add a docstring
    '''Function to apply probablity of movement between populations'''
    self.landscapeSize = landscapeSize
    self.land=[] #create list of populations
    self.dispersalMatrix = [[0.5,0.5,0.5],[0.5,0.5,0.5],
                           [0.5,0.5,0.5]]

    for i in range(landscapeSize): #for every population in the landscape
        #create a a population object that will pick the color phenotype from the colors list
        #when i has already used white, it will restart to red for the next population to be created 
      if i == 0:
          newPop = population(colorNumber = i % len(colors)) 
      else:
          newPop = population(id = i + 1, colorNumber = i % len(colors))  
        
      self.land.append(newPop)  #add the population just created into the landscape list with the populations
    
  def move(self):
      for i in range(len(self.land)):
          indRemoval = []
          newPop = None
          for ind in self.land[i].pop:
              newPop = random.choices(self.land, weights = self.dispersalMatrix[i])[0]
          if newPop != self.land[i]:
              indRemoval.append(ind)
          
          for ind in indRemoval:
              self.land[i].removeInd(ind)
              newPop.addInd(ind)


# In[5]:


#test code here 
#class phenotypeFreq:
 # myLandscape = landscape()
  #myLandscape.move()
 # def phenotypeFreq(self):
   # for i in myLandscape.land:
    # phenotypeFreq(myLandscape.land[i])
    #random.shuffle(phenotypeFreq)

myLandscape = landscape()
for i in range(100):
  myLandscape.move()

for populationObj in myLandscape.land:
    populationObj.phenotypeFreq()


# In[25]:


#Code to create plots of phenotype frequencies that shows three different lines
#for six different populations.

Red = []
Orange= []
Yellow =[]
Green = []
Blue = []
Purple = []
Time=100 
def newPop(): # Add necessary arguments
        # Add a docstring
        '''Function to plot population frequencies over time for six populations'''
        for i in range(Time):
          for i in land():
            i.move()
        plt.xlabel('Time') #creating x axis label
        plt.ylabel('Phenotype Frequencies within that Population') #creating y axis label where it 
        plt.xticks(rotation=90)
        plt.grid(True) #adding a grid
        #Plotting 6 lines.
        line1=plt.plot('time', 'Red', data=Red, color = 'r')
        line2=plt.plot('time', 'Orange', data=Orange, color = 'o')
        line3=plt.plot('time', 'Yellow', data=Yellow, color = 'y')
        line4=plt.plot('time', 'Green', data=Green, color = 'g')
        line5=plt.plot('time', 'Blue', data=Blue, color = 'b')
        line6=plt.plot('time', 'Purple', data=Purple, color = 'p')
        plt.set_xlim([0, gens]); plt.set_ylim([0, pop_size])
        plt.show()


# In[26]:


newPop()


# In[7]:


#Code to create plots of population sizes that shows three different lines
#for six different populations.

Red = []
Orange = []
Yellow = []
Green = []
Blue = []
Purple = []
Time = 100

def draw(self): #add arguments
  #add docstring
  '''Function to plot population sizes for three different populations'''
  for i in self.individ: #loop to plot population sizes
    plt.figure()
  plt.xlabel('Time')
  plt.ylabel('Population Size')
  print('Minimum x axis:', xaxis.min())
  print('Maximum x axis:', xaxis.max())
  plt.xticks(rotation=90) #creating min and max for x axis 
  plt.grid(True)#adding grid
  #plotting 6 lines
  line1=plt.plot('time', 'Red', data=Red, color = 'r')
  line2=plt.plot('time', 'Organge', data=Orange, color = 'o')
  line3=plt.plot('time', 'Yellow', data=Yellow, color = 'y')
  line4=plt.plot('time', 'Green', data=Green, color = 'g')
  line5=plt.plot('time', 'Blue', data=Blue, color = 'b')
  line6=plt.plot('time', 'Purple', data=Purple, color = 'p')
  plt.show()


# # Questions:
