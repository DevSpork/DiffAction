#!/usr/bin/env python3
import subprocess
import json

diff_cmd = subprocess.run(['git', 'diff', '--name-status', 'HEAD', 'HEAD~1'], stdout=subprocess.PIPE)
diff_files = diff_cmd.stdout.decode("utf-8")
files = diff_files.split("\n")
files.pop()
result_tuples = [s.split('\t')[1].split("/")[0] for s in files]


print("files=" + json.dumps(result_tuples))
