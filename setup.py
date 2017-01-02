from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
  options = {'py2exe': {'bundle_files': 2, 'compressed': True, 'dist_dir': "private_dist"}},
  windows = [{'script': "PyAutoClicker.py"}],
  zipfile = None,
)
