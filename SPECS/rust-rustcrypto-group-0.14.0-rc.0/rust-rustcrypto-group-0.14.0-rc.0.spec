# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustcrypto-group
%global full_version 0.14.0-rc.0
%global pkgname rustcrypto-group-0.14.0-rc.0

Name:           rust-rustcrypto-group-0.14.0-rc.0
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "rustcrypto-group"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/group
#!RemoteAsset:  sha256:57c4b1463f274a3ff6fb2f44da43e576cb9424367bd96f185ead87b52fe00523
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.10) >= 0.10.0
Requires:       crate(rustcrypto-ff-0.14.0-rc.0) >= 0.14.0-rc.0
Requires:       crate(subtle-2) >= 2.2.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rustcrypto-group"

%package     -n %{name}+chacha20
Summary:        Elliptic curve group traits and utilities - feature "chacha20"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chacha20-0.10.0-rc.10/rng) >= 0.10.0-rc.10
Provides:       crate(%{pkgname}/chacha20) = %{version}

%description -n %{name}+chacha20
This metapackage enables feature "chacha20" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memuse
Summary:        Elliptic curve group traits and utilities - feature "memuse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memuse-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/memuse) = %{version}

%description -n %{name}+memuse
This metapackage enables feature "memuse" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Elliptic curve group traits and utilities - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.10.0-rc.8) >= 0.10.0-rc.8
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tests
Summary:        Elliptic curve group traits and utilities - feature "tests"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/chacha20) = %{version}
Requires:       crate(%{pkgname}/rand) = %{version}
Provides:       crate(%{pkgname}/tests) = %{version}

%description -n %{name}+tests
This metapackage enables feature "tests" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wnaf-memuse
Summary:        Elliptic curve group traits and utilities - feature "wnaf-memuse"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/memuse) = %{version}
Provides:       crate(%{pkgname}/wnaf-memuse) = %{version}

%description -n %{name}+wnaf-memuse
This metapackage enables feature "wnaf-memuse" for the Rust rustcrypto-group crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
