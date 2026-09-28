# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-termina
%global full_version 0.1.0
%global pkgname ratatui-termina-0.1

Name:           rust-ratatui-termina-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "ratatui-termina"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:c0bf912d9e66f057a759d92e386a280ea886b352ab757d6ac4d653c7ed2c43c2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(instability-0.3/default) >= 0.3.0
Requires:       crate(ratatui-core-0.1/default) >= 0.1.2
Requires:       crate(termina-0.3/default) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/unstable) = %{version}
Provides:       crate(%{pkgname}/unstable-backend-writer) = %{version}

%description
Source code for takopackized Rust crate "ratatui-termina"

%package     -n %{name}+document-features
Summary:        Termina backend for the Ratatui Terminal UI library - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust ratatui-termina crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scrolling-regions
Summary:        Termina backend for the Ratatui Terminal UI library - feature "scrolling-regions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ratatui-core-0.1/scrolling-regions) >= 0.1.2
Provides:       crate(%{pkgname}/scrolling-regions) = %{version}

%description -n %{name}+scrolling-regions
This metapackage enables feature "scrolling-regions" for the Rust ratatui-termina crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+underline-color
Summary:        Termina backend for the Ratatui Terminal UI library - feature "underline-color" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ratatui-core-0.1/underline-color) >= 0.1.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/underline-color) = %{version}

%description -n %{name}+underline-color
This metapackage enables feature "underline-color" for the Rust ratatui-termina crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
