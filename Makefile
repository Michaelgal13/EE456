download: 
	git pull
	sudo apt-get update
	sudo apt-get --yes --force-yes upgrade
	sudo pip3 install setuptools || sudo apt-get -y install python3-pip
	sudo apt-get install -y python3 git python3-pip
	sudo pip3 install RPI.GPIO
	sudo pip3 install adafruit-blinka
	sudo pip3 install adafruit-circuitpython-ssd1306
	sudo pip3 install adafruit-circuitpython-framebuf
	sudo pip3 install adafruit-circuitpython-rfm9x


