# revision 33147
# category Package
# catalog-ctan /systems/knuth/local
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license knuth
# catalog-version undef
Name:		texlive-knuth-local
Version:	20140226
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
%{_texmfdistdir}/fonts/source/public/knuth-local/black.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/blackaps.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/blackimagen.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/blacklino.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/blacklj.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/domino.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/gray.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/grayaps.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/grayimagen.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/grayimagen3.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/grayimagenlight.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/graylj.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/local.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/logod10.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/logosl9.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/mfman.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/oneone.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/random.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/slantaps4.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/slantimagen4.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/slantimagen6.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/slantlino4.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/slantlj4.mf
%{_texmfdistdir}/fonts/source/public/knuth-local/snfont.mf
%{_texmfdistdir}/fonts/tfm/public/knuth-local/domino.tfm
%{_texmfdistdir}/fonts/tfm/public/knuth-local/random.tfm
%{_texmfdistdir}/fonts/tfm/public/knuth-local/snfont.tfm
%{_texmfdistdir}/mft/knuth-local/e.mft
%{_texmfdistdir}/tex/plain/knuth-local/xepsf.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex mft %{buildroot}%{_texmfdistdir}

