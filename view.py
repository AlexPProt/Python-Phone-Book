import text

def show_menu()->int:
    for i,item in enumerate (text.main_menu) :
        if i:
            print ('\t' + f'{i}.{item}')
        else:
            print(item)
    select_option = input("Выберите пункт меню: ")
    while True:
            if select_option.isdigit() and 0<int(select_option)<(len(text.main_menu)-1):
                return int(select_option)
            select_option= input (text.main_menu_imput_error)