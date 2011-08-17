### RPM external libungif 4.1.4

Source: http://switch.dl.sourceforge.net/sourceforge/giflib/%{n}-%{realversion}.tar.gz

%prep
%setup -n %n-%{realversion}

%build
./configure --prefix=%{i} --disable-static
make %makeprocesses

%install
make install
# Strip libraries, we are not going to debug them.
find %i/lib -type f -perm /a+x -exec strip {} \;
find %i/bin -type f -perm /a+x -exec strip {} \;
perl -p -i -e "s|^#!.*perl|#!/usr/bin/env perl|" %{i}/bin/gifburst

%post
%{relocateConfig}lib/libungif.la
