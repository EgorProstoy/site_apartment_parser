def ScrableUrl(coint_rooms=6,
                     cur='usd',
                     cena_from='',
                     cema_to='',
                     page=1):
    html='https://<start_url>'
    rent_room='rent_type[]=1_room'
    for i in range(coint_rooms-1):
        rent_room+='<>'.format(i+2)
    html_cena_from='<>'+str(cena_from) if cena_from != '' else ''
    html_cena_to='<>'+str(cena_to) if cema_to != '' else ''
    html_currency='<>'+cur
    html_addition='<>'
    html_page='<>'+str(page)
    html=(html+
          rent_room+
          html_cena_from+
          html_cena_to+
          html_currency+
          html_addition+
          html_page)
    return html

def soup_list():
    soup_list=[['div',{'id':"search-filter-results"}],['div',{'class':'classifieds-list'}]]
    return soup_list
    
def table_list():
    table_list=[['a']]
    return table_list

def table_dict():
    tbl_dict={}
    tbl_dict['count_flat']=['span',
        {'class':"classified__caption-item classified__caption-item_type"}]
    tbl_dict['address']=['span',
        {'class':"classified__caption-item classified__caption-item_adress"}]
    tbl_dict['price_in_$']=['span',
        {'data-bind':"text: SearchApartments.formatPrice(apartment.price, 'USD')"}]
    tbl_dict['price_in_BYN']=['span',
        {'data-bind':"text: SearchApartments.formatPrice(apartment.price, 'BYN')"}]
    return tbl_dict

if __name__=='__main__':
    hataByScrableUrl(page=2)
