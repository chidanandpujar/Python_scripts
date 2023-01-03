% cat snmp-fpcmem.py 
from jnpr.junos import Device
from jnpr.junos.op.fpc import FpcInfoTable
import warnings
import jcs

if __name__ == '__main__':

    snmp_action = jcs.get_snmp_action()
    snmp_oid = jcs.get_snmp_oid()

    jcs.syslog("8", "snmp_action = ", snmp_action, " snmp_oid = ", snmp_oid)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # open local device for access and get tables
        dev = Device()
        dev.open()

        qfxfpc = FpcInfoTable(dev)
        qfxfpc.get()
        for item in qfxfpc:
            if (item.key == '0'):
                fpcmem = item.memory
                fpccpu = item.cpu

        dev.close()

    if snmp_action == 'get':
        if snmp_oid == '.1.3.6.1.4.1.2636.13.61.1.9.1.1.1':
            jcs.syslog("8", "babud snmp_action = ", snmp_action, " snmp_oid = ",snmp_oid)
            #print("Hello")
            jcs.emit_snmp_attributes(snmp_oid, "Integer32", fpcmem)
        elif snmp_oid == '.1.3.6.1.4.1.2636.13.61.1.9.1.1.2':
            jcs.emit_snmp_attributes(snmp_oid, "Integer32", fpccpu)

    elif snmp_action == 'get-next':
        if snmp_oid == '.1.3.6.1.4.1.2636.13.61.1.9.1.1':
            jcs.emit_snmp_attributes(".1.3.6.1.4.1.2636.13.61.1.9.1.1.1", "Integer32", "22")
        elif snmp_oid == '.1.3.6.1.4.1.2636.13.61.1.9.1.1.1':
            jcs.emit_snmp_attributes(".1.3.6.1.4.1.2636.13.61.1.9.1.1.2", "Integer32", "340")
