import sys
import subprocess

run_thru_shell = sys.platform.startswith('win')
cwd = '../repo_name'

proc = subprocess.Popen(
    ['git', 'init'],
    shell=run_thru_shell,
    cwd=cwd
)
proc.wait()

# add
proc = subprocess.Popen(
    ['git', 'add', '-A'],
    shell=run_thru_shell,
    cwd=cwd
)
proc.wait()

# commit
proc = subprocess.Popen(
    ['git', 'commit', '-m', '"First commit"'],
    shell=run_thru_shell,
    cwd=cwd
)
proc.wait()
