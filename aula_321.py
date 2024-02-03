import encodings
import subprocess
import sys

print(sys.platform)


cmd = ['ping','127.0.0.1']
encoding = 'utf_8'
system = sys.platform


if sys.platform == 'win32':
    cmd = ['ping','127.0.0.1']
    encoding = 'cp850'

proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encoding,
    shell=True
)
print()

print(proc)
print(proc.args)
print(proc.stderr)
print(proc.stdout)
print(proc.returncode)