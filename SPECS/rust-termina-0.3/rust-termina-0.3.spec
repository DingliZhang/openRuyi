# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name termina
%global full_version 0.3.3
%global pkgname termina-0.3

Name:           rust-termina-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "termina"
License:        MIT OR MPL-2.0
URL:            https://github.com/helix-editor/termina
#!RemoteAsset:  sha256:9048a889effe34a5cddee0af7f53285198b16dca3be510858d38dfdb3e62a04e
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(rustix-1/event) >= 1.0.0
Requires:       crate(rustix-1/std) >= 1.0.0
Requires:       crate(rustix-1/stdio) >= 1.0.0
Requires:       crate(rustix-1/termios) >= 1.0.0
Requires:       crate(signal-hook-0.3/default) >= 0.3.0
Requires:       crate(windows-sys-0.60/win32-security) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-console) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-io) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-threading) >= 0.60.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "termina"

%package     -n %{name}+event-stream
Summary:        Cross-platform VT manipulation library - feature "event-stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/event-stream) = %{version}

%description -n %{name}+event-stream
This metapackage enables feature "event-stream" for the Rust termina crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-legacy
Summary:        Cross-platform VT manipulation library - feature "windows-legacy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-sys-0.60/win32-security) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-console) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-io) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-threading) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-ui-input-keyboardandmouse) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-ui-windowsandmessaging) >= 0.60.0
Provides:       crate(%{pkgname}/windows-legacy) = %{version}

%description -n %{name}+windows-legacy
This metapackage enables feature "windows-legacy" for the Rust termina crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
