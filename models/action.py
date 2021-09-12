import jimi

from plugins.networkCalc.includes import networkCalc

class _networkCalcSubnetCalculator(jimi.action._action):
    cidr = str()
    binaryMode = False

    def doAction(self,data):
        cidr = jimi.helpers.evalString(self.cidr,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        response = networkCalc._networkCalc().subnetCalculator(cidr,self.binaryMode)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

class _networkCalcBinaryCalculator(jimi.action._action):
    binaryNumber = str()
    fromBase = str()
    toBase = str()

    def doAction(self,data):
        binaryNumber = jimi.helpers.evalString(self.binaryNumber,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        fromBase = jimi.helpers.evalString(self.fromBase,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        toBase = jimi.helpers.evalString(self.toBase,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        response = networkCalc._networkCalc().binaryCalculator(binaryNumber,fromBase,toBase)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

class _networkCalcGetCertificate(jimi.action._action):
    domain = str()
    port = str()

    def doAction(self,data):
        domain = jimi.helpers.evalString(self.domain,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        port = jimi.helpers.evalString(self.port,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        response = networkCalc._networkCalc().getCertificate(domain,port)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

class _networkCalcDNSLookup(jimi.action._action):
    hostname = str()

    def doAction(self,data):
        hostname = jimi.helpers.evalString(self.hostname,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        response = networkCalc._networkCalc().dnsLookup(hostname)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }

class _networkCalcWHOISLookup(jimi.action._action):
    hostname = str()

    def doAction(self,data):
        hostname = jimi.helpers.evalString(self.hostname,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        response = networkCalc._networkCalc().whoisLookup(hostname)
        if response:
            return { "result" : True, "rc" : 200, "response" : response }
        else:
            return { "result" : False, "rc" : 404, "msg" : "Failed to get a valid response from API call" }