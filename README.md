# Janus-Avionics
This is my submission of task of Janus for Avionics. I have done both the task of Arudino and python.
## Task 1- Planning to surprise Galactus

This task required brainstorming on how to plot and animate flight data. I followed the given tutorial to gain deeper knowledge of data visualization and animation in Python.

Features:
1. Reads flight data from CSV files.
2. Converts Pressure to Altitude.
3. Applied Savgol_filter to smooth noisy altitude data.
4. Calculated velocity as the derivative of altitude over time.
5. Animated plots of:
  - Altitude vs Time  
  - Velocity vs Time

Libraries used :
1. Pandas
2. numpy
3. matplotlib
4. . scipy.signa


## Task 2- Surprising Galactus!
I worked on tinkercad for the Arduino project.

Components Needed
Arduino Uno
Force sensor 
3 LEDs (Green, Red, Yellow)
3 Resistors (300Ω each → for LEDs)
1 Piezo Buzzer
1 Resistor (10kΩ for force sensor)
Jumper wire- for connection

Researched about working and functioning of force sensor.
Attached the components to their respective digital and analog pin.
Tried different codes for making the bzzer to work at peak value.

This project:
Detected ascending, descending, stable states by force sensor
Flash LEDs accordingly.
Buzz at the peak.

###Through these two tasks, I learned how to:  
- Process and visualize real-world data in Python.  
- Work with sensors, actuators, and logic on Arduino.  
