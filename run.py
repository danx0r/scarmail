import  subprocess, time, os, sys

def run(*args, **kw):
    if 'timeout' in kw:
        timeout = float(kw['timeout'])
        print "running", args[0], "with timeout:", timeout,
        del kw['timeout']
    else:
        timeout = 0
    try:
        if not timeout:
            kw['stderr'] = subprocess.STDOUT
            out = subprocess.check_output(*args, **kw)
        else:
            proc = subprocess.Popen(*args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            t0 = time.time()
            out = "__TIMEOUT__"
            while time.time() < t0 + timeout:
                if proc.poll() != None:
                    out, err = proc.communicate()
                    print
                    sys.stdout.flush()
                    break
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(1.0)
            if out == "__TIMEOUT__":
                proc.kill()
                print
                sys.stdout.flush()

    except subprocess.CalledProcessError as e:
        out = e.output
    return out

if __name__ == "__main__":
    print "test run.py"
    cmd = "ls", "-rltR", "/home/dbm/"
    s = run(cmd, timeout=4)
    print "output----------\n", s
    print "end output------"
