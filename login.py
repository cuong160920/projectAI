from tkinter import *
import readUser1
import rule 
import submit_after1
import readUser2

choices = []

def readInput(a , b):
    with open("D:\\COURSES\\Project AI\\Node.txt", 'r', encoding='utf-8') as f:
        f_contents = f.readlines()
    a = {}

    for line in f_contents:
        tmp = ''
        tmp1 = ''
        i = 0
        for s in line:
            if(s != ' '):
                tmp =  tmp + s
                i = i+1
                continue
            tmp1 = line[(i+1):]
            break
        a[tmp] = tmp1

    return a

def retrieveValue(s, a, thuoctinh):
    index = 1;
    v = {}
    # while((s+str(index)) in a.keys()):
    #     v[s + str(index)] = a[s + str(index)]
    #     index = index + 1

    for tmps in thuoctinh:
        if(s == tmps[: len(tmps)-1]):
            v[tmps] = a[tmps]
    return v

def openSecondWindow():
    newWindow = Toplevel(root)

    newWindow.title("Detail Choices")

    a = readInput(0, 0) # NOTICE ME

    cc1 = 'n' + n.get()
    cc2 = 'p' + p.get()
    gt = [cc1, cc2]
    kl = readUser1.conclude(gt)
    re = rule.list_result(kl)
    thuoctinh = submit_after1.filter(re)

    m = retrieveValue('m', a, thuoctinh)
    mo = retrieveValue('mo', a, thuoctinh)
    ra = retrieveValue('ra', a, thuoctinh)
    ca = retrieveValue('ca', a, thuoctinh)
    ch = retrieveValue('ch', a, thuoctinh)
    h = retrieveValue('h', a, thuoctinh)
    w = retrieveValue('w', a, thuoctinh)
    b = retrieveValue('b', a, thuoctinh)
    c = retrieveValue('c', a, thuoctinh)
    # thiếu color(c)

    heading = Label(newWindow, text="The Criterias", bg="light green")
    heading.grid(row = 0, column = 0, ipady = 0, pady = 0, padx = 0)
    currentColumn = 0

    if(len(m) != 0):
        pm = Label(newWindow, text = "Hãng")
        pm.grid(row = 1, column = currentColumn, ipady = 5, pady = 5, padx = 40)
        i = 2
        for (t1, v1) in m.items():
            Radiobutton(newWindow, text = v1, variable = mvar,
                    value = t1).grid(row = i, column = currentColumn)
            i = i+1
        currentColumn = currentColumn + 1

    if(len(mo) != 0):
        pmo = Label(newWindow, text = "Màn Hình")
        pmo.grid(row = 1, column = currentColumn, ipady = 5, pady = 5, padx = 40)
        i = 2
        for (t2, v2) in mo.items():
            Radiobutton(newWindow, text = v2, variable = movar,
                        value = t2).grid(row = i, column = currentColumn)
            i = i+1
        currentColumn = currentColumn + 1

    if(len(ra) != 0):
        pra = Label(newWindow, text = "RAM")
        pra.grid(row = 1, column = currentColumn, ipady = 5, pady = 5, padx = 40)
        i = 2
        for (t3, v3) in ra.items():
            Radiobutton(newWindow, text = v3, variable = ravar,
                        value = t3).grid(row = i, column = currentColumn)
            i = i+1
        currentColumn = currentColumn + 1

    if(len(ca) != 0):
        pca = Label(newWindow, text = "VGA")
        pca.grid(row = 1, column = currentColumn, ipady = 5, pady = 5, padx = 40)
        i = 2
        for (t4, v4) in ca.items():
            Radiobutton(newWindow, text = v4, variable = cavar,
                        value = t4).grid(row = i, column = currentColumn)
            i = i+1
        currentColumn = currentColumn + 1

    if(len(ch) != 0):
        pch = Label(newWindow, text = "Chip")
        pch.grid(row = 1, column = currentColumn, ipady = 5, pady = 5, padx = 40)
        i = 2
        for (t5, v5) in ch.items():
            Radiobutton(newWindow, text = v5, variable = chvar,
                        value = t5).grid(row = i, column = currentColumn)
            i = i+1
        currentColumn = currentColumn + 1

    if(len(h) != 0):
        ph = Label(newWindow, text = "Ổ Cứng")
        ph.grid(row = 1, column = currentColumn, ipady = 5, pady = 5, padx = 40)
        i = 2
        for (t6, v6) in h.items():
            Radiobutton(newWindow, text = v6, variable = hvar,
                        value = t6).grid(row = i, column = currentColumn)
            i = i+1
        currentColumn = currentColumn + 1

    if(len(w) != 0):
        pw = Label(newWindow, text = "Cân nặng")
        pw.grid(row = 1, column = currentColumn, ipady = 5, pady = 5, padx = 40)
        i = 2
        for (t7, v7) in w.items():
            Radiobutton(newWindow, text = v7, variable = wvar,
                        value = t7).grid(row = i, column = currentColumn)
            i = i+1
        currentColumn = currentColumn + 1

    if(len(b) != 0):
        pb = Label(newWindow, text = "Pin")
        pb.grid(row = 1, column = currentColumn, ipady = 5, pady = 5, padx = 40)
        i = 2
        for (t8, v8) in b.items():
            Radiobutton(newWindow, text = v8, variable = bvar,
                        value = t8).grid(row = i, column = currentColumn)
            i = i+1
        currentColumn = currentColumn + 1

    if(len(c) != 0):
        pra = Label(newWindow, text = "Màu Sắc")
        pra.grid(row = 1, column = currentColumn, ipady = 5, pady = 5, padx = 40)
        i = 2
        for (t9, v9) in c.items():
            Radiobutton(newWindow, text = v9, variable = cvar,# NOTICE ME
                        value = t9).grid(row = i, column = currentColumn)
            i = i+1
        currentColumn = currentColumn + 1

    if(currentColumn == 9):
        newWindow.geometry("960x480")
    elif(currentColumn == 8):
        newWindow.geometry("840x480")
    elif(currentColumn == 7):
        newWindow.geometry("720x480")
    elif(currentColumn == 6):
        newWindow.geometry("600x480")
    else:
        newWindow.geometry("480x480")

    if(currentColumn == 0):
        w1 = Label(newWindow, text ='Khong co may tinh nao tuong thich', font = "50")
        w1.grid(row = 3, column = 3)
        submit1 = Button(newWindow, text="Quit", fg="Black",
                         bg="Red", command=emptyResult)
        submit1.grid(row=12, column=3)
    else:
        submit1 = Button(newWindow, text="Submit", fg="Black",
                         bg="Red", command=openThirdWindow)
        submit1.grid(row=12, column=3)


def emptyResult():
    root.quit()

def openThirdWindow():
    if(len(mvar.get()) != 0):
        choices.append(mvar.get())
    if(len(movar.get()) != 0):
        choices.append(movar.get())
    if(len(ravar.get()) != 0):
        choices.append(ravar.get())
    if(len(cavar.get()) != 0):
        choices.append(cavar.get())
    if(len(chvar.get()) != 0):
        choices.append(chvar.get())
    if(len(hvar.get()) != 0):
        choices.append(hvar.get())
    if(len(wvar.get()) != 0):
        choices.append(wvar.get())
    if(len(bvar.get()) != 0):
        choices.append(bvar.get())
    print(choices)
    cc1 = 'n' + n.get()
    cc2 = 'p' + p.get()
    gt = [cc1, cc2]
    kl = readUser1.conclude(gt)
    re = rule.list_result(kl)
    cc = readUser2.search(choices, re)
    choices.clear()

    newWindow = Toplevel(root)

    newWindow.title("List of the compatible Laptops")
    newWindow.geometry("640x300")

    h = Scrollbar(newWindow, orient = 'horizontal')
    h.pack(side = BOTTOM, fill = X)
    v = Scrollbar(newWindow)
    v.pack(side = RIGHT, fill = Y)
    t = Text(newWindow, width = 15, height = 15, wrap = NONE,
             xscrollcommand = h.set,
             yscrollcommand = v.set)

    if(cc == []):
        w1 = Label(newWindow, text ='Khong co may tinh nao tuong thich', font = "50")
        w1.pack()
    else:
        for i in cc:
            t.insert(END, "Hãng: " + i[0] + "\n")
            t.insert(END, "Loại máy: " + i[1] + "\n")
            t.insert(END, "Màu: " + i[2] + "\n")
            t.insert(END, "Bộ xử lý: " + i[3] + "\n")
            t.insert(END, "Ram: " + i[4] + "\n")
            t.insert(END, "Card màn hình: " + i[5] + "\n")
            t.insert(END, "Ổ Cứng: " + i[6] + "\n")
            t.insert(END, "Kích thước màn hình: " + i[7] + " inch" + "\n")
            t.insert(END, "Pin: " + i[8] + "\n")
            t.insert(END, "Cân nặng: " + i[9] + " kg" + "\n")
            t.insert(END, "Hệ Điều Hành: " + i[10] + "\n")
            t.insert(END, "Giá tiền: " + i[11] + " VND" + "\n")
            t.insert(END, "Link ảnh: " + i[12] + "\n")
            t.insert(END, "********************************************************************************************************\n")
            t.insert(END, "\n")



    t.pack(side=TOP, fill=X)
    h.config(command=t.xview)
    v.config(command=t.yview)
    submit1 = Button(newWindow, text="Quit", fg="Black",
                     bg="Red", command=emptyResult)
    submit1.pack()
    root.mainloop()

if __name__ == "__main__":

    root = Tk()
    root.configure(background='light green')
    root.title("The Form")
    root.geometry("500x400")

    heading = Label(root, text="Form", bg="light green")
    name = Label(root, text="Mục Đích", bg="light green")
    course = Label(root, text="Giá", bg="light green")

    heading.grid(row=0, column=2)
    name.grid(row=1, column=0)

    n = StringVar(root, "1")

    # Dictionary to create multiple buttons
    vn = {"Gaming" : "1",
              "Đồ họa kĩ thuật" : "2",
              "Mỏng nhẹ" : "3",
              "Cao cấp" : "4",
              "Lập trình" : "5",
             "thời trang": "6",
             "Học tập-Văn phòng": "7",
             "Pin khỏe": "8",
             "Phổ thông": "9"}

    i = 2
    j = 1
    for (text1, value1) in vn.items():
        if(j % 3 == 1 and j > 1):
            i = i+1
            j = 1
        Radiobutton(root, text = text1, variable = n,
                    value = value1).grid(row = i, column = j)
        j = j + 1
    i = i + 1

    p = StringVar(root, "1")

    vp = {"Dưới 10 triệu" : "1",
          "10-15 triệu" : "2",
          "15-20 triệu" : "3",
          "20-25 triệu": "4",
          "25-30 triệu": "5",
          "Trên 30 triệu" : "6"}

    course.grid(row=i, column=0)

    for (text2, value2) in vp.items():
        if(j % 3 == 1 and j > 1):
            i = i+1
            j = 1
        Radiobutton(root, text = text2, variable = p,
                    value = value2).grid(row = i, column = j)
        j = j + 1
    i = i+1
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=openSecondWindow)
    submit.grid(row=i, column=2)

    mvar = StringVar(root)
    movar = StringVar(root)
    ravar = StringVar(root)
    cavar = StringVar(root)
    chvar = StringVar(root)
    hvar = StringVar(root)
    wvar = StringVar(root)
    bvar = StringVar(root)
    cvar = StringVar(root)

    root.mainloop()