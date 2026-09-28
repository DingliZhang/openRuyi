# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name digest
%global full_version 0.11.0-rc.4
%global pkgname digest-0.11.0-rc.4

Name:           rust-digest-0.11.0-rc.4
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "digest"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/traits
#!RemoteAsset:  sha256:ea390c940e465846d64775e55e3115d5dc934acb953de6f6e6360bc232fe2bf7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(crypto-common-0.2.0-rc.5/default) >= 0.2.0-rc.5

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}

%description
Source code for takopackized Rust crate "digest"

%package     -n %{name}+blobby
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "blobby" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(blobby-0.4.0-pre.1/default) >= 0.4.0-pre.1
Provides:       crate(%{pkgname}/blobby) = %{version}
Provides:       crate(%{pkgname}/dev) = %{version}

%description -n %{name}+blobby
This metapackage enables feature "blobby" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev" feature.

%package     -n %{name}+block-buffer
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "block-buffer" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block-buffer-0.11.0-rc.5/default) >= 0.11.0-rc.5
Provides:       crate(%{pkgname}/block-api) = %{version}
Provides:       crate(%{pkgname}/block-buffer) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+block-buffer
This metapackage enables feature "block-buffer" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "block-api", and "default" features.

%package     -n %{name}+const-oid
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "const-oid" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-oid-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/const-oid) = %{version}
Provides:       crate(%{pkgname}/oid) = %{version}

%description -n %{name}+const-oid
This metapackage enables feature "const-oid" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "oid" feature.

%package     -n %{name}+getrandom
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(crypto-common-0.2.0-rc.5/getrandom) >= 0.2.0-rc.5
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crypto-common-0.2.0-rc.5/rand-core) >= 0.2.0-rc.5
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+subtle
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "subtle" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(subtle-2) >= 2.4.0
Provides:       crate(%{pkgname}/mac) = %{version}
Provides:       crate(%{pkgname}/subtle) = %{version}

%description -n %{name}+subtle
This metapackage enables feature "subtle" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mac" feature.

%package     -n %{name}+zeroize
Summary:        Traits for cryptographic hash functions and message authentication codes - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block-buffer-0.11.0-rc.5/zeroize) >= 0.11.0-rc.5
Requires:       crate(zeroize-1) >= 1.7.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust digest crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
