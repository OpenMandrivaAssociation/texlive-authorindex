Name:		texlive-authorindex
Version:	51757
Release:	1
Summary:	Index citations by author names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/indexing/authorindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authorindex.r51757.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authorindex.doc.r51757.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-authorindex.bin = %{EVRD}

%description
This package allows the user to create an index of all authors
cited in a LaTeX document. Each author entry in the index
contains the pages where these citations occur. Alternatively,
the package can list the labels of the citations that appear in
the references rather than the text pages. The package relies
on BibTeX being used to handle citations. Additionally, it
requires Perl (version 5 or higher).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/authorindex
%{_texmfdistdir}/scripts/authorindex/authorindex
%{_texmfdistdir}/tex/latex/authorindex/authorindex.sty
%doc %{_texmfdistdir}/doc/latex/authorindex/COPYING
%doc %{_texmfdistdir}/doc/latex/authorindex/NEWS
%doc %{_texmfdistdir}/doc/latex/authorindex/README
%doc %{_texmfdistdir}/doc/latex/authorindex/authorindex.pdf
%doc %{_texmfdistdir}/doc/latex/authorindex/authorindex.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/authorindex/authorindex authorindex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
