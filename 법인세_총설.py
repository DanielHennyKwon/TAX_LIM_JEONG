# -*- coding: utf-8 -*-
# 2018-12-24 권달현
import 결산의확정, 신고납부절차, 기한후신고, 수정신고, 경정청구, 법인의분류, 세금의종류, 실질과세, 소액주주, 대주주, 중소기업, 이월과세, 과세이연, 세무조정, 소득처분, 법인세비용, 세액계산_구조,세무조정_흐름도
_={
    "결산의 확정":결산의확정.결산의확정,
    "법인세의 신고납부절차":신고납부절차.법인세,
    "기한후신고":기한후신고.법인세,
    "수정신고":수정신고._,
    "경정청구":경정청구._,
    "법인세법상 법인의 분류":법인의분류.법인세,
    "법인세의 종류":세금의종류.법인세,
    "실질과세":실질과세.법인세,
    "소액주주":소액주주.법인세,
    "대주주":대주주.법인세,
    "중소기업":중소기업._,
    "이월과세":이월과세.법인세,
    "과세이연":과세이연.법인세,
    "세무조정 흐름도":세무조정_흐름도.법인세,
    "세무조정":세무조정.법인세,
    "소득처분":소득처분.법인세,
    "법인의 각 사업연도소득과 과세표준 및 세액계산의 구조":세액계산_구조.법인세,
    "법인세비용":법인세비용.법인세,
}
#___________________________________________________
제목='법인세 총설'
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