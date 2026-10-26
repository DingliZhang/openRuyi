# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global majorver        25
%global minorver        0
%global securityver     5
%global buildver        8
%global newjavaver      %{majorver}.%{minorver}.%{securityver}
%global _jvmdir         %{_libdir}/jvm
%global jvm_home        %{_jvmdir}/%{name}
%global rpm_state_dir   %{_localstatedir}/lib/rpm-state/java-openjdk
%global alternatives_priority 25000

# Package the JDK's external symbols directly, as in Fedora's release builds.
%global debug_package %{nil}
%global __brp_strip %{nil}
%global debug_source_dir %{_usrsrc}/debug/%{name}-%{version}-%{release}.%{_arch}

# Force the facilities to be recreated after RPM removes a ghost link that
# an older, still-installed monolithic package did not declare as its own.
%define refresh_alternatives() %{expand:
case "$(LC_ALL=C alternatives --display java 2>/dev/null)" in
    *'status is auto.'*)
        alternatives --auto java || : ;;
    *'status is manual.'*)
        selected_java=$(readlink -f %{_sysconfdir}/alternatives/java)
        if [ -x "$selected_java" ]; then
            alternatives --set java "$selected_java" || :
        fi ;;
esac
:
}

# Refresh the single Java group when optional tools are installed or removed.
# Repeating this after the transaction also repairs the old monolithic postun.
%define register_alternatives() %{expand:
if [ -x %{jvm_home}/bin/java ]; then
    java_was_auto=false
    case "$(LC_ALL=C alternatives --display java 2>/dev/null)" in
        *'status is auto.'*) java_was_auto=true ;;
    esac
    set -- --install %{_bindir}/java java %{jvm_home}/bin/java %{alternatives_priority} --slave %{_jvmdir}/default-java java_home %{jvm_home}
    for tool in %{jvm_home}/bin/*; do
        [ -x "$tool" ] || continue
        tool_name=${tool##*/}
        if [ "$tool_name" != java ]; then
            set -- "$@" --slave %{_bindir}/"$tool_name" "$tool_name" "$tool"
        fi
        for manpage in %{jvm_home}/man/man1/"$tool_name".1*; do
            [ -f "$manpage" ] || continue
            set -- "$@" --slave %{_mandir}/man1/"${manpage##*/}" "$tool_name.1" "$manpage"
        done
    done
    alternatives "$@" || :
    # chkconfig 1.33 can lose auto mode when an existing priority changes.
    if [ "$java_was_auto" = true ]; then
        alternatives --auto java || :
    else
        %refresh_alternatives
    fi
fi
:
}

%bcond bootstrap        1

Name:           java-25-openjdk
Version:        %{newjavaver}.%{buildver}
Release:        %autorelease
Summary:        OpenJDK 25 Runtime Environment
License:        GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.org
VCS:            git:https://github.com/openjdk/jdk25u
#!RemoteAsset:  sha256:e4cc23905feaec9d91033262d4f36a2932e145f80ed66638d61ab522f89ed8b1
Source0:        https://github.com/openjdk/jdk%{majorver}u/archive/refs/tags/jdk-%{newjavaver}+%{buildver}.tar.gz
%if %{with bootstrap}
#!RemoteAsset:  sha256:3fc35759502b620f010a9cd2b3da8454f8a49a156ceaebb00de1fd8335682d40
Source1:        https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25%2B36/OpenJDK25U-jdk_riscv64_linux_hotspot_25_36.tar.gz
#!RemoteAsset:  sha256:ee04de95ab9da7287d40bd2173076ecc2a6dd662f007bedfc6eb0380c0ef90e8
Source2:        https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25%2B36/OpenJDK25U-jdk_x64_linux_hotspot_25_36.tar.gz
%endif

# CVE-2026-91403: backport JDK-8395142 from jdk-25.0.5.0.2-ga.
# Upstream: https://github.com/openjdk/jdk25u/commit/1a8a646ef3c8f5ad2f766d43114847a2ee31cf41
Patch0:         1000-CA-Enhancements.patch

BuildRequires:  findutils
BuildRequires:  elfutils
BuildRequires:  gzip
BuildRequires:  fonts-dejavu
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  zip
BuildRequires:  pkgconfig
%if %{without bootstrap}
BuildRequires:  java-25-openjdk-devel
%endif
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(posttrans): update-alternatives
Provides:       java = %{version}-%{release}
Provides:       java-openjdk = %{version}-%{release}
Provides:       jre = %{version}-%{release}

%description
The OpenJDK desktop runtime libraries and graphical monitoring tool.

%package headless
Summary:        OpenJDK %{majorver} headless runtime environment
Requires:       fontconfig
Requires:       fonts-dejavu
Requires(post): coreutils
Requires(postun): coreutils
Requires(posttrans): coreutils
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(posttrans): update-alternatives
Provides:       java-headless = %{version}-%{release}
Provides:       java-openjdk-headless = %{version}-%{release}
Provides:       jre-headless = %{version}-%{release}

%description headless
The OpenJDK runtime environment without desktop and audio libraries.
The default-java link in the JVM directory follows the selected Java runtime.

%package devel
Summary:        OpenJDK %{majorver} development tools
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(posttrans): update-alternatives
Provides:       java-devel = %{version}-%{release}
Provides:       java-openjdk-devel = %{version}-%{release}
Provides:       java-sdk = %{version}-%{release}

%description devel
The OpenJDK compiler, command-line development tools, and JNI headers.
Install the jmods subpackage to create custom runtimes with jlink.

%package jmods
Summary:        OpenJDK %{majorver} packaged modules
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}

%description jmods
Packaged OpenJDK modules for creating custom runtimes with jlink.

%package src
Summary:        OpenJDK %{majorver} Java source archive
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}

%description src
The Java source archive for the OpenJDK class libraries.

%package demo
Summary:        OpenJDK %{majorver} demonstration programs
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description demo
Demonstration programs and examples for the OpenJDK development kit.

%package headless-debuginfo
Summary:        Native debug symbols for OpenJDK %{majorver}
AutoReq:        0
AutoProv:       1
Requires:       %{name}-headless%{?_isa} = %{version}-%{release}
Provides:       %{name}-debuginfo = %{version}-%{release}
Obsoletes:      %{name}-debuginfo < %{version}-%{release}

%description headless-debuginfo
Native debug symbols for the OpenJDK runtime libraries and development tools.

%package debugsource
Summary:        Native debug sources for OpenJDK %{majorver}
AutoReqProv:    0

%description debugsource
Native sources and generated headers for debugging OpenJDK.

%prep
%autosetup -p1 -n jdk25u-jdk-%{newjavaver}-%{buildver}

%build
%if %{with bootstrap}
%ifarch riscv64
tar -xf %{SOURCE1} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-25+36
%endif
%ifarch x86_64
tar -xf %{SOURCE2} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-25+36
%endif
%else
BOOTJDKPATH=%{_jvmdir}/java-25-openjdk
%endif

ARCH=$(uname -m)
echo $BOOTJDKPATH

mkdir -p build-release
pushd build-release
bash ../configure \
    --with-version-build=%{buildver} \
    --with-version-pre= \
    --with-version-opt= \
    --with-boot-jdk=$BOOTJDKPATH \
    --with-debug-level=release \
    --with-native-debug-symbols=external \
    --with-vendor-version-string=openRuyi \
    --with-vendor-name="openRuyi" \
    --with-vendor-url="%{_vendor_url}" \
    --with-vendor-bug-url="%{_vendor_bug_url}" \
    --enable-unlimited-crypto \
%ifarch riscv64
  %if "%{openruyi_riscv_arch}" == "-march=rva23u64"
    --with-extra-cxxflags="-march=rva23u64_zifencei" \
  %endif
%endif
    --disable-warnings-as-errors
make images
popd

%install -p
mkdir -p %{buildroot}%{_jvmdir}
cp -a build-release/images/jdk %{buildroot}%{jvm_home}
# Some image configurations keep packaged modules outside the JDK image.
if [ ! -d %{buildroot}%{jvm_home}/jmods ]; then
    cp -a build-release/images/jmods %{buildroot}%{jvm_home}/jmods
fi

# External symbols keep DWARF out of JMODs. Newer JDKs put the symbols in a
# separate image; older JDKs already include them next to the native libraries.
if [ -d build-release/images/symbols ]; then
    cp -a build-release/images/symbols/. %{buildroot}%{jvm_home}/
fi
test -s %{buildroot}%{jvm_home}/lib/server/libjvm.debuginfo
find %{buildroot}%{jvm_home} -type f -name '*.debuginfo' | while IFS= read -r debuginfo; do
    destination=%{buildroot}%{_prefix}/lib/debug${debuginfo#%{buildroot}}
    mkdir -p "${destination%/*}"
    mv "$debuginfo" "$destination"
done
find %{buildroot}%{jvm_home} -type f -name '*.so' -exec chmod 0755 {} +

# Keep native sources and generated headers separate from the runtime.
mkdir -p %{buildroot}%{debug_source_dir}
for directory in src make build-release; do
    destination=%{buildroot}%{debug_source_dir}/${directory#build-release}
    mkdir -p "$destination"
    (
        cd "$directory"
        find . -regextype posix-extended -type f \
            -regex '.*\.(c|cc|cpp|cxx|h|hh|hpp|hxx|inl|s|S|inc|ad)' \
            -exec cp -a --parents -t "$destination" {} +
    )
done

# Compress versioned manuals before creating the alternatives ghost entries.
if [ -d %{buildroot}%{jvm_home}/man ]; then
    find %{buildroot}%{jvm_home}/man -type f -name '*.1' -exec gzip -9n {} +
fi

mkdir -p %{buildroot}%{rpm_state_dir} %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
touch %{buildroot}%{_jvmdir}/default-java

# List each payload once, including directories and editable configuration.
for package in headless desktop devel jmods src demo; do
    : > "$package.files"
done
find %{buildroot}%{jvm_home} -print | LC_ALL=C sort | while IFS= read -r file; do
    path=${file#%{buildroot}}
    relative=${path#%{jvm_home}}
    case "$relative" in
        /jmods|/jmods/*) package=jmods ;;
        /demo|/demo/*) package=demo ;;
        /include|/include/*|/lib/ct.sym|/lib/libsaproc.so) package=devel ;;
        /lib/src.zip) package=src ;;
        /lib/libawt_xawt.so|/lib/libjawt.so|/lib/libsplashscreen.so|/lib/libjsound.so)
            package=desktop ;;
        /bin/*|/man/man1/*)
            tool=${relative##*/}
            tool=${tool%%.1*}
            case "$tool" in
                java|keytool|jfr|rmiregistry) package=headless ;;
                jconsole) package=desktop ;;
                *) package=devel ;;
            esac ;;
        *) package=headless ;;
    esac
    if [ -d "$file" ] && [ ! -L "$file" ]; then
        entry="%%dir $path"
    elif [ "${relative#/conf/}" != "$relative" ]; then
        entry="%%config(noreplace) $path"
    else
        entry=$path
    fi
    printf '%s\n' "$entry" >> "$package.files"
    case "$relative" in
        /bin/*)
            link=%{_bindir}/${relative##*/}
            touch "%{buildroot}$link"
            printf '%s\n' "%%ghost $link" >> "$package.files" ;;
        /man/man1/*)
            link=%{_mandir}/man1/${relative##*/}
            touch "%{buildroot}$link"
            # brp-compress also reads ghost placeholders, so use valid gzip.
            gzip -9nc < /dev/null > "%{buildroot}$link"
            printf '%s\n' "%%ghost $link" >> "$package.files" ;;
    esac
done
printf '%s\n' "%%ghost %{_jvmdir}/default-java" >> headless.files

%check
build-release/images/jdk/bin/java -version
build-release/images/jdk/bin/javac -version

cat > build-release/PackagingSmoke.java <<'EOF'
import java.awt.image.BufferedImage;

public class PackagingSmoke {
    public static void main(String[] args) throws Exception {
        var image = new BufferedImage(8, 8, BufferedImage.TYPE_INT_RGB);
        var graphics = image.createGraphics();
        graphics.drawLine(0, 0, 7, 7);
        graphics.drawString("Java", 0, 7);
        if (graphics.getFontMetrics().stringWidth("Java") <= 0) {
            throw new AssertionError("No usable headless font");
        }
        graphics.dispose();
    }
}
EOF
build-release/images/jdk/bin/javac -d build-release build-release/PackagingSmoke.java
build-release/images/jdk/bin/java -Djava.awt.headless=true -cp build-release PackagingSmoke

# Exercise the separately packaged modules, including configurations without
# jmods in images/jdk.
rm -rf build-release/packaging-test-runtime
build-release/images/jdk/bin/jlink --module-path build-release/images/jmods \
    --add-modules java.base --output build-release/packaging-test-runtime
build-release/packaging-test-runtime/bin/java -version

# Check the installed runtime, its external symbols and the native JMOD library.
test -x %{buildroot}%{jvm_home}/lib/server/libjvm.so
eu-readelf -S %{buildroot}%{jvm_home}/lib/server/libjvm.so > build-release/runtime-sections.txt
if grep -Eq '\.(debug|zdebug)_info' build-release/runtime-sections.txt; then
    echo "Unexpected DWARF in the runtime libjvm.so" >&2
    exit 1
fi
grep -q '\.symtab' build-release/runtime-sections.txt
libjvm_debug=%{buildroot}%{_prefix}/lib/debug%{jvm_home}/lib/server/libjvm.debuginfo
test -s "$libjvm_debug"
eu-readelf -S "$libjvm_debug" > build-release/debuginfo-sections.txt
grep -Eq '\.(debug|zdebug)_info' build-release/debuginfo-sections.txt
test -s %{buildroot}%{debug_source_dir}/src/hotspot/share/prims/jni.cpp
rm -rf build-release/packaging-test-jmod
build-release/images/jdk/bin/jmod extract --dir build-release/packaging-test-jmod \
    build-release/images/jmods/java.base.jmod
eu-readelf -S build-release/packaging-test-jmod/lib/server/libjvm.so > build-release/jmod-sections.txt
if grep -Eq '\.(debug|zdebug)_info' build-release/jmod-sections.txt; then
    echo "Unexpected DWARF in java.base.jmod libjvm.so" >&2
    exit 1
fi

%pretrans headless
# Snapshot the group before any old monolithic postun can change its mode.
# All JDK variants share this state and pretrans runs before payload changes.
# On a fresh system alternatives may not be installed until this transaction.
if command -v alternatives >/dev/null 2>&1 && command -v readlink >/dev/null 2>&1; then
    mkdir -p %{rpm_state_dir}
    rm -f %{rpm_state_dir}/java-auto %{rpm_state_dir}/java-manual
    case "$(LC_ALL=C alternatives --display java 2>/dev/null)" in
        *'status is auto.'*)
            touch %{rpm_state_dir}/java-auto ;;
        *'status is manual.'*)
            readlink -f %{_bindir}/java > %{rpm_state_dir}/java-manual || \
                rm -f %{rpm_state_dir}/java-manual ;;
    esac
fi
:

%post headless
%register_alternatives

%posttrans headless
%register_alternatives
if [ -f %{rpm_state_dir}/java-auto ]; then
    alternatives --auto java && rm -f %{rpm_state_dir}/java-auto
elif [ -s %{rpm_state_dir}/java-manual ]; then
    selected_java=$(cat %{rpm_state_dir}/java-manual)
    if [ -x "$selected_java" ]; then
        # Another JDK's posttrans may still need to restore its candidate.
        alternatives --set java "$selected_java" && rm -f %{rpm_state_dir}/java-manual
    else
        rm -f %{rpm_state_dir}/java-manual
    fi
fi
:

%postun headless
if [ "$1" -eq 0 ]; then
    alternatives --remove java %{jvm_home}/bin/java || :
    %refresh_alternatives
fi

%post
%register_alternatives

%posttrans
%register_alternatives

%postun
if [ "$1" -eq 0 ]; then
    %register_alternatives
fi

%post devel
%register_alternatives

%posttrans devel
%register_alternatives

%postun devel
if [ "$1" -eq 0 ]; then
    %register_alternatives
fi

%files -f desktop.files

%files headless -f headless.files
%license LICENSE
%doc README.md
%dir %{_jvmdir}
%dir %{rpm_state_dir}

%files devel -f devel.files

%files jmods -f jmods.files

%files src -f src.files

%files demo -f demo.files

%files headless-debuginfo
%{_prefix}/lib/debug%{jvm_home}

%files debugsource
%license LICENSE
%{debug_source_dir}

%changelog
%autochangelog
