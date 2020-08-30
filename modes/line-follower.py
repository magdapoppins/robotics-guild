#!/usr/bin/env python3
from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, SpeedRPM, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
import logging

logging.getLogger().setLevel(logging.INFO)

# ------Input--------
logging.info('Setting input values')
power = 40
target = 15
kp = float(0.65)  	# Proportional gain. Start value 1
kd = 1           		# Derivative gain. Start value 0
ki = float(0.02)  	# Integral gain. Start value 0
direction = -1
minRef = 0       		# 0 is the blackest black
maxRef = 30      		# Under 30 = black, ~65 is white
# -------------------

# Connect two large motors on output ports B and C and check that
# the device is connected using the 'connected' property.
logging.info('Connecting motors')
left_motor = LargeMotor(OUTPUT_B)
right_motor = LargeMotor(OUTPUT_C)
# One left and one right motor should be connected

# Connect color and touch sensors and check that they
# are connected.
logging.info('Connecting sensors')
#ts = TouchSensor()
col = ColorSensor()

# Change color sensor mode
logging.info('Setting color sensor mode')
col.mode = 'COL-REFLECT'

# Adding button so it would be possible to break the loop using
# one of the buttons on the brick
logging.info('Adding button')
btn = Button()


def steering2(course, power):
	"""
	Computes how fast each motor in a pair should turn to achieve the
	specified steering.
	Input:
		course [-100, 100]:
		* -100 means turn left as fast as possible,
		*  0   means drive in a straight line, and
		*  100  means turn right as fast as possible.
		* If >100 power_right = -power
		* If <100 power_left = power
	power: the power that should be applied to the outmost motor (the one
		rotating faster). The power of the other motor will be computed
		automatically.
	Output:
		a tuple of power values for a pair of motors.
	Example:
		for (motor, power) in zip((left_motor, right_motor), steering(50, 90)):
			motor.run_forever(speed_sp=power)
	"""
	if course >= 0:
		if course > 100:
			logging.info('TURN RIGHT')
			power_right = 0
			power_left = power
		else:
			logging.info('TURN SLIGHTLY RIGHT')
			power_left = power
			power_right = power - ((power * course) / 100)
	else:
		if course < -100:
			logging.info('TURN LEFT')
			power_left = 0
			power_right = power
		else:
			logging.info('TURN SLIGHTLY LEFT')
			power_right = power
			power_left = power + ((power * course) / 100)
	return (int(power_left), int(power_right))


def run(power, target, kp, kd, ki, direction, minRef, maxRef):
	"""
	PID controlled line follower algoritm used to calculate left and right motor power.
	Input:
		power. Max motor power on any of the motors
		target. Normalized target value.
		kp. Proportional gain
		ki. Integral gain
		kd. Derivative gain
		direction. 1 or -1 depending on the direction the robot should steer
		minRef. Min reflecting value of floor or line
		maxRef. Max reflecting value of floor or line
	"""
	lastError = error = integral = 0
	left_motor.run_direct()
	right_motor.run_direct()

	# How much has been turned since last direction swap
	previousRefRead = col.value()

	while not btn.any():
		#if ts.value():
		#	logging.info('Breaking loop')  # User pressed touch sensor
		#	break
		refRead = col.value()
		error = target - (100 * ( refRead - minRef ) / ( maxRef - minRef ))
		derivative = error - lastError
		lastError = error
		integral = float(0.5) * integral + error

		logging.info('previousRefRead {}, refRead {}, direction {}, abs {}'.format(previousRefRead, refRead, direction, abs(previousRefRead - refRead)))
		if abs(previousRefRead - refRead) > 20 and previousRefRead < 30:
			# Change direction
			#run = MoveTank(left_motor, right_motor) MAGDA WAS HERE
			#run.on_for_rotations(-10, -10, 8)
			logging.info('*** ASDADADDADADASSAD ***')
			direction = direction*(-1)
			previousRefRead = refRead

		course = (kp * error + kd * derivative +ki * integral) * direction

		logging.info('refRead: {}, error: {}, derivative: {}, lastError: {}, integral: {}, course: {}'.format(refRead, error, derivative, lastError, integral, course))

		for (motor, pow) in zip((left_motor, right_motor), steering2(course, power)):
			motor.duty_cycle_sp = pow
		sleep(0.06) # Aprox 100Hz

run(power, target, kp, kd, ki, direction, minRef, maxRef)

# Stop the motors before exiting.
logging.info('Stopping motors')
left_motor.stop()
right_motor.stop)(
