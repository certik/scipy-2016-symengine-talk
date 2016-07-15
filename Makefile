all: tex

tex: images
	pdflatex --halt-on-error talk.tex
	pdflatex --halt-on-error talk.tex

images: benchmarks/data.json benchmarks/Plots.ipynb
	mkdir -p images
	cp pdfs/n-pendulum-with-cart.pdf images/n-pendulum-with-cart.pdf
	cd benchmarks; jupyter nbconvert --execute  --to notebook Plots.ipynb
