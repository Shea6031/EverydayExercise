#-*- coding:utf-8 -*-

from thrift import Thrift  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  

from hbase import Hbase  
from hbase.ttypes import *

thrift_host = "30.26.96.10"
thrift_port = 9090
thrift_timeout = 5000

# Make socket
transport = TSocket.TSocket(thrift_host, thrift_port)
# Set timeout
transport.setTimeout(thrift_timeout)

trans = TTransport.TBufferedTransport(transport)
# Wrap in a protocol
protocol = TBinaryProtocol.TBinaryProtocol(trans)
# Make client
client = Hbase.Client(protocol)
# Connect
transport.open()

