%% This is a class file which  contains the code required to style the paper, and change how it looks.

\LoadClass[12pt]{article} % Start with the basic article class DO NOT alter font size; this is a competition requirement
\NeedsTeXFormat{LaTeX2e} % version requirement
\ProvidesClass{mthree}[M3 Challenge Team 15440 Paper]

% Extra packages required to do the styling
\RequirePackage{titlesec}
\RequirePackage{tabularx}
\RequirePackage{pgffor}
\RequirePackage{pbox}
\RequirePackage{geometry}
\RequirePackage{xcolor}
\RequirePackage{listings}
\RequirePackage{textcomp}
\RequirePackage[T1]{fontenc}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{chngcntr}
\counterwithin{figure}{section}


% Colours to be used in the document
\definecolor{navyblue}{rgb}{0.0, 0.0, 0.5}
\definecolor{lbcolor}{rgb}{1.0,1.0,1.0}

% Format of the code listings for the appendix
\lstset{
	backgroundcolor=\color{lbcolor},
	tabsize=4,
	rulecolor=,
	language=python,
        basicstyle=\scriptsize,
        upquote=false,
        aboveskip={1.5\baselineskip},
        columns=fixed,
        showstringspaces=false,
        extendedchars=true,
        breaklines=true,
        prebreak = \raisebox{0ex}[0ex][0ex]{\ensuremath{\hookleftarrow}},
        frame=single,
        showtabs=false,
        showspaces=false,
        showstringspaces=false,
        identifierstyle=\ttfamily,
        keywordstyle=\color{orange},
        commentstyle=\color[rgb]{0.133,0.545,0.133},
        stringstyle=\color[rgb]{0.627,0.126,0.941},
        numbers=left
}


% lengths and orientation of page; use US letter paper because it is larger than A4 and so we get more space 
\setlength{\parindent}{0ex} % Remove indent
\setlength{\parskip}{0ex}
\geometry{letterpaper, portrait, margin=1in} % Do not alter margin: This is a competition requirement

% Changes how the title at the start of the document displays to put it in capital letters - we can change this as you wish.
\def\@maketitle{%
  \newpage
  %\null
  %\vskip 2em%
  \begin{center}%
  \let \footnote \thanks
    {\normalfont\Large\bfseries \@title \par}%
    %\vskip 1.5em%
    %{\large
     % \lineskip .5em%
     % \begin{tabular}[t]{c}%
      %  \@author
      %\end{tabular}\par}%
    \vskip 1em%
    {\large \@date}%
  \end{center}%
 % \par
 % \vskip 1.5em
  }

% format of section headings
\titleformat{\section}
    {\Large\scshape\raggedright}
    {\thesection. }{0em}
    {}
    [\color{navyblue}\titlerule]
    
\titlespacing*{\section}{0pt}{1.6ex}{2.5ex}

% format subsection headings
\titleformat{\subsection}
    {\large\bfseries\raggedright}
    {\thesubsection. }{0em}
    {}
    

    

%Assumption and Justification
\newcommand{\assume}[2]{
    \textit{#1}
    \\
    \textbf{Justification:} #2
}

% Ensures figures are numbered 1.1 3.2 etc and not just 1,2,3,4
%\renewcommand{\thefigure}{\arabic{figure}}

%Creates headers and footers as required by competition specification
\pagestyle{fancy}
%%
\lfoot{Page \thepage~of \pageref{LastPage}}
\cfoot{}
\rfoot{Team 15440}
%%
\lhead{Page \thepage~of \pageref{LastPage}}
\chead{}
\rhead{Team 15440}
%%
\renewcommand{\headrulewidth}{0.4pt} % line between header and main content
\renewcommand{\footrulewidth}{0.4pt} % line between footer and main content
