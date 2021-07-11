# -*- coding: utf-8 -*-
#Created on 2021-7-10 @author: 권달현
import tax0301
import tax0302
import tax0303
import tax0304
import tax0305
import tax0306
import tax0307
import tax0308
import tax0309
import tax0310
import tax0311
import tax0312

#___________________________________________________
#___________________________________________________
제목='3. 법인세법'
tax={
    "3-1 총설": tax0301.tax,
    "3-2 법인세의 계산구조": tax0302.tax,
    "3-3 익금": tax0303.tax,
    "3-4 손금": tax0304.tax,
    "3-5 손익의 귀속사업연도와 자산,부채의 평가": tax0305.tax,
    "3-6 자산의 감가상각": tax0306.tax,
    "3-7 충당금과 준비금": tax0307.tax,
    "3-8 합병 및 분할 등에 대한 특례": tax0308.tax,
    "3-9 부당행위계산의 부인": tax0309.tax,
    "3-10 과세표준과 세액의 계산": tax0310.tax,
    "3-11 법인세의 납세절차": tax0311.tax,
    "3-12 그 밖의 법인세": tax0312.tax,
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
        #self.
        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________

