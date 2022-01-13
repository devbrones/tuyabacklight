import pyyaml
import tinytuya
import logging
import re

class config:
    # configuration class
    raw = open("config.yml")
    config = yaml.load(rawconfig, Loader=yaml.FullLoader)
    log = str(config["log_path"])
    def n_lights():
        for n_l in config:
            # find how many lights there are defined in the config. 
            # use regex. example = re.match(name, "device_[0-9][0-9][0-9]")
            n_l += 1
        return n_l

    def get(devn):
        if str(config[str("device_" + str(devn))]):
            return config[str("device_" + str(devn))]
        else:
            return {"error":"nosuchdevice"}
    def getuuid(devn):
        infarr = get(devn)
        return infarr.get("dev_id")
    def getip(devn):

    def getpos(devn):
        

# logging
log = logging.basicConfig(filename=config.log, level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
log.info("-±- New Session -±-")

