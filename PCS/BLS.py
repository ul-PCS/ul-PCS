from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, pair
from charm.core.engine.util import objectToBytes
from charm.toolbox.IBSig import *


debug = False


class BLS01(IBSig):
    def __init__(self, groupObj):
        IBSig.__init__(self)
        global group
        group = groupObj
        
    def dump(self, obj):
        return objectToBytes(obj, group)
            
    def keygen(self, pp):
        x = group.random()
        return (x, pp['G1'] ** x)
        
    def sign(self,pp, x, message):
        #M = self.dump(message)
        return group.hash(objectToBytes(message, group), G2) ** x
        
    def verify(self, pp, vk, sig, message):
        #M = self.dump(message)
        h = group.hash(objectToBytes(message, group), G2)
        return pair(pp['G1'], sig) == pair(vk, h)