# -*- coding: utf-8 -*-
"""
Created on Fri Apr 9 14:55:20 2021

@authors: Jameson Epstein and Abhishek Kamatkar
"""

import os.path
from os import path
import re

#Global variables needed to hander parser and respective output
tokenList = []
tokenListId = 0
tokenListLen = 0
parseError = 0
inpTok = ""
outputStr = ""
indentBuffer = 0

#main function called to handle all sub functions
def main():
    global tokenList
    global tokenListLen
    global inpTok
    global parseError
    global outputStr
    filename = menu()
    #if an unrecognized token is met, gettok returns 0, and program prints 
    #unrecognized token, then ends
    if getTok(filename) == 0:
        print("unrecognized token!")
    else:
        #initializes global variables, then calls the scanner function
        tokenList = getTok(filename)
        tokenListLen = len(tokenList) - 1
        inpTok = tokenList[tokenListId]
        # print(tokenList)
        scanner(inpTok)
        #if there is no parse error, then the outputStr is printed
        if(parseError == 0):
            print(outputStr)
        # print("outputStr = {0}".format(outputStr))
        # print("done")

def funcSelect():
    #Prompts user input, checks for 2 args, asking user to re enter if number of args not met
    #returns user input at string if they input correct parameters
    inpArg = input(">>")
    #case to check if there are the right amounts of arguments
    if len(inpArg.split()) != 2:
        return 3
    #initializes the arguments
    else:
        func = inpArg.split()[0]
        fPath  = inpArg.split()[1]
    #if the first argument is not parser, then print error and exit
    if(func != "parser"):
        print("error")
        return 1
    #case to check if the path exists
    else:
        pExists = path.exists(str(fPath))  
        if pExists == 0:
            return 4
        else:
            return inpArg
        
def menu():
    flag = 0
    print("Project 2 By Jameson Epstein and Abhishek Kamatkar")  
    args = funcSelect()
    while flag != 1:
        if (args == 1):
            print("invalid function, please try again")
            args = funcSelect()
        elif (args == 2):
            print("invalid file path, please try again")
            args = funcSelect()
        elif(args == 3):
            print("invalid amount of arguments, please try again, Are there spaces?")
            print("this program does not allow for spaces")
            args = funcSelect()
        elif(args == 4):
            print("invalid file path, please try again")
            args = funcSelect()
        else:
            if (args.split()[0] == "parser"):
                filename = args.split()[1]
                flag = 1
    return filename

def getTok(filename):
    #steps through each character, and compares it to any possible tokens that are in the table
    #probably a better way of doing this by using a table, but i really, really like nested loops
    commentFlag = 1
    error = 0
    file = open(filename, "r")
    filePeek = open(filename, "r")
    charPeek = filePeek.read(1)
    char = file.read(1)
    outPutArr = []
    outArr = []

    while 1:

        tokenFound = 0
        charPeek = filePeek.read(1)

        #Breaks at EOF
        if not char:
            break
        
        #Comment Tolken
        if tokenFound == 0:
            commentStr = 'comment'
            if char == '/':
                if charPeek == '*':
                    char = file.read(1)
                    charPeek = filePeek.read(1)
                    char = file.read(1)
                    charPeek = filePeek.read(1)
                    char = file.read(1)
                    charPeek = filePeek.read(1)
                    while commentFlag:
                        if char == '*':
                            if charPeek == '/':
                                char = file.read(1)
                                charPeek = filePeek.read(1)                   
                                commentFlag = 0
                        else:
                            char = file.read(1)
                            charPeek = filePeek.read(1)
                    tokenFound = 1

        #read Tolken
        if tokenFound == 0:
            if char == 'r':
                if charPeek == 'e':
                    charPeek = filePeek.read(1)
                    char = file.read(1)
                    if charPeek == 'a':
                        charPeek = filePeek.read(1)
                        char = file.read(1)
                        if charPeek == 'd':
                            charPeek = filePeek.read(1)
                            char = file.read(1)
                            if charPeek.isalpha():
                                outPutArr.append('id')
                                tokenFound = 1
                                idFlag = 1
                                while idFlag:
                                    if charPeek.isalpha():
                                        char = file.read(1)
                                        charPeek = filePeek.read(1)
                                    else:
                                        idFlag = 0
                            else:
                                outPutArr.append('read')
                                outArr.append('read')
                                tokenFound = 1
        #write Tolken
        if tokenFound == 0:
            if char == 'w':
                if charPeek == 'r':
                    charPeek = filePeek.read(1)
                    char = file.read(1)
                    if charPeek == 'i':
                            charPeek = filePeek.read(1)
                            char = file.read(1)
                            if charPeek == 't':
                                charPeek = filePeek.read(1)
                                char = file.read(1)
                                if charPeek == 'e':
                                    char = file.read(1)
                                    charPeek = filePeek.read(1)
                                    if charPeek.isalpha():
                                        outPutArr.append('id')
                                        tokenFound = 1
                                        idFlag = 1
                                        while idFlag:
                                            if charPeek.isalpha():
                                                char = file.read(1)
                                                charPeek = filePeek.read(1)
                                            else:
                                                idFlag = 0
                                    else:
                                        outPutArr.append('write')
                                        outArr.append('write')
                                        tokenFound = 1
            
        #assign Tolken
        if tokenFound == 0:
            if char == ':':
                if charPeek == '=':
                    char = file.read(1)
                    charPeek = filePeek.read(1)
                    assignStr = ':='
                    outPutArr.append(':=') 
                    outArr.append(':=')
                    tokenFound = 1
                
        #multiply Tolken
        if tokenFound == 0:
            if char == '*':
                multiplyStr = '*'
                outPutArr.append("*")
                outArr.append('*')
                tokenFound = 1
            
        #Divide Token
        if tokenFound == 0:
            if char == '/':
                divideStr = '/'
                outPutArr.append("/")
                outArr.append('/')
                tokenFound = 1
                    
        #plus Tolken
        if tokenFound == 0:
            if char == '+':
                plusStr = '+'
                outPutArr.append('+')
                outArr.append('+')
                tokenFound = 1
                
        #subtract Tolken
        if tokenFound == 0:
            if char == '-':
                subtractStr = '-'
                outPutArr.append('-')
                outArr.append('-')
                tokenFound = 1
            
        #lparen Tolken
        if tokenFound == 0:
            if char == '(':
                lparenStr = '('
                outPutArr.append('(')
                outArr.append('(')
                tokenFound = 1
        
        #rparen Tolken
        if tokenFound == 0:
            if char == ')':
                rparenStr = ')'
                outPutArr.append(')')
                outArr.append(')')
                tokenFound = 1
                
        #number Tolken
        if tokenFound == 0:
            if char.isdigit():
                numberFlag = 1
                numberStr = 'number'
                outPutArr.append('number')
                numTok = ""
                numTok = numTok + char
                tokenFound = 1
                while numberFlag:
                    if charPeek.isdigit():
                        char = file.read(1)
                        numTok = numTok + char
                        charPeek = filePeek.read(1)
                    else:
                        numberFlag = 0
                outArr.append(numTok)
        
        #id Tolken
        if tokenFound == 0:
            if char.isalpha():
                idTok = ""
                idStr = 'id'
                idFlag = 1
                outPutArr.append('id')
                idTok = idTok + char
                tokenFound = 1
                while idFlag:
                    if charPeek.isalpha():
                        char = file.read(1)
                        idTok = idTok + char
                        charPeek = filePeek.read(1)
                    else:
                        idFlag = 0
                outArr.append(idTok)

        #skips whitespace and newlines                
        if tokenFound == 0:
            if char == " " or char == "\n":
                tokenFound = 1

        #if token is not recognized,set error flag, then print the character that
        #is not recognized
        if tokenFound == 0:
            error = 1
            print(char)
        char = file.read(1)
          
    if error == 1:
        return 0
    outPutArr.append("$$")
    outArr.append('$$')
    return outArr

#function that matches an input (expected token) with the inpTok global variable
#if they match, push inpTok into print function, then get next token
def match(expected):
    global inpTok
    global indentBuffer
    printStr = ""
    
    #match for number
    if(expected == "number"):
        if(inpTok.isdigit()):
            indentBuffer = indentBuffer + 1
            printFunc(indentBuffer, "<number>")
            indentBuffer = indentBuffer + 1
            printFunc(indentBuffer, inpTok)
            indentBuffer = indentBuffer - 1
            printFunc(indentBuffer, "</number>")  
            indentBuffer = indentBuffer - 1
        inpTok = getNextTok()
    elif(inpTok == expected):
        if(inpTok != "$$"):
            indentBuffer = indentBuffer + 1
            printStr = "<" + inpTok + ">"
            printFunc(indentBuffer, printStr)
            indentBuffer = indentBuffer + 1
            printFunc(indentBuffer, inpTok)
            indentBuffer = indentBuffer - 1
            printStr = "</" + inpTok + ">"
            printFunc(indentBuffer, printStr)
            indentBuffer = indentBuffer - 1
        inpTok = getNextTok()
        
    #match for ID
    elif(expected == "id"):
        if(inpTok.isalpha()):
            indentBuffer = indentBuffer + 1
            printFunc(indentBuffer, "<id>")
            indentBuffer = indentBuffer + 1
            printFunc(indentBuffer, inpTok)
            indentBuffer = indentBuffer - 1
            printFunc(indentBuffer, "</id>")  
            indentBuffer = indentBuffer - 1
        inpTok = getNextTok()

    #case for parse error
    else:
        print("Parse Error")
        global parseError
        parseError = 1

# recursion functions that define the proper grammer of the language        
def program():
    global indentBuffer
    printFunc(indentBuffer, "<Program>")
    if(inpTok ==  "read"):
        stmt_list()
        match("$$")
        indentBuffer = indentBuffer - 1
        printFunc(indentBuffer, "</Program>")
        return 1
    elif(inpTok == "write"):
        stmt_list()
        match("$$")
        indentBuffer = indentBuffer - 1
        printFunc(indentBuffer, "</Program>")
        return 1
    elif(isId(inpTok)):
        stmt_list()
        match("$$")
        indentBuffer = indentBuffer - 1
        printFunc(indentBuffer, "</Program>")
        return 1
    else:
        return 0

def stmt_list():
    global indentBuffer
    indentBuffer = indentBuffer + 1
    printFunc(indentBuffer, "<stmt_list>")

    if(inpTok == "read"):
        stmt()
        stmt_list()
        indentBuffer = indentBuffer - 1
        printFunc(indentBuffer, "</stmt_list>")
    elif(inpTok == "write"):
        stmt()
        stmt_list()
        indentBuffer = indentBuffer - 1
        printFunc(indentBuffer, "</stmt_list>")
    elif(isId(inpTok)):
        stmt()
        stmt_list()
        indentBuffer = indentBuffer - 1
        printFunc(indentBuffer, "</stmt_list>")
    elif(inpTok == "$$"):
        #indentBuffer = indentBuffer - 1
        printFunc(indentBuffer, "</stmt_list>")
        return 
    else:
        return 0

def stmt():
    global indentBuffer
    indentBuffer = indentBuffer + 1
    printFunc(indentBuffer, "<stmt>")
    
    if(inpTok == "read"):
        match("read")
        match("id")
        printFunc(indentBuffer, "</stmt>")
        indentBuffer = indentBuffer - 1
    elif(inpTok == "write"):
        match("write")
        expr()
        printFunc(indentBuffer, "</stmt>")
        indentBuffer = indentBuffer - 1
    if(isId(inpTok)):
        match("id")
        match(":=")
        expr()  
        printFunc(indentBuffer, "</stmt>")
        indentBuffer = indentBuffer - 1
    else:
        return 0
        
def expr():
    global indentBuffer
    indentBuffer = indentBuffer + 1
    printFunc(indentBuffer, "<expr>")
    if(isId(inpTok)):
        term()
        term_tail()
        printFunc(indentBuffer, "</expr>")
        indentBuffer = indentBuffer - 1
    elif(inpTok == "number"):
        term()
        term_tail()
        printFunc(indentBuffer, "</expr>")
        indentBuffer = indentBuffer - 1
    elif(inpTok == "("):
        term()
        term_tail()
        printFunc(indentBuffer, "</expr>")
        indentBuffer = indentBuffer - 1
    else:
        return 0
    
def term_tail():
    global indentBuffer
    indentBuffer = indentBuffer + 1
    printFunc(indentBuffer, "<term_tail>")
    if(inpTok == "+"):
        add_op()
        term()
        term_tail()
        printFunc(indentBuffer, "</term_tail>")
        indentBuffer = indentBuffer - 1
    elif(inpTok == "-"):
        add_op()
        term()
        term_tail()
        printFunc(indentBuffer, "</term_tail>")
        indentBuffer = indentBuffer - 1
    elif(inpTok == ")"):
        printFunc(indentBuffer, "</term_tail>")
        indentBuffer = indentBuffer - 1
        return
    elif(isId(inpTok)):
        printFunc(indentBuffer, "</term_tail>")
        indentBuffer = indentBuffer - 1
        return
    elif(inpTok == "read"):
        printFunc(indentBuffer, "</term_tail>")
        indentBuffer = indentBuffer - 1
        return
    elif(inpTok == "write"):
        printFunc(indentBuffer, "</term_tail>")
        indentBuffer = indentBuffer - 1
        return
    elif(inpTok == "$$"):
        printFunc(indentBuffer, "</term_tail>")
        indentBuffer = indentBuffer - 1
        return
    else:
        return 0

def term():
    global indentBuffer
    indentBuffer = indentBuffer + 1
    printFunc(indentBuffer, "<term>")
    if(isId(inpTok)):
       factor()
       factor_tail()
       printFunc(indentBuffer, "</term>")
       indentBuffer = indentBuffer - 1
    elif(isNumber(inpTok)):
       factor()
       factor_tail()
       printFunc(indentBuffer, "</term>")
       indentBuffer = indentBuffer - 1
    elif(inpTok == "("):
        factor()
        factor_tail()
        printFunc(indentBuffer, "</term>")
        indentBuffer = indentBuffer - 1
    else:
        return 0
        
def factor_tail():
    global indentBuffer
    indentBuffer = indentBuffer + 1
    printFunc(indentBuffer, "<factor_tail>")
    if(inpTok == "*"):
        mult_op()
        factor()
        factor_tail()
        printFunc(indentBuffer, "</factor_tail>")
        indentBuffer = indentBuffer - 1
    elif(inpTok == "/"):
        mult_op()
        factor()
        factor_tail()
        printFunc(indentBuffer, "</factor_tail>")
        indentBuffer = indentBuffer - 1
    elif(inpTok == "+"):
        printFunc(indentBuffer, "</factor_tail>")
        indentBuffer = indentBuffer - 1
        return 
    elif(inpTok == "-"):
        printFunc(indentBuffer, "</factor_tail>")
        indentBuffer = indentBuffer - 1
        return 
    elif(inpTok == ")"):
        printFunc(indentBuffer, "</factor_tail>")
        indentBuffer = indentBuffer - 1
        return 
    elif(isId(inpTok)):
        printFunc(indentBuffer, "</factor_tail>")
        indentBuffer = indentBuffer - 1
        return 
    elif(inpTok == "read"):
        printFunc(indentBuffer, "</factor_tail>")
        indentBuffer = indentBuffer - 1
        return 
    elif(inpTok == "write"):
        printFunc(indentBuffer, "</factor_tail>")
        indentBuffer = indentBuffer - 1
        return 
    elif(inpTok == "$$"):
        printFunc(indentBuffer, "</factor_tail>")
        indentBuffer = indentBuffer - 1
        return 
    else:
        return 0
    
def factor():
    global indentBuffer
    indentBuffer = indentBuffer + 1
    printFunc(indentBuffer, "<factor>")
    if(isId(inpTok)):
        match("id")
        printFunc(indentBuffer, "</factor>")
        indentBuffer = indentBuffer -1
    elif(isNumber(inpTok)):
        match("number")
        printFunc(indentBuffer, "</factor>")
        indentBuffer = indentBuffer -1
    elif(inpTok == "("):
        match("(")
        expr()
        match(")")
        printFunc(indentBuffer, "</factor>")
        indentBuffer = indentBuffer -1
    else:
        return 0

def add_op():
    global indentBuffer
    indentBuffer = indentBuffer + 1
    printFunc(indentBuffer, "<add_op>")
    if(inpTok == "+"):
        match("+")
        printFunc(indentBuffer, "</add_op>")
        indentBuffer = indentBuffer - 1
    elif(inpTok == "-"):
        match("-")
        printFunc(indentBuffer, "</add_op>")
        indentBuffer = indentBuffer - 1
    else:
        return 0
    
def mult_op():
    global indentBuffer
    indentBuffer = indentBuffer + 1
    printFunc(indentBuffer, "<mult_op>")
    if(inpTok == "*"):
        match("*")
        printFunc(indentBuffer, "</mult_op>")
        indentBuffer = indentBuffer - 1
    elif(inpTok == "/"):
        match("/")
        printFunc(indentBuffer, "</mult_op>")
        indentBuffer = indentBuffer - 1
    else:
        return 0   

#function that gets the next token, as long as the next token exists
def getNextTok():
    global tokenListId
    if(tokenListId < tokenListLen):
        tokenListId = tokenListId + 1
        return tokenList[tokenListId]

#highest level of the recursion program. recives the inpTok, and calls the program
#function    
def scanner(inpTok):
    global tokenListId
    global tokenList
    program()

#function handles the output of the program. recives the indent int, and the strin
#to be appended. builds the string and appends it to the print string
#which is the combination of all previous strings    
#i: number of spaces to be indented, strApp: string to be appended after intented
def printFunc(i, strApp):
    j = 0
    global outputStr
    printStr = ""
    printInt = 0
    if(strApp == "$$"):
        return
    else:
        while(j < i):
            printStr = printStr + "  "
            printInt = printInt + 1
            j = j + 1
        printStr = printStr + strApp + "\n"
        outputStr = outputStr + printStr

#function that checks if the input is a digit, returns true or false    
def isNumber(inpTok):
    x = inpTok.isdigit()
    return x

#function that checks if the input is alpha, returns true or false
def isId(inpTok):
    x = inpTok.isalpha()
    return x
