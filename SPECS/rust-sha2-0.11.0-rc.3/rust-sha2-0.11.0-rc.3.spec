# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sha2
%global full_version 0.11.0-rc.3
%global pkgname sha2-0.11.0-rc.3

Name:           rust-sha2-0.11.0-rc.3
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "sha2"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/hashes
#!RemoteAsset:  sha256:19d43dc0354d88b791216bb5c1bfbb60c0814460cc653ae0ebd71f286d0bd927
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(cpufeatures-0.2/default) >= 0.2.0
Requires:       crate(digest-0.11.0-rc.4/default) >= 0.11.0-rc.4

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "sha2"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11.0-rc.4/alloc) >= 0.11.0-rc.4
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/oid) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+oid
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "oid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11.0-rc.4/oid) >= 0.11.0-rc.4
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+oid
This metapackage enables feature "oid" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Pure Rust implementation of the SHA-2 hash function family including SHA-224, SHA-256, SHA-384, and SHA-512 - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(digest-0.11.0-rc.4/zeroize) >= 0.11.0-rc.4
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust sha2 crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
