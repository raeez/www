%% momentum.cls -- Momentum Research paper class.
%%
%% Hand-authored LaTeX class for research-grade papers from
%% Momentum Research (research.momentum.inc).  xelatex only.
%%
%% Typography notes:
%%   - Text:    Garamond Premier Pro, 11pt, oldstyle figures
%%   - Display: Garamond Premier Pro Display (headings, title)
%%   - Mono:    JetBrains Mono at 0.88 scale
%%   - Math:    Latin Modern Math (xelatex default)
%%   - Links:   Navy #1b2a4a, matching paper.css on the web site
%%
%% Usage (in paper .tex):
%%     \documentclass{momentum}
%%     \title{The Multi-Harbored Institution}
%%     \author{Raeez Lorgat}
%%     \date{April 2026}
%%     \shorttitle{Multi-Harbored Institution}
%%     \begin{document}
%%     \maketitle
%%     \begin{abstract} ... \end{abstract}
%%     \section{...}
%%     ...
%%     \end{document}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{momentum}[2026/04/19 Momentum Research paper class]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[11pt,letterpaper,oneside]{article}

% -----------------------------------------------------------------
% Page geometry
% -----------------------------------------------------------------
\RequirePackage[
  letterpaper,
  margin=1.25in,
  top=1.15in,
  bottom=1.25in,
  headheight=14pt,
  headsep=18pt,
  footskip=30pt,
]{geometry}

% -----------------------------------------------------------------
% Fonts (xelatex + fontspec)
% -----------------------------------------------------------------
\RequirePackage{fontspec}
\defaultfontfeatures{Ligatures=TeX}

%% Only the Regular face of Garamond Premier Pro is present on the build host, so
%% xelatex silently substituted for bold and italic and every emphasis rendered flat —
%% theorem heads, proof markers and bolded findings indistinguishable from body text.
%% Map the missing shapes onto Baskerville, which the site's own CSS already names as a
%% fallback for this stack. The regular face is unchanged.
\setmainfont[
  Numbers={OldStyle,Proportional},
  Ligatures={TeX,Common},
  BoldFont={Baskerville Bold},
  ItalicFont={Baskerville Italic},
  BoldItalicFont={Baskerville Bold Italic},
]{Garamond Premier Pro}

\newfontfamily\displayfont[
  Numbers={OldStyle,Proportional},
  Ligatures={TeX,Common},
]{Garamond Premier Pro Display}

% Nerd Font variant is what's installed locally; fall back to DejaVu
% Sans Mono if it's absent so the class keeps compiling on fresh machines.
\IfFontExistsTF{JetBrainsMono Nerd Font Mono}{%
  \setmonofont[Scale=0.86]{JetBrainsMono Nerd Font Mono}%
}{%
  \IfFontExistsTF{JetBrains Mono}{%
    \setmonofont[Scale=0.86]{JetBrains Mono}%
  }{%
    \setmonofont[Scale=0.86]{DejaVu Sans Mono}%
  }%
}

% Math — keep default Latin Modern Math (classic, well-rendered)
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{amsthm}
\RequirePackage{mathtools}

% Inference rules for type-theory papers (Lex, Sovereign Kernel).
\RequirePackage{mathpartir}

% Double-bracket semantics [[ . ]] via stmaryrd's \llbracket / \rrbracket
\RequirePackage{stmaryrd}

% Tables
\RequirePackage{booktabs}
\RequirePackage{array}

% -----------------------------------------------------------------
% Typography refinements
% -----------------------------------------------------------------
\RequirePackage{microtype}
\RequirePackage{setspace}
\setstretch{1.18}

\setlength{\parindent}{1.25em}
\setlength{\parskip}{0pt plus 1pt}
\RequirePackage{indentfirst}   % indent first paragraph after heading

\clubpenalty=10000
\widowpenalty=10000
\displaywidowpenalty=10000
\raggedbottom

% Justify with microtype font protrusion, but allow slightly looser
% spacing for long lines to avoid overfull hboxes in dense prose.
\emergencystretch=3em
\hyphenpenalty=200
\tolerance=400

% -----------------------------------------------------------------
% Color palette (matches paper.css on the web site)
% -----------------------------------------------------------------
\RequirePackage{xcolor}
\definecolor{mr@navy}{HTML}{1B2A4A}
\definecolor{mr@ink}{HTML}{2C2C2C}
\definecolor{mr@inkmuted}{HTML}{4A4744}
\definecolor{mr@inkfaint}{HTML}{7A7672}
\definecolor{mr@accent}{HTML}{8B4C3A}
\definecolor{mr@rule}{HTML}{DAD4C9}
\definecolor{mr@paperdim}{HTML}{F8F6F3}

\color{mr@ink}   % default body colour (warm near-black)

% -----------------------------------------------------------------
% Section heading typography
%   - Display font, navy, hanging number
%   - Generous vertical space above, modest below
% -----------------------------------------------------------------
\RequirePackage{titlesec}

\titleformat{\section}
  {\normalfont\displayfont\fontsize{17pt}{20pt}\selectfont\color{mr@navy}}
  {\thesection\hspace{0.6em}}{0pt}{}
\titleformat{\subsection}
  {\normalfont\displayfont\fontsize{13.5pt}{16pt}\selectfont\color{mr@navy}}
  {\thesubsection\hspace{0.55em}}{0pt}{}
\titleformat{\subsubsection}
  {\normalfont\bfseries\color{mr@navy}}
  {\thesubsubsection\hspace{0.5em}}{0pt}{}
\titleformat{\paragraph}[runin]
  {\normalfont\bfseries\color{mr@ink}}
  {}{0pt}{}[\,]

\titlespacing*{\section}      {0pt}{2.8em plus 0.4em minus 0.2em}{0.9em}
\titlespacing*{\subsection}   {0pt}{2.0em plus 0.3em minus 0.15em}{0.7em}
\titlespacing*{\subsubsection}{0pt}{1.4em plus 0.2em minus 0.1em}{0.5em}
\titlespacing*{\paragraph}    {0pt}{0.8em plus 0.2em minus 0.1em}{0.4em}

% -----------------------------------------------------------------
% Theorem-like environments
% -----------------------------------------------------------------
\newtheoremstyle{mr@plain}%
  {1.1em}{0.6em}%               above / below
  {\itshape}%                    body
  {0pt}%                         indent
  {\bfseries\color{mr@navy}}%    head
  {.}%                           head punctuation
  {0.5em}%                       head-body sep
  {}%                            head spec

\newtheoremstyle{mr@def}%
  {1.1em}{0.6em}%
  {}%                            body upright
  {0pt}%
  {\bfseries\color{mr@navy}}%
  {.}%
  {0.5em}%
  {}

\newtheoremstyle{mr@remark}%
  {1.0em}{0.5em}%
  {}%
  {0pt}%
  {\itshape\color{mr@inkmuted}}%
  {.}%
  {0.5em}%
  {}

\theoremstyle{mr@plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}

\theoremstyle{mr@def}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}

\theoremstyle{mr@remark}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{note}[theorem]{Note}

% -----------------------------------------------------------------
% Lists
% -----------------------------------------------------------------
\RequirePackage[shortlabels]{enumitem}
\setlist{
  topsep=0.4em,
  itemsep=0.2em,
  parsep=0.2em,
  partopsep=0pt,
  leftmargin=1.9em,
  labelsep=0.6em,
}
\setlist[itemize,1]{label=\color{mr@inkfaint}\textbullet}
\setlist[enumerate,1]{label=\color{mr@inkfaint}(\arabic*)}

% -----------------------------------------------------------------
% Code blocks — fancyvrb with left rule
% -----------------------------------------------------------------
\RequirePackage{fvextra}
\RequirePackage{fancyvrb}
\RequirePackage{csquotes}   % must load after fvextra
\fvset{
  fontsize=\small,
  baselinestretch=1.1,
  frame=leftline,
  framerule=0.6pt,
  rulecolor=\color{mr@rule},
  xleftmargin=1em,
  breaklines=true,
  breakanywhere=false,
  breaksymbolleft={\color{mr@inkfaint}\tiny$\hookrightarrow$},
}

% listings fallback for inline language highlighting
\RequirePackage{listings}
\lstset{
  basicstyle=\ttfamily\small,
  keywordstyle=\color{mr@navy}\bfseries,
  stringstyle=\color{mr@accent},
  commentstyle=\itshape\color{mr@inkmuted},
  showstringspaces=false,
  breaklines=true,
  breakatwhitespace=true,
  frame=leftline,
  framerule=0.6pt,
  rulecolor=\color{mr@rule},
  xleftmargin=1em,
  belowskip=0.6em,
  aboveskip=0.8em,
}

% -----------------------------------------------------------------
% Quotation — left rule, muted ink
% -----------------------------------------------------------------
\renewenvironment{quote}
  {\par\vspace{0.4em}\begin{list}{}{%
      \leftmargin=1.6em\rightmargin=1em\topsep=0.3em
      \listparindent=0em\itemindent=0em\parsep=0.2em}\item\relax
   \color{mr@inkmuted}\itshape}
  {\end{list}\vspace{0.4em}}

% -----------------------------------------------------------------
% Title block -- custom \maketitle (load titling before hyperref)
% -----------------------------------------------------------------
\RequirePackage{titling}

% -----------------------------------------------------------------
% Hyperlinks (load near end)
% -----------------------------------------------------------------
\RequirePackage[
  colorlinks=true,
  linkcolor=mr@navy,
  urlcolor=mr@navy,
  citecolor=mr@navy,
  filecolor=mr@navy,
  pdfborderstyle={/S/U/W 0},
  bookmarksnumbered=true,
  bookmarksopen=true,
  pdfusetitle,
]{hyperref}

\RequirePackage[capitalise,noabbrev]{cleveref}
\crefname{section}{Section}{Sections}
\crefname{subsection}{Section}{Sections}
\crefname{theorem}{Theorem}{Theorems}
\crefname{lemma}{Lemma}{Lemmas}
\crefname{proposition}{Proposition}{Propositions}
\crefname{corollary}{Corollary}{Corollaries}
\crefname{conjecture}{Conjecture}{Conjectures}
\crefname{definition}{Definition}{Definitions}
\crefname{example}{Example}{Examples}
\crefname{remark}{Remark}{Remarks}
\crefname{equation}{equation}{equations}
\crefname{figure}{Figure}{Figures}
\crefname{table}{Table}{Tables}

% -----------------------------------------------------------------
% Custom \maketitle using titling-provided \thetitle/\theauthor/\thedate
% -----------------------------------------------------------------

\renewcommand{\maketitle}{%
  \begingroup
    \thispagestyle{plain}%
    \setlength{\parindent}{0pt}%
    \vspace*{-0.3em}%
    {\raggedright\displayfont\fontsize{28pt}{32pt}\selectfont\color{mr@navy}%
     \thetitle\par}%
    \vspace{1.0em}%
    {\raggedright\large\color{mr@inkmuted}\theauthor\par}%
    \vspace{0.35em}%
    {\raggedright\small\color{mr@inkfaint}\thedate\par}%
    \vspace{1.2em}%
    {\color{mr@rule}\hrule height 0.5pt}%
    \vspace{1.6em}%
  \endgroup
}

% Abstract — small, muted, set off by rules top and bottom.
\renewenvironment{abstract}{%
  \par\noindent
  \begingroup
    \small
    \color{mr@ink}%
    \noindent\textbf{\color{mr@navy}Abstract.}\enspace\ignorespaces
}{%
  \par
  \endgroup
  \vspace{1.0em}%
  {\color{mr@rule}\hrule height 0.5pt}%
  \vspace{1.5em}%
}

% -----------------------------------------------------------------
% Running heads
%   - Short title (italic, muted) on left
%   - Page number on right
% -----------------------------------------------------------------
\RequirePackage{fancyhdr}

\newcommand{\mr@shorttitle}{}
\newcommand{\shorttitle}[1]{\renewcommand{\mr@shorttitle}{#1}}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyhead[L]{\small\itshape\color{mr@inkfaint}\mr@shorttitle}
\fancyhead[R]{\small\color{mr@inkfaint}\thepage}

\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[R]{\small\color{mr@inkfaint}\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
}

% -----------------------------------------------------------------
% Caption styling
% -----------------------------------------------------------------
\RequirePackage[
  font=small,
  labelfont={bf,color=mr@navy},
  textfont={color=mr@ink},
  skip=6pt,
  justification=justified,
  singlelinecheck=false,
]{caption}

% -----------------------------------------------------------------
% Convenience macros
% -----------------------------------------------------------------
\newcommand{\emphNavy}[1]{\textbf{\color{mr@navy}#1}}
\providecommand{\keyword}[1]{\textit{#1}}

% Typeset pull-quotes with display font accent.
\newcommand{\pullquote}[1]{%
  \begin{quote}\displayfont\large #1\end{quote}%
}

\endinput
