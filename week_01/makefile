file_name = 01

linal_lecture_$(file_name).pdf: linal_lecture_$(file_name).tex chapters/ figures/ linal_preamble.tex
	# protection against biber error
	# http://tex.stackexchange.com/questions/140814/
	rm -rf `biber --cache`

	# create pdf
	# will automatically run pdflatex/biber if necessary
	latexmk -xetex $(file_name).tex

	# clean auxillary files
	latexmk -c $(file_name).tex

	echo To make pngs use 'make png'

png:
	mkdir -p slides
	pdftocairo linal_lecture_$(file_name).pdf slides/la-$(file_name) -png -r 300 -transp 
