# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
import 법인의현물출자로인한자산양도차익상당액의손금산입 , 교환으로인한자산양도차익상당액의손금산입
import 국고보조금등으로취득한고정자산의손금산입조정
법인세={
    '법인세법상의 준비금':{
        '책임준비금':{},
        '비상위험준비금':{},
    },
    '법인세법상 충당금':{
        '퇴직급여충당금':{},
        '퇴직연금 부담금 등':{},
        '대손충당금':{},
        '구상채권상각충당금':{},
    },
    '국고보조금 등으로 취득한 고정자산의 손금산입 조정':국고보조금등으로취득한고정자산의손금산입조정.법인세,
    '현물출자로 인한 자산양도차익 상당액의 손금산입':법인의현물출자로인한자산양도차익상당액의손금산입.법인세,
    '교환으로 인한 자산양도차익 상당액의 손금산입':교환으로인한자산양도차익상당액의손금산입.법인세,
    '조세특례제한법상의 준비금':{},
}
tax=법인세
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        제목='신고납부'
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