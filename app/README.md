# Compile
To compile this app can be used `pyinstaller` package:

```
pip install pyinstaller
```

The command to compile is:

```
pyinstaller pyssview.spec
```

Its important to mentioning that the variable paths `pathex` and `datas` must be changes to locals one. This variables can be found inside `Analysis` method.


```
a = Analysis(['pyssview.py'],
             pathex=['/dados/GoogleDrive/rotinas_python/github_projects/PyssView/app'],
             binaries=[],
             datas=[('/dados/GoogleDrive/rotinas_python/github_projects/PyssView/app/saves/sav.pkl', 'saves'), 
                    ('/dados/GoogleDrive/rotinas_python/github_projects/PyssView/app/states/state.dat', 'states'),
                    ('/dados/GoogleDrive/rotinas_python/github_projects/PyssView/app/icons/*', 'icons')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
```
