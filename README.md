# py3status-amdfan
Python module for monitoring fan RPMs and temperature for `amdgpu` cards in **i3wm** using py3status.

[![Downloads](https://static.pepy.tech/personalized-badge/py3status-amdfan?period=total&units=international_system&left_color=blue&right_color=green&left_text=Downloads)](https://pepy.tech/project/py3status-amdfan)

## Screenshot
![Status Bar with py3status_amdfan](https://raw.githubusercontent.com/mcgillij/py3status-amdfan/main/images/py3status-amdfan.png)

## Prerequisites

* i3
* py3status
* [amdfan](https://github.com/mcgillij/amdfan)
* poetry (if installing from git)

## Installation

### From Git

``` bash
git clone https://github.com/mcgillij/py3status-amdfan.git
cd py3status-amdfan && poetry install
mkdir -p ~/.i3/py3status && cd ~/.i3/py3status
ln -s <PATH_TO_CLONED_REPO>/src/py3status_amdfan/fan_monitor.py ./
```

### With Pip, Pipenv or Poetry

``` bash
pip install py3status-amdfan amdfan
pipenv install py3status-amdfan amdfan
poetry add py3status-amdfan amdfan && poetry install
```

### With `yay`

``` bash
yay -S py3status-amdfan amdfan
```

### Building Arch package w/PKGBUILD

``` bash
git clone https://aur.archlinux.org/py3status-amdfan.git
cd py3status-amdfan.git
makechrootpkg -c -r $HOME/$CHROOT
```

### Installing built Arch package

``` bash
sudo pacman -U --asdeps py3status-amdfan-*-any.pkg.tar.zst
```

## Configuration

Next you will need to add the services you want to monitor, and optionally choose some appropriate emoji's.
You can also configure actions to open up your browser when you click on the icon, which I find pretty handy.

**~/.config/i3/i3status.conf**

```bash
...
order += "fan_monitor"
order += "clock"
order += "mail"
...
```

## Configuration Options

You can pass in the following configuration options:

* cache_timeout
* format

## Restart i3

Once the package is installed and configured you just need to restart i3.
