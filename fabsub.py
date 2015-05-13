#!/usr/bin/python
# -*- coding: utf8 -*-

import os

def init_docs(handdoc,beamer,vers):

	handdoc.write("\documentclass{article}\n")
	handdoc.write("\usepackage[utf8]{inputenc}\n")
	handdoc.write("\usepackage[a4paper, total={19cm, 27cm}]{geometry}\n")
	handdoc.write("\\title{Gestion des sous-titres de la thèse de F. Benureau}\n")
	handdoc.write("\date{\\today \\\\ v"+vers+"}\n")
	handdoc.write("\\begin{document}\n")
	handdoc.write("\maketitle\n")

	beamer.write("\documentclass{beamer}\n")
	beamer.write("\usepackage[utf8]{inputenc}\n")
	beamer.write("\\beamertemplatenavigationsymbolsempty\n")
	beamer.write("\\begin{document}\n")


def end_docs(handdoc,beamer):
	handdoc.write("\end{document}")
	beamer.write("\end{document}")


def add_element(handdoc,beamer,num,txt_en,txt_fr):
	handdoc.write("\n")
	handdoc.write("\\begin{tabular}{ | p{1cm} | p{8cm} | p{8cm} |}\n")
	handdoc.write("\hline\n")
	handdoc.write(num+" & "+txt_en+" & "+txt_fr+" \\\\ \n")
	handdoc.write("\hline\n")
	handdoc.write("\end{tabular}\n")

	beamer.write("\n")
	beamer.write("\\begin{frame}\n")
	beamer.write("\\begin{center}\n")
	beamer.write("\\textbf{"+txt_fr+"}\n")
	beamer.write("\let\\thefootnote\\relax\\footnotetext{"+num+"}\n")
	beamer.write("\end{center}\n")
	beamer.write("\end{frame}\n")

def parse_sub_file(handdoc, beamer, subfilename):
	with open(subfilename,"r") as subfile:
		parse_list=subfile.readlines()
		for i in range(0,len(parse_list)/3):
			add_element(handdoc,beamer,str(i+1),parse_list[3*i],parse_list[3*i+1])

def compile_pdfs(filename):
	os.system("pdflatex "+filename+"_handdoc.tex")
	os.system("pdflatex "+filename+"_beamer.tex")




if __name__ == "__main__":
	filename = "subtitles"
	subfilename = "subtitles.txt"
	vers = "0"
	with open(filename+"_handdoc.tex","w") as handdoc:
		with open(filename+"_beamer.tex","w") as beamer:
			init_docs(handdoc,beamer,vers)
			parse_sub_file(handdoc, beamer, subfilename)
			end_docs(handdoc,beamer)
			#compile_pdfs(filename)






