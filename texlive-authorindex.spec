# revision 18835
# category Package
# catalog-ctan /indexing/authorindex
# catalog-date 2008-08-10 21:45:45 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-authorindex
Version:	20080810
Release:	1
Summary:	Index citations by author names
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/indexing/authorindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authorindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authorindex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-authorindex.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package allows the user to create an index of all authors
cited in a LaTeX document. Each author entry in the index
contains the pages where these citations occur. Alternatively,
the package can list the labels of the citations that appear in
the references rather than the text pages. The package relies
on BibTeX being used to handle citations. Additionally, it
requires Perl (version 5 or higher).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/authorindex/authorindex authorindex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
