# -*- coding: utf-8 -*-
#Created on 2018-11- @author: 권달현
import 과점주주
증여세_평가={#증여세'로
    '세법상 주식평가방법 개요':{},
    '유가증권시장 상장법인 주식의 평가':{},
    '코스닥 상장법인 주식의 평가':{},
    '상장 추진중인 주식의 평가':{},
    '비상장주식의 평가':{},
    '상속세및증여세법상 비상장주식평가점검표':{
        '일반사항':{},
        '순손익가치 평가':{},
        '순자산가치 평가':{},
        '개별자산의 평가':{},
        '최대주주 할증평가':{},
    },
}
양도소득세_과세대상={#과세대상'으로
    '과세대상 상장주식 및 비상장주식':{},
    '대주주의 범위':{},
    '시가총액의 계산':{},
    '주식양도차익 과세대상 대주주 판정기준':{},
    '상장주식 사례':{},
    '비상장주식 사례':{},
}
양도소득세_과세대상_기타자산={#기타자산'으로
    '특정주식(과점주주)등':{
        '과점주주':과점주주.양도소득세_주식,
    },
    '부동산과다보유법인의 주식 등':{},
}
양도소득세_비과세={
    '중소기업창업투자회사 등에 출자한 주식 등의 비과세':{},
    '퇴직자가 우리사주를 우리사주조합에 양도시 과세특례':{}
}
양도소득세_감면={
    '임대주택 부동산투자회사의 현물출자자에대한 과세특례(조특법97조의6)': {},
}
양도소득세={
    '양도소득세_과세대상_주식': 양도소득세_과세대상,
    '양도소득세_과세대상_기타자산_주식': 양도소득세_과세대상_기타자산,
    '주식_양도소득세_비과세': 양도소득세_비과세,
    '주식_양도소득세_감면': 양도소득세_감면,
}
#___________________________________________________
제목='주식'
_={
    '증여세_주식_평가':증여세_평가,
    #"기업회계":기업회계,
    #"법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    #"증여세":증여세,
    #"상속세":상속세,
    "양도소득세":양도소득세,
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