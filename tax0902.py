# -*- coding: utf-8 -*-
#Created on 2021-7-10 @author: 권달현
import 가업승계,가산세
#___________________________________________________
제목='9-2 증여세'
tax={
    "9-2-1 증여세 총설": {
        "9-2-1-1 증여세의 의의":{},
        "9-2-1-2 증여세의 과세체계":{},
        "9-2-1-3 증여세의 과세대상":{},
        "9-2-1-4 증여세의 납부의무자":{},
        "9-2-1-5 증여세의 과세관할":{},
        "9-2-1-6 증여재산의 취득시기":{},
        "9-2-1-7 증여세의 계산구조":{},
    },
    "9-2-2 증여세 과세가액의 계산": {
        "9-2-2-1 증여재산":{},
        "9-2-2-2 증여재산가액 계산의 일반원칙":{},
        "9-2-2-3 부담부증여시 인수채무액":{},
        "9-2-2-4 비과세되는 증여재산":{},
        "9-2-2-5 증여세 과세가액 불산입":{},
    },
    "9-2-3 증여세 과세표준과 세액의 계산": {
        "9-2-3-1 증여세 과세표준의 계산":{},
        "9-2-3-2 증여세 산출세액의 계산":{},
        "9-2-3-3 세액공제":{},
    },
    "9-2-4 증여세의 납세절차": {
        "9-2-4-1 증여세의 신고":{},
        "9-2-4-2 증여세의 납부":{},
        "9-2-4-3 증여세의 결정":{},
        "9-2-4-4 증여세의 갱정":{},
    },
    "9-2-5 변칙적 거래에 따른 이익의 증여": {
        "9-2-5-1 신탁이익의 증여":{},
        "9-2-5-2 보험금의 증여":{},
        "9-2-5-3-1 저가양수에 따른 이익의 증여":{},
        "9-2-5-3-2 고가양도에 따른 이익의 증여":{},
        "9-2-5-4 채무면제 등에 따른 이익의 증여":{},
        "9-2-5-5 부동산무상사용 등에 따른 이익의 증여":{},
        "9-2-5-6 금전무상대출 등에 따른 이익의 증여":{},
        "9-2-5-7 합병에 다른 이익의 증여":{},
        "9-2-5-8 증자에 따른 이익의 증여":{},
        "9-2-5-9 현물출자에 따른 이익의 증여":{},
        "9-2-5-10 감자에 따른 이익의 증여":{},
        "9-2-5-11 전환사채 등의 주식전환 등에 따른 이익의 증여":{},
        "9-2-5-12 초과배당에 따른 이익의 증여":{},
        "9-2-5-13 주식의 상장에 따른 이익의 증여":{},
        "9-2-5-14 합병에 따른 이익의 증여":{},
        "9-2-5-15 그 밖의 이익의 증여":{},
    },
    "9-2-6 증여추정": {
        "9-2-6-1 배우자 등에게 양도한 재산의 증여추정":{},
        "9-2-6-2 재산취득자금 및 채무상환금의 증여추정":{},
    },
    "9-2-7 증여의제": {
        "9-2-7-1 명의신탁재산의 증여의제":{},
        "9-2-7-2 특수관계법인과의 거래를 통한 이익의 증여의제":{},
        "9-2-7-3 특수관계법인으로부터 제공받은 사업기회로 발생한 이익의 증여의제":{},
        "9-2-7-4 특정법인과의 거래를 통한 이익의 증여의제":{},
    },
    "9-2-8 증여 과세특례":가업승계.증여세,
    "9-2-9 가산세": 가산세.tax,
}


import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title=제목)
        self.SetSize(420,320*2)
        self.mainPanel=wx.Panel(self)
        self.expandButton=wx.Button(self.mainPanel,label='펼침')
        self.tree=wx.TreeCtrl(self.mainPanel)
        root=self.tree.AddRoot(제목)
        for i in tax:
            ii=self.tree.AppendItem(root,i)
            for j in tax[i]:
                jj=self.tree.AppendItem(ii,j)
                for k in tax[i][j]:
                    kk=self.tree.AppendItem(jj,k)
                    for m in tax[i][j][k]:
                        mm=self.tree.AppendItem(kk,m)
                        for n in tax[i][j][k][m]:
                            nn=self.tree.AppendItem(mm,n)
                            for p in tax[i][j][k][m][n]:
                                pp=self.tree.AppendItem(nn,p)
                                for q in tax[i][j][k][m][n][p]:
                                    qq=self.tree.AppendItem(pp,q)
                                    for r in tax[i][j][k][m][n][p][q]:
                                        rr=self.tree.AppendItem(qq,r)

        self.staticText =wx.TextCtrl(self.mainPanel,style=wx.TE_MULTILINE)


        self.vtBoxSizer=wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.expandButton,0,wx.EXPAND|wx.ALL,5)
        self.vtBoxSizer.Add(self.tree        ,5,wx.EXPAND|wx.ALL,5)
        self.vtBoxSizer.Add(self.staticText  ,0,wx.EXPAND|wx.ALL,5)


        self.mainPanel.SetSizer(self.vtBoxSizer)

        self.Bind(wx.EVT_BUTTON          ,self.OnExpandButton,self.expandButton)
        self.Bind(wx.EVT_TREE_SEL_CHANGED,self.OnNodeSelected,self.tree)
    def OnExpandButton(self,e):
        self.tree.ExpandAll()
    def OnNodeSelected(self,e):
        selected=self.tree.GetSelection()
        self.staticText.SetLabel(self.tree.GetItemText(selected))

        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________
