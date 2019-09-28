#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ostree
Version  : 2019.4
Release  : 34
URL      : https://github.com/ostreedev/ostree/releases/download/v2019.4/libostree-2019.4.tar.xz
Source0  : https://github.com/ostreedev/ostree/releases/download/v2019.4/libostree-2019.4.tar.xz
Summary  : Git for operating system binaries
Group    : Development/Tools
License  : BSD-2-Clause LGPL-2.0 LGPL-2.1
Requires: ostree-bin = %{version}-%{release}
Requires: ostree-config = %{version}-%{release}
Requires: ostree-data = %{version}-%{release}
Requires: ostree-lib = %{version}-%{release}
Requires: ostree-libexec = %{version}-%{release}
Requires: ostree-license = %{version}-%{release}
Requires: ostree-man = %{version}-%{release}
Requires: ostree-services = %{version}-%{release}
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : gjs
BuildRequires : gjs-dev
BuildRequires : gpgme-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libarchive-devel
BuildRequires : libassuan-dev
BuildRequires : libcap-dev
BuildRequires : libxslt-bin
BuildRequires : parallel
BuildRequires : pkgconfig(e2p)
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libgsystem)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(zlib)
BuildRequires : util-linux

%description
libostree
---------
New! See the docs online at [Read The Docs (OSTree)](https://ostree.readthedocs.org/en/latest/ )

%package bin
Summary: bin components for the ostree package.
Group: Binaries
Requires: ostree-data = %{version}-%{release}
Requires: ostree-libexec = %{version}-%{release}
Requires: ostree-config = %{version}-%{release}
Requires: ostree-license = %{version}-%{release}
Requires: ostree-services = %{version}-%{release}

%description bin
bin components for the ostree package.


%package config
Summary: config components for the ostree package.
Group: Default

%description config
config components for the ostree package.


%package data
Summary: data components for the ostree package.
Group: Data

%description data
data components for the ostree package.


%package dev
Summary: dev components for the ostree package.
Group: Development
Requires: ostree-lib = %{version}-%{release}
Requires: ostree-bin = %{version}-%{release}
Requires: ostree-data = %{version}-%{release}
Provides: ostree-devel = %{version}-%{release}
Requires: ostree = %{version}-%{release}

%description dev
dev components for the ostree package.


%package extras
Summary: extras components for the ostree package.
Group: Default

%description extras
extras components for the ostree package.


%package lib
Summary: lib components for the ostree package.
Group: Libraries
Requires: ostree-data = %{version}-%{release}
Requires: ostree-libexec = %{version}-%{release}
Requires: ostree-license = %{version}-%{release}

%description lib
lib components for the ostree package.


%package libexec
Summary: libexec components for the ostree package.
Group: Default
Requires: ostree-config = %{version}-%{release}
Requires: ostree-license = %{version}-%{release}

%description libexec
libexec components for the ostree package.


%package license
Summary: license components for the ostree package.
Group: Default

%description license
license components for the ostree package.


%package man
Summary: man components for the ostree package.
Group: Default

%description man
man components for the ostree package.


%package services
Summary: services components for the ostree package.
Group: Systemd services

%description services
services components for the ostree package.


%prep
%setup -q -n libostree-2019.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1569641182
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check ||:

%install
export SOURCE_DATE_EPOCH=1569641182
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ostree
cp COPYING %{buildroot}/usr/share/package-licenses/ostree/COPYING
cp bsdiff/LICENSE %{buildroot}/usr/share/package-licenses/ostree/bsdiff_LICENSE
cp libglnx/COPYING %{buildroot}/usr/share/package-licenses/ostree/libglnx_COPYING
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/ostree/ostree-prepare-root
/usr/lib/ostree/ostree-remount

%files bin
%defattr(-,root,root,-)
/usr/bin/ostree
/usr/bin/rofiles-fuse

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/ostree-tmpfiles.conf

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/OSTree-1.0.typelib
/usr/share/bash-completion/completions/ostree
/usr/share/gir-1.0/*.gir
/usr/share/ostree/trusted.gpg.d/README-gpg

%files dev
%defattr(-,root,root,-)
/usr/include/ostree-1/ostree-async-progress.h
/usr/include/ostree-1/ostree-autocleanups.h
/usr/include/ostree-1/ostree-bootconfig-parser.h
/usr/include/ostree-1/ostree-core.h
/usr/include/ostree-1/ostree-deployment.h
/usr/include/ostree-1/ostree-diff.h
/usr/include/ostree-1/ostree-dummy-enumtypes.h
/usr/include/ostree-1/ostree-gpg-verify-result.h
/usr/include/ostree-1/ostree-kernel-args.h
/usr/include/ostree-1/ostree-mutable-tree.h
/usr/include/ostree-1/ostree-ref.h
/usr/include/ostree-1/ostree-remote.h
/usr/include/ostree-1/ostree-repo-deprecated.h
/usr/include/ostree-1/ostree-repo-file.h
/usr/include/ostree-1/ostree-repo-finder-avahi.h
/usr/include/ostree-1/ostree-repo-finder-config.h
/usr/include/ostree-1/ostree-repo-finder-mount.h
/usr/include/ostree-1/ostree-repo-finder-override.h
/usr/include/ostree-1/ostree-repo-finder.h
/usr/include/ostree-1/ostree-repo.h
/usr/include/ostree-1/ostree-sepolicy.h
/usr/include/ostree-1/ostree-sysroot-upgrader.h
/usr/include/ostree-1/ostree-sysroot.h
/usr/include/ostree-1/ostree-types.h
/usr/include/ostree-1/ostree-version.h
/usr/include/ostree-1/ostree.h
/usr/lib64/libostree-1.so
/usr/lib64/pkgconfig/ostree-1.pc

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/system-generators/ostree-system-generator

%files lib
%defattr(-,root,root,-)
/usr/lib64/libostree-1.so.1
/usr/lib64/libostree-1.so.1.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/libostree/grub2-15_ostree
/usr/libexec/libostree/ostree-trivial-httpd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ostree/COPYING
/usr/share/package-licenses/ostree/bsdiff_LICENSE
/usr/share/package-licenses/ostree/libglnx_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ostree-admin-cleanup.1
/usr/share/man/man1/ostree-admin-config-diff.1
/usr/share/man/man1/ostree-admin-deploy.1
/usr/share/man/man1/ostree-admin-init-fs.1
/usr/share/man/man1/ostree-admin-instutil.1
/usr/share/man/man1/ostree-admin-os-init.1
/usr/share/man/man1/ostree-admin-pin.1
/usr/share/man/man1/ostree-admin-set-origin.1
/usr/share/man/man1/ostree-admin-status.1
/usr/share/man/man1/ostree-admin-switch.1
/usr/share/man/man1/ostree-admin-undeploy.1
/usr/share/man/man1/ostree-admin-unlock.1
/usr/share/man/man1/ostree-admin-upgrade.1
/usr/share/man/man1/ostree-admin.1
/usr/share/man/man1/ostree-cat.1
/usr/share/man/man1/ostree-checkout.1
/usr/share/man/man1/ostree-checksum.1
/usr/share/man/man1/ostree-commit.1
/usr/share/man/man1/ostree-config.1
/usr/share/man/man1/ostree-create-usb.1
/usr/share/man/man1/ostree-diff.1
/usr/share/man/man1/ostree-export.1
/usr/share/man/man1/ostree-find-remotes.1
/usr/share/man/man1/ostree-fsck.1
/usr/share/man/man1/ostree-gpg-sign.1
/usr/share/man/man1/ostree-init.1
/usr/share/man/man1/ostree-log.1
/usr/share/man/man1/ostree-ls.1
/usr/share/man/man1/ostree-prune.1
/usr/share/man/man1/ostree-pull-local.1
/usr/share/man/man1/ostree-pull.1
/usr/share/man/man1/ostree-refs.1
/usr/share/man/man1/ostree-remote.1
/usr/share/man/man1/ostree-reset.1
/usr/share/man/man1/ostree-rev-parse.1
/usr/share/man/man1/ostree-show.1
/usr/share/man/man1/ostree-static-delta.1
/usr/share/man/man1/ostree-summary.1
/usr/share/man/man1/ostree.1
/usr/share/man/man1/rofiles-fuse.1
/usr/share/man/man5/ostree.repo-config.5
/usr/share/man/man5/ostree.repo.5

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ostree-finalize-staged.path
/usr/lib/systemd/system/ostree-finalize-staged.service
/usr/lib/systemd/system/ostree-prepare-root.service
/usr/lib/systemd/system/ostree-remount.service
