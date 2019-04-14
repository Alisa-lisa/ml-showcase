env:
	python3 -m venv env
	env/bin/pip install --upgrade pip
	env/bin/pip install -r requirements.txt

.PHONY: start-jupyter
start-jupyter:
	rm -r env/
	make env
	env/bin/jupyter notebook .