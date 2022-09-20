 #!/bin/bash

echo "This will install the Calc-V1 software on your Pico!"
echo -n "Please enter the folder of your Pico: "
read location
echo ${location}

if [ ${location##*/} == "CIRCUITPY" ]; then
    echo -e "\e[32mThis is indeed your Pico :)\e[0m"
else
    echo -e "\e[31mThis does not seem to be your Pico!\e[0m"
    exit
fi

echo -e "\e[1;33mMoving files...\e[0m"

cp code.py ${location}/code.py
cp -r lib ${location}/lib
cp font5x8.bin ${location}/font5x8.bin

echo -e "\e[32mAll done!\e[0m"