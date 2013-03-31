import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.IN)

time.sleep(2)

mc= minecraft.Minecraft.create()

while (True):
	if (GPIO.input(23)==False):
		mc.postToChat("Hello World!!")
	time.sleep(2)
