


.PHONY: test


run: main.py
	echo 'run main.py'
	clear
	python main.py


test:
	clear
	python -m test
    
venv:
	python -m venv venv


install: venv
	source ./venv/bin/activate; python -m pip install -r requirements.txt
