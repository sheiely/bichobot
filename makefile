build:
	rasa train --domain domain
shell:
	rasa shell
start:
	rasa train --domain domain
	rasa shell