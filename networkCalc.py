import jimi

class _networkCalc(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("networkCalcSubnetCalculator","_networkCalcSubnetCalculator","_action","plugins.networkCalc.models.action")
        jimi.model.registerModel("networkCalcBinaryCalculator","_networkCalcBinaryCalculator","_action","plugins.networkCalc.models.action")
        jimi.model.registerModel("networkCalcGetCertificate","_networkCalcGetCertificate","_action","plugins.networkCalc.models.action")
        jimi.model.registerModel("networkCalcDNSLookup","_networkCalcDNSLookup","_action","plugins.networkCalc.models.action")
        jimi.model.registerModel("networkCalcWHOISLookup","_networkCalcWHOISLookup","_action","plugins.networkCalc.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("networkCalcSubnetCalculator","_networkCalcSubnetCalculator","_action","plugins.networkCalc.models.action")
        jimi.model.deregisterModel("networkCalcBinaryCalculator","_networkCalcBinaryCalculator","_action","plugins.networkCalc.models.action")
        jimi.model.deregisterModel("networkCalcGetCertificate","_networkCalcGetCertificate","_action","plugins.networkCalc.models.action")
        jimi.model.deregisterModel("networkCalcDNSLookup","_networkCalcDNSLookup","_action","plugins.networkCalc.models.action")
        jimi.model.deregisterModel("networkCalcWHOISLookup","_networkCalcWHOISLookup","_action","plugins.networkCalc.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        #if self.version < 0.2:
        return True
