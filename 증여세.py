# -*- coding: utf-8 -*-
#Created on 2018-11-5 @author: 권달현
import 과세원인, 과세대상 , 납세의무,손익의귀속사업연도, 계산흐름도, 과세가액,과세표준,산출세액
import  세액공제 , 징수유예세액 , 세액감면 , 과세특례, 증여,평가 , 신고납부절차
_={
    '증여세 일반사항':{
        '증여세 과세원인':과세원인.증여세,
        '증여세 과세대상':과세대상.증여세,
        '증여세 납세의무':납세의무._,
        '증여재산의 취득시기':손익의귀속사업연도.증여세,
    },
    '증여세 과세표준 및 세액계산':{
        '증여세 계산흐름':계산흐름도.증여세,
        '증여세 과세가액':과세가액.증여세,
        '증여세 과세표준':과세표준.증여세,
        '세액계산과 공제감면세액':{
            '증여세 산출세액':산출세액.증여세,
            '세액공제':세액공제.증여세,
            '징수유예세액':징수유예세액.증여세,
            '세액감면':세액감면.증여세,
        },
        '증여세 과세특례':과세특례.증여세,
    },
    '증여예시,증여추정 및 증여의제':증여._,
    '증여재산의 평가':평가.증여세,
    '증여세 신고납부':신고납부절차.증여세,
}
#___________________________________________________
제목='증여세'
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