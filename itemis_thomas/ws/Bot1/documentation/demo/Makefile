.PHONY: clean

DOC=ess_demo_notes
all: $(DOC).pdf

$(DOC).pdf: $(DOC).txt
	rst2pdf $< -o $(DOC).pdf -s kerning

clean:
	rm -f $(DOC).pdf
