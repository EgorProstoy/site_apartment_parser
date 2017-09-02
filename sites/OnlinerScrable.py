def ScrableUrl(coint_rooms=6,
                     cur='usd',
                     cena_from='',
                     cema_to='',
                     page=1):
    html='https://r.onliner.by/ak/?'
    rent_room='rent_type[]=1_room'
    for i in range(coint_rooms-1):
        rent_room+='&rent_type[]={}_rooms'.format(i+2)
    html_cena_from='&price[min]='+str(cena_from) if cena_from != '' else ''
    html_cena_to='&price[max]='+str(cena_to) if cema_to != '' else ''
    html_currency='&currency='+cur
    html_page='&page='+str(page)
    html=(html+
          rent_room+
          html_cena_from+
          html_cena_to+
          html_currency+
          '#bounds[lb][lat]=53.812409559871966&bounds[lb][long]=27.34085083007813&bounds[rt][lat]=53.98355023169905&bounds[rt][long]=27.78305053710938'+
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

def pl_inf():
    return ['div', {'class':"apartment-bar__part apartment-bar__part_33 apartment-bar__part_right"}]

def info():
    return ['div',
            {'class':'apartment-info'}]

def info_ind_descr():
    return ['div',
            {'class':"apartment-info__cell apartment-info__cell_66"}]

def info_inf_cont():
    return ['div',
            {'class':"apartment-info__cell apartment-info__cell_33 apartment-info__cell_right"}]

def tel_info():
    return ['li',
            {'class':"apartment-info__item"}]

def time_info():
    return ['div',
            {'class':"apartment-info__sub-line apartment-info__sub-line_extended"}]

def name_info():
    return ['a']
                    
if __name__=='__main__':
    ScrableUrl(page=2)
