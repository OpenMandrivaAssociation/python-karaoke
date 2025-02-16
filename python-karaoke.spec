%define name python-karaoke
%define tarname pykaraoke
%define version 0.7.3
%define release %mkrel 1

Summary:	Free CD+G/MPEG/KAR Karaoke Player
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source: 	http://www.kibosh.org/pykaraoke/%{tarname}-%{version}.tar.bz2
Patch0:         remove-fonts.patch
License:	LGPL 
Group:		Sound
URL:		https://www.kibosh.org/
BuildRoot:	%{_tmppath}/%{tarname}-%{version}%{release}-buildroot
BuildRequires:  desktop-file-utils
BuildRequires:	python-devel
%ifarch x86_64
BuildRequires:  lib64wxPythonGTK2.8-devel
%else
BuildRequires:  libwxPythonGTK2.8-devel
%endif
BuildRequires:  wxPythonGTK-wxversion
BuildRequires:  pygame-devel
Requires:       python-base >= 2.7
Requires:       python-numpy
Requires:       pygame
Requires:       wxPythonGTK
Requires:       TiMidity++
Requires:       timidity-patch-freepats
Requires:       fonts-ttf-dejavu


%description
Free karaoke player for Linux, FreeBSD, NetBSD, Windows and GP2X.
You can use this program to play your collection of CDG, MIDI and MPEG
 karaoke songs. No songs are provided, you must obtain these from elsewhere.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p3
sed 1,2d -i py{karaoke,karaoke_mini,kar,cdg,mpg}.py performer_prompt.py # remove-shebang

%build
#CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

rm -fr fonts
%{__python} setup.py install --prefix=/usr --root=$RPM_BUILD_ROOT

# pykaraoke will not run without this modifified timidity.cfg
mkdir -p %buildroot%{_sysconfdir}/timidity
mkdir -p %buildroot%{_sysconfdir}/alternatives
cat > %buildroot%{_sysconfdir}/timidity/timidity.cfg << EOF
##############################################################################
# These are the standard patches that come with the GUS, mapped into GM
# programs. 
#
bank 0

	0 /usr/share/timidity/instruments/acpiano
	1 /usr/share/timidity/instruments/britepno
	2 /usr/share/timidity/instruments/synpiano
	3 /usr/share/timidity/instruments/honky
	4 /usr/share/timidity/instruments/epiano1
	5 /usr/share/timidity/instruments/epiano2
	6 /usr/share/timidity/instruments/hrpschrd
	7 /usr/share/timidity/instruments/clavinet
	8 /usr/share/timidity/instruments/celeste
	9 /usr/share/timidity/instruments/glocken
	10 /usr/share/timidity/instruments/musicbox
	11 /usr/share/timidity/instruments/vibes
	12 /usr/share/timidity/instruments/marimba
	13 /usr/share/timidity/instruments/xylophon amp=200
	14 /usr/share/timidity/instruments/tubebell
	15 /usr/share/timidity/instruments/santur
	16 /usr/share/timidity/instruments/homeorg
	17 /usr/share/timidity/instruments/percorg
	18 /usr/share/timidity/instruments/rockorg
	19 /usr/share/timidity/instruments/church
	20 /usr/share/timidity/instruments/reedorg
	21 /usr/share/timidity/instruments/accordn
	22 /usr/share/timidity/instruments/harmonca
	23 /usr/share/timidity/instruments/concrtna
	24 /usr/share/timidity/instruments/nyguitar
	25 /usr/share/timidity/instruments/acguitar
	26 /usr/share/timidity/instruments/jazzgtr
	27 /usr/share/timidity/instruments/cleangtr
	28 /usr/share/timidity/instruments/mutegtr
	29 /usr/share/timidity/instruments/odguitar
	30 /usr/share/timidity/instruments/distgtr
	31 /usr/share/timidity/instruments/gtrharm
	32 /usr/share/timidity/instruments/acbass
	33 /usr/share/timidity/instruments/fngrbass
	34 /usr/share/timidity/instruments/pickbass
	35 /usr/share/timidity/instruments/fretless
	36 /usr/share/timidity/instruments/slapbas1
	37 /usr/share/timidity/instruments/slapbas2
	38 /usr/share/timidity/instruments/synbass1
	39 /usr/share/timidity/instruments/synbass2
	40 /usr/share/timidity/instruments/violin
	41 /usr/share/timidity/instruments/viola
	42 /usr/share/timidity/instruments/cello
	43 /usr/share/timidity/instruments/contraba
	44 /usr/share/timidity/instruments/tremstr
	45 /usr/share/timidity/instruments/pizzcato
	46 /usr/share/timidity/instruments/harp
	47 /usr/share/timidity/instruments/timpani
	# This sounds pretty dumb with the default panning
	48 /usr/share/timidity/instruments/marcato pan=center
	49 /usr/share/timidity/instruments/slowstr
	50 /usr/share/timidity/instruments/synstr1
	51 /usr/share/timidity/instruments/synstr2
	52 /usr/share/timidity/instruments/choir
	53 /usr/share/timidity/instruments/doo
	54 /usr/share/timidity/instruments/voices
	55 /usr/share/timidity/instruments/orchhit
	56 /usr/share/timidity/instruments/trumpet
	57 /usr/share/timidity/instruments/trombone
	58 /usr/share/timidity/instruments/tuba
	59 /usr/share/timidity/instruments/mutetrum
	60 /usr/share/timidity/instruments/frenchrn
	61 /usr/share/timidity/instruments/hitbrass
	62 /usr/share/timidity/instruments/synbras1
	63 /usr/share/timidity/instruments/synbras2
	64 /usr/share/timidity/instruments/sprnosax
	65 /usr/share/timidity/instruments/altosax
	66 /usr/share/timidity/instruments/tenorsax
	67 /usr/share/timidity/instruments/barisax
	68 /usr/share/timidity/instruments/oboe
	69 /usr/share/timidity/instruments/englhorn
	70 /usr/share/timidity/instruments/bassoon
	71 /usr/share/timidity/instruments/clarinet
	72 /usr/share/timidity/instruments/piccolo
	73 /usr/share/timidity/instruments/flute
	74 /usr/share/timidity/instruments/recorder
	75 /usr/share/timidity/instruments/woodflut
	76 /usr/share/timidity/instruments/bottle
	77 /usr/share/timidity/instruments/shakazul
	78 /usr/share/timidity/instruments/whistle
	79 /usr/share/timidity/instruments/ocarina
	80 /usr/share/timidity/instruments/sqrwave
	81 /usr/share/timidity/instruments/sawwave
	82 /usr/share/timidity/instruments/calliope
	83 /usr/share/timidity/instruments/chiflead
	84 /usr/share/timidity/instruments/charang
	85 /usr/share/timidity/instruments/voxlead
	86 /usr/share/timidity/instruments/lead5th
	87 /usr/share/timidity/instruments/basslead
	88 /usr/share/timidity/instruments/fantasia
	89 /usr/share/timidity/instruments/warmpad
	90 /usr/share/timidity/instruments/polysyn
	91 /usr/share/timidity/instruments/ghostie
	92 /usr/share/timidity/instruments/bowglass
	93 /usr/share/timidity/instruments/metalpad
	94 /usr/share/timidity/instruments/halopad
	95 /usr/share/timidity/instruments/sweeper
	96 /usr/share/timidity/instruments/aurora
	97 /usr/share/timidity/instruments/soundtrk
	98 /usr/share/timidity/instruments/crystal
	99 /usr/share/timidity/instruments/atmosphr
	100 /usr/share/timidity/instruments/freshair
	101 /usr/share/timidity/instruments/unicorn
	102 /usr/share/timidity/instruments/echovox
	103 /usr/share/timidity/instruments/startrak
	104 /usr/share/timidity/instruments/sitar
	105 /usr/share/timidity/instruments/banjo
	106 /usr/share/timidity/instruments/shamisen
	107 /usr/share/timidity/instruments/koto
	108 /usr/share/timidity/instruments/kalimba
	109 /usr/share/timidity/instruments/bagpipes
	110 /usr/share/timidity/instruments/fiddle
	111 /usr/share/timidity/instruments/shannai
	112 /usr/share/timidity/instruments/carillon
	113 /usr/share/timidity/instruments/agogo
	114 /usr/share/timidity/instruments/steeldrm
	115 /usr/share/timidity/instruments/woodblk
	116 /usr/share/timidity/instruments/taiko
	117 /usr/share/timidity/instruments/toms
	118 /usr/share/timidity/instruments/syntom
	119 /usr/share/timidity/instruments/revcym
	120 /usr/share/timidity/instruments/fx-fret
	121 /usr/share/timidity/instruments/fx-blow
	122 /usr/share/timidity/instruments/seashore
	123 /usr/share/timidity/instruments/jungle
	124 /usr/share/timidity/instruments/telephon
	125 /usr/share/timidity/instruments/helicptr
	126 /usr/share/timidity/instruments/applause note=69
	127 /usr/share/timidity/instruments/pistol

##############################################################################
# The GUS drum patches

drumset 0

	27 /usr/share/timidity/instruments/highq
	28 /usr/share/timidity/instruments/slap
	29 /usr/share/timidity/instruments/scratch1
	30 /usr/share/timidity/instruments/scratch2
	31 /usr/share/timidity/instruments/sticks strip=tail
	32 /usr/share/timidity/instruments/sqrclick
	33 /usr/share/timidity/instruments/metclick
	34 /usr/share/timidity/instruments/metbell keep=loop keep=env
	35 /usr/share/timidity/instruments/kick1
	36 /usr/share/timidity/instruments/kick2
	37 /usr/share/timidity/instruments/stickrim strip=tail
	38 /usr/share/timidity/instruments/snare1
	39 /usr/share/timidity/instruments/claps
	40 /usr/share/timidity/instruments/snare2 note=38
	41 /usr/share/timidity/instruments/tomlo2
	42 /usr/share/timidity/instruments/hihatcl
	43 /usr/share/timidity/instruments/tomlo1
	44 /usr/share/timidity/instruments/hihatpd
	45 /usr/share/timidity/instruments/tommid2
	46 /usr/share/timidity/instruments/hihatop
	47 /usr/share/timidity/instruments/tommid1
	48 /usr/share/timidity/instruments/tomhi2
	49 /usr/share/timidity/instruments/cymcrsh1
	50 /usr/share/timidity/instruments/tomhi1
	51 /usr/share/timidity/instruments/cymride1
	52 /usr/share/timidity/instruments/cymchina
	53 /usr/share/timidity/instruments/cymbell
	54 /usr/share/timidity/instruments/tamborin
	55 /usr/share/timidity/instruments/cymsplsh
	56 /usr/share/timidity/instruments/cowbell
	57 /usr/share/timidity/instruments/cymcrsh2
	58 /usr/share/timidity/instruments/vibslap
	59 /usr/share/timidity/instruments/cymride2
	60 /usr/share/timidity/instruments/bongohi
	61 /usr/share/timidity/instruments/bongolo
	62 /usr/share/timidity/instruments/congahi1
	63 /usr/share/timidity/instruments/congahi2
	64 /usr/share/timidity/instruments/congalo
	65 /usr/share/timidity/instruments/timbaleh
	66 /usr/share/timidity/instruments/timbalel
	67 /usr/share/timidity/instruments/agogohi
	68 /usr/share/timidity/instruments/agogolo
	69 /usr/share/timidity/instruments/cabasa strip=tail
	70 /usr/share/timidity/instruments/maracas
	71 /usr/share/timidity/instruments/whistle1 keep=loop keep=env
	72 /usr/share/timidity/instruments/whistle2 keep=loop keep=env
	73 /usr/share/timidity/instruments/guiro1
	74 /usr/share/timidity/instruments/guiro2
	75 /usr/share/timidity/instruments/clave
	76 /usr/share/timidity/instruments/woodblk1
	77 /usr/share/timidity/instruments/woodblk2
	78 /usr/share/timidity/instruments/cuica1
	79 /usr/share/timidity/instruments/cuica2
	80 /usr/share/timidity/instruments/triangl1
	81 /usr/share/timidity/instruments/triangl2
	82 /usr/share/timidity/instruments/shaker
	83 /usr/share/timidity/instruments/jingles
	84 /usr/share/timidity/instruments/belltree keep=loop keep=env
	85 /usr/share/timidity/instruments/castinet
	86 /usr/share/timidity/instruments/surdo1
	87 /usr/share/timidity/instruments/surdo2

dir /usr/share/timidity/freepats
source /etc/timidity/freepats/freepats.cfg
EOF
cp -a %{buildroot}%{_sysconfdir}/timidity/timidity.cfg %{buildroot}%{_sysconfdir}/alternatives
#desktop menu
%__install -dm 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{tarname}.desktop << EOF
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=PyKaraoke
Comment=Universal karaoke songs and movies player
Icon=/usr/share/pykaraoke/icons/pykaraoke.xpm
Exec=pykaraoke
Terminal=false
MimeType=audio/x-karaoke;audio/x-midi;audio/midi;
Categories=AudioVideo;Player;Player;X-MandrivaLinux-Multimedia-Sound;
EOF

%__rm -f %{buildroot}%{_datadir}/applications/%{tarname}_mini.desktop
#desktop mini
#%__install -dm 755 %{buildroot}%{_datadir}/applications
#%__cat > %{buildroot}%{_datadir}/applications/%{name}_mini.desktop << EOF
#[Desktop Entry]
#Type=Application
#Encoding=UTF-8
#Name=PyKaraoke Mini
#GenericName=Karaoke player
#Comment=Minimum-interface PyKaraoke
#Icon=/usr/share/pykaraoke/icons/pykaraoke.xpm
#Exec=pykaraoke_mini
#Terminal=false
#MimeType=audio/x-karaoke;audio/x-midi;audio/midi
#Categories=AudioVideo;Player;Player;Player;X-MandrivaLinux-Multimedia-Sound;
#EOF

%__install -dm 755 %{buildroot}%{_datadir}/mime/packages
%__cat >%{buildroot}%{_datadir}/mime/packages/%{name}.xml <<EOF
<?xml version="1.0"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="audio/x-karaoke">
    <comment>Karaoke file</comment>
    <glob pattern="*.cdg"/>
    <glob pattern="*.kar"/>
     <magic priority="60">
       <match value="foobar-file" type="string" offset="20:140"/>
     </magic>
  </mime-type>
</mime-info>
EOF


chmod +x $RPM_BUILD_ROOT/usr/bin/cdg2mpg
chmod +x $RPM_BUILD_ROOT/usr/bin/py*

%clean
rm -rf %{buildroot}

#%post
#%{update_menus}
#%{update_mime_database}

#%postun
#%{clean_menus}
#%{clean_mime_database}

%files
%defattr(-, root,root)
%doc README.txt COPYING TODO
%config(noreplace) %{_sysconfdir}/timidity/*.cfg
%config(noreplace) %{_sysconfdir}/alternatives/*.cfg
%{_bindir}/%{tarname}
%{_bindir}/%{tarname}_mini
%{_bindir}/pykar
%{_bindir}/pympg
%{_bindir}/cdg2mpg
%{_bindir}/pycdg
%{_datadir}/%{tarname}
#%{py_sitedir}/*
%{py_platsitedir}/*
%{_datadir}/applications/%{tarname}.desktop
#%{_datadir}/applications/%{name}_mini.desktop
%{_datadir}/mime/packages/%{name}.xml

