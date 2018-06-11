import runpy,pickle

from stackless import tasklet,run,schedule

from pynput import keyboard


def running():
    runpy.run_module("tekli")

def s():
    print("in s")
a=tasklet(running)()
a.insert()
run(5000)


s=pickle.dumps(a)

ns=pickle.load(s)

ns.insert()
run()