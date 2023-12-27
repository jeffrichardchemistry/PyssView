# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['pyssview.py'],
             pathex=['/dados/GoogleDrive/rotinas_python/github_projects/PyssView/app'],
             binaries=[],
             datas=[('/dados/GoogleDrive/rotinas_python/github_projects/PyssView/app/saves/sav.pkl', 'saves'), 
                    ('/dados/GoogleDrive/rotinas_python/github_projects/PyssView/app/states/state.dat', 'states'),
                    ('/dados/GoogleDrive/rotinas_python/github_projects/PyssView/app/icons/*', 'icons')],
             hiddenimports=['PyQt5'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='pyssview',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pyssview')
