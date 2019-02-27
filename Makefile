all: dataset power.png communities.png

dataset:
	make -C data

power.png: ca3.py
    python $<

communities.png: ca3.py
	python $<

clean:
	-rm power.png communities.png

dist-clean: clean
	-make -C data clean