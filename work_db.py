import sqlite3
class WorkWithDb:
    import sqlite3
    con=sqlite3.connect('rscrable.res.db')
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS scrable
(address STRING,
count_flat INTEGER,
href STRING PRIMARYKEY UNIQUE,
price_in_dol INTEGER,
price_in_BYN INTEGER)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS info
(href STRING UNIQUE,
images STRING,
description STRING,
contacts STRING,
FOREIGN KEY (href) REFERENCES scrable(href))''')
    cur.close()
    con.close()
    con=sqlite3.connect('rscrable.res.db')
    cur=con.cursor()
    def select_all_address(self):
        self.cur.execute('SELECT address FROM scrable')
        self.res_all=self.cur.fetchall()
        self.res_all_0=[]
        for i in self.res_all:
            self.res_all_0.append(i[0])
        return self.res_all_0
    def insert_to_db(self,inf_ind):
        try:
            self.cur.execute('INSERT INTO scrable VALUES((?),(?),(?),(?),(?))',
                    (inf_ind['address'],
                    inf_ind['count_flat'],
                    inf_ind['href'],
                    inf_ind['price_in_$'],
                    inf_ind['price_in_BYN'])
                    )
        except sqlite3.IntegrityError:
            pass
        else:
            self.con.commit()
    def select_from_db(self,address):
        self.cur.execute('SELECT address FROM scrable WHERE address=(?)',(address,))
        self.res=self.cur.fetchone()
        self.res_0=[]
        for i in self.res:
            self.res_0.append(i)
        print(self.res_0)
        return self.res_0
    def del_from_db(self,address):
        self.cur.execute('DELETE FROM scrable WHERE address=(?)',(address,))
        self.con.commit()
    def select_all_href(self):
        self.cur.execute('SELECT href FROM scrable')
        self.res_all=self.cur.fetchall()
        self.res_all_0=[]
        for i in self.res_all:
            self.res_all_0.append(i[0])
        return self.res_all_0
    def insert_info_to_db(self,res):
        try:
            self.cur.execute('SELECT href FROM info WHERE href=(?)',(res['href'],))
            p=self.cur.fetchone()
        except:
            p=None
        if not p:
            self.cur.execute('INSERT INTO info VALUES((?),(?),(?),(?))',
                         (res['href'],'Not',res['desc_end'],res['dict_cont_info']))
            self.con.commit()
        
    def end_db(self):
        self.cur.close()
        self.con.close()
    
if __name__=='__main__':
    test=WorkWithDb()
    test_dict={'address':'olimp','count_flat':'infinity','href':'www.will_be_gods_is_good.olp','price_in_$':'infinity','price_in_BYN':'infinity*2'}
    test.insert_to_db(test_dict)
    test.select_from_db('olimp')
    print(test.select_all_href())
    test.del_from_db('olimp')
    test.insert_info_to_db({'href': 'https://r.onliner.by/ak/apartments/103773', 'dict_cont_info': 'Агент;tel: +375 44 510-96-57\n+375 29 538-96-53\n\nname: Гарант Недвижимость\ntime: Звоните в любое время'})
    test.end_db()

    
