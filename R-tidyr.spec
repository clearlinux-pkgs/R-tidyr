#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tidyr
Version  : 1.3.0
Release  : 64
URL      : https://cran.r-project.org/src/contrib/tidyr_1.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tidyr_1.3.0.tar.gz
Summary  : Tidy Messy Data
Group    : Development/Tools
License  : MIT
Requires: R-tidyr-lib = %{version}-%{release}
Requires: R-cli
Requires: R-cpp11
Requires: R-dplyr
Requires: R-glue
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-purrr
Requires: R-rlang
Requires: R-stringr
Requires: R-tibble
Requires: R-tidyselect
Requires: R-vctrs
BuildRequires : R-cli
BuildRequires : R-cpp11
BuildRequires : R-data.table
BuildRequires : R-dplyr
BuildRequires : R-glue
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-stringr
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : R-vctrs
BuildRequires : buildreq-R

%description
variable, each row is an observation, and each cell contains a single
    value.  'tidyr' contains tools for changing the shape (pivoting) and
    hierarchy (nesting and 'unnesting') of a dataset, turning deeply
    nested lists into rectangular data frames ('rectangling'), and
    extracting values out of string columns. It also includes tools for
    working with missing values (both implicit and explicit).

%package lib
Summary: lib components for the R-tidyr package.
Group: Libraries

%description lib
lib components for the R-tidyr package.


%prep
%setup -q -n tidyr
cd %{_builddir}/tidyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678828497

%install
export SOURCE_DATE_EPOCH=1678828497
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyr/DESCRIPTION
/usr/lib64/R/library/tidyr/INDEX
/usr/lib64/R/library/tidyr/LICENSE
/usr/lib64/R/library/tidyr/Meta/Rd.rds
/usr/lib64/R/library/tidyr/Meta/data.rds
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
/usr/lib64/R/library/tidyr/doc/in-packages.R
/usr/lib64/R/library/tidyr/doc/in-packages.Rmd
/usr/lib64/R/library/tidyr/doc/in-packages.html
/usr/lib64/R/library/tidyr/doc/index.html
/usr/lib64/R/library/tidyr/doc/nest.R
/usr/lib64/R/library/tidyr/doc/nest.Rmd
/usr/lib64/R/library/tidyr/doc/nest.html
/usr/lib64/R/library/tidyr/doc/pivot.R
/usr/lib64/R/library/tidyr/doc/pivot.Rmd
/usr/lib64/R/library/tidyr/doc/pivot.html
/usr/lib64/R/library/tidyr/doc/programming.R
/usr/lib64/R/library/tidyr/doc/programming.Rmd
/usr/lib64/R/library/tidyr/doc/programming.html
/usr/lib64/R/library/tidyr/doc/rectangle.R
/usr/lib64/R/library/tidyr/doc/rectangle.Rmd
/usr/lib64/R/library/tidyr/doc/rectangle.html
/usr/lib64/R/library/tidyr/doc/tidy-data.R
/usr/lib64/R/library/tidyr/doc/tidy-data.Rmd
/usr/lib64/R/library/tidyr/doc/tidy-data.html
/usr/lib64/R/library/tidyr/help/AnIndex
/usr/lib64/R/library/tidyr/help/aliases.rds
/usr/lib64/R/library/tidyr/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/tidyr/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/tidyr/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/tidyr/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/tidyr/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/tidyr/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/tidyr/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/tidyr/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/tidyr/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/tidyr/help/figures/logo.png
/usr/lib64/R/library/tidyr/help/paths.rds
/usr/lib64/R/library/tidyr/help/tidyr.rdb
/usr/lib64/R/library/tidyr/help/tidyr.rdx
/usr/lib64/R/library/tidyr/html/00Index.html
/usr/lib64/R/library/tidyr/html/R.css
/usr/lib64/R/library/tidyr/tests/testthat.R
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/append.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/chop.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/complete.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/drop-na.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/expand.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/extract.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/fill.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/gather.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/hoist.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/nest-legacy.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/nest.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/pack.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/pivot-long.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/pivot-wide.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/pivot.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/replace_na.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/separate-longer.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/separate-rows.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/separate-wider.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/separate.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/seq.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/spread.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/uncount.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/unite.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/unnest-helper.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/unnest-longer.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/unnest-wider.md
/usr/lib64/R/library/tidyr/tests/testthat/_snaps/unnest.md
/usr/lib64/R/library/tidyr/tests/testthat/test-append.R
/usr/lib64/R/library/tidyr/tests/testthat/test-chop.R
/usr/lib64/R/library/tidyr/tests/testthat/test-complete.R
/usr/lib64/R/library/tidyr/tests/testthat/test-drop-na.R
/usr/lib64/R/library/tidyr/tests/testthat/test-expand.R
/usr/lib64/R/library/tidyr/tests/testthat/test-extract.R
/usr/lib64/R/library/tidyr/tests/testthat/test-fill.R
/usr/lib64/R/library/tidyr/tests/testthat/test-gather.R
/usr/lib64/R/library/tidyr/tests/testthat/test-hoist.R
/usr/lib64/R/library/tidyr/tests/testthat/test-id.R
/usr/lib64/R/library/tidyr/tests/testthat/test-nest-legacy.R
/usr/lib64/R/library/tidyr/tests/testthat/test-nest.R
/usr/lib64/R/library/tidyr/tests/testthat/test-pack.R
/usr/lib64/R/library/tidyr/tests/testthat/test-pivot-long.R
/usr/lib64/R/library/tidyr/tests/testthat/test-pivot-wide.R
/usr/lib64/R/library/tidyr/tests/testthat/test-pivot.R
/usr/lib64/R/library/tidyr/tests/testthat/test-replace_na.R
/usr/lib64/R/library/tidyr/tests/testthat/test-separate-longer.R
/usr/lib64/R/library/tidyr/tests/testthat/test-separate-rows.R
/usr/lib64/R/library/tidyr/tests/testthat/test-separate-wider.R
/usr/lib64/R/library/tidyr/tests/testthat/test-separate.R
/usr/lib64/R/library/tidyr/tests/testthat/test-seq.R
/usr/lib64/R/library/tidyr/tests/testthat/test-spread.R
/usr/lib64/R/library/tidyr/tests/testthat/test-uncount.R
/usr/lib64/R/library/tidyr/tests/testthat/test-unite.R
/usr/lib64/R/library/tidyr/tests/testthat/test-unnest-auto.R
/usr/lib64/R/library/tidyr/tests/testthat/test-unnest-helper.R
/usr/lib64/R/library/tidyr/tests/testthat/test-unnest-longer.R
/usr/lib64/R/library/tidyr/tests/testthat/test-unnest-wider.R
/usr/lib64/R/library/tidyr/tests/testthat/test-unnest.R
/usr/lib64/R/library/tidyr/tests/testthat/test-utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tidyr/libs/tidyr.so
/usr/lib64/R/library/tidyr/libs/tidyr.so.avx2
/usr/lib64/R/library/tidyr/libs/tidyr.so.avx512
