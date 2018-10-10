import argparse
from pythonosc import dispatcher, osc_server

def muse_callback(unused_addr, args, ch1="nan", ch2="nan", ch3="nan", ch4="nan"):
        print("battery level : ", ch1)

if __name__ == "__main__":
    disp = dispatcher.Dispatcher()
    disp.map("/muse/batt", muse_callback, "battery")

    server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 5000), disp)
    print("server is ready")

    server.serve_forever()