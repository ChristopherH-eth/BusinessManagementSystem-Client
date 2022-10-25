from Network.tcp import Tcp

def test_CreateTcp():
    tcp = Tcp()
    assert tcp

def test_GetHost():
    tcp = Tcp()
    host = tcp.GetHost()
    assert host == "127.0.0.1"