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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(authorindex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows the user to create an index of all authors cited in
a LaTeX document. Each author entry in the index contains the pages
where these citations occur. Alternatively, the package can list the
labels of the citations that appear in the references rather than the
text pages. The package relies on BibTeX being used to handle citations.
Additionally, it requires Perl (version 5 or higher).

