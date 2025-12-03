# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           perl-Getopt-Long
Version:        2.58
Release:        %autorelease
Summary:        Extended processing of command line options
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Getopt-Long
#!RemoteAsset
Source0:        http://www.cpan.org/authors/id/J/JV/JV/Getopt-Long-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-rpm-packaging
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Usage) >= 1.14

Requires:       perl(Pod::Usage) >= 1.14

%description
The Getopt::Long module implements an extended getopt function called
GetOptions(). It parses the command line from @ARGV, recognizing and
removing specified options and their possible values.

%prep
%setup -q -n Getopt-Long-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%{make_build}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md

%changelog
%{?autochangelog}
