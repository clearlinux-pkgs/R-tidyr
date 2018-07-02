#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tidyr
Version  : 0.8.1
Release  : 14
URL      : https://cran.r-project.org/src/contrib/tidyr_0.8.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tidyr_0.8.1.tar.gz
Summary  : Easily Tidy Data with 'spread()' and 'gather()' Functions
Group    : Development/Tools
License  : MIT
Requires: R-tidyr-lib
Requires: R-dplyr
Requires: R-tibble
Requires: R-tidyselect
BuildRequires : R-dplyr
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : clr-R-helpers

%description
tidying (not general reshaping or aggregating) and works well with
    'dplyr' data pipelines.

%package lib
Summary: lib components for the R-tidyr package.
Group: Libraries

%description lib
lib components for the R-tidyr package.


%prep
%setup -q -c -n tidyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526648605

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1526648605
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tidyr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tidyr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyr/DESCRIPTION
/usr/lib64/R/library/tidyr/INDEX
/usr/lib64/R/library/tidyr/LICENSE
/usr/lib64/R/library/tidyr/Meta/Rd.rds
/usr/lib64/R/library/tidyr/Meta/data.rds
/usr/lib64/R/library/tidyr/Meta/demo.rds
/usr/lib64/R/library/tidyr/Meta/features.rds
/usr/lib64/R/library/tidyr/Meta/hsearch.rds
/usr/lib64/R/library/tidyr/Meta/links.rds
/usr/lib64/R/library/tidyr/Meta/nsInfo.rds
/usr/lib64/R/library/tidyr/Meta/package.rds
/usr/lib64/R/library/tidyr/Meta/vignette.rds
/usr/lib64/R/library/tidyr/NAMESPACE
/usr/lib64/R/library/tidyr/NEWS.md
/usr/lib64/R/library/tidyr/R/tidyr
/usr/lib64/R/library/tidyr/R/tidyr.rdb
/usr/lib64/R/library/tidyr/R/tidyr.rdx
/usr/lib64/R/library/tidyr/data/Rdata.rdb
/usr/lib64/R/library/tidyr/data/Rdata.rds
/usr/lib64/R/library/tidyr/data/Rdata.rdx
/usr/lib64/R/library/tidyr/demo/dadmom.R
/usr/lib64/R/library/tidyr/demo/so-15668870.R
/usr/lib64/R/library/tidyr/demo/so-16032858.R
/usr/lib64/R/library/tidyr/demo/so-17481212.R
/usr/lib64/R/library/tidyr/demo/so-9684671.R
/usr/lib64/R/library/tidyr/doc/index.html
/usr/lib64/R/library/tidyr/doc/tidy-data.R
/usr/lib64/R/library/tidyr/doc/tidy-data.Rmd
/usr/lib64/R/library/tidyr/doc/tidy-data.html
/usr/lib64/R/library/tidyr/help/AnIndex
/usr/lib64/R/library/tidyr/help/aliases.rds
/usr/lib64/R/library/tidyr/help/figures/logo.png
/usr/lib64/R/library/tidyr/help/paths.rds
/usr/lib64/R/library/tidyr/help/tidyr.rdb
/usr/lib64/R/library/tidyr/help/tidyr.rdx
/usr/lib64/R/library/tidyr/html/00Index.html
/usr/lib64/R/library/tidyr/html/R.css
/usr/lib64/R/library/tidyr/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyr/libs/tidyr.so
/usr/lib64/R/library/tidyr/libs/tidyr.so.avx2
/usr/lib64/R/library/tidyr/libs/tidyr.so.avx512
