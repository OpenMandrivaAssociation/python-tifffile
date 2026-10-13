%global module tifffile

Summary:        Read and write TIFF(r) files with Python
Name:           python-%{module}
Version:        2026.7.14
Release:        1
Source0:	https://github.com/cgohlke/tifffile/archive/refs/tags/v%{version}/%{module}-%{version}.tar.gz
License:        BSD
Group:          Development/Python
URL:            https://www.lfd.uci.edu/~gohlke/

BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(setuptools)
# Testing
#BuildRequires:	python%%{pyver}dist(fsspec)
#BuildRequires:	python%%{pyver}dist(lxml)
#BuildRequires:	python%%{pyver}dist(numpy)
#BuildRequires:	python%%{pyver}dist(pytest)

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
%autosetup -n tifffile-2026.7.14

%build
%py3_build

%install
%py3_install

