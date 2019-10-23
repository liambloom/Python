from yesno import yn
import time

if yn("Is it raining"): 
  if yn("Do you have an umbrella"): print("You should go outside!")
  else:
    def wait():
      print("We should wait for the rain to stop", end="", flush=True)
      for _ in range(6):
        print(".", end="", flush=True)
        time.sleep(0.5)
      print("")
      if yn("Is it still raining"): wait()
      else: print("You should go outside!")
    wait()
else: print("You should go outside!")