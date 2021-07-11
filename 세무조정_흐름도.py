# -*- coding: utf-8 -*-
# 2018-12-24 권달현
import 세무조정 , 결산조정, 신고조정, 익금산입, 익금불산입, 손금산입, 손금불산입, 기부금, 이월결손금, 비과세, 소득공제, 과세표준, 세율,세액공제, 세액감면, 최저한세, 가산세, 기납부세액
법인세={
        '결산서상 당기순손익':{},
        '결산조정':결산조정.법인세,
        '신고조정':신고조정.법인세,
        '익금산입':익금산입.법인세,
        '익금불산입':익금불산입.법인세,
        '손금산입':손금산입.법인세,
        '손금불산입':손금불산입.법인세,
        '차가감 소득금액':{},
        '기부금 한도초과 및이월액 손금산입':기부금.법인세,
        '각 사업연도 소득금액':{},
        '이월결손금':이월결손금.법인세,
        '비과세소득':비과세.법인세,
        '소득공제':소득공제.법인세,
        '과세표준':과세표준.법인세,
        '세율':세율.법인세,
        '산출세액':{},
        '공제감면세액':{
                '세액공제':세액공제.법인세,
                '세액감면':세액감면.법인세,
                },
        '최저한세':최저한세.법인세,
        '가산세':가산세.법인세,
        '가감계':{},
        '기납부세액':기납부세액.법인세,
        '감면분 추가납부세액':{},
        '차감납부할세액':{},
}
법인세2={
    "세무조정흐름도1":법인세,
    '결산서상 당기순손익':{},
    '차가감 소득금액':{},
    '기부금 한도초과 및이월액 손금산입':기부금.법인세,
    '각 사업연도 소득금액':{},
    '이월결손금':이월결손금.법인세,
    '비과세소득':비과세.법인세,
    '소득공제':소득공제.법인세,
    '과세표준':과세표준.법인세,
    '세율':세율.법인세,
    '산출세액':{},
    '공제감면세액':{
        '세액공제':세액공제.법인세,
        '세액감면':세액감면.법인세,
        },
    '최저한세':최저한세.법인세,
    '가산세':가산세.법인세,
    '가감계':{},
    '기납부세액':기납부세액.법인세,
    '감면분 추가납부세액':{},
    '차감납부할세액':{},
}
tax=법인세2
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