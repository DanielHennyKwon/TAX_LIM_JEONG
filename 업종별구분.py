# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
import 예정신고납부
부동산매매업_소득구분={
    '부동산매매업(사업소득)':{},
    '부동산매매업 등의 구분': {},
    '부동산매매업으로 보는 경우': {},
    '부동산매매업으로 보지 아니한 경우': {},
    '오피스텔': {},
}
부동산매매업={
    '양도소득세_부동산매매업_토지매매차익예정신고납부':예정신고납부.양도소득세,
    '부동산매매업_소득구분':부동산매매업_소득구분,
}

주택신축판매업_소득구분={
    '주택신축판매업(건설업=사업소득)':{},
    '사업소득으로 보는 경우': {},
    '부가가치세 납세의무': {},
    '개인과 법인이 공동으로 사업을 영위하는 경우': {},
    '미분양주택의 소득구분': {},
}
주택신축판매업={
    '주택신축판매업_소득구분':주택신축판매업_소득구분,
}

주택신축판매업_부동산매매업={
    '소득의 구분 등': {
        '완공후 양도한 경우': {},
        '완공전 양도한 경우': {},
        '부동산임대업': {},
    },
    '양도소득': {
        '양도소득의 개념': {},
        '양도소득으로 보는 경우': {},
        '사업의 계속성이 없는 경우': {},
    },
    '부동산매매업': 부동산매매업_소득구분,
    '주택신축판매업': 주택신축판매업_소득구분,
}
양도소득세={
    "주택신축판매업_부동산매매업":주택신축판매업_부동산매매업,
}
#___________________________________________________
제목='업종별 구분'
_={
    '부동산매매업': 부동산매매업,
    '주택신축판매업': 주택신축판매업,

    #"기업회계":기업회계,
    #"법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
    "양도소득세":양도소득세,
    #"농어촌특별세":{},
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