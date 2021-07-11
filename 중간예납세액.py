# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
import 납부기한, 분납
연결={
    "연결중간예납":{
        "직전 사업연도 납부실적에 의한 계산":{},
        "중간예납기간의 실적에 의한 계산":{},
        "분납 등":{},
    },
    "개별납세 전환법인의 중간예납세액":{},
}
법인세={ # to:a1_제7부법인세계산
    "중간예납 대상법인":{},
    "중간예납기간":{
        "원칙":{},
        "사업연도를 변경한 경우":{},
        "신설합병의 경우":{},
    },
    "중간예납세액의 계산":{
        "직전 사업연도 납부실적에 의한 계산":{},
        "중간예납기간의 실적에 의한 계산":{},
    },
    "중간예납세액의 납부 및 징수":{
        "납부기한":납부기한.법인세,
        "분납":분납.법인세,
        "미납세액의 징수":{},
    },
    "제출서류":{},
    "법인세_연결중간예납":연결,
}
tax=법인세
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        제목='법인조정과세무조정실무'
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