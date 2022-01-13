import pyyaml
class config:
    # configuration class
    raw = open("config.yml")
    config = yaml.load(rawconfig, Loader=yaml.FullLoader)
    log = str(config["log_path"])
    def n_lights():
        for n in config:
            # find how many lights there are defined in the config. 
            # use regex. example = re.match(name, "device_[0-9][0-9][0-9]")
            if re.match(config[n], "device_[0-9][0-9]"):
                nlight += 1
        return nlight

    def get(devn):
        if str(config[str("device_" + str(devn))]):
            return config[str("device_" + str(devn))]
        else:
            return {"error":"nosuchdevice"}
    def getuuid(devn):
        infarr = get(devn)
        return infarr.get("dev_id")
    def getip(devn):
        infarr = get(devn)
        return infarr.get("ip")
    def getpos(devn):
        infarr = get(devn)
        return infarr.get("screen_rel")
    def getlk(devn):
        infarr = get(devn)
        return infarr.get("loc_key")

    debug = bool(config["debug"])