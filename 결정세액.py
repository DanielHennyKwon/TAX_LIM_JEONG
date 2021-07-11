# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
import 세액계산_구조 ,세율, 토지양도소득 , 세액감면 , 세액감면 , 세액감면 , 세액공제
import 최저한세,추가납부세액,세무조정서식 , 구분경리
연결={    #연결납세제도
    '연결과세표준의 계산':{},
    '연결집단 산출세액의 계산-연결산출세액':{},
    '연결법인별 산출세액의 계산':{},
    '연결집단의 세액공제·감면':{},
    '연결집단의 최저한세의 적용':{},
}
법인세={#a1_제7부법인세계산
    "개요":세액계산_구조.법인세_각사업연도소득,
    "세율":세율.법인세,
    "토지 등 양도소득에 대한 법인세": 토지양도소득.법인세,
    "면제,감면세액": 세액감면.법인세,
    "세액공제": 세액공제.법인세,
    "최저한세":최저한세.법인세,
    "공제감면세액의 적용순위와 중복적용 배제": 세액감면.공제감면세액_순위_중복적용배제,
    "무신고,과소신고 및 수정신고 등의 경우 공제,감면 배제": 세액감면.무신고등_공제감면적용배제,
    "추가납부세액의 계산": 추가납부세액.법인세,
    "공제감면세액의 신청":{},
    "세무조정서식": 세무조정서식.법인세,
    "구분경리": 구분경리.법인세,
    "법인세_연결결정세액":연결,
}
tax=법인세
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