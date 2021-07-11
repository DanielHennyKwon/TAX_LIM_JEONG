# -*- coding: utf-8 -*-
#Created on 2021-7-10 @author: 권달현
import tax0801,tax0802,tax0803,tax0804,tax0805,tax0806,tax0807,tax0808,tax0809,tax0810,tax0811
#___________________________________________________
제목=' 8. 소득세법'
tax={
    "8-1 소득세법 총설": tax0801.tax,
    "8-2 이자소득과 배당소득": tax0802.tax,
    "8-3 사업소득": tax0803.tax,
    "8-4 근로소득,연금소득 및 기타소득": tax0804.tax,
    "8-5 소득금액계산의 특례":tax0805.tax,
    "8-6 종합소득과세표준의 계산": tax0806.tax,
    "8-7 종합소득세액의 계산": tax0807.tax,
    "8-8 퇴직소득세": tax0808.tax,
    "8-9 종합,퇴직소득세의 납세절차": tax0809.tax,
    "8-10 양도소득세": tax0810.tax,
    "8-11 비거주자와 외국법인의 납세의무": tax0811.tax,
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
