
FILENAME ?= main.ms
ROFF = groff
MACRO_SET = -ms

.DEFAULT_GOAL := out

# .PHONY: .default
# default: out; 

out:
	pic $(FILENAME) | \
	tbl | \
	eqn -Tpdf | \
	$(ROFF) $(MACRO_SET) -T pdf > out.pdf 	

auto_comp:
	python3 auto_compiler.py $(FILENAME)