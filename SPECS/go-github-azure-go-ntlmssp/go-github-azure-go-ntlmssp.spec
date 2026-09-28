# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-ntlmssp
%define go_import_path  github.com/Azure/go-ntlmssp

Name:           go-github-azure-go-ntlmssp
Version:        0.1.1
Release:        %autorelease
Summary:        NTLM/Negotiate authentication over HTTP for Go
License:        MIT
URL:            https://github.com/Azure/go-ntlmssp
#!RemoteAsset:  sha256:9c4d159972a7bde756522e008484e8aa352007151d19baea9db4598f95be628c
Source0:        https://github.com/Azure/go-ntlmssp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/Azure/go-ntlmssp) = %{version}

%description
go-ntlmssp implements NTLMv2 authentication over HTTP. It covers
authentication only, not key exchange or encryption, and uses Unicode
protocol strings.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
