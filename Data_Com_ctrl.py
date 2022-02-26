import time
import numpy as np
import ast


class DataMaster():
    def __init__(self):
        self.sync = "#?#\n"
        self.sync_ok = "!"
        self.StartStream = "#A#\n"
        self.StopStream = "#S#\n"
        self.SynchChannel = 0

        self.msg = []
        self.IntMsg = []

        self.XData = []
        self.YData = []

        self.XDisplay = []
        self.YDisplay = []

        self.FunctionMaster = [
            "RowData",
            "VoltageDisplay"
        ]

        self.DisplayTimeRange = 5

    def DecodeMsg(self, input_msg):
        print("DecodeMsg")
        # temp = self.RowMsg.decode('utf8')
        # temp = input_msg.decode('utf8')
        temp = input_msg.decode('utf8').replace(',', '.').replace(' ', '')[:-1]
        if len(temp) > 0:
            # if "#" in temp:
            self.msg = temp.split(";")
                # del self.msg[0]
                # if self.msg[0] in "D":
                #     self.messageLen = 0
                #     self.messageLenCheck = 0
                #     del self.msg[0]
                #     del self.msg[len(self.msg)-1]
                #     self.messageLen = int(self.msg[len(self.msg)-1])
                #     del self.msg[len(self.msg)-1]
                #     for item in self.msg:
                #         self.messageLenCheck += len(item)

    # def GenChannels(self):
    #     self.Channels = [f"Ch{ch}" for ch in range(self.SynchChannel)]

    # def buildYdata(self):
    #     self.YData = []
    #     for _ in range(self.SynchChannel):
    #         self.YData.append([])

    def ClearData(self):
        self.XData = []
        self.YData = []
        self.XDisplay = []
        self.YDisplay = []
        self.IntMsg = []
        self.msg = []

    def IntMsgFunc(self):
        print("IntMsgFunc")
        # self.IntMsg = [float(x) for x in self.msg]
        for element in self.msg:
            self.IntMsg.append(float(element))

    def AdjustDataCheck(self):
        print("AdjustDataCheck")
    #     self.StreamData = False
    #     if self.SynchChannel == len(self.msg):
    #         if self.messageLen == self.messageLenCheck:
    #             self.StreamData = True
        self.IntMsgFunc()
    #
    # def SetRefTime(self):
    #     if len(self.XData) == 0:
    #         self.RefTime = time.perf_counter()
    #     else:
    #         self.RefTime = time.perf_counter() - self.XData[len(self.XData)-1]

    def UpdataXdata(self):
        print("UpdataXdata")
        for i in range(200):
            self.XData.append(i)
        # if len(self.XData) == 0:
        #     self.XData.append(0)
        # else:
        #     self.XData.append(time.perf_counter()-self.RefTime)

    def UpdataYdata(self):
        print("UpdataYdata")
        # IntMsgY = self.IntMsg[0].split(";")
        # for i in range(self.IntMsg):
        #     self.YData[0].append(i)
        # for ChNumber in range(self.SynchChannel):
        #     self.YData[ChNumber].append(self.IntMsg[ChNumber])
        for element in self.msg:
            self.YData.append(float(element))

    def AdjustData(self):
        print("AdjustData")
        # lenXdata = len(self.XData)
        # if (self.XData[lenXdata-1] - self.XData[0]) > self.DisplayTimeRange:
        #     del self.XData[0]
        #     for ydata in self.YData:
        #         del ydata[0]
        #
        # x = np.array(self.XData)
        # self.XDisplay = np.linspace(x.min(), x.max(), len(x), endpoint=0)
        for element in self.msg:
            self.YDisplay.append(float(element))
        # self.YDisplay = np.array(self.YData)
        self.XDisplay = list(range(1, len(self.YDisplay)+1))

