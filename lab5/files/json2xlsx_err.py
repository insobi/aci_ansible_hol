import json
import pandas as pd

class json2xlsx_phys_err(object):

    def __init__(self):
        self.JSON_PATH = "./"
        self.XLSX_PATH = "./"
    
    def main(self):
        with open(self.JSON_PATH + "l1PhysIf.json") as json_file:
            l1PhysIf = json.load(json_file)

        with open(self.JSON_PATH + "rmonDot3Stats.json") as json_file:
            rmonDot3Stats = json.load(json_file)

        with open(self.JSON_PATH + "rmonDot1d.json") as json_file:
            rmonDot1d = json.load(json_file)

        with open(self.JSON_PATH + "rmonEtherStats.json") as json_file:
            rmonEtherStats = json.load(json_file)
        
        data_new = []

        for dn in l1PhysIf:
            temp = {"dn" : dn}

            for item_rmonDot3Stats in rmonDot3Stats:
                key = '/'.join(item_rmonDot3Stats['dn'].split('/')[:-1])
                if key == dn:
                    temp["Allignment Errors"           ] = item_rmonDot3Stats['alignmentErrors']
                    temp["Carrier Sense Errors"        ] = item_rmonDot3Stats['carrierSenseErrors']
                    temp["Deferred Transmisstions"     ] = item_rmonDot3Stats['deferredTransmissions']
                    temp["Internal Mac Receive Errors" ] = item_rmonDot3Stats['internalMacReceiveErrors']
                    temp["Internal Mac Transmit Errors"] = item_rmonDot3Stats['internalMacTransmitErrors']
                    temp["Late Collisions"             ] = item_rmonDot3Stats['lateCollisions']
                    temp["Multiple Collision Frames"   ] = item_rmonDot3Stats['multipleCollisionFrames']
                    temp["SQETTest Errors"             ] = item_rmonDot3Stats['sQETTestErrors']
                    temp["Single Collision Frames"     ] = item_rmonDot3Stats['singleCollisionFrames']
                    temp["Symbol Errors"               ] = item_rmonDot3Stats['symbolErrors']

            for item_rmonDot1d in rmonDot1d:
                key = '/'.join(item_rmonDot1d['dn'].split('/')[:-1])
                if key == dn:
                    temp["Port in Discards"           ] = item_rmonDot1d['portInDiscards']
                    break
    
            for item_rmonEtherStats in rmonEtherStats:
                key = '/'.join(item_rmonEtherStats['dn'].split('/')[:-1])
                if key == dn:
                    temp["CRC Align Errors"  ] = item_rmonEtherStats['cRCAlignErrors']
                    temp["Collisions"        ] = item_rmonEtherStats['collisions']

            data_new.append(temp)

        df = pd.DataFrame(data_new)
        df.to_excel(self.XLSX_PATH + "인터페이스_에러.xlsx")

if __name__ == "__main__":
    func = json2xlsx_phys_err()
    func.main()