import discord
import os
from sympy import *


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    def multiply(value):
      if '*' in value:
        y = value.split('*')
        x = float(y[0]) * float(y[1])
        
        return x

    def divide(value):
      if '/' in value:
        y = value.split('/')
        x = float(y[0]) / float(y[1])
        return x

    def add(value):
      if '+' in value:
        y = value.split('+')
        x = float(y[0]) + float(y[1])
        return x

    def subtract(value):
      if '-' in value:
        y = value.split('-')
        x = float(y[0]) - float(y[1])
        return x

    msg = message.content
    if msg.startswith('Help'):
      await message.channel.send("Add, Subtract, Multiply, Divide: Straight-forward")
    if msg.startswith('Add'):
      equation = msg.split()
      out = add(equation[1])
      await message.channel.send(out)

    if msg.startswith('Subtract'):
      equation = msg.split()
      out = subtract(equation[1])
      await message.channel.send(out)

    if msg.startswith('Multiply'):
      equation = msg.split()
      out = multiply(equation[1])
      await message.channel.send(out)

    if msg.startswith('Divide'):
      equation = msg.split()
      out = divide(equation[1])
      await message.channel.send(out)

    
    if msg.startswith('Deriv'):
      second = msg.split()
      function = ""
      for i in second[1]:
        if i == '^':
          function += '**'
        else:
          function += i
        
          
      x = Symbol('x')
      y = eval(function)
      yprime = y.diff(x)
      
      await message.channel.send(yprime)
      

    if msg.startswith('DerivEval'):
      second = msg.split()
      function = ""
      

    if msg.startswith('IntegrateIn'):
      second = msg.split()
      function = ""
      for i in second[1]:
        if i == '^':
          function += '**'
        elif i == 'e':
          function += 'math.e'
        elif i == 'p':
          function += 'p'
        else:
          function += i
        

      x = Symbol('x')
      y = eval(function)
      indef = integrate(y, x)
      await message.channel.send(indef)
    if msg.startswith('SeriesConDi'):
      value = msg.split()
      function = ""
      for i in second[1]:
        if i == '^':
          function += '**'
        elif i == 'e':
          function += 'math.e'
        elif i == 'p':
          function += 'math.pi'
        else:
          function += i

        start = second[2]
        end = second[3]
      pass
    if msg.startswith('IntegrateDef'):
      second = msg.split()
      function = ""
      for i in second[1]:
        if i == '^':
          function += '**'
        elif i == 'e':
          function += 'math.e'
        elif i == 'p':
          function += 'math.pi'
        else:
          function += i
        
      bottom = second[2]
      top = second[3]
      x = Symbol('x')
      y = eval(function)
      indef = integrate(y, x)
      defint = integrate(y, (x, bottom, top))
      await message.channel.send(indef)
      await message.channel.send(defint) 


client.run('OTUzODIzNTMwMDg3MjI3NDMz.YjKLYg.ovioqBTPKB6x2vm-Mu1CfGoG8Uo')
