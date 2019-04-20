#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : terminado
Version  : 0.8.2
Release  : 22
URL      : https://files.pythonhosted.org/packages/ae/fc/f5c7c36ac0da236078a26da7dce5748db45c8273cd551232ae01b26043b3/terminado-0.8.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ae/fc/f5c7c36ac0da236078a26da7dce5748db45c8273cd551232ae01b26043b3/terminado-0.8.2.tar.gz
Summary  : Terminals served to xterm.js using Tornado websockets
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: terminado-license = %{version}-%{release}
Requires: terminado-python = %{version}-%{release}
Requires: terminado-python3 = %{version}-%{release}
Requires: XStatic
Requires: XStatic-term.js
Requires: terminado
Requires: tornado
BuildRequires : buildreq-distutils3

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

%description python3
python3 components for the terminado package.


%prep
%setup -q -n terminado-0.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554402889
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/terminado
cp LICENSE %{buildroot}/usr/share/package-licenses/terminado/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/terminado/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
