def template_one(data, image_name):
    s_formatted_head = r'''
    \usepackage{fullpage}
    \usepackage{amsmath}
    \usepackage{amssymb}
    \textheight=10in
    \pagestyle{empty}
    \raggedright




\def\bull{\vrule height 0.8ex width .7ex depth -.1ex }


\newcommand{\area} [2] {
    \vspace*{-9pt}
    \begin{verse}
        \textbf{#1}   #2
    \end{verse}
}

\newcommand{\lineunder} {
    \vspace*{-8pt} \\
    \hspace*{-18pt} \hrulefill \\
}

\newcommand{\header} [1] {
    {\hspace*{-18pt}\vspace*{6pt} \textsc{#1}}
    \vspace*{-6pt} \lineunder
}

\newcommand{\employer} [3] {
    { \textbf{#1} (#2)\\ \underline{\textbf{\emph{#3}}}\\  }
}

\newcommand{\contact} [3] {
    \vspace*{-10pt}
    \begin{center}
        {\Huge \scshape {#1}}\\
        #2 \\ #3
    \end{center}
    \vspace*{-8pt}
}

\newenvironment{achievements}{
    \begin{list}
        {$\bullet$}{\topsep 0pt \itemsep -2pt}}{\vspace*{4pt}
    \end{list}
}

\newcommand{\schoolwithcourses} [4] {
    \textbf{#1} #2 $\bullet$ #3\\
    #4 \\
    \vspace*{5pt}
}

\newcommand{\school} [4] {
    \textbf{#1} #2 $\bullet$ #3\\
    #4 \\
}
'''

    s_formatted_body = r'''
\vspace*{-40pt}


\vspace*{-10pt}
\begin{center}
	{\Huge \scshape {''' + data["basics"]["name"] + r'''}}\\
	Jaipur $\cdot$ ''' + data["basics"]["email"] + r''' $\cdot$ ''' + data["basics"]["phone"] + r'''\\
\end{center}


\header{''' + data["headings"]["education"] + r'''}
'''
    for education in data["education"]:
        s_formatted_body += r'''\textbf{''' + education["institution"].replace('&', r'\&') + r'''}\hfill ''' + education["location"].replace('&', r'\&') + r'''\\'''
        s_formatted_body += "\n"
        s_formatted_body += education["studyType"] + r''' ''' + education["area"].replace('&', r'\&') + r''' \textit{GPA: ''' + education["gpa"] + r'''} \hfill ''' + education["startDate"] + r''' - ''' + education['endDate'] + r'''\\'''
        s_formatted_body += "\n"
        s_formatted_body += r'''\vspace{2mm}'''




    s_formatted_body += r'''


\header{''' + data["headings"]['work'] + r'''}
\vspace{1mm}
'''

# Loop over work history to insert job entries
    for job in data["work"]:
        if "company" in job:
            s_formatted_body += r'''
\textbf{''' + job["company"].replace('&', r'\&') +r'''} \hfill ''' + job["location"].replace('&', r'\&') +r'''\\
\textit{''' + job["position"].replace('&', r'\&') +r'''} \hfill ''' + job["startDate"].replace('&', r'\&') +r''' - ''' + job["endDate"].replace('&', r'\&') +r'''\\
\vspace{-1mm}
\begin{itemize} \itemsep 1pt
'''
            duties = "\n".join([f"      \\item {duty}" for duty in job["highlights"]])
            s_formatted_body += duties + "\n"
            s_formatted_body += r'''
\end{itemize}
'''

    s_formatted_body += r'''

\header{''' + data["headings"]['skills'] + r'''}
\begin{tabular}{ l l }
'''
    for skill in data["skills"]:
        if "name" in skill:
            s_formatted_body += skill["name"] + r''':  &''' + ", ".join([f" {keys}" for keys in skill["keywords"]]) +r'''\\'''
            s_formatted_body += "\n"
    s_formatted_body+= r'''\end{tabular}
\vspace{2mm}

\header{''' + data["headings"]['projects'] + r'''}
'''
    for project in data["projects"]:
        if "name" in project:
            s_formatted_body += r'''{\textbf{''' + project["name"] + r'''}} {\sl ''' + ", ".join(project["keywords"]) + r'''} \hfill '''+  project["url"].replace('_', r'\_')+r'''\\
'''+project["description"] + r'''\\
\vspace*{2mm}
'''


    s_formatted_body += r'''

\header{''' + data["headings"]['awards'] + r'''}
'''

    for award in data["awards"]:
        if "title" in award:
            s_formatted_body += r'''\textbf{'''+ award["title"]+r'''} \hfill '''+award["awarder"] +r'''\\'''
            s_formatted_body += "\n"
            if "summary" in award:
                s_formatted_body += award["summary"].replace('&', r'\&')
            s_formatted_body += r''' \hfill '''+ award["date"] + r'''\\'''
            s_formatted_body += "\n"
            s_formatted_body += r'''\vspace*{2mm}'''
            s_formatted_body += "\n"
    s_formatted_body+= r'''

\

'''



    return s_formatted_head, s_formatted_body

def template_two(data, image_name):
    s_formatted_head = r'''
\newlength{\outerbordwidth}
\pagestyle{empty}
\raggedbottom
\raggedright
\usepackage[svgnames]{xcolor}
\usepackage{framed}
\usepackage{tocloft}
\usepackage{enumitem}
\usepackage{textcomp}
\usepackage[utf8]{inputenc}


\setlength{\outerbordwidth}{3pt}
\definecolor{shadecolor}{gray}{0.75}
\definecolor{shadecolorB}{gray}{0.93}

\setlength{\evensidemargin}{-0.25in}
\setlength{\headheight}{0in}
\setlength{\headsep}{0in}
\setlength{\oddsidemargin}{-0.25in}
\setlength{\tabcolsep}{0in}
\setlength{\textheight}{9.5in}
\setlength{\textwidth}{7in}
\setlength{\topmargin}{-0.3in}
\setlength{\topskip}{0in}
\setlength{\voffset}{0.1in}


\newcommand{\resitem}[1]{\item #1 \vspace{-4pt}}
\newcommand{\resheading}[1]{
  \parbox{\textwidth}{\setlength{\FrameSep}{\outerbordwidth}
    \begin{shaded}
\setlength{\fboxsep}{0pt}\framebox[\textwidth][l]{\setlength{\fboxsep}{4pt}\fcolorbox{shadecolorB}{shadecolorB}{\textbf{\sffamily{\mbox{~}\makebox[6.762in][l]{\large #1} \vphantom{p\^{E}}}}}}
    \end{shaded}
  }\vspace{-11pt}
}
\newcommand{\ressubheading}[4]{
\begin{tabular*}{6.5in}{l@{\cftdotfill{\cftsecdotsep}\extracolsep{\fill}}r}
    \textbf{#1} & #2 \\
    \textit{#3} & \textit{#4} \\

\end{tabular*}\vspace{-6pt}}

\newcommand{\school}[4]{\vspace{1.5mm}
  \textbf{#1} \hfill #2 \textit{#3} \hfill \textit{#4} \vspace{1.5mm}
}

\newcommand{\job}[4]{
  \textbf{#1} \hfill #2 \hfill \textit{#3} \hfill \textit{#4}
}

\newcommand{\skill}[2]{
  \textbf{#1} #2
}

\newcommand{\project}[4]{ \vspace{1.5mm}
  \textbf{#1} #2 \hfill \textit{#3}#4 \vspace{1.5mm}
}

\newcommand{\award}[4]{ \vspace{1.5mm}
  \textbf{#1} #2 \hfill \textit{#3} #4 \vspace{1.5mm}
}
'''

    s_formatted_body = r'''
\begin{tabular*}{7in}{l@{\extracolsep{\fill}}r}
	\textbf{\Large ''' + data["basics"]["name"] + r'''} & \textit{''' + data["basics"]["email"] + r''' | ''' + data["basics"]["phone"] + r''' | ''' + data["basics"]["location"]["address"] + r'''}
\end{tabular*}


\resheading{''' + data["headings"]["education"] + r'''}
\begin{itemize}[leftmargin=*]
'''
    for education in data["education"]:
        s_formatted_body += r'''
        \item[]
	        \school
            {''' + education["institution"].replace('&', r'\&') + r'''}
            {''' + education["location"].replace('&', r'\&') + r'''\\}
                {''' + education["studyType"].replace('&', r'\&') + r''' ''' + education["area"].replace('&', r'\&') + r''', GPA:''' + education["gpa"].replace('&', r'\&') + r'''}
	      	    {''' + education["startDate"].replace('&', r'\&') + r''' | ''' + education["endDate"].replace('&', r'\&') + r'''}
'''
    s_formatted_body += r'''
\end{itemize}
'''
    s_formatted_body += r'''
\resheading{''' + data["headings"]['work'] + r'''}
\begin{itemize}[leftmargin=*]
'''

# Loop over work history to insert job entries
    for job in data["work"]:
        if "company" in job:
            s_formatted_body += r'''
            \item[]
	      	      \job
	      	      {''' + job["company"].replace('&', r'\&') +r'''}
	      	      {''' + job["location"].replace('&', r'\&') +r'''}
	      	      {''' + job["position"].replace('&', r'\&') +r'''}
	      	      {''' + job["startDate"].replace('&', r'\&') +r''' | ''' + job["endDate"].replace('&', r'\&') +r'''}
	      	      \begin{itemize}
'''
            for duties in job["highlights"]:
                s_formatted_body += r'''
                        \item ''' + duties.replace('&', r'\&') +r'''
'''
            s_formatted_body += r'''
                \end{itemize}
'''

    s_formatted_body += r'''
\end{itemize}
\resheading{''' + data["headings"]['skills'] + r'''}
\begin{itemize}[leftmargin=*]
    \setlength\itemsep{0em}
'''
    for skill in data["skills"]:
        if "name" in skill:
            s_formatted_body += r'''
              \item[] \skill{'''+skill["name"]+r'''}{''' + ", ".join([f" {keys}" for keys in skill["keywords"]]) +r'''}
'''
    s_formatted_body+= r'''\end{itemize}
	      \resheading{''' + data["headings"]['projects'] + r'''}
	      \begin{itemize}[leftmargin=*]
'''
    for project in data["projects"]:
        if "name" in project:
            s_formatted_body += r'''
                \item[]
	      	        \project
	      	        {''' + project["name"] + r'''}
	      	        {''' + ", ".join(project["keywords"]) + r'''}
	      	        {'''+  project["url"].replace('_','\_')+r'''}
	      	        {\\'''+project["description"] + r'''}
'''


    s_formatted_body += r'''\end{itemize}
	      \resheading{''' + data["headings"]['awards'] + r'''}
	      \begin{itemize}[leftmargin=*]
'''

    for award in data["awards"]:
        if "title" in award:
            s_formatted_body += r'''
                \item[]
	      	        \award
	      	        {'''+ award["title"]+r'''}
	      	        {'''+ award["date"] + r'''}
	      	        {'''+award["awarder"] +r'''}'''
            if "summary" in award:
                s_formatted_body += r'''
	      	      {\\'''+ award["summary"].replace('&', r'\&') +r'''}
'''
            else:
                s_formatted_body += r'''
                {}'''

    s_formatted_body+= r'''
\end{itemize}
	      \

'''



    return s_formatted_head, s_formatted_body

def template_three(data, image_name):
    s_formatted_head = r'''
\usepackage{latexsym}
\usepackage{xcolor}
\usepackage{float}
\usepackage{ragged2e}
\usepackage[empty]{fullpage}
\usepackage{wrapfig}
\usepackage{lipsum}
\usepackage{tabularx}
\usepackage{titlesec}
\usepackage{geometry}
\usepackage{marvosym}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage{multicol}
\usepackage{graphicx}
\usepackage{cfr-lm}

\setlength{\multicolsep}{0pt}
\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\geometry{left=1.4cm, top=0.8cm, right=1.2cm, bottom=1cm}
% Adjust margins
%\addtolength{\oddsidemargin}{-0.5in}
%\addtolength{\evensidemargin}{-0.5in}
%\addtolength{\textwidth}{1in}
\usepackage[most]{tcolorbox}
\tcbset{
	frame code={}
	center title,
	left=0pt,
	right=0pt,
	top=0pt,
	bottom=0pt,
	colback=gray!20,
	colframe=white,
	width=\dimexpr\textwidth\relax,
	enlarge left by=-2mm,
	boxsep=4pt,
	arc=0pt,outer arc=0pt,
}

\urlstyle{same}

\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-7pt}]

%-------------------------
% Custom commands
\newcommand{\resumeItem}[2]{
  \item{
    \textbf{#1}{:\hspace{0.5mm}#2 \vspace{-0.5mm}}
  }
}

\newcommand{\resumePOR}[3]{
\vspace{0.5mm}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1},\hspace{0.3mm}#2 & \textit{\small{#3}}
    \end{tabular*}
    \vspace{-2mm}
}

\newcommand{\resumeSubheading}[4]{
\vspace{0.5mm}\item
    \begin{tabular*}{0.98\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1} & \textit{\footnotesize{#4}} \\
        \textit{\footnotesize{#3}} &  \footnotesize{#2}\\
    \end{tabular*}
    \vspace{-2.4mm}
}

\newcommand{\resumeProject}[4]{
\vspace{0.5mm}\item
    \begin{tabular*}{0.98\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1} & \textit{\footnotesize{#3}} \\
        \footnotesize{\textit{#2}} & \footnotesize{#4}
    \end{tabular*}
    \vspace{-2.4mm}
}

\newcommand{\resumeSubItem}[2]{\resumeItem{#1}{#2}\vspace{-4pt}}

% \renewcommand{\labelitemii}{$\circ$}
\renewcommand{\labelitemi}{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=*,labelsep=0mm]}
\newcommand{\resumeHeadingSkillStart}{\begin{itemize}[leftmargin=*,itemsep=1.7mm, rightmargin=2ex]}
\newcommand{\resumeItemListStart}{\begin{justify}\begin{itemize}[leftmargin=3ex, rightmargin=2ex, noitemsep,labelsep=1.2mm,itemsep=0mm]\small}

\newcommand{\resumeSubHeadingListEnd}{\end{itemize}\vspace{2mm}}
\newcommand{\resumeHeadingSkillEnd}{\end{itemize}\vspace{-2mm}}
\newcommand{\resumeItemListEnd}{\end{itemize}\end{justify}\vspace{-2mm}}
\newcommand{\cvsection}[1]{%
\vspace{2mm}
\begin{tcolorbox}
    \textbf{\large #1}
\end{tcolorbox}
    \vspace{-4mm}
}

\newcolumntype{L}{>{\raggedright\arraybackslash}X}%
\newcolumntype{R}{>{\raggedleft\arraybackslash}X}%
\newcolumntype{C}{>{\centering\arraybackslash}X}%
%---- End of Packages and Functions ------

%-------------------------------------------
%%%%%%  CV STARTS HERE  %%%%%%%%%%%
%%%%%% DEFINE ELEMENTS HERE %%%%%%%
\newcommand{\name}{Students Name} % Your Name
\newcommand{\course}{} % Your Course
\newcommand{\department}{}
\newcommand{\roll}{XXXXXXXXX} % Your Roll No.
\newcommand{\phone}{XXXXXXXXX} % Your Phone Number
\newcommand{\emaila}{something@example.com} %Email 1
\newcommand{\emailb}{somethingelse@example.com} %Email 2
\newcommand{\github}{USERID} %Github
\newcommand{\website}{https://example.com} %Website
\newcommand{\linkedin}{LINKEDINUSERID} %linkedin


'''
    s_formatted_body = r'''
\fontfamily{cmr}\selectfont
%----------HEADING-----------------
\parbox{2.8cm}{%

\includegraphics[width=2.5cm,clip]{''' + image_name + r'''}
% replace the fields with your details


}\parbox{\dimexpr\linewidth-3.1cm\relax}{
\begin{tabularx}{\linewidth}{L r}
  {} & \href{mailto:''' + data["basics"]["email"] + r'''}{''' + data["basics"]["email"] + r'''}\\
  \textbf{\LARGE ''' + data["basics"]["name"] + r'''} &  ''' + data["basics"]["phone"] + r'''\\
  {} &  {''' + data["basics"]["location"]["address"] + r'''} \\
  {} & \ {}
    \end{tabularx}
}



% %-----------EDUCATION-----------------
\section{Education}
\setlength{\tabcolsep}{5pt} % Default value: 6pt

\small{\begin{tabularx}
{\dimexpr\textwidth-3mm\relax}{|c|C|c|c|}

  \hline
  \textbf{Degree/Certificate } & \textbf{Institute/Board} & \textbf{CGPA/Percentage} & \textbf{Year}\\
'''
    for education in data["education"]:
        s_formatted_body += r'''
        \hline
        ''' + education["studyType"].replace('&', r'\&') + r'''  & ''' + education["institution"].replace('&', r'\&') + r''' & ''' + education["gpa"].replace('&', r'\&') + r''' & ''' + education["startDate"].replace('&', r'\&') + r'''-''' + education["endDate"].replace('&', r'\&') + r'''\\
'''
    s_formatted_body += r'''
  \hline
\end{tabularx}}
\vspace{-2mm}

% %-----------EXPERIENCE-----------------
 \section{Experience}
   \resumeSubHeadingListStart
'''
    for job in data["work"]:
        if "company" in job:
            s_formatted_body += r'''
            \resumeSubheading
                {''' + job["company"].replace('&', r'\&') +r'''}{''' + job["company"].replace('&', r'\&') +r'''}
                {''' + job["position"].replace('&', r'\&') +r'''}{''' + job["startDate"].replace('&', r'\&') +r''' - ''' + job["endDate"].replace('&', r'\&') +r'''}
                \resumeItemListStart
'''
            for duties in job["highlights"]:
                s_formatted_body += r'''
                \item {''' + duties.replace('&', r'\&') +r'''}
'''
            s_formatted_body += r'''
                \resumeItemListEnd
'''
    s_formatted_body += r'''
     \resumeSubHeadingListEnd
 \vspace{-5.5mm}

\section{Projects}
\resumeSubHeadingListStart
'''

    for project in data["projects"]:
        if "name" in project:
            s_formatted_body += r'''
                \resumeProject
                    {''' + project["name"] + r'''}
                    {''' + ", ".join(project["keywords"]) + r'''}
                    {\href{'''+  project["url"].replace('_','\_')+r'''}{'''+  project["url"].replace('_','\_')+r'''}}
                    {}
                    \resumeItemListStart
                        \item {'''+project["description"] + r'''}
                    \resumeItemListEnd
'''
    s_formatted_body += r'''



  \resumeSubHeadingListEnd
\vspace{-5.5mm}


\section{Skills}
\resumeHeadingSkillStart
'''
    for skill in data["skills"]:
        if "name" in skill:
            s_formatted_body += r'''
            \resumeSubItem{'''+skill["name"]+r'''}
                {''' + ", ".join([f" {keys}" for keys in skill["keywords"]]) +r'''}
'''

    s_formatted_body += r'''
\resumeHeadingSkillEnd


\section{Certifications}
\resumeHeadingSkillStart
'''
    for award in data["awards"]:
        if "title" in award:
            s_formatted_body += r'''
            \resumeSubItem{'''+ award["title"]+r'''}
                {'''+award["awarder"].replace('&','\&') +r'''}
'''
    s_formatted_body += r'''
\resumeHeadingSkillEnd
'''
    return s_formatted_head, s_formatted_body

def template_four(data, image_name):
    s_formatted_head = r'''
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{fontawesome5}
\usepackage{multicol}
\usepackage[dvipsnames]{xcolor}
\setlength{\multicolsep}{-3.0pt}
\setlength{\columnsep}{-1pt}
\input{glyphtounicode}


%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.6in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1.19in}
\addtolength{\topmargin}{-.7in}
\addtolength{\textheight}{1.4in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\color{BrickRed}\scshape\raggedright\large\bfseries
}{}{0em}{}[\color{BrickRed}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\classesList}[4]{
    \item\small{
        {#1 #2 #3 #4 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & \textbf{\small #2} \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{1.001\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & \textbf{\small #2}\\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemi{$\vcenter{\hbox{\tiny$\bullet$}}$}
\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

'''
    s_formatted_body = r'''
\begin{center}
  {\Huge \scshape ''' + data["basics"]["name"].replace('&',r'\&') + r'''} \\ \vspace{5pt}
  \small \raisebox{-0.1\height}\faPhone\ ''' + data["basics"]["phone"].replace('&',r'\&') + r'''~ \href{mailto:''' + data["basics"]["email"].replace('&',r'\&') + r'''}{\raisebox{-0.2\height}\faEnvelope\ {''' + data["basics"]["email"].replace('&',r'\&') + r'''}} ~
  \href{https://algouniversity.com/accelerator}{\raisebox{-0.2\height}{{''' + data["basics"]["location"]["address"].replace('&',r'\&') + r'''}}}  ~

  \vspace{-8pt}
\end{center}

\vspace{-10pt}
%-----------EDUCATION-----------
\section{''' + data["headings"]["education"].replace('&',r'\&') + r'''}
\resumeSubHeadingListStart
'''
    for edu in data["education"]:
        s_formatted_body += r'''
    \resumeSubheading
    {''' + edu["institution"].replace('&',r'\&') + r'''}{''' + edu["startDate"].replace('&',r'\&') + r''' - ''' + edu["endDate"].replace('&', r'\&') + r'''}{''' + edu["studyType"].replace('&', r'\&') + r''' in ''' + edu["area"].replace('&', r'\&') + r'''}{''' + edu["gpa"].replace('&', r'\&') + r''' cgpa}
    '''
    s_formatted_body += r'''
\resumeSubHeadingListEnd
\vspace{-15pt}



% -----------EXPERIENCE-----------
\section{''' + data["headings"]["work"].replace('&',r'\&') + r'''}
\resumeSubHeadingListStart
'''
    for work in data["work"]:
        if "company" in work:
          s_formatted_body += r'''
    \resumeSubheading
    {''' + work["company"].replace('&',r'\&') + r'''}{''' + work["startDate"].replace('&',r'\&') + r''' - ''' + work["endDate"].replace('&',r'\&') + r'''}
    {''' + work["position"].replace('&',r'\&') + r'''}{''' + work["location"].replace('&',r'\&') + r'''}
    \resumeItemListStart
    '''
          for item in work["highlights"]:
            s_formatted_body += r'''
        \resumeItem{''' + item.replace('&', r'\&') + r'''}'''
          s_formatted_body += r'''
    \resumeItemListEnd

        '''
    s_formatted_body += r'''
\resumeSubHeadingListEnd
\vspace{-16pt}

\section{''' + data["headings"]["projects"].replace('&', r'\&') + r'''}
\vspace{-5pt}
\resumeSubHeadingListStart'''

    for project in data["projects"]:
      if "name" in project:
        s_formatted_body += r'''
    \resumeProjectHeading{\textbf{''' + project["name"].replace('&', r'\&') + r'''}}{\href{''' + project["url"].replace('_','\_')+r'''}{\underline{''' + project["url"].replace('_','\_')+r'''}}}
    \resumeItemListStart
      \resumeItem{'''+project["description"].replace('&', r'\&') + r'''}'''

        s_formatted_body += r'''
    \resumeItemListEnd
'''
    s_formatted_body += r'''
\vspace{-13pt}

\resumeSubHeadingListEnd
\vspace{-3pt}


%
%-----------PROGRAMMING SKILLS-----------
\section{''' + data["headings"]["skills"].replace('&', r'\&') + r'''}
\begin{itemize}[leftmargin=0.15in, label={}]
  \item{
'''
    for skill in data["skills"]:
        if "name" in skill:
          s_formatted_body += r'''
        \textbf{'''+skill["name"]+r'''}{: ''' + ", ".join([f" {keys}" for keys in skill["keywords"]]) +r'''} \\'''
    s_formatted_body += r'''
    }

\end{itemize}
\vspace{-15pt}

\section{''' + data["headings"]["awards"].replace('&', r'\&') + r'''}
\resumeSubHeadingListStart
'''
    for award in data["awards"]:
      if "title" in award:
        s_formatted_body += r'''
  \resumeSubheading{'''+ award["title"].replace('&','\&') +r'''}{'''+ award["date"].replace('&','\&') +r'''}{'''+ award["awarder"].replace('&','\&') +r'''}{}'''
        if "summary" in award:
           s_formatted_body += r'''
  \resumeItemListStart
    \resumeItem{'''+ award["summary"].replace('&','\&') +r'''}
  \resumeItemListEnd'''

    s_formatted_body += r'''
\resumeSubHeadingListEnd
'''
    return s_formatted_head, s_formatted_body