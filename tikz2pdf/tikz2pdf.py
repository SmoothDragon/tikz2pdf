# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

header=r'''\documentclass{article}
\usepackage[pdftex,active,tightpage]{preview}
\usepackage{tikz}
\usetikzlibrary{decorations.pathreplacing,decorations.pathmorphing}
\usepackage{hyperref}
%\usepackage{geometry}
\definecolor{bg}{rgb}{1,1,1}
'''

prescript=r'''\begin{document}
\begin{preview}
'''

postscript=r'''\end{preview}
\end{document}
'''

header_flag = '%!'

def tikz2tex(text):
    yield header
    prescript_done = False
    for line in text:
        if line.startswith(header_flag):
            yield line[len(header_flag):]
            continue
        if not prescript_done:
            yield prescript
            prescript_done = True
        yield line
    yield postscript
