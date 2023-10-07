#!/usr/bin/env python3
import subprocess
import json

def filter_files(string):
    return ".github" not in string and "/" in string

diff_cmd = subprocess.run(['git', 'diff', '--name-status', 'HEAD', 'HEAD~1'], stdout=subprocess.PIPE)
diff_files = diff_cmd.stdout.decode("utf-8")
files = diff_files.split("\n")
files.pop()

result_tuples = [s.split('\t')[1] for s in files]
filtered_strings = list(filter(filter_files, result_tuples))
files = [s.split('/')[0] for s in filtered_strings]

print("files=" + json.dumps(files))
