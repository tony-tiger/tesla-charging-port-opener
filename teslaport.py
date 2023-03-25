#!/usr/bin/python3

#############################
## Use at your own risk!!! ##
#############################

from rflib import *
import bitstring
import time
import logging
import atexit

# this function will always run even on exit
def the_end(msg):
    logging.info(msg)

# atexit handler
atexit.register(the_end, 'End')

log_file='tesla.log'

# logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m-%d-%Y %H:%M:%S', filename=log_file, filemode='a', level=logging.INFO)
logging.info('Start up')


# tesla data packet
data_bin = '101010101010101010101010100010101100101100110010110011001100110011001011010011010010110101001010110100110100110010101011010010110001010110010110011001011001100110011001100101101001101001011010100101011010011010011001010101101001011000101011001011001100101100110011001100110010110100110100101101010010101101001101001100101010110100101000'

msg = "Setting all configs"
logging.info(msg)

d = RfCat()
d.setMdmModulation(MOD_ASK_OOK)
d.setFreq(315000000)
d.setMdmSyncMode(0)
d.setMdmDRate(2500)
d.setModeIDLE()
d.setMaxPower()
d.makePktFLEN(0)
d.setMdmDeviatn(6500)
d.setEnableMdmManchester(0)

bin_packed = bitstring.BitArray(bin=data_bin).tobytes()

msg = "Starting up........"
logging.info(msg)

sleep_time=.5
number_of_packets=10

while(1):
   msg = "Transmit {0} packets".format( number_of_packets )
   logging.info(msg)
   for x in range(number_of_packets):
       d.RFxmit(bin_packed)
   time.sleep(sleep_time)



d.setModeIDLE()
d.setAmpMode(0)

