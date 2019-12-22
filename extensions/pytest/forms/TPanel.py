import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReference('System')

from System.Windows.Forms import *
from System.Drawing import *

class TPanel(UserControl):
    def __init__(self, text='hello world', width=500, height=400):
        self.btnSave = Button()
        self.btnExit = Button()
        self.btnOpen = Button()
        self.txtBox = TextBox()
        self.Text = text
        self.Size = Size(width, height)
        self.StartPosition = FormStartPosition.CenterScreen
        self.__initControls();      

    def __initControls(self):
        self.btnSave.Text = "&Save"
        self.btnSave.Location = Point(10, 10);     

        self.btnExit.Text = "E&xit"
        self.btnExit.Location = Point(self.btnSave.Left+self.btnSave.Width+10, self.btnSave.Top)
        self.btnExit.Click += self.__btnExit_Click

        self.btnOpen.Text = "&Open"
        self.btnOpen.Location = Point(self.btnExit.Left+self.btnExit.Width+10, self.btnSave.Top)
        self.btnOpen.Click += self.__btnOpen_Click

        self.txtBox.Location = Point(self.btnSave.Left, self.btnExit.Height + self.btnExit.Top+10)
        self.txtBox.Width = 470
        self.txtBox.Height = 320
        self.txtBox.Multiline = True
        self.txtBox.ScrollBars = ScrollBars.Vertical
        self.txtBox.WordWrap = True

        self.Controls.Add(self.btnSave)
        self.Controls.Add(self.btnExit)
        self.Controls.Add(self.btnOpen)
        self.Controls.Add(self.txtBox)  

    def __btnExit_Click(self, sender, e):
        self.Close()

    def __btnOpen_Click(self, sender, e):
        openFileDialog1 = OpenFileDialog()
        openFileDialog1.InitialDirectory = "c:\\"
        openFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*"
        openFileDialog1.FilterIndex = 1
        openFileDialog1.RestoreDirectory = True
        if openFileDialog1.ShowDialog() == DialogResult.OK:
            self.txtBox.Text = ''
            with open(openFileDialog1.FileName) as f:
                for i in f.readlines():
                    self.txtBox.Text += i