"""
The author of this code is: Hashm. A
Github: MD5-Hashm
Discord: MD5 Hash(m)#2779
This code is licenced under the GNU Affero General Public License version 3.0
For more information about this license and its limitations, see: https://www.gnu.org/licenses/agpl-3.0.html
"""
import sys
import subprocess
dl = []
not_installed = []
def download_and_check(package):
    if type(package) is str:
        pass
    else:
        raise TypeError("'package' must be str")
    try:
        print("Installing: " + str(package))
        subprocess.run(f'{sys.executable} -m pip -q -q install {package}')
        __import__(package)
    except ImportError:
        return False
    return True

def install_packages(packs):
    if type(packs) is list:
        pass
    else:
        raise TypeError("Error: install_packages() requires a 'list' of packages")
    for mod in packs:
        if download_and_check(mod):
            pass
        else:
            not_installed.append(str(mod))
    if len(not_installed) > 0:
        return False
    else:
        return True

def test_packages(packs):
    if type(packs) is list:
        pass
    else:
        raise TypeError("Error: import_packages() requires a 'list' of packages")
    for mod in packs:
        try:
            __import__(mod)
        except ImportError:
            dl.append(str(mod))
    if len(dl) > 0:
        if install_packages(dl):
            return True
        else:
            return False
    else:
        return True

def import_packages(packs):
    if test_packages(packs) == True:
        return 'for mod in packages: exec(f\"import {mod}\")'
    else:
        return 'print("Automatic package installation failed please manually install the required packages.") & exit(1)'
