
import json, sys, subprocess, time, os
from urllib.request import urlopen


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("Usage: gitget <username>")
        sys.exit(1)
    
    user = sys.argv[1] ## github username

    repoURL = ('https://api.github.com/users/' + user) + '/repos'
    html = urlopen(repoURL).read().decode('utf-8')
    repoJSON = json.loads(html)
    file = open("{}.txt".format(user), "w")
    for url in repoJSON:
       file.write("{}".format(url["html_url"] + ".git" + "\n"))


    ##os.system('bash cloner.sh ' + user + '.txt')
    
    sys.exit(1)
