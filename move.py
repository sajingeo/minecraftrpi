#
#  Author :Sajin George
# web :mycrobonics.com
#  free to use    
import minecraft.minecraft as minecraft
import minecraft.block as block
import time
import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.OUT)

time.sleep(2)

mc= minecraft.Minecraft.create()
while (True):
	if (GPIO.input(23)==False):
		playerPos=mc.player.getPos()
		playerPos=minecraft.Vec3(int(playerPos.x),int(playerPos.y),int(playerPos.z))
		mc.player.setPos(playerPos.x+10,playerPos.y,playerPos.z)

	time.sleep(2)
