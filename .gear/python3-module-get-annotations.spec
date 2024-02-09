%define pypi_name get-annotations

Name:           python3-module-%pypi_name
Version:        0.1.2
Release:        alt1
Summary:        A backport of Python 3.10's inspect.get_annotations() function.
Group:          Development/Python3

License:        MIT
URL:            https://github.com/shawwn/get-annotations?tab=License-1-ov-file
Source0:        %{name}-%{version}.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-dev
BuildRequires:  python3(setuptools)
BuildRequires:  python3(wheel)
BuildRequires:  python3-module-poetry

%py3_provides %pypi_name

BuildArch:      noarch

%description
This package provides a backport of the inspect.get_annotations() function from Python 3.10, making it available for use in earlier Python versions. It is designed to facilitate compatibility with newer Python features, particularly for interpreting annotations in a manner consistent with Python 3.10's enhanced functionality.

%prep
%setup -v

%build
%pyproject_build

%install
%pyproject_install
install -Dm644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE


%files
%doc README.md
%_licensedir/%name/LICENSE
%python3_sitelibdir/*

%changelog
* Thu Feb 8 2024 Aleksandr A. Voyt <vojtaa@basealt.ru> 0.1.2-alt1
- First package version

