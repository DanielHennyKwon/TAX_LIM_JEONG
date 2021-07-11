# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
import 명의신탁,특수관계
의제={
    '명의신탁재산의 증여의제':명의신탁.재산의증여의제,
    '특수관계법인과의 거래를 통한 증여의제':특수관계.법인과의거래를통한증여의제,
    '특수관계법인으로부터 제공받은 사업기회로 발생한 이익의 증여의제':특수관계.법인제공사업기회이익의증여의제,
    '특정법인과의 거래를 통한 이익의 증여의제':특수관계.특정법인거래이익의증여의제,
}
부담부={
    "부담부 증여시의 양도의제": {},
    "부담부 증여시 채무액이 증여가액을 초과하는 경우": {},
    "": {},
}
예시={
    '신탁이익의 증여':{},
    '보험금의 증여':{},
    '저가양수 또는 고가양도에 따른 이익의 증여':{},
    '채무변제 등에 따른 이익의 증여':{},
    '부동산 무상사용에따른 이익의 증여':{},
    '합병에 따른 이익의 증여':{},
    '증자에 따른 이익의 증여':{},
    '감자에 따른 이익의 증여':{},
    '현물출자에 따른 이익의 증여':{},
    '전환사채 등의 주식전환 등에 따른 이익의 증여':{},
    '초과배당에 따른 이익의 증여':{},
    '주식 등 상장 등에 따른 이익의 증여':{},
    '합병에 따른 상장 등 이익의 증여':{},
    '금전무상대출 등에 따른 이익의 증여':{},
    '그 밖의 이익의 증여':{},
    '증여세 특례와 공통 적용사항':{}
}
추정={
    '증여추정의 의의':{},
    '배우자 등에 양도한 재산의 증여추정':{},
    '재산취득자금 등의 증여추정':{
        "재산취득자금 등의 증여추정 배제기준": {},
        "": {},
    },
    "증여추정 등 사례":{},
}
#___________________________________________________
제목='증여'
_={
    '유형별 증여예시':예시,
    '증여추정':추정,
    "증여의제":의제,
    "부담부증여" :부담부,
}
tax=_
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