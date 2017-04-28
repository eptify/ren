ANTLR4=java -jar .antlr/antlr-4.6-complete.jar

.antlr/antlr-4.6-complete.jar:
	mkdir -p .antlr && cd .antlr && curl -O http://www.antlr.org/download/antlr-4.6-complete.jar

grammar: .antlr/antlr-4.6-complete.jar ren.g4
	$(ANTLR4) -Dlanguage=Python2 -visitor -no-listener -o ren/gen ren.g4 && touch ren/gen/__init__.py
