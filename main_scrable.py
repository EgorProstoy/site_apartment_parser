from scrable_selenium import SelScrable
from bs4 import BeautifulSoup
import time, copy, requests
from work_db import WorkWithDb
from sites import HataScrable
from sites import OnlinerScrable


class Scrable_all(WorkWithDb,SelScrable):
    def createurl_setanchor(self,site=None,target='rent',coint_rooms=1,currency='$',cena_from=None, cema_to=None):
        html=site
        if html == 'https://www.hata.by/':
            pass

    def scrbl(self,site=OnlinerScrable, coint_rooms=6,currency='usd',cena_from='', cema_to='', page=1):
        html=site.ScrableUrl(coint_rooms,currency,cena_from, cema_to, page)
        x=SelScrable.search(html)
        soup=BeautifulSoup(x,"lxml")
        for i in site.soup_list():
            soup=soup.find(i[0],i[1])
        site_table_list=site.table_list()
        if len(site_table_list) == 1:
            for i in site_table_list:
                table=soup.find_all(i[0])
        else:
            for i in site_table_list:
                table=soup.find_all(i[0],i[1])
        inf={}
        tbl_dict=site.table_dict()
        for i in table:
            inf_ind={}
            inf_ind['href']=i['href']
            for j in tbl_dict:
                inf_ind[j]=i.find(tbl_dict[j][0],tbl_dict[j][1]).text
            inf[inf_ind['address']]=inf_ind
        return inf, len(inf)

    def scrbl_all(self):
        i=1
        self.info_all,count =self.scrbl(page=i)
        self.info_keys=list(self.info_all.keys())
        while 1:
            print(i)
            i+=1
            try:
                self.info, count_pl=self.scrbl(page=i)
                count+=count_pl
            except:
                print("it's all")
                break
            else:
                if self.info_keys == list(self.info.keys()):
                    print("it's all")
                    break
                else:
                    self.info_all.update(self.info)
                    self.info_keys = list(self.info.keys())
        info_all = self.info_all
        print(count)
        self.insert_del_to_db(info_all)

    def insert_del_to_db(self, info_all):
        set_db = set(self.select_all_address())
        print(list(set_db)[:15])
        set_scrable = set(list(info_all.keys()))
        print(list(set_scrable)[:15])
        self.set_del_from_db = set_db-set_scrable
        print(list(self.set_del_from_db)[:15])
        self.set_add_in_db = set_scrable-set_db
        print(list(self.set_add_in_db)[:15])
        for i in self.set_del_from_db:
            self.del_from_db(i)
        for i in self.set_add_in_db:
            self.insert_to_db(info_all[i])
        self.end_db()

    def change_text(self,z):
        
        while z[0] in [' ','\n']:
            z=z[1:]
        while z[-1] in [' ','\n']:
            z=z[:-1]
        return z
    def scrable_info(self,site=OnlinerScrable):
        self.all_href=self.select_all_href()
        res={}
        for i in self.all_href:
            try:
                x = requests.get(i)
                x = x.text
                soup = BeautifulSoup(x,"lxml")
                addit_info = self.change_text(soup.find(site.pl_inf()[0],
                                site.pl_inf()[1]).text)
                soup = soup.find(site.info()[0], site.info()[1])
                descr_info = soup.find_all(site.info_ind_descr()[0],
                                site.info_ind_descr()[1])
                descr_info_pr=[]
                for j in descr_info:
                    z=j.text
                    z=self.change_text(z)
                    descr_info_pr.append(z)
                descr_info_pr[1]=descr_info_pr[1].split('\n')[0]
                cont_inf = soup.find(site.info_inf_cont()[0],
                                site.info_inf_cont()[1])
                dict_cont={}
                dict_cont['tel']=''
                for j in cont_inf.find_all(site.tel_info()[0],
                                       site.tel_info()[1]):
                    dict_cont['tel']+=self.change_text(j.text)+'\n'
                if len(site.time_info())!=1:
                    dict_cont['time']=self.change_text(cont_inf.find(site.time_info()[0],
                                            site.time_info()[1]).text)
                else:
                    dict_cont['time']=self.change_text(cont_inf.find(site.time_info()[0]).text)    
                if len(site.name_info())!=1:
                    dict_cont['name']=self.change_text(cont_inf.find_all(site.name_info()[0],
                                            site.name_info()[1])[-1].text)
                else:
                    dict_cont['name']=self.change_text(cont_inf.find_all(site.name_info()[0])[-1].text)    
                descr_info_pr='\n'.join(descr_info_pr)
                dict_cont_info=''
                for j in dict_cont:
                    dict_cont_info += j+': '+dict_cont[j]+'\n'
                dict_cont_info=(self.change_text(addit_info)+';'+
                          self.change_text(dict_cont_info))
                res['href']=i
                res['dict_cont_info']=dict_cont_info
                res['desc_end']=desc_end
                for i in res:
                    for j in [i for i in range(1,6)][::-1]:
                        res[i]=res[i].replace('\n'*j,'\n')
                #for i,j in res.items():
                #    print(i,j,sep=':')
                #print(res)
                print(res)
                break
                self.insert_info_to_db(res)
                print(res)
            except:
                print(res)
                print(self.change_text(cont_inf.find(site.name_info()[0]).text))
                print('fail')
        self.end_db()

if __name__=='__main__':
    test=Scrable_all()
    test.scrable_info()
