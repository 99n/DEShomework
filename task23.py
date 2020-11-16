import random
import DES
import operation


# 对arr数组改变n位
def changeText(arr, n):
    tag = [False for _ in range(64)]  # 也可以arr = [0]*10
    res = [0]*64

    for i in range(64):
        res[i] = arr[i]

    while n > 0:
        id = random.randint(0, 63)
        if tag[id] == False:
            tag[id] = True
            n = n - 1
            if arr[id] == "1":
                res[id] = "0"
            else:
                res[id] = "1"

    #res = res + ''
    return res

#找arr1和arr2不同的位数
def checkBitDif(cipher_bin,change_cipher_bin):
    change_num = 0
    for j in range(64):
        if change_cipher_bin[j] != cipher_bin[j]:
            change_num = change_num + 1
    return change_num


#参数是明文，密钥，任务，改变位数
def solveTask23(plainText,key,kind,initCipherText,lun):
    #8位的明文、密钥、密文转化为64位的二进制数组
    initBitPlainText=operation.string2bin(plainText)
    initBitKey=operation.string2bin(key)
    cipher_bin=operation.string2bin(initCipherText)
    sum=0 #用来求平均数
    if int(kind)==2:
        print("密钥固定，明文改变模式下,循环"+str(lun)+"次结果有：")

        for n in range(1,65):
            print("************************")
            print("明文改变" + str(n) + "位的情况下，循环"+str(lun)+"次：")
            sum=0
            for i in range(1,lun+1):
                s1=changeText(initBitPlainText,n)
                str1=DES.cipher(operation.bin2string(s1),operation.bin2string(initBitKey))
                str1_bin=operation.string2bin(str1)
                dif=checkBitDif(cipher_bin,str1_bin)
                sum=sum+dif
                print("第" + str(i) + "次循环，密文改变" + str(dif) + "位")
            avg=sum/lun
            print("明文改变" + str(n) + "位,统计"+str(lun)+"次,密文平均改变"+str(avg)+"位")

    else :
        print("明文固定，密钥改变模式下,循环"+str(lun)+"次结果有：")

        for n in range(1,65):
            print("************************")
            print("密钥改变" + str(n) + "位的情况下，循环"+str(lun)+"次：")
            sum=0
            for i in range(1,lun+1):
                s2 = changeText(initBitKey, n)
                str2 = DES.cipher(operation.bin2string(initBitPlainText), operation.bin2string(s2))
                str2_bin = operation.string2bin(str2)
                dif = checkBitDif(cipher_bin, str2_bin)
                sum = sum + dif
                print("第" + str(i) + "次循环，密文改变" + str(dif) + "位")
            avg=sum/lun
            print("密钥改变" + str(n) + "位,统计"+str(lun)+"次,密文平均改变"+str(avg)+"位")

kind=input("选择模式(2代表密钥固定，明文改变模式；3代表明文固定，密钥改变模式):")
#n=int(input("请输入改变位数（1-64）："))
plainText=input("请输入明文（8位字母或数字）：")
key=input("请输入密钥（8位字母或数字）：")

initCipherText = DES.cipher(plainText, key)
print("生成的密文为："+initCipherText)
print("即将开始循环统计【改变1-64位明文\密钥，循环N次】的DES密文改变结果：")
lun=int(input("请输入循环次数（1-100）："))
solveTask23(plainText,key,kind,initCipherText,lun)

