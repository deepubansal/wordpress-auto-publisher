from postmaster import PostMaster
import sys

if len(sys.argv) != 5:
    print "Usage: python {0} <url> <username> <password> <base-directory>".format(sys.argv[0])
    sys.exit(1)

postmaster = PostMaster(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
postmaster.process_next()
