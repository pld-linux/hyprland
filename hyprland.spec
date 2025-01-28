Summary:	Independent, highly customizable, dynamic tiling Wayland compositor
Name:		hyprland
Version:	0.47.0
Release:	1
License:	BSD
Group:		Applications
#Source0Download: https://github.com/hyprwm/hyprland/releases
Source0:	https://github.com/hyprwm/hyprland/releases/download/v%{version}/source-v%{version}.tar.gz
# Source0-md5:	f02d018805b1c24fbdf9b67c46b48e6c
Patch0:		flags.patch
URL:		https://hyprland.org/
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGLESv3-devel
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 3.30
BuildRequires:	glaze-devel >= 4.2.3
BuildRequires:	glib2 >= 2.0
BuildRequires:	hypr-aquamarine-devel >= 0.4.5
BuildRequires:	hyprcursor-devel >= 0.1.7
BuildRequires:	hyprgraphics-devel >= 0.1.1
BuildRequires:	hyprland-protocols >= 0.6.0
BuildRequires:	hyprlang-devel >= 0.3.2
BuildRequires:	hyprutils-devel >= 0.4.0
BuildRequires:	hyprwayland-scanner >= 0.3.10
BuildRequires:	libdrm-devel
BuildRequires:	libinput-devel
BuildRequires:	libstdc++-devel >= 6:14
BuildRequires:	libuuid-devel
BuildRequires:	libxcb-devel
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pango-devel
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig
BuildRequires:	re2-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tomlplusplus-devel
BuildRequires:	wayland-devel >= 1.22.90
BuildRequires:	wayland-protocols
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-errors-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires:	hypr-aquamarine >= 0.4.5
Requires:	hyprcursor >= 0.1.7
Requires:	hyprgraphics >= 0.1.1
Requires:	hyprlang >= 0.3.2
Requires:	hyprutils >= 0.4.0
Requires:	wayland >= 1.22.90
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hyprland is a 100% independent, dynamic tiling Wayland compositor that
doesn't sacrifice on its looks. Its features include:
- All of the eyecandy: gradient borders, blur, animations, shadows and
  much more
- A lot of customization
- 100% independent, no wlroots, no libweston, no kwin, no mutter
- Custom bezier curves for the best animations
- Powerful plugin support
- Built-in plugin manager
- Tearing support for better gaming performance
- Easily expandable and readable codebase
- Fast and active development
- Not afraid to provide bleeding-edge features
- Config reloaded instantly upon saving
- Fully dynamic workspaces
- Two built-in layouts and more available as plugins
- Global keybinds passed to your apps of choice
- Tiling/pseudotiling/floating/fullscreen windows
- Special workspaces (scratchpads)
- Window groups (tabbed mode)
- Powerful window/monitor/layer rules
- Socket-based IPC
- Native IME and Input Panels Support

%package devel
Summary:	Header files for hyprland
Group:		Development/Libraries

%description devel
Header files for hyprland.

%prep
%setup -q -n %{name}-source
%patch0 -p1

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/Hyprland
%attr(755,root,root) %{_bindir}/hyprctl
%attr(755,root,root) %{_bindir}/hyprland
%attr(755,root,root) %{_bindir}/hyprpm
%{_datadir}/hypr
%{_datadir}/wayland-sessions/hyprland.desktop
%{_datadir}/xdg-desktop-portal/hyprland-portals.conf
%{_mandir}/man1/Hyprland.1*
%{_mandir}/man1/hyprctl.1*
%{bash_compdir}/hyprctl
%{bash_compdir}/hyprpm
%{fish_compdir}/hyprctl.fish
%{fish_compdir}/hyprpm.fish
%{zsh_compdir}/_hyprctl
%{zsh_compdir}/_hyprpm

%files devel
%defattr(644,root,root,755)
%{_includedir}/hyprland
%{_npkgconfigdir}/hyprland.pc
