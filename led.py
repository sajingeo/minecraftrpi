#
#  Author :Sajin George
# web :mycrobonics.com
#  free to use    
#  LED blinky with minecraft world
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

playerPos=mc.player.getPos()
playerPos=minecraft.Vec3(int(playerPos.x),int(playerPos.y),int(playerPos.z))
blockx=playerPos.x+5
blockz=playerPos.z
mc.setBlock(blockx,playerPos.y,playerPos.z,block.TNT)
while (True):
	GPIO.output(24,False)
	playerPos=mc.player.getPos()
	playerPos=minecraft.Vec3(int(playerPos.x),int(playerPos.y),int(playerPos.z))
	if(playerPos.x==blockx):
		GPIO.output(24,True)	

	time.sleep(2)
