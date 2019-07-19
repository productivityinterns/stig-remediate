import subprocess
import os

subprocess.call(["rpm -gf <filename>", "-1"])
subprocess.call(["rpm --setperms <packagename>", "-2"])
subprocess.call(["rpm --setugids<packagename>", "-3"])
os.access()