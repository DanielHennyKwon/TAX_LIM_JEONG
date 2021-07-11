# -*- coding: utf-8 -*-
# 2018-12-24 권달현
import 법인세법,법인세법시행령,법인세법시행규칙
법인세={
        "일반법인의 제출서류":{
                "법인세법 제60조(과세표준 등의 신고) 2,5항  ": 법인세법.제60조,
                "법인세법시행령 제97조(과세표준의 신고) 2,3,4항 ": 법인세법시행령.제97조,
                "법인세법시행규칙 제82조(서식) 3항 ": 법인세법시행규칙.제82조,
        },
        "기능통화로 재무제표를 작성하는 법인의 제출서류":{},
        "합병 분할로 해산하는 법인의 제출서류":{
                "법인세법 제60조(과세표준 등의 신고) 4항  ": 법인세법.제60조,
                "법인세법시행령 제97조(과세표준의 신고) 7항 ": 법인세법시행령.제97조,
                "법인세법시행규칙 제82조(서식) 3항 ": 법인세법시행규칙.제82조,
        },
        "해외직접투자를 한 법인의 제출서류":{},
        "전자신고시 제출할 기타의 제출서류":{
                "법인세법시행령 제97조(과세표준의 신고) 5,11항 ": 법인세법시행령.제97조,
                "법인세법시행규칙 제82조(서식) 3항 ": 법인세법시행규칙.제82조,
        },
        "국제조세조정에 관한 법률상 기타의 제출서류":{},
}
#___________________________________________________
제목='신고서류'
_={
    #"기업회계":기업회계,
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