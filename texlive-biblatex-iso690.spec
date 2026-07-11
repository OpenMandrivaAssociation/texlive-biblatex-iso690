%global tl_name biblatex-iso690
%global tl_revision 62866

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4.1
Release:	%{tl_revision}.1
Summary:	BibLaTeX style for ISO 690 standard
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-iso690
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-iso690.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-iso690.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a bibliography and citation style which conforms to
the latest revision of the international standard ISO 690:2010. The
implementation follows BibLaTeX conventions and requires BibLaTeX [?]
3.4 and biber [?] 2.5.

