# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['info.py'],
             pathex=['C:\\Users\\Playdata\\Desktop\\final'],
             binaries=[],
             datas=[('opencv_videoio_ffmpeg420.dll', '.')],
             hiddenimports=['pyttsx3.drivers','pyttsx3.drivers.sapi5','cv2'],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='info',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='icon.ico')
