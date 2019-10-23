import re
def yn(question):
  res = input(question + "? ")
  if re.search("yes", res, re.IGNORECASE): return True
  elif re.search("no", res, re.IGNORECASE): return False
  else: return yn('Please answer with "yes" or "no". ' + question)