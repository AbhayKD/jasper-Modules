# pause to pause

#dynamic : "volume +10 0" or "volume -10 0"  this inc / dec 10,
#static : "volume 10 1" this set volume to 10

import main,time,socket,sys
import urllib2,subprocess

def handleCmd(p):
    while True:
        cmd = raw_input("Enter cmd: ")
        if cmd == 'p':
            p.stdin.write('stop\n')
            return
        elif cmd == 'q':
            p.stdin.write('quit\n')
            time.sleep(1)
            sys.exit()
        else:
            p.stdin.write('volume %s 1\n' % cmd)
            continue

def playsong(url):
    openCmd = ['mplayer','-idle','-audiofile-cache','1500','-prefer-ipv4','-nolirc','-slave',url]
    p = subprocess.Popen(openCmd, stdout = subprocess.PIPE, stdin=subprocess.PIPE)
    return p


def mainfunc():

    term = "benny dayal"

    list,dis = main.search(term)

#for n,x in enumerate(list):
#    try:
#        url = main.get_stream(x)
#        print url
#    except (urllib2.HTTPError,socket.timeout):
#        print "Skipping ", list.index(x)," ",x.get('song')
#        time.sleep(1)
#        continue
    opener = urllib2.build_opener()

    it = iter(range(len(list)))
    for i in it:
        try:
            url = main.get_stream(list[i])
            cl = opener.open(url, timeout=3)
            openCmd = ['mplayer','-idle','-audiofile-cache','1500','-prefer-ipv4','-nolirc','-slave',url]
            p = subprocess.Popen(openCmd, stdout = subprocess.PIPE, stdin=subprocess.PIPE)
            print list[i].get('song')

        except (urllib2.HTTPError,socket.timeout):
            print "Skipping ",x.get('song')
            time.sleep(1)
            continue
        except (IOError, KeyError):
            print ('track unresolved')
            continue

            #p.stdin.write('\n'+cmd+'\n')
            #output = p.stdout.readline()
            #sys.stdout.flush()
        handleCmd(p)


if __name__ == "__main__":
    mainfunc()
