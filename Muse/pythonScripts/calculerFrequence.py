import argparse
from pythonosc import dispatcher, osc_server

tampon0 = 0
tampon = 0
tampon1 = 0

def trouverMaxMin():
    global tampon0
    global tampon
    global tampon1
    if (int(tampon0) < int(tampon)) & (int(tampon) > int(tampon1)):
        print(tampon, " is a maximum")
        return tampon
    elif (int(tampon0) > int(tampon)) & (int(tampon) < int(tampon1)):
        print(tampon, " is a minimum")
        return tampon


def muse_callback(unused_addr, args, ch1=0, ch2="nan", ch3="nan", ch4="nan", ch5="nan", ch6="nan"):
    if ch1 != 0:
        global tampon0
        global tampon
        global tampon1
        print("eeg : ", ch1)
        tampon0 = tampon
        tampon = tampon1
        tampon1 = ch1
        trouverMaxMin()

if __name__ == "__main__":
    disp = dispatcher.Dispatcher()
    disp.map("/muse/eeg", muse_callback, "eeg")

    server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 5000), disp)
    print("server is ready")

    server.serve_forever()