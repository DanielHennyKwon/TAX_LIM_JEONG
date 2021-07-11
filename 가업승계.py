일반= {
    '가업승계 세무가이드':{},
    '가업승계 법률 검토': {
        '지배권 확보 및 타상속인 배려': {
            '지배권 확보': {},
            '타상속인에대한 배려': {}
        },
        '재산의 승계': {
            '생전승계': {},
            '사후승계': {},
            '상속의 승인 및 포기': {},
            '상속재산의 분할': {},
            '유증과 사인증여': {},
            '이혼에 따른 재산분할청구권': {}
        },
        '상법등의 활용': {
            '자기주식 취득': {},
            '정관에의한 주식양도의 제한': {},
            '의결권 제한 주식의 발행': {},
            '복수의결권 제도': {}
        },
        '상속관련신탁': {
            '명의신탁': {},
            '신탁법상 신탁': {}
        },
        '성년후견제도': {},
        '체크리스트': {}
    },
    '가업승계 과세일반': {
        '가업승계와 세금': {
            '세금의 중요성': {},
            '가업승계관련 세무전략': {},
            '상속세와 증여세의 비교': {}
        },
        '체크리스트': {}
    },
    '세금납부대책': {
        '연부연납제도': {
            '연부연납의 요건': {},
            '연부연납의 신청과 허가': {},
            '연부연납의 기간 및 금액의 결정': {},
            '납세담보의 제공': {},
            '연부연납의 취소 또는 변경': {},
            '연부연납 가산금': {}
        },
        '물납제도': {
            '물납의 요건': {},
            '물납의 한도': {},
            '물납 재산의 범위 및 충당순서': {},
            '물납재산 수납가액의 평가': {},
            '물납재산의 환급': {}
        },
        '분납 제도': {
            '분납 요건': {},
            '분납세액': {},
            '분납 배제': {}
        },
        '기타': {
            '자산의 매각': {},
            '자금의 차입': {},
            '퇴직금의 활용': {},
            '보험의 활용': {}
        },
        '체크리스트': {}
    },
}
증여세={
    '제목: 가업승계 주식에대한 증여세 과세특례': {},
    '가업승계 일반':일반,
    '과세특례의 의의': {},
    '과세특례의 요건': {},
    '과세특례의 내용 및 계산': {},
    '사후관리': {},
    '과세특례 적용시 고려사항': {},
    '체크리스트': {}
}
상속세={
    '제목: 가업상속공제': { },
    '가업승계 일반':일반,
    '가업상속공제의 의의': {},
    '가업상속공제의 요건': {},
    '가업상속공제 적용 효과': {},
    '사후관리': {},
    '가업상속공제의 신청': {},
    '양도소득세 이월과세': {},
    '체크리스트': {}
}
#___________________________________________________
제목='가업승계'
_={
    #"법인세":법인세,
    #"조세특례제한법":조세특례제한법,
    "증여세":증여세,
    "상속세":상속세,
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
        #self.
        self.mainPanel.Layout()
if __name__=='__main__':
    app=wx.App()
    frame=MyFrame()
    frame.Show()
    app.MainLoop()
#___________________________________________________