import minecraft.minecraft as minecraft
import mincraft.block as block
import time
import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.IN)

time.sleep(2)

mc= minecraft.Minecraft.create()
while (True):
	if (GPIO.input(23)==False):
		mc.postToChat("hi you have pressed a button!")
	time.sleep(2)
