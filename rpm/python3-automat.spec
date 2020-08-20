%define upstream_version 20.2.0
Name:           python3-automat
Version:        %{upstream_version}
Release:        0
Summary:        Self-service finite-state machines for the programmer on the go
License:        MIT
URL:            https://github.com/sailfishos/python-automat
Source0:        %{name}-%{version}.tar.gz
Patch0:	        Skip-setup_requires.patch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sed

%description
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).

%prep
%autosetup -p1 -n %{name}-%{version}/upstream
# Remove bundled egg-info
rm -rf Automat.egg-info
# Set version number
sed "/version='VERSION'/s/VERSION/%{upstream_version}/" -i setup.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{_bindir}/automat-visualize
%{python3_sitelib}/automat
%{python3_sitelib}/Automat-%{upstream_version}-py%{python3_version}.egg-info/
