build:
	rasa train --domain domain
shell:
	rasa shell
start:
	rasa train --domain domain
	rasa shell
test:
	rasa test --domain domain core --stories ./tests
install:
	pip install rasa