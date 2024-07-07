# Maintainer: Jason McGillivray < mcgillivray dot jason at gmail dot com>


pkgname=py3status-amdfan
pkgdesc="Py3status module for monitoring fan and temp of amdgpu video cards"
pkgver=0.1.15
pkgrel=1
arch=('any')
license=('MIT')
depends=('python' 'py3status' 'amdfan')
makedepends=('python-build' 'python-installer' 'python-poetry-core')
url="https://github.com/mcgillij/py3status-amdfan"
#source=("py3status_amdfan-$pkgver.tar.gz")
source=("https://github.com/mcgillij/py3status-amdfan/releases/download/$pkgver/py3status_amdfan-$pkgver.tar.gz")
md5sums=('47eda0c0884a5fccf3bbbbc245462c9b')

build() {
  cd "$srcdir/py3status_amdfan-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/py3status_amdfan-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
