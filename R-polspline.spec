#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-polspline
Version  : 1.1.19
Release  : 45
URL      : https://cran.r-project.org/src/contrib/polspline_1.1.19.tar.gz
Source0  : https://cran.r-project.org/src/contrib/polspline_1.1.19.tar.gz
Summary  : Polynomial Spline Routines
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-polspline-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
hazard regression, hazard estimation with flexible tails, logspline,
  lspec, polyclass, and polymars, by C. Kooperberg and co-authors.

%package lib
Summary: lib components for the R-polspline package.
Group: Libraries

%description lib
lib components for the R-polspline package.


%prep
%setup -q -c -n polspline
cd %{_builddir}/polspline

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590680979

%install
export SOURCE_DATE_EPOCH=1590680979
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polspline
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polspline
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library polspline
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc polspline || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/polspline/DESCRIPTION
/usr/lib64/R/library/polspline/INDEX
/usr/lib64/R/library/polspline/Meta/Rd.rds
/usr/lib64/R/library/polspline/Meta/features.rds
/usr/lib64/R/library/polspline/Meta/hsearch.rds
/usr/lib64/R/library/polspline/Meta/links.rds
/usr/lib64/R/library/polspline/Meta/nsInfo.rds
/usr/lib64/R/library/polspline/Meta/package.rds
/usr/lib64/R/library/polspline/NAMESPACE
/usr/lib64/R/library/polspline/R/polspline
/usr/lib64/R/library/polspline/R/polspline.rdb
/usr/lib64/R/library/polspline/R/polspline.rdx
/usr/lib64/R/library/polspline/help/AnIndex
/usr/lib64/R/library/polspline/help/aliases.rds
/usr/lib64/R/library/polspline/help/paths.rds
/usr/lib64/R/library/polspline/help/polspline.rdb
/usr/lib64/R/library/polspline/help/polspline.rdx
/usr/lib64/R/library/polspline/html/00Index.html
/usr/lib64/R/library/polspline/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/polspline/libs/polspline.so
/usr/lib64/R/library/polspline/libs/polspline.so.avx2
/usr/lib64/R/library/polspline/libs/polspline.so.avx512
