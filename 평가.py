# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
import 시가, 주식 , 토지, 건물
기업회계={
    "K-IFRS1016호 문단29,31":{},
    "일반회계기준 10장 문단 10.22, 10.24":{},
    "법인세법상으로는 해당 재평가를 임의평가로 보는 것이므로 당해 유형자산의 세무상 장부가액은 그 평가하기 전의 가액으로 하여야 한다 : 법인-782,2009.2.25.:법인435,2009.4.10":{},
}
법인세={
    "...":{}
}
증여세={
    '재산의 평가원칙':{
        '재산평가의 이해':{},
        '증여재산의 평가방법':{}
    },
    '재산의 시가평가':시가.증여세,
    '부동산 및 기타재산의 보충적 평가방법':{
        '재산종류별 기준시가':{},
        '토지의 평가':토지.증여세_평가,
        '건물의 평가':건물.증여세_평가,
        '기타 재산 등의 평가':{},
        '채권 등의 평가':{},
        '기타 권리 등의 평가':{}
    },
    '주식의 평가방법':주식.증여세_평가,
    '저당권 등이 설정된 재산의 평가특례':{}
}
#___________________________________________________
제목='평가'
_={
    "기업회계":기업회계,
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    "증여세":증여세,
    #"상속세":상속세,
    #"양도소득세":양도소득세,
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