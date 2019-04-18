FILES = $(shell ls naloge/*.tex)
NAME = $(shell basename $(CURDIR))

default: $(FILES:.tex=.pdf)
	mv naloge $(NAME)
	zip $(NAME).zip $(NAME)/*.pdf
	mv $(NAME) naloge
	latexmk resitve.tex
	mv resitve.pdf ../$(NAME)-resitve.pdf
	mv $(NAME).zip ../

%.pdf: %.tex
	pdflatex -interaction=batchmode -output-directory=naloge $<

clean:
	rm -rf $(NAME)
	rm -f *.{aux,log}
	rm -f $(NAME).zip
