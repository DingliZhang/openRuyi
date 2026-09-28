# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name scrypt
%global full_version 0.12.0-rc.9
%global pkgname scrypt-0.12.0-rc.9

Name:           rust-scrypt-0.12.0-rc.9
Version:        0.12.0
Release:        %autorelease
Summary:        Rust crate "scrypt"
License:        MIT OR Apache-2.0
URL:            https://github.com/RustCrypto/password-hashes/tree/master/scrypt
#!RemoteAsset:  sha256:1f847dca682a96ca7c9a3683e155cc91f3acd57b6ff8fc19dcf4f5190bf732b3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(pbkdf2-0.13.0-rc.8/default) >= 0.13.0-rc.8
Requires:       crate(salsa20-0.11.0-rc.2) >= 0.11.0-rc.2
Requires:       crate(sha2-0.11.0-rc.3) >= 0.11.0-rc.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "scrypt"

%package     -n %{name}+alloc
Summary:        Scrypt password-based key derivation function - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6.0-rc.10/alloc) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Scrypt password-based key derivation function - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/password-hash) = %{version}
Requires:       crate(password-hash-0.6.0-rc.10/getrandom) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kdf
Summary:        Scrypt password-based key derivation function - feature "kdf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(kdf-0.1.0-pre.1/default) >= 0.1.0-pre.1
Provides:       crate(%{pkgname}/kdf) = %{version}

%description -n %{name}+kdf
This metapackage enables feature "kdf" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mcf
Summary:        Scrypt password-based key derivation function - feature "mcf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/phc) = %{version}
Requires:       crate(mcf-0.6.0-rc.3/default) >= 0.6.0-rc.3
Requires:       crate(subtle-2) >= 2.0.0
Provides:       crate(%{pkgname}/mcf) = %{version}

%description -n %{name}+mcf
This metapackage enables feature "mcf" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Scrypt password-based key derivation function - feature "parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/parallel) = %{version}

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+password-hash
Summary:        Scrypt password-based key derivation function - feature "password-hash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6.0-rc.10) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/password-hash) = %{version}

%description -n %{name}+password-hash
This metapackage enables feature "password-hash" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phc
Summary:        Scrypt password-based key derivation function - feature "phc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6.0-rc.10/phc) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/phc) = %{version}

%description -n %{name}+phc
This metapackage enables feature "phc" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Scrypt password-based key derivation function - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(password-hash-0.6.0-rc.10/rand-core) >= 0.6.0-rc.10
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust scrypt crate, by pulling in any additional dependencies needed by that feature.

%install
%__install -d %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}
%__cp -a . %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/
%__rm -f %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/*checksum.json
echo '{"files":{},"package":null}' > %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/.cargo-checksum.json

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
