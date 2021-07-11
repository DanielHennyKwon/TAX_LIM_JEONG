# -*- coding: utf-8 -*-
# Modified on 2021-7-11 @author: 권달현
# 2-6-3
국세기본법={
    '무신고': {},
    '과소신고': {},
    '납부불성실가산세': {},
    "가산세의 감면": {
        "가산세의 10%~50$감면": {},
        "가산세의 100% 감면": {
            "기한연장사유에 해당되는 경우": {},
            "정당한 사유가 있는 때": {},
        },
        "단순협력의무 위반에 대한 가산세 한도제": {},
    },
}
법인세={
    '무기장':{},
    '주주등의 명세서 제출불성실':{},
    '지출증명 미수취가산세':{},
    "장부의 비치,기장 및 증명서류의 수취,보관과 관련한 가산세":{},
    "법인세 연결 가산세": {},
}
부가가치세세={
    "...":{}
}
상속세={
    "...":{}
}
소득세={
    "...":{}
}
증여세={
    "...":{}
}
조세특례제한법={
    "세금우대자료 미제출가산세":{}
}
지방소득세_법인세분={
	'...':{},
}
#___________________________________________________
제목='가산세'
_={
    "국세기본법":국세기본법,
    "지방소득세_법인세분 가산세": 지방소득세_법인세분,
    "법인세":법인세,
    "부가가치세세":부가가치세세,
    "증여세":증여세,
    "상속세":상속세,
    "소득세":소득세,
    "조세특례제한법":조세특례제한법,
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
        #self.
        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________