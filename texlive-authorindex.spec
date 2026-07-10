%global tl_name authorindex
%global tl_revision 51757

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Index citations by author names
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/indexing/authorindex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authorindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authorindex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(authorindex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the user to create an index of all authors cited in
a LaTeX document. Each author entry in the index contains the pages
where these citations occur. Alternatively, the package can list the
labels of the citations that appear in the references rather than the
text pages. The package relies on BibTeX being used to handle citations.
Additionally, it requires Perl (version 5 or higher).

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
%dir %{_datadir}/texmf-dist/texmf-dist
%dir %{_datadir}/texmf-dist/texmf-dist/doc
%dir %{_datadir}/texmf-dist/texmf-dist/scripts
%dir %{_datadir}/texmf-dist/texmf-dist/tex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/texmf-dist/scripts/authorindex
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/texmf-dist/doc/latex/authorindex
%dir %{_datadir}/texmf-dist/texmf-dist/tex/latex/authorindex
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/authorindex/COPYING
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/authorindex/NEWS
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/authorindex/README
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/authorindex/authorindex.pdf
%doc %{_datadir}/texmf-dist/texmf-dist/doc/latex/authorindex/authorindex.tex
%{_datadir}/texmf-dist/texmf-dist/scripts/authorindex/authorindex
%{_datadir}/texmf-dist/texmf-dist/tex/latex/authorindex/authorindex.sty
