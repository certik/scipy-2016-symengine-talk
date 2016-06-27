all: tex

tex: images
	pdflatex talk.tex
	pdflatex talk.tex

images: benchmarks/data.json benchmarks/gen_images.py
	mkdir -p images
	cd benchmarks; python gen_images.py
