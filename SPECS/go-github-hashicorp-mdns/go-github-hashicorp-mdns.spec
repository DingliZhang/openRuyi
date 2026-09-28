# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           mdns
%define go_import_path  github.com/hashicorp/mdns

# The server/client tests need real multicast networking, which the isolated
# build sandbox restricts; run them but tolerate the failures.
%define go_test_ignore_failure 1

Name:           go-github-hashicorp-mdns
Version:        1.0.7
Release:        %autorelease
Summary:        Simple mDNS client/server library in Go
License:        MIT
URL:            https://github.com/hashicorp/mdns
#!RemoteAsset:  sha256:e511deeb21156c917cc23384ef043f5e3d22aa9064f01ed751ce0a4c3a25e274
Source0:        https://github.com/hashicorp/mdns/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(golang.org/x/net)

Provides:       go(github.com/hashicorp/mdns) = %{version}

Requires:       go(github.com/miekg/dns)
Requires:       go(golang.org/x/net)

%description
mdns is a simple multicast DNS (mDNS) client and server library, used for
zero-configuration service discovery. It is an optional backend of the
hashicorp/serf agent CLI.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
