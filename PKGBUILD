# Maintainer: Jason McGillivray < mcgillivray dot jason at gmail dot com>


pkgname=py3status_amdfan
pkgdesc="Py3status module for monitoring fan and temp of amdgpu video cards"
pkgver=0.1.7
pkgrel=1
arch=('any')
license=('MIT')
depends=('python' 'py3status' 'amdfan')
makedepends=('python-setuptools')
url="https://github.com/mcgillij/py3status-amdfan"
source=("https://github.com/mcgillij/py3status-amdfan/releases/download/$pkgver/py3status-amdfan-$pkgver.tar.gz")
md5sums=('d82a10d09c67334e1092b8592bb1e8cc')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --prefix=/usr --root="$pkgdir"
}
