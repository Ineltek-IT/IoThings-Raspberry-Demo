# IoThings-Raspberry-Demo

The demo for IoThings trade fair has the setup showed below.
The Raspberry Pi Pico H is used to measure the pressure from a Novosense evk based on [NSPGS2](https://www.novosns.com/en/mems-pressure-sensor-1641) and to display it to a 7 segment module `SSE3642WWG` by Tricomtek which used the `TM1637` driver. 
The connections are as follows

|Raspberry Pico|SSE3642WWG|NSPGS2|
|---|---|---|
|GP0 ||SDA|
|GP1 ||SCL|
|GP20|DIO||
|GP21|CLK||

## Setup
![setup](setup.png)


