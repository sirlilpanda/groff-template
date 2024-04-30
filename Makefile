
PROJECT_NAME = Template
AUTHOR = the baddest bitch around
FILENAME ?= main.ms
OUT_FILENAME ?= out
TYPE ?= ps
ROFF = groff
MACRO_SET = -ms

.DEFAULT_GOAL := out

out:
	pic $(FILENAME) | \
	tbl | \
	eqn -T$(TYPE) | \
	$(ROFF) $(MACRO_SET) -U -T $(TYPE) > cache/$(OUT_FILENAME).$(TYPE) 
	ps2pdf cache/$(OUT_FILENAME).$(TYPE)

auto_comp:
	python3 auto_compiler.py $(FILENAME)

convert_images:
	find images \*.png -exec convert {} cache/{}.eps \;

hard_clean:
	rm cache/*

image_clean:
	rm cache/*.eps

reload_template:
	mkdir -p .trash
	cat main.ms > .trash/old.ms
	echo "\
	.TL \n\
	Template \n\
	.AU \n\
	the baddest bitch around\n\
	.AB \n\
	abstract \n\
	.AE \n\
	.NH \n\
	section \n\
	.PP \n\
	lorum testing\n\
	\n\
	.PSPIC -I 2i "cache/frog.eps" 2i\n\
	" > main.ms


