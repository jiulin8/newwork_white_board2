from tkinter import *


class UserDialog:
    _Ip = ''
    _port = 0
    @classmethod
    def getUserInputIp(cls):
        def getUserIpAndPort():
            cls._Ip = e1

        ClientWindow = Tk()
        Label(ClientWindow,text='请输入IP').grid(row=0)
        Label(ClientWindow,text='IP').grid(row=1)
        Label(ClientWindow,text='Port').grid(row=2)

        e1 = Entry(ClientWindow)
        e2 = Entry(ClientWindow)

        e1.grid(row=1,column=1)
        e1.grid(row=2, column=1)

        button = Button(ClientWindow)
        button.config(text='ok',command = getUserIpAndPort)
        button.grid(row = 3, column= 0)

        ClientWindow.mainloop()

if __name__ == '__main__':
    UserDialog.getUserInputIp()
