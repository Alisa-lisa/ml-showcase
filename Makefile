env:
	python3 -m venv env
	env/bin/pip install --upgrade pip
	env/bin/pip install -r requirements.txt

.PHONY: start-jupyter
start-jupyter:
	rm -rf env/
	make env
	env/bin/jupyter notebook .

.PHONY: simple-start
simple-start:
	env/bin/jupyter notebook .

.PHONY: run
run:
	cd runnables && docker build -t proto .
	cd runnables && docker run -p 5000:5000 proto