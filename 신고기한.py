# -*- coding: utf-8 -*-
# 2018-12-24 권달현
import 법인세법,법인세법시행령
법인세={
    "법인세과세표준과 세액의 신고기한":{},
    "일반적인 경우": {
        "법인세법 제60조(과세표준 등의 신고) 제1항":법인세법.제60조,
    },
    "외부감사 미종결로 결산확정이 되지 아니한 경우": {
        "법인세법 제60조(과세표준 등의 신고) 제7,8항": 법인세법.제60조,
        "법인세법시행령 제97조(과세표준의 신고) 제12,13항": 법인세법시행령.제97조,
    },
    "비영리법인의 경우":{
        "법인세법 제62조(비영리내국법인의 과세표준 신고 특례)": 법인세법.제62조,
        "법인세법 제62조의2(비영리내국법인의 자산양도소득에 대한 과세특례)": 법인세법.제62_02조,
    },
}

#___________________________________________________
제목='신고기한'
_={
    "법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
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