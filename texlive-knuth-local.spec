Name:		texlive-knuth-local
Version:	20190228
Release:	1
Summary:	Knuth's local information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/local
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-local.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of experimental programs and developments based
on, or complementary to, the matter in his distribution
directories.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/knuth-local
%{_texmfdistdir}/fonts/tfm/public/knuth-local
%{_texmfdistdir}/mft/knuth-local
%{_texmfdistdir}/tex/plain/knuth-local

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex mft %{buildroot}%{_texmfdistdir}

