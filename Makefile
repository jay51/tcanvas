

NAME := 'turtule'

.PHONY: test


run: main.py
	echo 'run main.py'
	clear
	python3 main.py


test:
	clear
	# make test NAME=turtule
	python3 -m test $(NAME)
    
venv:
	python3 -m venv venv


install: venv
	source ./venv/bin/activate; python3 -m pip install -r requirements.txt
