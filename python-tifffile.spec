%global module tifffile

Summary:        Read and write TIFF(r) files with Python
Name:           python-%{module}
Version:        2023.9.26
Release:        1
Source0:	https://github.com/cgohlke/tifffile/archive/refs/tags/v%{version}/%{module}-%{version}.tar.gz
License:        BSD
Group:          Development/Python
URL:            https://www.lfd.uci.edu/~gohlke/

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
# Testing
#BuildRequires:	python3dist(fsspec)
#BuildRequires:	python3dist(lxml)
#BuildRequires:	python3dist(numpy)
#BuildRequires:	python3dist(pytest)

BuildArch:      noarch

%description
Tifffile is a Python library to
  * store numpy arrays in TIFF (Tagged Image File Format) files, and
  * read image and metadata from TIFF-like files used in bioimaging.

%files
%license LICENSE
%doc README.rst
%{_bindir}/*
%{python3_sitelib}/%{module}/
%{python3_sitelib}/%{module}-*.egg-info/

#---------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py3_build

%install
%py3_install

