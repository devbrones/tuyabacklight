import yaml
import re
class config:
    # configuration class
    raw = open("config.yml")
    global mconfig
    global nlight
    mconfig = yaml.load(raw, Loader=yaml.FullLoader)
    log = str(mconfig["log_path"])
    print(type(mconfig))
    def n_lights(self):
        nlight = str(mconfig).count("device_")
        print(nlight)
        return nlight

    def __init__(self):
        devn = self

    def get(self, devn):
        if str(mconfig[str("device_" + str(devn))]):
            return mconfig[str("device_" + str(devn))]
        else:
            return {"error":"nosuchdevice"}
    def getuuid(self, devn):
        infarr = self.get(devn)
        return infarr.get("dev_id")
    def getip(self, devn):
        infarr = self.get(devn)
        return infarr.get("ip")
    def getpos(self, devn):
        infarr = self.get(devn)
        return infarr.get("screen_rel")
    def getlk(self, devn):
        infarr = self.get(devn)
        return infarr.get("loc_key")

    debug = bool(mconfig["debug"])