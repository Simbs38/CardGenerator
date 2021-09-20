#import argparse
import os
import subprocess

def remove_quotes(x):
    return x.replace("'", "")
    
def remove_braces(x):
    return x.replace("{{", "{").replace("}}","}")
    
def get_dir_files(path):
    files = []
# r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.png' in file:
                files.append(remove_quotes(file))
    
    return(files)

path = 'events'
DIR = 'outputs/'
f_path = DIR + path + '/'
cards = get_dir_files(f_path)
## https://stackoverflow.com/questions/8085520/generating-pdf-latex-with-python-script


header = r'''
\documentclass{{article}}

\usepackage{{graphicx}}
\usepackage{{trimclip}}
\graphicspath{{ {{{}}} }}
\thispagestyle{{empty}}

\begin{{document}}

\addtolength{{\oddsidemargin}}{{-.875in}}
\addtolength{{\evensidemargin}}{{-.875in}}
\addtolength{{\textwidth}}{{1.75in}}
\addtolength{{\topmargin}}{{-.875in}}
\addtolength{{\textheight}}{{1.75in}}


\begin{{figure}}[!htpb]
\trimbox{{0.8cm 0.8cm 0.8cm 0.8cm}}{{
'''
header = header.format(f_path)

footer = r'''\end{document}
'''

corpus_begin = r'''
\begin{{figure}}[!htpb]
\trimbox{{0.8cm 0.8cm 0.8cm 0.8cm}}{{
'''

corpus_end =r'''
}}
\end{{figure}}

\bigskip
\bigskip
\bigskip
\bigskip
\bigskip
'''
corpus_image= r'''
\begin{{minipage}}{{.50\linewidth}}
\includegraphics[width=5.3cm,height=8.2cm]{{{}}}
\end{{minipage}}
'''
def build_pdf(cards, header, footer, pdf=''):
    pdf = pdf + header
    for i, card in enumerate(cards):
        #print(i,card)
        if (i + 1) == len(cards):
            if i%3 == 0:
                pdf =  pdf + corpus_end  + corpus_begin +  corpus_image.format(card) + corpus_end 
                break
            else:                
                pdf = pdf + corpus_image.format(card) + corpus_end  
                break
        if i%3 != 0 or i == 0:
            #print(i)
            pdf = pdf + corpus_image.format(card)
        else:
            pdf = pdf + corpus_end  + corpus_begin +  corpus_image.format(card) 
            
    pdf = pdf + footer
    return(pdf)
        
pdf = build_pdf(cards, header,footer)
pdf = remove_braces(pdf)



with open('main.tex','w') as f:
    #f.write(content%args.__dict__)
    f.write(pdf)

cmd = ['pdflatex', '-interaction', 'nonstopmode', 'main.tex']
#cmd = ['pdflatex', 'main.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink('main.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

os.unlink('main.tex')
os.unlink('main.log')


