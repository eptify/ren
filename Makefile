ANTLR4=java -jar .antlr/antlr-4.7-complete.jar

.antlr/antlr-4.7-complete.jar:
	mkdir -p .antlr && cd .antlr && curl -O http://www.antlr.org/download/antlr-4.7-complete.jar

grammar: .antlr/antlr-4.7-complete.jar ren.g4
	$(ANTLR4) -Dlanguage=Python2 -visitor -no-listener -o ren/py2grammar ren.g4 && touch ren/py2grammar/__init__.py
	$(ANTLR4) -Dlanguage=Python3 -visitor -no-listener -o ren/py3grammar ren.g4 && touch ren/py3grammar/__init__.py

test:
	pytest --cov=ren --cov-report=html
