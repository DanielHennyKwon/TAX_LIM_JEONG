# -*- coding: utf-8 -*-
#Created on 2021-7-10 @author: 권달현
import 퇴직급여,퇴직급여충당금,퇴직연금부담금
import 대손금,대손충당금
import 일시상각충당금,압축기장충당금,준비금
#___________________________________________________
제목='3-7 충당금과 준비금'
tax={
    "3-7-1 퇴직부담금": {
        "퇴직급여":퇴직급여.법인세,
        "퇴직급여충당금":퇴직급여충당금.법인세,
        "퇴직연금부담금":퇴직연금부담금.법인세
    },
    "3-7-2 대손금과 대손충당금": {
        "대손금":대손금.법인세,
        "대손충당금":대손충당금.법인세
    },
    "3-7-3 일시상각충당금과 업축기장충당금": {
        "일시상각충당금":일시상각충당금.법인세,
        "압축기장충당금":압축기장충당금.법인세,
    },
    "3-7-4 준비금": {
        "법인세법":준비금.법인세,
        "조세특례제한법":준비금.조세특례제한법,
    },
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
