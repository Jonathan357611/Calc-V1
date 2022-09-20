 #!/bin/bash

echo "This will install the Calc-V1 software on your Pico!"
echo -n "Please enter the folder of your Pico: "
read location
echo ${location}

if [ ${location##*/} == "CIRCUITPY" ]; then
    echo "This is indeed your Pico :)"
else
    echo -e "\e[31mThis does not seem to be your Pico!\e[0m"
    exit
fi

cp code.py ${location}/code.py
cp -r lib ${location}/lib
cp font5x8.bin ${location}/font5x8.bin

echo -e "\e[32mAll done!\e[0m"