#!/usr/bin/env python3
import subprocess

last_tag_cmd = subprocess.run(['git', 'diff', '--name-only', 'HEAD', 'HEAD~1'], stdout=subprocess.PIPE)
last_tag = last_tag_cmd.stdout.decode("utf-8")
last_tag = last_tag.replace("\n", "")
print(last_tag)
