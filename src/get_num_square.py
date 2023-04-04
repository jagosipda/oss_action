import os

num = os.environ.get("INPUT_NUM")
if num:
  try:
      num = int(num)
