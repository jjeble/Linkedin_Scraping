from xlutils.copy import copy
import xlwt
import urllib
from openpyxl import Workbook, load_workbook
#25 93
import zlib
import urllib, urllib2, cookielib
import json
try:
    from urllib.error import HTTPError
except:
    from urllib2 import HTTPError
from xlrd import open_workbook

a = (u'37 Robert-Koch-Stra\xdfe')
import ast
from lxml import html  
import csv,os,json
import requests
import re
print("yas")
import sys    
try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen

alpha_errors =[]
company_errors =[]
alphanum1_errors = []
alphanum2_errors = []
current_letter = ""
current_num1 = 0
current_num2 = 0
current_company = ""
total_comp = 92256
randomvar = 0
randomvar1 = 0
    
username = 'jayj2019@gmail.com'
password = 'clover1'

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'session_key' : username, 'session_password' : password})
opener.open('https://www.linkedin.com/uas/login', login_data)

#print resp.read()

#/div[@class="columns"]/ul[@class="column dual-column/li[@class="content"]/a
#['atlanta','baltimore','charlotte','chicago','cleveland','columbus-ohio','denver','houston','indianapolis','las-vegas','miami','milwaukee','oklahoma-city','orlando','phoenix','portland','provo','rochester'

#wb = Workbook()
#ws = wb.create_sheet()
##ws.title = 'Pi'
#wb.save(filename='book4.xls')
##
##
##book = xlwt.Workbook(encoding = "utf-8")
##sheet1 = book.add_sheet("Sheet 1")
##sheet1.write(0,0,"Company Name")
##sheet1.write(0,1,"Company Address")
##sheet1.write(0,2,"Company Website")
##sheet1.write(0,3,"Comapny Size")
##sheet1.write(0,4,"Company Industry Type")

def data(linklist):
            global randomvar1
            global total_comp
            times = 0
            global company_errors
            global current_company
            ecount = 0
            errcount = 0
            unierr = 0
            error_list = []
            xy = 0
            randomvar1+=1
            
            if randomvar1 == 1:
                times = 1
            else:
                times = 1
                
            while times < len(linklist):
            #for j in linklist[times:]:
                print(times)
                
                total_comp+=1
                try:
                    print("Company on page count: ", times)
                    ecount = ecount+1
                    #print(j)
                    #url = "https://www.linkedin.com/company/a-taste-of-pittsburgh-home-and-lifestyle-magazine"
                    url = linklist[times]
                    
                    req = Request(url, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
                    resp4 = opener.open(req)
                    cont4 = resp4.read()
                    doc4 = html.fromstring(cont4)
                    error =  doc4.xpath('//div[@class="alert error"]/p/strong/text()')
                    times+=1
                    if error:
                        print("ERRRRRRRRRRRRRROR")
                       
                        #errcount+=1
                    else:
                        address = ""
                        website = ""
                        name = ""
                        specialities = ""
                        size = ""
                        ctype = ""
                        industry = ""
                        
                        #print("hereeee")
                        success = doc4.xpath('//code[@id="stream-about-section-embed-id-content"]/comment()')
                        unic = unicode(success[0])
                        string = (unic)[4:-3]
                        compname = doc4.xpath('//meta[@property="og:title"]/@content')
                        string = json.loads(string)
                        name = str(compname[0])
                        if 'headquarters' in string.keys():
                            if 'street1' in string['headquarters'].keys() and len(str(string['headquarters']['street1']))!=0:
                                address = address + str(string['headquarters']['street1'])+ ", "
                            if 'street2' in string['headquarters'].keys() and len(str(string['headquarters']['street2']))!=0 :
                                address = address + str(string['headquarters']['street2'])+ ", "
                            if 'city' in string['headquarters'].keys() and len(str(string['headquarters']['city']))!=0:
                                address = address + str(string['headquarters']['city'])+ ", "
                            if 'state' in string['headquarters'].keys() and len(str(string['headquarters']['state']))!=0:
                                address = address + str(string['headquarters']['state']) + " "
                            if 'zip' in string['headquarters'].keys() and len(str(string['headquarters']['zip']))!=0:
                                address = address + "-"+str(string['headquarters']['zip'])+ ", "
                            if 'country' in string['headquarters'].keys():
                                address = address + string['headquarters']['country']
                            #address = str(string['headquarters'])
                        else:
                            address = "Address not available"
                        if 'website' in string.keys():
                            website = str(string['website'])
                        else:
                            website = "Website not available"
                        if 'size' in string.keys():
                            size = str(string['size'])
                        else:
                            size = "Company Size not available"
                        if 'companyType' in string.keys():
                            ctype = str(string['companyType'])
                        else:
                            ctype = "Company Type not available"
                        if 'industry' in string.keys():
                            industry = str(string['industry'])
                        else:
                            industry = "Industry not available"
                        print(total_comp)
                        print "Name: " + name
                        print "Address: " + address
                        print "Website: " + website
                        print "Company Size: " + size
                        print "Company Type: " + ctype
                        print "Industry: " + industry
                        print
                        print
                        print
                        with open("games.txt", "a") as text_file:
                             text_file.write("\n\n"+ "Name: " + name + "\n")
                             text_file.write("Address: " + address + "\n")
                             text_file.write("Website: " + website + "\n")
                             text_file.write("Company Size: " + size+ "\n")
                             text_file.write("Industry: " + industry + "\n\n")
                        with open("games2.txt", "a") as text_file:
                             text_file.write(name + "^"+address+"^"+website+"^"+size+"^"+industry+"\n")
                             
                        
            

##                    book.save("compnames.xls")
                    
                          
                             

                    
                    
##                        for k,value in string['headquarters'].items():
##                            print(value)
##                            print(str(value))
##                            print(unicode(value))
##                            if type(value) == str:
##                                
##                                value = unicode(value, "utf-8", errors="ignore")
##                            else:
##
##                                value = unicode(value)
##                            #y = v.encode('ascii', 'ignore')
##                            print(k,"kkdk  ",value)
##                            #v = v.decode('unicode-escape')
##                            string['headquarters'][k] = value
                            
                        #string['headquarters'] = string['headquarters'].decode('unicode-escape')
                        #print(,": ",)
                        
                    #else:
                        #print(str(compname[0]), ": Headquarters not given")
                    
                        #except:
                            #pass
                        #print(string["yearFounded"])
                        
                        #print(s)
                        #ab=dict(e.split(":") for e in s.translate(None,"{}").split(","))
                        #print(ab)
                        #ab = eval(dict(s))
                        #print(ab)
                        #print(success_dict["yearFounded"])
                        #Now removing { and}
    ##                    s = ""
    ##                    s = string.replace("{" ,"");
    ##                    finalstring = s.replace("}" , "");
    ##
    ##                    #Splitting the string based on , we get key value pairs
    ##                    list1 = finalstring.split(",")
    ##                    #print(string)
    ##                    print()
    ##                    print(list1)
    ##
    ##                    dicta ={}
    ##                    for i in list1:
    ##                        #
    ##                        print(i)
    ##                        #Get Key Value pairs separately to store in dictionary
    ##                        keyvalue = i.split(":")
    ##                        print(keyvalue)
    ##                        #print(keyvalue[1])
    ##                        #Replacing the single quotes in the leading.
    ##                        m= keyvalue[0]
    ##                        #m = m.replace("\"", "")
    ##                        dicta[m] = keyvalue[1]
    ##
    ##                    print dicta
    ##                    ecount+=1
                
                except HTTPError:
                    print("prrrrrrrrrrrroooooooooobbbbbbbbbbllllllllllllleeemmmmmm")
                    #errcount+=1
                    company_errors.append(url)
                    
                    continue
                    
                except UnicodeEncodeError:

                    unierr+=1
                    print("UNIIIIIIICODDDDDDE",unierr)
                    pass

                except IndexError:
                    print("INDDDDDDDDDDEEEEEEEEEEEEEEEXXXXXXX",url)
           



def crawl():
    global alphanum1_errors
    global alphanum2_errors
    global alpha_errors
    global current_letter
    global current_num1
    global current_num2
    global randomvar
    opener1 = ""
    i = 0
    j = 0
    htmla =""
    company_list= []
    url_comp_list = []
    linklist = []
    count  = 1
    xy = 1
     
    randomvar+=1
    if randomvar == 1:
        xy = 97
    letter_list = ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for letter in letter_list:
        current_letter = letter
        print("Current letter: ",current_letter)
        try:
            url1 = 'https://www.linkedin.com/directory/companies-' + letter+'/'
            resp1 = opener.open(url1)
            cont1 = resp1.read()
            doc1 = html.fromstring(cont1)
            companies =  doc1.xpath('//li[@class="content"]/a/text()')
            print(len(companies))
            for count in range(xy,len(companies)):
                try:
                    print("First number : ",count)
                    i = i+1
                    url2 = 'https://www.linkedin.com/directory/companies-' + letter+'-'+str(count)+'/'
                    #print(url2)
                    resp2 = opener.open(url2)
                    cont2 = resp2.read()
                    doc2 = html.fromstring(cont2)
                    companies1 =  doc2.xpath('//li[@class="content"]/a/text()')
                    companies = companies + companies1
                    if randomvar == 1:
                        randomvar+=1
                        count1 = 6
                        while(count1<len(companies1)):
                        #for count1 in range(28,):
                            
                            try:
                                print("Second number: ", count1)
                                print(alpha_errors)
                                print(company_errors)
                                print(alphanum1_errors)
                                print(alphanum2_errors)
                                j+=1
                                url3 = 'https://www.linkedin.com/directory/companies-' + letter+'-'+str(count)+'-'+str(count1)+'/'
                                print(url3)
                                
                                    
                                resp3 = opener.open(url3)
                                cont3 = resp3.read()
                                doc3 = html.fromstring(cont3)
                                companies2 =  doc3.xpath('//li[@class="content"]/a/@href')
                                linklist=companies2
                                data(linklist)
                                count1+=1
                                
                            except HTTPError:
                                print("prrrrrrrrrrrrobbbbbbblemm2222")
                                alphanum2_errors.append(url3)
                                continue
                                
                                
                    
                   
                    else:
                        count1 = 1
                        while(count1<len(companies1)):
                        #for count1 in range(1,len(companies1)):
                            try:
                                print("Second number: ", count1)
                                print(alpha_errors)
                                print(company_errors)
                                print(alphanum1_errors)
                                print(alphanum2_errors)
                                j+=1
                                url3 = 'https://www.linkedin.com/directory/companies-' + letter+'-'+str(count)+'-'+str(count1)+'/'
                                print(url3)
                                
                                resp3 = opener.open(url3)
                                cont3 = resp3.read()
                                doc3 = html.fromstring(cont3)
                                companies2 =  doc3.xpath('//li[@class="content"]/a/@href')
                                linklist=companies2
                                data(linklist)
                                count1+=1
                            except HTTPError:
                                alphanum2_errors.append(url3)
                                continue
                except HTTPError:
                    alphanum1_errors.append(url2)
                    print("me1")
                    pass
                    #if j == 2:
                       # break
                #if i == 1:
                    #break
            #for k in link_list:
                #print(k)
            print("success")
        except HTTPError:
            alpha_errors.append(url1)
            print("me")
            continue
    
    








##        for company in company_list:
##            linklist.append('https://www.linkedin.com/company/'+str(url_comp_list[i]))
##            try:
##                alist = company.split()
##                alist = [x.lower() for x in alist]
##                if alist[-1][-1]!='.':
##                    for a in range(len(alist)):
##                        alist[a] = re.sub('[!@#$.,"()]', '', alist[a])
##                else:
##                    for a in range(len(alist)):
##                        alist[a] = re.sub('[!@#$.,"]()', '', alist[a])
##                    alist[-1] = str(alist[-1]) + '-'
##                url_comp_list.append('-'.join(alist))
##            except TypeError:
##                pass
##                
##        for i in range(len(url_comp_list)-1):
##            if url_comp_list[i] == url_comp_list[i+1]:
##                url_comp_list[i] = url_comp_list[i]+'_'+str(count)
##                count = count+1
##            else:
##                count = 1
##            
##            try:
##                linklist.append('https://www.linkedin.com/company/'+str(url_comp_list[i]))
##            except UnicodeEncodeError:
##                pass
        

            
##            
##            
            



            #url.addheaders = [{'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}]
            #url = "http://de.linkedin.com/directory/companies-a-3-1/"
            
            #htmla = requests.get(url).text
            #print htmla
            #print(j)
            #req.add_header({'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"})
            #resp = urllib.urlopen(req)
            #content = resp.read()            
            #resp2.add_header('User-Agent', "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36")
            #resp2 = opener.open("https://www.linkedin.com/company/377948?trk=tyah&trkInfo=clickedVertical%3Acompany%2CentityType%3AentityHistoryName%2CclickedEntityId%3Acompany_377948%2Cidx%3A1")
                        
            
        
    #url = 'https://www.linkedin.com/company/3858'
##    resp2 = opener.open(
##    resp = opener.open('https://www.linkedin.com/directory/companies-computer-software/')
##    #printresp.read().xpath('//title'))
##    x = resp.read()
##    doc = html.fromstring(x)
##    alist = []
##    urllist = []
##    companylist = []
##    
##    
##    text1 =  doc.xpath('//li[@class="content"]/a/text()')
##    #print(text1)
##    for i in text1[0:-1]:
##        if i != u'S\xe3o Paulo - Computer Software/Engineering':
##            
##            #print(i)
##            y = i.split()
##            if len(y) == 4:
##                
##                y[0] = re.sub('[!@#$.,]', '', y[0])
##                alist.append(y[0].lower())
##            elif len(y) == 5:
##                y[0] = re.sub('[!@#$.,]', '', y[0])
##                y[1] = re.sub('[!@#$.,]', '', y[1])
##                alist.append(y[0].lower()+'-'+y[1].lower())
##            elif len(y) == 6:
##                y[0] = re.sub('[!@#$.,]', '', y[0])
##                y[1] = re.sub('[!@#$.,]', '', y[1])
##                y[2] = re.sub('[!@#$.,]', '', y[2])
##                alist.append(y[0].lower()+'-'+y[1].lower()+'-'+y[2].lower())
##            
##                
##            
##            
##    #print(alist)
##    for j in alist:
##        name = 'https://www.linkedin.com/directory/companies-'+j+'-computer-software/'
##        #print(name)
##        urllist.append(name)
##    #print(urllist)
##    for url in urllist:
##        resp1 = opener.open(url)
##        x1 = resp1.read()
##        doc1 = html.fromstring(x1)
##        text2 =  doc1.xpath('//li[@class="content"]/a/text()')
##        try:
##            for company in text2:
##                print(company)
##                companylist.append(company)
##                
##        except TypeError:
##            pass
##
##    #for i in companylist:
##       # print(i)
        
        
        
    
    #page = urllib.urlopen(url)
    #print(page)
    #print("okayyyyyyyyyyy")
    #x = ""
    #for l in page:
        
     #Filter it somehow
    #x = (resp.read())
    #print(x.xpath('//title'))
    # x = x + l
##                filename = 'yyyaj.html'
##                with open(filename, 'wb') as f:
##                    f.write(cont3)
    
    

def main():
    crawl()

if __name__ == '__main__':
    print("executing")
    main()
