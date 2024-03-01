# def tratativa(**kwargs):
#     ti = kwargs['ti']
#     x = ti.xcom_pull(task_ids='webscraping')
#     x = x.replace('R$','').replace('.','').replace(',','.')
#     x = x.strip()
#     x = float(x)
#     return x
def transform_data(x):
    x = str(x).replace('R$','').replace('.','').replace(',','.').replace('(','').replace(')','').replace(' ','')
    x = x.strip()
    return x

def apply_transform(**kwargs):
    ti = kwargs['ti']
    lista = ti.xcom_pull(task_ids='webscraping')
    lista_new = [transform_data(x) for x in lista]
    print(lista_new)
    return lista_new