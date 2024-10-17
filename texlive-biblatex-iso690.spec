Name:		texlive-biblatex-iso690
Version:	62866
Release:	2
Summary:	BibLaTeX style for ISO 690 standard
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-iso690
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-iso690.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-iso690.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a bibliography and citation style which
conforms to the latest revision of the international standard
ISO 690:2010. The implementation follows BibLaTeX conventions
and requires BibLaTeX [?] 3.4 and biber [?] 2.5.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-iso690
%doc %{_texmfdistdir}/doc/latex/biblatex-iso690

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
