# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Han Gao <gaohan@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
%global modpath %{_prefix}/lib/modules/%{kver}

%ifarch riscv64
#!BuildConstraint: hardware:jobs 32
%endif

# Whether dtbs needed for arch
%ifarch riscv64
%global need_dtbs 1
%else
%global need_dtbs 0
%endif

%global signmodules 1
%global kver %{version}-%{release}
%global kernel_make_flags LD=ld.bfd KBUILD_BUILD_VERSION=%{release}
Name:             linux
Version:          6.18.5
Release:          %autorelease
Summary:          The Linux Kernel
License:          GPL-2.0-only
URL:              https://www.kernel.org/

#!RemoteAsset:    sha256:189d1f409cef8d0d234210e04595172df392f8cb297e14b447ed95720e2fd940
Source0:          https://cdn.kernel.org/pub/linux/kernel/v6.x/%{name}-%{version}.tar.xz
Source1:          config.%{_arch}

BuildRequires:    gcc, bison, binutils, glibc-devel, make, perl
BuildRequires:    flex, bison
BuildRequires:    bc, cpio, dwarves, gettext, python3, rsync, tar, xz, zstd
BuildRequires:    libasm-devel
BuildRequires:    libdebuginfod-dummy-devel
BuildRequires:    ncurses-devel
BuildRequires:    libcap-devel
BuildRequires:    libssh-devel
BuildRequires:    libdw-devel
BuildRequires:    libelf-devel
BuildRequires:    zstd-devel
BuildRequires:    python3-devel
BuildRequires:    slang-devel
BuildRequires:    zlib-devel
BuildRequires:    openssl-devel
BuildRequires:    kmod
BuildRequires:    rpm-config-openruyi

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-modules%{?_isa} = %{version}-%{release}
%if %{need_dtbs}
Requires:       %{name}-dtbs%{?_isa} = %{version}-%{release}
%endif
Requires(post):   kmod
Requires(post):   kernel-install
Requires(postun): kernel-install

%patchlist
0001-UPSTREAM-drm-ttm-add-pgprot-handling-for-RISC-V.patch
0002-UPSTREAM-riscv-sophgo-dts-add-PCIe-controllers-for-S.patch
0003-UPSTREAM-riscv-sophgo-dts-enable-PCIe-for-PioneerBox.patch
0004-UPSTREAM-riscv-sophgo-dts-enable-PCIe-for-SG2042_EVB.patch
0005-UPSTREAM-riscv-sophgo-dts-enable-PCIe-for-SG2042_EVB.patch
0006-UPSTREAM-riscv-dts-sophgo-Add-SPI-NOR-node-for-SG204.patch
0007-UPSTREAM-riscv-dts-sophgo-Enable-SPI-NOR-node-for-Pi.patch
0008-UPSTREAM-riscv-dts-sophgo-Enable-SPI-NOR-node-for-SG.patch
0009-UPSTREAM-riscv-dts-sophgo-Enable-SPI-NOR-node-for-SG.patch
0010-UPSTREAM-dt-bindings-net-sophgo-sg2044-dwmac-add-phy.patch
0011-UPSTREAM-perf-vendor-events-riscv-add-T-HEAD-C920V2-.patch
0012-UPSTREAM-rust-macros-Add-support-for-imports_ns-to-m.patch
0013-UPSTREAM-pwm-Export-pwmchip_release-for-external-use.patch
0014-UPSTREAM-rust-pwm-Add-Kconfig-and-basic-data-structu.patch
0015-UPSTREAM-rust-pwm-Add-complete-abstraction-layer.patch
0016-UPSTREAM-rust-pwm-Add-module_pwm_platform_driver-mac.patch
0017-UPSTREAM-rust-pwm-Drop-wrapping-of-PWM-polarity-and-.patch
0018-UPSTREAM-rust-pwm-Fix-broken-intra-doc-link.patch
0019-UPSTREAM-pwm-Add-Rust-driver-for-T-HEAD-TH1520-SoC.patch
0020-UPSTREAM-dt-bindings-pwm-thead-Add-T-HEAD-TH1520-PWM.patch
0021-UPSTREAM-pwm-Fix-Rust-formatting.patch
0022-UPSTREAM-pwm-th1520-Fix-clippy-warning-for-redundant.patch
0023-UPSTREAM-pwm-th1520-Use-module_pwm_platform_driver-m.patch
0024-UPSTREAM-pwm-th1520-Fix-missing-Kconfig-dependencies.patch
0025-UPSTREAM-riscv-dts-thead-add-xtheadvector-to-the-th1.patch
0026-UPSTREAM-riscv-dts-thead-add-ziccrse-for-th1520.patch
0027-UPSTREAM-riscv-dts-thead-add-zfh-for-th1520.patch
0028-UPSTREAM-riscv-dts-thead-Add-PWM-controller-node.patch
0029-UPSTREAM-riscv-dts-thead-Add-PWM-fan-and-thermal-con.patch
0030-UPSTREAM-dt-bindings-vendor-prefixes-Add-UltraRISC.patch
0031-UPSTREAM-dt-bindings-interrupt-controller-Add-UltraR.patch
0032-UPSTREAM-irqchip-sifive-plic-Cache-the-interrupt-ena.patch
0033-UPSTREAM-irqchip-sifive-plic-Add-support-for-UltraRI.patch
0034-UPSTREAM-riscv-boot-Always-make-Image-from-vmlinux-n.patch
0035-UPSTREAM-riscv-cpu_ops_sbi-smp_processor_id-returns-.patch
0036-UPSTREAM-riscv-trace-fix-snapshot-deadlock-with-sbi-.patch
0037-UPSTREAM-spi-dt-bindings-fsl-qspi-support-SpacemiT-K.patch
0038-UPSTREAM-spi-dt-bindings-fsl-qspi-add-optional-reset.patch
0039-UPSTREAM-spi-fsl-qspi-add-optional-reset-support.patch
0040-UPSTREAM-spi-fsl-qspi-switch-predicates-to-bool.patch
0041-UPSTREAM-spi-fsl-qspi-add-a-clock-disable-quirk.patch
0042-UPSTREAM-spi-fsl-qspi-introduce-sfa_size-devtype-dat.patch
0043-UPSTREAM-spi-fsl-qspi-support-the-SpacemiT-K1-SoC.patch
0044-UPSTREAM-dt-bindings-pci-spacemit-Introduce-PCIe-hos.patch
0045-UPSTREAM-PCI-spacemit-Add-SpacemiT-PCIe-host-driver.patch
0046-UPSTREAM-ASoC-dt-bindings-Add-bindings-for-SpacemiT-.patch
0047-UPSTREAM-ASoC-spacemit-add-i2s-support-for-K1-SoC.patch
0048-UPSTREAM-riscv-dts-spacemit-add-UART-pinctrl-combina.patch
0049-UPSTREAM-riscv-dts-spacemit-enable-the-i2c8-adapter.patch
0050-UPSTREAM-riscv-dts-spacemit-define-fixed-regulators.patch
0051-UPSTREAM-riscv-dts-spacemit-define-regulator-constra.patch
0052-UPSTREAM-riscv-dts-spacemit-enable-the-i2c2-adapter-.patch
0053-UPSTREAM-riscv-dts-spacemit-add-24c02-eeprom-on-BPI-.patch
0054-UPSTREAM-riscv-dts-spacemit-add-i2c-aliases-on-BPI-F.patch
0055-UPSTREAM-riscv-dts-spacemit-add-Ethernet-and-PDMA-to.patch
0056-UPSTREAM-riscv-dts-spacemit-add-MusePi-Pro-board-dev.patch
0057-UPSTREAM-riscv-dts-spacemit-enable-K1-SoC-QSPI-on-BP.patch
0058-UPSTREAM-riscv-dts-spacemit-Add-OrangePi-R2S-board-d.patch
0059-UPSTREAM-riscv-dts-spacemit-reorder-i2c2-node.patch
0060-UPSTREAM-riscv-dts-spacemit-define-all-missing-I2C-c.patch
0061-UPSTREAM-rtc-spacemit-MFD_SPACEMIT_P1-as-dependencie.patch
0062-UPSTREAM-mfd-simple-mfd-i2c-Remove-select-I2C_K1-fro.patch
0063-UPSTREAM-driver-reset-spacemit-p1-add-driver-for-pow.patch
0064-FROMLIST-riscv-errata-Add-ERRATA_THEAD_WRITE_ONCE-fi.patch
0065-FROMLIST-PCI-Release-BAR0-of-an-integrated-bridge-to.patch
0066-BACKPORT-FROMLIST-drm-ttm-save-the-device-s-DMA-cohe.patch
0067-BACKPORT-FROMLIST-drm-ttm-downgrade-cached-to-write_.patch
0068-FROMLIST-dt-bindings-clock-thead-th1520-clk-ap-Add-I.patch
0069-FROMLIST-clk-thead-th1520-ap-Poll-for-PLL-lock-and-w.patch
0070-FROMLIST-clk-thead-th1520-ap-Add-C910-bus-clock.patch
0071-FROMLIST-clk-thead-th1520-ap-Support-setting-PLL-rat.patch
0072-FROMLIST-clk-thead-th1520-ap-Add-macro-to-define-mul.patch
0073-FROMLIST-clk-thead-th1520-ap-Support-CPU-frequency-s.patch
0074-FROMLIST-NFU-riscv-dts-thead-Add-CPU-clock-and-OPP-t.patch
0075-FROMLIST-dt-bindings-vendor-prefixes-add-verisilicon.patch
0076-FROMLIST-dt-bindings-display-add-verisilicon-dc.patch
0077-FROMLIST-drm-verisilicon-add-a-driver-for-Verisilico.patch
0078-FROMLIST-dt-bindings-display-bridge-add-binding-for-.patch
0079-FROMLIST-drm-bridge-add-a-driver-for-T-Head-TH1520-H.patch
0080-FROMLIST-riscv-dts-thead-add-DPU-and-HDMI-device-tre.patch
0081-FROMLIST-riscv-dts-thead-lichee-pi-4a-enable-HDMI.patch
0082-FROMLIST-MAINTAINERS-assign-myself-as-maintainer-for.patch
0083-FROMLIST-mailmap-map-all-Icenowy-Zheng-s-mail-addres.patch
0084-FROMLIST-dt-bindings-usb-Add-T-HEAD-TH1520-USB-contr.patch
0085-FROMLIST-usb-dwc3-add-T-HEAD-TH1520-usb-driver.patch
0086-FROMLIST-rust-export-BINDGEN_TARGET-from-a-separate-.patch
0087-FROMLIST-rust-generate-a-fatal-error-if-BINDGEN_TARG.patch
0088-FROMLIST-rust-add-a-Kconfig-function-to-test-for-sup.patch
0089-FROMLIST-RISC-V-handle-extension-configs-for-bindgen.patch
0090-FROMLIST-PCI-MSI-Conservatively-generalize-no_64bit_.patch
0091-FROMLIST-PCI-MSI-Check-msi_addr_mask-in-msi_verify_e.patch
0092-FROMLIST-drm-radeon-Raise-msi_addr_mask-to-40-bits-f.patch
0093-FROMLIST-ALSA-hda-intel-Raise-msi_addr_mask-to-dma_b.patch
0094-FROMLIST-rust-clk-implement-Send-and-Sync.patch
0095-FROMLIST-tyr-remove-impl-Send-Sync-for-TyrData.patch
0096-FROMLIST-pwm-th1520-remove-impl-Send-Sync-for-Th1520.patch
0097-FROMLIST-riscv-dts-sophgo-enable-hardware-clock-RTC-.patch
0098-FROMLIST-dt-bindings-mmc-spacemit-sdhci-add-reset-su.patch
0099-FROMLIST-mmc-sdhci-of-k1-add-reset-support.patch
0100-FROMLIST-riscv-dts-spacemit-sdhci-add-reset-support.patch
0101-FROMLIST-i2c-spacemit-move-i2c_xfer_msg.patch
0102-FROMLIST-i2c-spacemit-introduce-pio-for-k1.patch
0103-FROMLIST-mfd-simple-mfd-i2c-add-a-reboot-cell-for-th.patch
0104-FROMLIST-dt-bindings-phy-spacemit-Add-SpacemiT-PCIe-.patch
0105-FROMLIST-phy-spacemit-Introduce-PCIe-combo-PHY.patch
0106-FROMLIST-riscv-dts-spacemit-Add-a-PCIe-regulator.patch
0107-FROMLIST-riscv-dts-spacemit-PCIe-and-PHY-related-upd.patch
0108-FROMLIST-phy-Kconfig-spacemit-add-COMMON_CLK-depende.patch
0109-FROMLIST-regulator-spacemit-MFD_SPACEMIT_P1-as-depen.patch
0110-FROMLIST-mfd-simple-mfd-i2c-add-default-value.patch
0111-FROMLIST-rtc-spacemit-default-module-when-MFD_SPACEM.patch
0112-FROMLIST-dmaengine-mmp_pdma-Fix-race-condition-in-mm.patch
0113-FROMLIST-dt-bindings-i2c-spacemit-add-optional-reset.patch
0114-FROMLIST-i2c-k1-add-reset-support.patch
0115-FROMLIST-riscv-dts-spacemit-add-reset-property.patch
0116-FROMLIST-dt-bindings-phy-spacemit-add-K1-USB2-PHY.patch
0117-FROMLIST-phy-spacemit-support-K1-USB2.0-PHY-controll.patch
0118-FROMLIST-riscv-dts-spacemit-Add-USB2-PHY-node-for-K1.patch
0119-FROMLIST-riscv-dts-spacemit-Add-DWC3-USB-3.0-control.patch
0120-FROMLIST-riscv-dts-spacemit-Enable-USB3.0-on-BananaP.patch
0121-FROMLIST-dt-bindings-spi-add-SpacemiT-K1-SPI-support.patch
0122-FROMLIST-spi-spacemit-introduce-SpacemiT-K1-SPI-cont.patch
0123-FROMLIST-riscv-dts-spacemit-define-a-SPI-controller-.patch
0124-FROMLIST-dt-bindings-pinctrl-spacemit-convert-drive-.patch
0125-FROMLIST-dt-bindings-pinctrl-spacemit-add-K3-SoC-sup.patch
0126-FROMLIST-pinctrl-spacemit-k3-add-initial-pin-support.patch
0127-FROMLIST-pinctrl-spacemit-k3-adjust-drive-strength-a.patch
0128-FROMLIST-dt-bindings-pinctrl-spacemit-add-syscon-pro.patch
0129-FROMLIST-pinctrl-spacemit-support-I-O-power-domain-c.patch
0130-FROMLIST-riscv-dts-spacemit-modify-pinctrl-node-in-d.patch
0131-FROMLIST-dt-bindings-riscv-add-SpacemiT-X100-CPU-com.patch
0132-FROMLIST-dt-bindings-timer-add-SpacemiT-K3-CLINT.patch
0133-FROMLIST-dt-bindings-interrupt-controller-add-Spacem.patch
0134-FROMLIST-dt-bindings-interrupt-controller-add-Spacem.patch
0135-FROMLIST-dt-bindings-riscv-spacemit-add-K3-and-Pico-.patch
0136-FROMLIST-dt-bindings-riscv-Add-B-ISA-extension-descr.patch
0137-FROMLIST-dt-bindings-riscv-Add-descriptions-for-Za64.patch
0138-FROMLIST-dt-bindings-riscv-Add-Ssccptr-Sscounterenw-.patch
0139-FROMLIST-dt-bindings-riscv-Add-Sha-and-its-comprised.patch
0140-FROMLIST-riscv-dts-spacemit-add-initial-device-tree-.patch
0141-FROMLIST-riscv-dts-spacemit-add-SpacemiT-K3-Pico-ITX.patch
0142-FROMLIST-clk-spacemit-Respect-Kconfig-setting-when-b.patch
0143-FROMLIST-clk-spacemit-Hide-common-clock-driver-from-.patch
0144-FROMLIST-clk-spacemit-prepare-common-ccu-header.patch
0145-FROMLIST-clk-spacemit-extract-common-ccu-functions.patch
0146-FROMLIST-clk-spacemit-add-platform-SoC-prefix-to-res.patch
0147-FROMLIST-reset-spacemit-fix-auxiliary-device-id.patch
0148-FROMLIST-dt-bindings-soc-spacemit-k3-add-clock-suppo.patch
0149-FROMLIST-clk-spacemit-ccu_mix-add-inverted-enable-ga.patch
0150-FROMLIST-clk-spacemit-ccu_pll-add-plla-type-clock.patch
0151-FROMLIST-clk-spacemit-k3-extract-common-header.patch
0152-FROMLIST-clk-spacemit-k3-add-the-clock-tree.patch
0153-FROMLIST-dt-bindings-soc-spacemit-Add-K3-reset-suppo.patch
0154-FROMLIST-reset-Create-subdirectory-for-SpacemiT-driv.patch
0155-FROMLIST-reset-spacemit-Extract-common-K1-reset-code.patch
0156-FROMLIST-reset-spacemit-Add-SpacemiT-K3-reset-driver.patch
0157-FROMLIST-dt-bindings-gpio-spacemit-add-compatible-na.patch
0158-FROMLIST-gpio-spacemit-Add-GPIO-support-for-K3-SoC.patch
0159-FROMLIST-PCI-ASPM-Avoid-L0s-and-L1-on-Sophgo-2042-PC.patch
0160-FROMLIST-PCI-ASPM-Avoid-L0s-and-L1-on-Sophgo-2044-PC.patch
0161-XUANTIE-riscv-dts-th1520-add-licheepi4a-16g-support.patch
0162-XUANTIE-riscv-dts-thead-Add-TH1520-USB-nodes.patch
0163-XUANTIE-riscv-dts-thead-Add-TH1520-I2C-nodes.patch
0164-XUANTIE-riscv-dts-thead-Add-Lichee-Pi-4A-IO-expansio.patch
0165-XUANTIE-riscv-dts-thead-Enable-Lichee-Pi-4A-USB.patch
0166-REVYOS-riscv-dts-th1520-rename-thead-to-xuantie.patch
0167-REVYOS-riscv-dts-th1520-add-xuantie-th1520-mbox-r.patch
0168-SOPHGO-dt-bindings-nvmem-Add-SG2044-eFuse-controller.patch
0169-SOPHGO-nvmem-Add-Sophgo-SG2044-eFuse-driver.patch
0170-SOPHGO-riscv-dts-sophgo-sg2044-Add-eFUSE-device.patch
0171-SOPHGO-dts-sg2044-Modify-pcie-bar-address.patch
0172-REVYSR-dt-bindings-net-ultrarisc-dp1000-gmac-Add-sup.patch
0173-REVYSR-net-stmmac-add-support-for-dwmac-5.10a.patch
0174-RVCK-riscv-dp1000-8250_dw-support-ultrarisc-dp1000-u.patch
0175-RVCK-riscv-dts-add-dp1000.dts-for-UltraRIsc-DP1000-S.patch
0176-RVCK-riscv-dp1000-arch-add-UltraRISC-DP1000-SoC-supp.patch
0177-RVCK-riscv-dp1000-pci-support-UltraRISC-pcie-rc.patch
0178-RVCK-pcie-update-the-outbound-mapping-process.patch
0179-RVCK-pinctrl-add-pinctrl-dirver-for-UltraRisc-DP1000.patch
0180-RVCK-dts-add-pinctrl-dtsi-dts-for-UltraRisc-DP1000.patch
0181-RVCK-pci-Update-the-number-of-outbound-and-inbound.patch
0182-RVCK-riscv-dp1000-pci-Add-custom-PCI-host-ops.patch
0183-RVCK-riscv-dp1000-dts-add-the-dts-of-UltraRISC-dp100.patch
0184-RVCK-riscv-dp1000-dts-Move-mmc0-node-from-SoC-to-boa.patch
0185-RVCK-riscv-dp1000-plic-add-plic-early-init-supports.patch
0186-RVCK-pcie-ultrarisc-Add-suspend-resume-support.patch
0187-RVCK-riscv-dp1000-dts-Move-chosen-node-from-common-t.patch
0188-RVCK-dts-riscv-ultrarisc-Refactor-DP1000-device-tree.patch
0189-RVCK-riscv-pinctrl-ultrarisc-Implement-pin-configura.patch
0190-RVCK-riscv-dts-dp1000-add-dts-dtsi-for-Milk-V-Titan-.patch

%description
This is a meta-package that installs the core kernel image and modules.
For a minimal boot environment, install the 'linux-core' package instead.

%package core
Summary:        The core Linux kernel image and initrd

%description core
Contains the bootable kernel image (vmlinuz) and a generic, pre-built initrd,
providing the minimal set of files needed to boot the system.

%package modules
Summary:        Kernel modules for the Linux kernel
Requires:       %{name}-core = %{version}-%{release}

%description modules
Contains all the kernel modules (.ko files) and associated metadata for
the hardware drivers and kernel features.

%package devel
Summary:          Development files for building external kernel modules
Requires:         %{name} = %{version}-%{release}
Requires:         dwarves

%description devel
This package provides the kernel headers and Makefiles necessary to build
external kernel modules against the installed kernel. The development files are
located at %{_usrsrc}/kernels/%{kver}, with symlinks provided under
%{_prefix}/lib/modules/%{kver}/ for compatibility.

%if %{need_dtbs}

%package dtbs
Summary:          Devicetree blob files from Linux sources

%description dtbs
This package provides the DTB files built from Linux sources that may be used
for booting.

%endif

%prep
%autosetup -p1
cp %{SOURCE1} .config
echo "-%{release}" > localversion

%conf
%make_build %{kernel_make_flags} olddefconfig

%build

%make_build %{kernel_make_flags}

%if %{need_dtbs}
%make_build %{kernel_make_flags} dtbs
%endif

%install
%define ksrcpath %{buildroot}%{_usrsrc}/kernels/%{kver}
install -d %{buildroot}%{modpath} %{ksrcpath}

%make_build %{kernel_make_flags} INSTALL_MOD_PATH=%{buildroot}%{_prefix} INSTALL_MOD_STRIP=1 DEPMOD=true modules_install

%if %{need_dtbs}
%make_build %{kernel_make_flags} INSTALL_DTBS_PATH=%{buildroot}%{modpath}/dtb dtbs_install
%endif

%make_build run-command %{kernel_make_flags} KBUILD_RUN_COMMAND="$(pwd)/scripts/package/install-extmod-build %{ksrcpath}"

pushd %{buildroot}%{modpath}
ln -sf %{_usrsrc}/kernels/%{kver} build
ln -sf %{_usrsrc}/kernels/%{kver} source
popd

install -Dm644 $(make %{kernel_make_flags} -s image_name) %{buildroot}%{modpath}/vmlinuz

echo "Module signing would happen here for version %{kver}."

%post
%{_bindir}/kernel-install add %{kver} %{modpath}/vmlinuz

%postun
if [ $1 -eq 0 ] ; then
    %{_bindir}/kernel-install remove %{kver}
fi

%files
%license COPYING
%doc README

%files core
%{modpath}/vmlinuz

%files modules
%{modpath}/*
%exclude %{modpath}/vmlinuz
%exclude %{modpath}/build
%exclude %{modpath}/source

%files devel
%{_usrsrc}/kernels/%{kver}/
%{modpath}/build
%{modpath}/source

%if %{need_dtbs}
%files dtbs
%{modpath}/dtb
%endif

%changelog
%{?autochangelog}
