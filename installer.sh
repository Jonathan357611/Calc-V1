 #!/bin/bash

echo "This will install the Calc-V1 software on your Pico!"
echo -n "Please enter the folder of your Pico: "
location = read 
echo ${location}
if [ ${location##*/} == "CIRCUITPY" ]; then
    echo "This is indeed your Pico :)"
else
    echo -e "\e[31mThis does not seem to be your Pico!\e[0m"
    exit
fi

echo "Copying files..."

mv code.py ${location}
mv lib ${location}
mv font5x8 ${location}

echo -e "\e[32mAll done!\e[0m"