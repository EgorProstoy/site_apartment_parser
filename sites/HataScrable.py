def hataByScrableUrl(target='',coint_rooms='',currency='$', cena_from='', cena_to='',page=1):
    html='https://www.hata.by/search/list/'
    html_target='~s_do='+target
    html_coint_rooms=''
    html_coint_rooms='~rooms='+str(coint_rooms) if coint_rooms != '' else ''
    html_cena_from = '~cena_from='+str(cena_from) if cena_from != '' else ''
    html_cena_to = '~cena_to='+str(cena_to) if cena_to != '' else ''
    curr={'$':'840','e':'978','BYN':'974'}
    html_currency='~currency='+curr[currency]
    html_page='/page/%d/' % page
    html=(html+
          html_target+
          '~s_what=flat'+
          html_coint_rooms+
          html_cena_from+
          html_cena_to+
          html_currency+
          '~ckod=5000000000~ctype=ckod'+
          html_page)
    return html


soup_list=[['body',{'class':'gray'}],['div',{'class':'main'}],['div',{'class':'list'}]]
table_list=['div',{'class':'list-item'}]
info_dict={
'name':['div',{'class':'list-line-addr'}],
'info':'aa'
    }

if __name__=='__main__':
    hataByScrableUrl(target='rent',coint_rooms=1)
