import test

# n-gram에 사용되는 n값을 받아온다.
def GetWhatGram():
	gram_n = int (input("Input N for N-Gram : "))
	return gram_n;
# 주어진 리스트를 set에 넣고 jaccard index를 구한 후 출력한다. 
def PutsetGetindex(nGramSet1,nGramSet2,dir_list1,dir_list2):
	set1 = set(nGramSet1)
	set2 = set(nGramSet2) 
	
	intersection = set1 & set2
	union =set1 | set2

	count_inter = len(intersection)
	count_uni = len(union)
	if(count_uni != 0):
		jac_con = count_inter/count_uni
	else:
		jac_con = 0

	w_count_inter = "%d\n" %count_inter
	w_count_uni = "%d\n" %count_uni
	w_jac_con = "%f\n" %jac_con
	#if(jac_con > 0.6): 자카르트 인뎃스를 얼마로 해야할까에 대한 기준 설정

	result.write(dir_list1)
	result.write(" & ")
	result.write(dir_list2)
	result.write("\n")
	result.write("How many intersection: ")
	result.write(w_count_inter)
	result.write("How many union: ")
	result.write(w_count_uni)
	result.write("jaccard containment is ")
	result.write(w_jac_con)
	result.write("\n")
# 파일로 부터 읽어온 문자들을 함수를 이용하여 nGram으로 나눠진 리스트로 만든다.
def GetFiletoList(nGram,filename,dirname):

	try:
		infile = open(dirname+filename, "r") #디렉토리부분을 사용자로 부터 입력 받을 수있다.
		lines = infile.readlines()

	except:
		infile = open(dirname+filename, "r",encoding = "utf-8")
		lines = infile.readlines()
	
	totalStr_r = ""
	totalStr = ""

	#rstrip으로 \n 제거 
	for line in lines :
		line = Remove_comment(line)
		totalStr_r += line.rstrip()
	#split으로 space 제거 
	lines_r = totalStr_r.split()

	for line in lines_r :
		totalStr += line

	nGramSet = []
	# size=len(totalStr)-nGram+1

	for i in range(0, len(totalStr) - nGram + 1) :
	   if not totalStr[i:i+nGram] in nGramSet :
	      nGramSet.append(totalStr[i:i+nGram])

	return nGramSet;

def Get_dir_list(dirname):
    flist = os.listdir(dirname)

    print (flist)
    return flist
# '//' 형태의 주석 제거
def Remove_comment(string):

	str_r = ""
	length = len(string)
	for pos in range (0,length - 1):
		if string[pos] == "#":
			break
		str_r += string[pos]

	return str_r



#########################main#################################
import os

result = open("result.txt",'w')
dirname = input("Enter dirname: ")
nGram = GetWhatGram();
nGramset = []
dir_list = Get_dir_list(dirname);
for j in range (0,len(dir_list)) :
	nGramset.append(GetFiletoList(nGram,dir_list[j],dirname))  
for k in range (0,len(dir_list)) :
	for j in range (k+1,len(dir_list)) :
		
		PutsetGetindex(nGramset[k],nGramset[j],dir_list[k],dir_list[j])





## 클래스를 이용하여  handler클래스와 nGramset클래스를 만들어 해결할수 있지 않을까?