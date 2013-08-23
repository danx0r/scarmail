import  subprocess, time, os

def run(*args, **kw):
    if 'timeout' in kw:
        timeout = float(kw['timeout'])
        print "timeout:", timeout
        del kw['timeout']
    else:
        timeout = 0
    try:
        if not timeout:
            kw['stderr'] = subprocess.STDOUT
            out = subprocess.check_output(*args, **kw)
        else:
            proc = subprocess.Popen(*args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            time.sleep(timeout)
            if proc.poll() is None:
                out = "__TIMEOUT__"
            else:
                out, err = proc.communicate()

    except subprocess.CalledProcessError as e:
        out = e.output
    return out

if __name__ == "__main__":
    print "test run.py"
    cmd = "ls", "-rltR", "/home/dbm/mp3"
    s = run(cmd, timeout=10)
    print "output----------\n", s
    print "end output------"
