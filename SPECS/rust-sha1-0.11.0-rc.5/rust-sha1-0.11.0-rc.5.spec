# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha1
%global full_version 0.11.0-rc.5
%global pkgname sha1-0.11.0-rc.5

Name:           rust-sha1-0.11.0-rc.5
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "sha1"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:3b167252f3c126be0d8926639c4c4706950f01445900c4b3db0fd7e89fcb750a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cpufeatures-0.2/default) >= 0.2.0
Requires:       crate(digest-0.11.0-rc.11/default) >= 0.11.0-rc.11

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/force-soft) = %{version}

%description
Source code for takopackized Rust crate "sha1"

%package     -n %{name}+alloc
Summary:        SHA-1 hash function - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11.0-rc.11/alloc) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sha1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        SHA-1 hash function - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/oid) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sha1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        SHA-1 hash function - feature "oid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11.0-rc.11/oid) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust sha1 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        SHA-1 hash function - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11.0-rc.11/zeroize) >= 0.11.0-rc.11
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust sha1 crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
