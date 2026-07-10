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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a bibliography and citation style which conforms to
the latest revision of the international standard ISO 690:2010. The
implementation follows BibLaTeX conventions and requires BibLaTeX [?]
3.4 and biber [?] 2.5.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-iso690
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-iso690
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-iso690/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-iso690/biblatex-iso690-examples.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-iso690/biblatex-iso690.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-iso690/biblatex-iso690.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/bulgarian-iso.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/czech-iso.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/english-iso.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/french-iso.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/german-iso.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-alphabetic.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-alphabetic.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-alphabetic.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-authortitle.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-authortitle.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-authortitle.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-authoryear.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-authoryear.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-authoryear.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-fullcite.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-numeric.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-numeric.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso-numeric.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/iso.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/ngerman-iso.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/polish-iso.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/slovak-iso.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-iso690/spanish-iso.lbx
