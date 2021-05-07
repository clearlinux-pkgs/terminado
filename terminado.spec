#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : terminado
Version  : 0.9.4
Release  : 37
URL      : https://files.pythonhosted.org/packages/93/65/bdfa6296624e647008bec3dc47a1d2c4f52ab6104b55b3961e0b30e9b80f/terminado-0.9.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/65/bdfa6296624e647008bec3dc47a1d2c4f52ab6104b55b3961e0b30e9b80f/terminado-0.9.4.tar.gz
Summary  : Tornado websocket backend for the Xterm.js Javascript terminal emulator library.
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: terminado-license = %{version}-%{release}
Requires: terminado-python = %{version}-%{release}
Requires: terminado-python3 = %{version}-%{release}
Requires: ptyprocess
Requires: tornado
BuildRequires : buildreq-distutils3
BuildRequires : ptyprocess
BuildRequires : tornado

%description
This is a `Tornado <http://tornadoweb.org/>`_ websocket backend for the
`Xterm.js <https://xtermjs.org/>`_ Javascript terminal emulator
library.

%package license
Summary: license components for the terminado package.
Group: Default

%description license
license components for the terminado package.


%package python
Summary: python components for the terminado package.
Group: Default
Requires: terminado-python3 = %{version}-%{release}

%description python
python components for the terminado package.


%package python3
Summary: python3 components for the terminado package.
Group: Default
Requires: python3-core
Provides: pypi(terminado)
Requires: pypi(ptyprocess)
Requires: pypi(tornado)

%description python3
python3 components for the terminado package.


%prep
%setup -q -n terminado-0.9.4
cd %{_builddir}/terminado-0.9.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619280390
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/terminado
cp %{_builddir}/terminado-0.9.4/LICENSE %{buildroot}/usr/share/package-licenses/terminado/c469161e7fddd1ac349b03fa2732d18e96c579d2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/terminado/c469161e7fddd1ac349b03fa2732d18e96c579d2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
