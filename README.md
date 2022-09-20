# Calc V1 🧮

This is RP2040 (Raspberry Pi Pico) driven calculator using mechanical switches based on the MX-format which doubles as an HID-numpad if wanted.

This is my very first *real* physical and polished project and thus im very proud of it as a 14 year old :)


![alt text](./images/img1.jpg)

## PCB

![alt text](./images/img2.jpg)

The 2 sided PCB was designed in kicad and some rookie experience!
You can find the design files in the kicad folder and production in gerber.


## Installation 📀

Before installing, it is very important to flash **circuipy** on your Pico. You can download the newest version [here](https://circuitpython.org/board/raspberry_pi_pico/)

Now there are two options:

### Installer (only linux tested!):
1. Open a terminal
2. run ```git clone https://github.com/Jonathan357611/Calc-V1.git```
3. ... and now ```./installer.sh```. The installer should copy all necessary files to your Pico!
4. Done!

### Manual

1. Clone the repo ```git clone https://github.com/Jonathan357611/Calc-V1.git```
2. Take these files: code.py font5x8.bin lib/
3. And copy them on your Pico!

That should be it. If you have any troubles installing it, hit me up!

## HID Numpad
Want to use it as a numpad? Easy!
Just set ```HID``` to ```True``` in line 7 in code.py!

## Other

Any contributions in code, installation and PCB very welcomed :)
I'll try my best to fix any issues you run into.

If you *really* like my project, consider donating some ETH :)
```0x1f2C6e62622051b3F4d4a3545B17018704630c35```