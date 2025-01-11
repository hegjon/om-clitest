%global forgeurl https://github.com/aureliojargas/clitest
%global tag %{version}

Name:    clitest
Version: 0.5.0
Release: 5%{?dist}
Summary: Command Line Tester

License: MIT
URL:     %{forgeurl}

%forgemeta
Source:  %{forgesource}

BuildArch:     noarch
BuildRequires: /usr/bin/perl
BuildRequires: bash dash mksh zsh
BuildRequires: make

Requires: diffutils
Requires: sed
Requires: grep
Suggests: perl

%description
clitest is a portable POSIX shell script that performs automatic testing in \
Unix command lines.

It's the same concept as in Python's doctest module: you document both the \
commands and their expected output, using the familiar interactive prompt \
format, and a specialized tool tests them.

%prep
%forgesetup

%build
#no build, only shell script

%check
make test docker_run=

%install
install -D -m755 -p clitest %{buildroot}%{_bindir}/clitest

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/clitest

