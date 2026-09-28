# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           emoji
%define go_import_path  github.com/kyokomi/emoji/v2

Name:           go-github-kyokomi-emoji-v2
Version:        2.2.14
Release:        %autorelease
Summary:        :sushi: emoji terminal output for golang
License:        MIT
URL:            https://github.com/kyokomi/emoji
#!RemoteAsset:  sha256:ae8ccd13beee52a37b10b9e3b4b8823c08fe2042c66b9ce9c3d9ca6c161ebdbd
Source0:        https://github.com/kyokomi/emoji/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kyokomi/emoji/v2) = %{version}

%description
emoji provides emoji support for Go, turning :emoji: aliases into their Unicode characters.

# cmd/ is a code generator pulling goquery; not needed by the library.
%prep -a
rm -rf cmd

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
