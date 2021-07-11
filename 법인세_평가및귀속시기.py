# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:21:21 2018

@author: SAMSUNG 11
"""
from 	취득가액 		import *
from 	금융자산 		import *
from 	금융부채 		import *
from 	재고자산 		import *
from 	유가증권 		import *
from 	외화자산부채	import *
from 	현재가치할인차금 	import *
from 	사채발행비 	import *
from 	신주발행비 	import *
from 	손익의귀속사업연도 import *

법인세_자산부채취득가액과평가및손익귀속시기 ={
       "자산부채의 취득가액과 평가":법인세_취득가액,
       "금융자산":법인세_금융자산,
       "재고자산의 평가":법인세_재고자산,
       "유가증권의 평가":법인세_유가증권,
       "외화자산 및 부채의 평가":법인세_외화자산부채,
       "금융부채":법인세_금융부채,
       "현재가치할인차금":법인세_현재가치할인차금,
       "사채발행비 및 사채할인발행차금":법인세_사채발행비,
       "신주발행비":법인세_신주발행비,
       "손익의 귀속시기":법인세_손익의귀속사업연도,
       }
tax=법인세_자산부채취득가액과평가및손익귀속시기
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
