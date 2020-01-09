# to make this source tree a little cleaner, all the actual python code for the program itself goes in src/
# data files and build scripts shouldn't go in that directory. so if you want to run the code while working on it,
# you can use this script
import os, sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
os.chdir("src")
sys.path.append(".")
import item_tracker
item_tracker.main()