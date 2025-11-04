# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname zstandard

Name:           python-%{srcname}
Version:        0.25.0
Release:        %autorelease
Summary:        Zstandard bindings for Python
License:        BSD-3-Clause
URL:            https://github.com/indygreg/python-zstandard
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/z/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install): %{srcname} +auto

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros
BuildRequires:  zstd-devel

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
Provides:       bundled(zstd) = 1.5.7

%description
This project provides Python bindings for interfacing with
the Zstandard compression library.  A C extension and CFFI
interface are provided.

%generate_buildrequires


# TODO: Add python-ffi
%check

%files -f %{pyproject_files}
%license LICENSE zstd/COPYING
%doc README.rst

%changelog
%{?autochangelog}
