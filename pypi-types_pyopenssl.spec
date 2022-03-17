#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-types_pyopenssl
Version  : 22.0.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/19/20/28f276b0253cd398b894f1290a6a0b68d7097a3a444b3eb3422279d37f14/types-pyOpenSSL-22.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/19/20/28f276b0253cd398b894f1290a6a0b68d7097a3a444b3eb3422279d37f14/types-pyOpenSSL-22.0.1.tar.gz
Summary  : Typing stubs for pyOpenSSL
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-types_pyopenssl-python = %{version}-%{release}
Requires: pypi-types_pyopenssl-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(types_cryptography)

%description
No detailed description available

%package python
Summary: python components for the pypi-types_pyopenssl package.
Group: Default
Requires: pypi-types_pyopenssl-python3 = %{version}-%{release}

%description python
python components for the pypi-types_pyopenssl package.


%package python3
Summary: python3 components for the pypi-types_pyopenssl package.
Group: Default
Requires: python3-core
Provides: pypi(types_pyopenssl)
Requires: pypi(types_cryptography)

%description python3
python3 components for the pypi-types_pyopenssl package.


%prep
%setup -q -n types-pyOpenSSL-22.0.1
cd %{_builddir}/types-pyOpenSSL-22.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647529017
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
