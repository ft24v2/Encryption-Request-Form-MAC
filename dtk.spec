# -*- mode: python -*-

a = Analysis(['/Users/sweetpapa/Desktop/lazy/compile/dtk/dtk.py'],
             pathex=['/Users/sweetpapa/Desktop/lazy/PyInstaller-2.1/dtk'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

a.datas += [('YO.png', 'YO.png',  'DATA')]
a.datas += [('spreadsheet.xlsx', 'spreadsheet.xlsx',  'DATA')]
a.datas += [('spreadsheetcrypt.xlsx', 'spreadsheetcrypt.xlsx',  'DATA')]
a.datas += [('spreadsheetnew.xlsx', 'spreadsheetnew.xlsx',  'DATA')]
a.datas += [('spreadsheetready.xlsx', 'spreadsheetready.xlsx',  'DATA')]
             
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='dtk',
          debug=False,
          strip=None,
          upx=True,
          console=False          )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='dtk')
app = BUNDLE(coll,
             name='dtk.app',
             icon=None)
