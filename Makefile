all: tex

tex: images
	pdflatex --halt-on-error talk.tex
	pdflatex --halt-on-error talk.tex

images: benchmarks/data.json benchmarks/gen_images.py
	mkdir -p images
	cd benchmarks; python gen_images.py
