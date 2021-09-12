import requests
import json
from pathlib import Path

class _networkCalc():
    apiAddress = "https://networkcalc.com/api"

    def __init__(self, ca=None, requestTimeout=15):
        self.requestTimeout = requestTimeout
        if ca != None:
            if type(ca) is str:
                self.ca = str(Path(ca))
            elif type(ca) is bool:
                self.ca = ca
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        if self.ca != None:
            kwargs["verify"] = self.ca
        try:
            url = "{0}/{1}".format(self.apiAddress,endpoint)
            if methord == "GET":
                response = requests.get(url, **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            return 0, "Connection Timeout - {0}".format(e)
        return response.status_code, json.loads(response.text)

    def subnetCalculator(self,cidr,binary=False):
        if binary:
            statusCode, response = self.apiCall("ip/{0}?binary=true".format(cidr))
        else:
            statusCode, response = self.apiCall("ip/{0}".format(cidr))
        return response

    def binaryCalculator(self,binaryNumber,fromBase,toBase):
        statusCode, response = self.apiCall("binary/{0}?from={1}&to={2}".format(binaryNumber,fromBase,toBase))
        return response

    def getCertificate(self,domain,port=None):
        if port:
            statusCode, response = self.apiCall("security/certificate/{0}?port={1}".format(domain,port))
        else:
            statusCode, response = self.apiCall("security/certificate/{0}".format(domain))
        return response

    def dnsLookup(self,hostname):
        statusCode, response = self.apiCall("dns/lookup/{0}".format(hostname))
        return response

    def whoisLookup(self,hostname):
        statusCode, response = self.apiCall("dns/whois/{0}".format(hostname))
        return response
