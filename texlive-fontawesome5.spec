Name:		texlive-fontawesome5
Version:	63207
Release:	2
Summary:	Font Awesome 5 with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fontawesome5
License:	ofl lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome5.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontawesome5.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides LaTeX support for the included "Font
Awesome 5 Free" icon set. These icons were designed by Fort
Awesome and released under the SIL OFL 1.1 license. The
commercial "Pro" version is also supported, if it is installed
and XeLaTeX or LuaLaTeX is used.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/fontawesome5
%{_texmfdistdir}/fonts/type1/public/fontawesome5
%{_texmfdistdir}/fonts/tfm/public/fontawesome5
%{_texmfdistdir}/fonts/opentype/public/fontawesome5
%{_texmfdistdir}/fonts/map/dvips/fontawesome5
%{_texmfdistdir}/fonts/enc/dvips/fontawesome5
%doc %{_texmfdistdir}/doc/fonts/fontawesome5

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
