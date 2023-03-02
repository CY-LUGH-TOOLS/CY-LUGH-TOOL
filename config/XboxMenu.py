import os
os.system('clear')
print("""                                         ..':;::;;;;:;;;'..                                         
                                      .;;,,''''......'''',,,;'.                                     
                                   .;,,,'................''',,,:'.                                  
                                .;',,''......................'',,,:.                                
                              .,.,,,'...''',,'''.....'''','''...',,,;.                              
                             ,.,,,'..'',,,,,,,,,,'',,,,,,,,,,,,''.',,',                             
                            ,',,'.'',,,..      ......       ..',,,''',,,                            
                          .',,,''',,'.                         ..',,,',,..                          
                          ',,,',,''.                             .',,,,,,'.                         
                         '',,,,''..,co,.                    .,lo:. .,,,,,,.                         
                        ,.,,,,'..cOOOOOOOkkOd;.      .,lkkxOKKKKKKo..,',,,.'                        
                       ..,,,,,.,OOOOO00KKKKKKKKxlccokKKKKKKKKKKKKKKKo.'',,,..                       
                      ..,,,,,.cOOOOO0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKd ',,,,..                      
                      '',,,'.cOOOO0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKo ',,,'.                      
                     ,.,,,,..OOO00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOxx0KKK' ,,,,.'                     
                    '.,,,,. ;OOd'  .'lOKKKKKKKKKKKKKKKKKKKKKKOc.    cKKd .,,,,.'                    
                   ..,,,,'  lO:  .'..  .l0KKKKKKKKKKKKKKKKKk,  'coc. :K0  ',,,,..                   
                   '',,,,   xl l000O0x:.  c0KKKKKKKKKKKKKO;  :k0OOOOo xK   ,,,,,'                   
                  ,.,,,,.   0'kKOOOOOOOOd' .l0KKKKKKKKKO:  ,O0OOOOOOOd.K'  .',,,''                  
                 ,.,,,''.  ;kxK0OOOOOOOOOOo. .kKKKKKKKl  .x0O000KK00OOdxd   .'',,',                 
                ,.,,,''.   kOKK0000000OO000Ol,xKKKKKKKl,l0OOkkOOOOKKK000K.  ..',,,.'                
               '.,,,,'.   :O000KK0OKK0000O000OKKKKKKKKK0OOkOOO000OO0KK00Ko   ..,,,,.'               
              ..',,,.  ...OOOO0K0KWMNkkKK0K0K000KKKKK00OO0O0KkkXMMXOKKKKKK.. ...',,,..              
              '.,,'.  ...dOOO0KKkWMM'  .MWX0KK0OKKKKO0000KWM:   NMMOKKKKKKo.. ...',,'.              
             '.,,..   .. xOOOKKKKOKXOllkNXK00K0O0KKKO0KKOKXX0lcxNXO0KKKKK0;.  . ..',,.,             
            ..,,.. . ... xOOO0K0K,dK0000KKKKKK0kKKKKOKKKKKKK00000O.K0KKK0O'.....  .',,.'            
            .','.........lOOO0KK0;.KKKKKKKKKKK0kKKKKO0KKKKKKKKKKK,'00KKK0O,....    .,,'.            
           ,.,'.  ........OOOO0KKk lKKKKKKKKKKOOKKKKKOKKKKKKKKK0x dKKKK0Ok...... . ..,,..           
          ..,,.. .........lOOOO0KO dKKKKKKKKK0kKKKKKKOKKKKKKKKKKO xKKKKOO;...... ....',,..          
          .',,.. ..........xOOOOK: 0KKKKKKKKKOOKKKKKK00KKKKKKKKKK.'KKK0Oc.......... ..,,'.          
         ..,,,.. ..........'kOOO0 'KKKKKKKKK0OKKKKKKKK0KKKKKKKKKK; 0KKOl........... ..,''..         
         ..',,.. ...........:OOOx oKKKKKKKKK00KKKKKKKK0KKKKKKKKKKx oKOo...........  ..,''..         
         ..',,...............xOOo kKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK :0k,........... ...,,'..         
         ...,,,..............,OOo OKKKKKK0Kxk0KKKKKKKKKkx0K0KKKKKK :Ok...............,,,..          
          ...,,,...........  .kO0 'dkOOxdolcclO0KKKKK0d:clodxOOOd; OOd..............,,,...          
           ...,,,'.......... .k0Kx.           .'cloc,.            dKOo............',,,...           
            ...',,,'........ .x0KK0o,.. ....,;cloddolc:,'... ..,l0K0Ol...........',,'..             
              ...',,,'........:O0KKKKKKKKKOxddooooooooddxOKKKKKKKK0OO:.........',,'...              
               ....',,,........cO0KKKKKKKOooooddddddddooooOKKKKKK0OOo........,,,'...                
                  ...'',,.......:O0KKKKKK0KKK00000O000KKKK0KKKKK0Ok:.......,,''...                  
                    ...'','......,x0KKKKKKKK00000KKKKKKKKKKKKKK0Oo.......,,'....                    
                      ....',.......:k0KKKKKKKKKKKKKKKKKKKKKKK0Od,.....',''...                       
                        ....''.......lOKKKKKKKKKKKKKKKKKKKK0Ok;.....'''....                         
                           ...........'d0KKKKKKKKKKKKKKKK00k:.....''.....                           
                              ..........'lx00KKKKKKKKKKKOd:....'......                              
                                 ...........',:cllooolc;,.........                                  
                                     ..........................""")
#by
print('')
#sla
escolha = -1

#escolhas

while escolha < 1 or escolha > 99:
    escolha = int(input("""
\033[0;30;32m[ 1 ]\033[0;30;0m \033[0;30;31mgerar
\033[0;30;32m[ 2 ]\033[0;30;0m \033[0;30;31mvoltar ao menu
\033[0;30;32m[ 99 ]\033[0;30;0m \033[0;30;31msair\033[0;30;34m
Sua escolha: """))
    print(''' ''')
    print('')
    print('')
    
# escolha

if escolha == 1:
    exec(open('xboxGen.py', encoding="utf-8").read(), globals())

if escolha == 2:
    exec(open('CY-LUGH.py', encoding="utf-8").read(), globals())

if escolha == 99:
        print('\033[0;30;32m"Um soldado da tiros, um hacker da enter."')
        exit()
    
