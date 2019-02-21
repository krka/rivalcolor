#!/usr/bin/python

# Depends on python-psutil
import psutil

import time
from itertools import cycle

import rivalcfg.rival_mouse as mouse
import rivalcfg.cli as cli

delta = 0.05

speed = 2

idle_color = (0, 0, 0)
config = [
  (0.5, (20, 0, 0)),
  (0.5, (255, 0, 0)),
]

def interpolate(t, a, b):
  if t > 1: t = 1
  if t < 0: t = 0
  return tuple( int((1 - t) * x + t * y) for (x, y) in zip(a, b))

def clamp(x, a, b):
   if x < a: return a
   if x > b: return b
   return x

def cpu_usage():
  x = psutil.cpu_percent()
  if x < 20: return 0
  if x >= 50: return 100
  return 50

while True:
  profile = cli.get_plugged_mouse_profile()
  if profile is None:
    time.sleep(1)
  else:
    print "Found mouse: " + profile["name"]
    try:
      instance = mouse.RivalMouse(profile)
      prev = (0, 0, 0)
      percentage = 0
      for (total_time, color) in cycle(config):
         total_time *= speed
         t = 0
         while t < total_time:
           c = interpolate(t / total_time, prev, color)

           percentage = percentage + clamp(cpu_usage() - percentage, -0.1, 0.1)
           c2 = interpolate(percentage / 100.0, idle_color, c)

           instance.set_color(*c2)
           t += delta
           time.sleep(delta)
         prev = color
    except Exception, e:
      print "Could not talk to mouse: " + str(e)

