# Overview
  This Project combines the SHTC3 sensor on the ESP32c3 and the DFRobot_RGBLCD display screen using the I2C interface. It displays the surrounding temperature in Celsius, aswell as the humidity percentage.

<img width="414" height="242" alt="image" src="https://github.com/user-attachments/assets/2fa13733-b170-44c8-bcc1-3c992f567d78" />

# Resources
  ### DFRobot 
  #### https://github.com/DFRobot/DFRobot_RGBLCD1602.
  The DFRobot library was modified to work with the esp32c3 board, as it was originally intended for Arduino.
  ### I2C
  #### https://github.com/espressif/esp-idf/tree/master/examples/peripherals/i2c/i2c_basic 
  This example code was modified to initialize, read, and write from the SHTC3 sensor.
