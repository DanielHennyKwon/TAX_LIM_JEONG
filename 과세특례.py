# -*- coding: utf-8 -*-
#Created on 2018-12-24 @author: 권달현
import 창업  , 가업승계,동업기업과세특례,국외전출
증여세={
    '창업자금에대한 증여세과세특례(조특법30조의5)':창업.창업자금에대한증여세과세특례,
    '가업승계에대한 증여세과세특례(조특법30조의6)':가업승계.증여세,
}
조세특례제한법={#_기업구조조정_과세특례
    '사업전환 무역조정지원기업에 대한 과세특례(조특법33조)': {},
    '내국법인의 금융채무 상환을 위한 자산매각에 대한 과세특례(조특법34조)': {},
    '주식의 포괄적 교환·이전에 대한 과세 특례(조특법38조)': {},
    '주식의 현물출자 등에의한 지주회사의 설립 등에 대한 과세특례(조특법38조의2)': {},
    '내국법인의 외국자회사 주식 등의 현물출자에 대한 과세특례(조특법38조의3)': {},
    '주주등의 자산양도에 관한 법인세 등 과세특례(조특법40조)': {},
    '기업 간 주식등의 교환에 대한 과세특례(조특법46조)': {},
    '벤처기업의 전략적 제휴를 위한 주식교환 등에 대한 과세특례(조특법46조의2)': {},
    '물류기업의 전략적 제휴를 위한 주식교환 등에 대한 과세특례(조특법46조의3)': {},
    '전략적 제휴를 위한 비상장 주식교환등에 대한 과세특례(조특법46조의7)': {},
    '주식매각 후 벤처기업등 재투자에 대한 과세특례(조특법46조의8)': {},
}
양도소득세={
    "거주자의 출국시(국외전출세) 국내주식 등에 대한 과세특례" :국외전출.양도소득세,
}

법인토지등양도소득={#to:토지양도소득
        '개요':{
            "토지등 양도소득에 대한 법인세 과세제도는 ":{},
        },
        '법인세 계산 구조':{},
        '적용세율':{},
        '과세대상':{
            '주택':(),
            '비사업용 토지':(),
            },
        '비과세 대상':{},
}
비영리내국법인자산양도={#비영리법인에대한과세특례
    "개요":{},
    "자산양도소득":{},
    "신고납부":{},
}
법인세={
    "법인토지등양도소득에대한과세특례":법인토지등양도소득,
    "비영리내국법인자산양도특례":비영리내국법인자산양도,
    "동업기업과세특례":동업기업과세특례.법인세,
    "투자,상생협력 촉진을 위한 과세특례":{},
}
#__________________________________________________________________
제목='과세특례'
_={
    "법인세":법인세,
    "조세특례제한법":조세특례제한법,
    "증여세":증여세,
    "양도소득세":양도소득세,
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
#__________________________________________________________________