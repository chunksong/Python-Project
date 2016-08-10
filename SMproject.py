# -*- coding: utf-8 -*-
# A first script Python script
from tkinter import *

num_val = 0
val_list =[]
val_slist = []


def print_output():

    output.delete(0.0, END)

    for val in val_list:
        output.insert(END, str(val[0]) + '\t' + val[1] + '\t\t' + '\t' + str(val[2]) +'\n' )


def click(key):

    global num_val

    if key == '추가':
        try:
            state.delete(0.0, END)
            val_name = str(name.get())
            val_score = eval(score.get())
            state_message = " 성공적으로 읽어왔습니다. "
            state.insert(END, state_message)
        except:
            state.delete(0.0, END)
            state_message = " 제대로 읽어오지 못하였습니다. "
            state.insert(END,state_message)

        val_name = val_name.rstrip()

        if(len(val_name) == 0):
            state.delete(0.0,END)
            state_message = " [추가 실패] 이름이 없습니다. "
            state.insert(END,state_message)
            return
        elif(val_score > 100 or val_score < 0):
            state.delete(0.0,END)
            state_message = " [추가 실패] 잘못된 점수 입니다. "
            state.insert(END,state_message)
            return

        for val in val_list:
            if val_name == val[1]:
                state.delete(0.0, END)
                state_message = " [추가 실패] 동일한 이름이 이미 존재 합니다. "
                state.insert(END,state_message)
                return
        num_val = num_val +1
        val_data = [num_val, val_name, val_score]
        val_list.append(val_data)

        name.delete(0, END)
        score.delete(0, END)
        print_output()

    elif key == '삭제':

        del_num = 0
        try:
            del_num = int(num.get())
        except:
            state.delete(0.0,END)
            state_message = " 삭제에 실패하였습니다. "
            state.insert(END,state_message)

        for val in val_list:
            if(del_num == val[0]):
                val_list.remove(val)
                print_output()
                state.delete(0.0,END)
                state_message = " 성공적으로 삭제하였습니다. "
                state.insert(END,state_message)
                return

        state.delete(0.0,END)
        state_message = " 삭제에 실패하였습니다. "
        state.insert(END,state_message)

    elif key == "저장":

        save_filename = filename1.get()

        try:
            file = open(save_filename, 'w')
        except:
            state.delete(0.0,END)
            state_message = " 파일 저장에 실패하였습니다. "
            state.insert(END,state_message)

        for val in val_list:
            file.write(str(val)+'\n')

        fileerr = ['\\', '/', ':', '*',  '?' , '"', '<', '>', '|']

        for errname in fileerr:
            if(save_filename.find(errname) != -1):
                state.delete(0.0,END)
                state_message = " 파일 저장에 실패하였습니다. "
                state.insert(END,state_message)
                return

        state.delete(0.0,END)
        state_message = " 성공적으로 저장하였습니다. (파일 이름 : " + str(save_filename) + ")"
        state.insert(END,state_message)

        file.close()
        filename1.delete(0, END)

    elif key == "열기":

        load_filename = filename2.get()

        try:
            file = open(load_filename, 'r')
        except:
            state.delete(0.0,END)
            state_message = " 파일 불러오기에 실패하였습니다. "
            state.insert(END,state_message)
            return

        fileerr = ['\\', '/', ':', '*',  '?' , '"', '<', '>', '|']

        for errname in fileerr:
            if(load_filename.find(errname) != -1):
                state.delete(0.0,END)
                state_message = " 파일 저장에 실패하였습니다. "
                state.insert(END,state_message)
                return

        val_list.clear()
        num_val = 0

        for line in file.readlines():
            line = line.rstrip('\n').strip('[').rstrip(']')
            line_split = line.split(',')
            val_data = [int(line_split[0]), line_split[1].lstrip(" '").rstrip("'"), int(line_split[2])]
            val_list.append(val_data)
            num_val = num_val + 1


        print_output()
        filename2.delete(0,END)
        state.delete(0.0,END)
        state_message = " 성공적으로 읽습니다. (파일 이름 : " + str(load_filename) + ")"
        state.insert(END,state_message)

    elif key == '번호순':
        state.delete(0.0,END)
        val_list.sort()
        print_output()

    elif key == '이름순':
        state.delete(0.0,END)

        val_slist.clear()
        for val in val_list:
            val_slist.append([val[1],val[0],val[2]])
        val_slist.sort()

        val_list.clear()
        for val in val_slist:
            val_list.append([val[1],val[0],val[2]])

        print_output()

    elif key == '점수내림차순':
        state.delete(0.0,END)

        val_slist.clear()
        for val in val_list:
            val_slist.append([val[2],val[1],val[0]])
        val_slist.sort(reverse=True)

        val_list.clear()
        for val in val_slist:
            val_list.append([val[2],val[1],val[0]])

        print_output()

    elif key == '점수오름차순':
        state.delete(0.0,END)

        val_slist.clear()
        for val in val_list:
            val_slist.append([val[2],val[1],val[0]])
        val_slist.sort()

        val_list.clear()
        for val in val_slist:
            val_list.append([val[2],val[1],val[0]])

        print_output()
#    else:
#        display.insert(END, key)

window = Tk()
window.title("SM Program")

### textbox
Label(window, text="이름 :").grid(row = 0, column = 0, sticky = W)
name_frame = Frame(window)
name_frame.grid(row=0, column=1, sticky = W)
name = Entry(name_frame, width= 20, bg="light green")
name.grid()

Label(window, text="점수 :").grid(row = 0, column =2, sticky = E)
score_frame = Frame(window)
score_frame.grid(row = 0, column = 3, columnspan = 10, sticky = W)
score = Entry(score_frame, width= 7, bg="light green")
score.grid()
def cmd1(x='추가'):
    click(x)
Button(window, text="추가", width = 5, command = cmd1).grid(row = 0, column = 4, sticky = W)


Label(window, text="번호 :").grid(row = 1, column =2, sticky = E)
num_frame = Frame(window)
num_frame.grid(row = 1, column = 3, sticky=W)
num = Entry(num_frame, width= 5, bg="light green")
num.grid()
def cmd2(x='삭제'):
    click(x)
Button(window, text="삭제", width = 5, command = cmd2).grid(row = 1, column = 4, sticky = W)


Label(window, text="파일이름 :").grid(row = 2, column =2, sticky = E)
fname_frame = Frame(window)
fname_frame.grid(row = 2, column = 3, sticky=W)
filename1 = Entry(fname_frame, width= 20, bg="light blue")
filename1.grid()
def cmd3(x='저장'):
    click(x)
Button(window, text="저장", width = 5, command = cmd3).grid(row = 2, column = 4, sticky = W)


Label(window, text="파일이름 :").grid(row = 3, column =2, sticky = E)
fname_frame2 = Frame(window)
fname_frame2.grid(row = 3, column = 3, columnspan = 10, sticky=W)
filename2 = Entry(fname_frame2, width= 20, bg="light blue")
filename2.grid()
def cmd4(x='열기'):
    click(x)
Button(window, text="열기", width = 5, command = cmd4).grid(row = 3, column = 4, sticky = W)

# reshape_frame
reshape_frame = [
    '번호순',
    '이름순',
    '점수내림차순',
    '점수오름차순'
]

reshape_button_frame = Frame(window)
reshape_button_frame.grid(row = 4,column = 0, columnspan = 5, sticky = N)

# reshape_Button
for i in range(4):
    def cmd(x=reshape_frame[i]):
        click(x)
    if(i < 2):
        Button(reshape_button_frame, text=reshape_frame[i],width = 5, command = cmd).grid(row = 4, column = i, sticky = N)
    else:
        Button(reshape_button_frame, text=reshape_frame[i],width = 15, command = cmd).grid(row = 4, column = i, sticky = N)

# output box
output = Text(window, width=75, height=10, wrap=WORD, background="light yellow")
output.grid(row = 5, column = 0,columnspan = 5, sticky = N)

# state box
state = Text(window, width=75, height=1, wrap=WORD, background="pink")
state.grid(row = 8, column = 0, columnspan = 5, sticky = N)


window.mainloop()
