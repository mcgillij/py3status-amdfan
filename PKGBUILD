# Maintainer: Jason McGillivray < mcgillivray dot jason at gmail dot com>


pkgname=py3status-amdfan
pkgdesc="Py3status module for monitoring fan and temp of amdgpu video cards
pkgver=0.1.0
pkgrel=1
arch=('any')
license=('MIT')
depends=('python' 'py3status' 'amdfan')
makedepends=('python-setuptools')
url="https://github.com/mcgillij/py3status-amdfan"
source=("https://github.com/mcgillij/py3status-amdfan/releases/download/0.1.0/py3status-amdfan-0.1.0.tar.gz")
md5sums=('f5102f23175f091d126f91d982b3f9c1')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --prefix=/usr --root="$pkgdir"
}
