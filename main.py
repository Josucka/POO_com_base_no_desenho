from personagem import Personagem
from personagem1 import Personagem1
personagem = Personagem('robin', 'ravena', 'estelar', 'mutano', 'cyborg', 'todos')
personagem1 = Personagem1('fantasminha_ravena', 'fantasminha_estelar', 'fantasminha_mutano', 'fantasminha_cyborg', 'todos_fantasminha')
print('Bem vindo ao jogo de ficçao direcionada\nPra começarmos vamos apresentar os personagens')

while True:
  persona = int(input('''
        Escolha um personagem
        [ 1 ] Robin
        [ 2 ] Ravena
        [ 3 ] Estelar
        [ 4 ] Mutano
        [ 5 ] Cyborg
        -->
        '''))
  if persona == 1:
    print('Vamos começar\n')
    print(f'Voce começa jogando com {personagem.robin}')
    print('RAIVA')
    print(f'{personagem.ravena}: Alguem liga o ar-condicionado, ou eu vou suar em vc, vou suar em vc!!!\nPREGUIÇA\n{personagem.mutano}: Nossa maninho andar ate la vai demora um seculo!!!\nMELANCOLIA\n{personagem.estelar}:\nNois não temos o controle remoto;\n{personagem.cyborg}:\nO negocio e manual tem que usar as manuais!\nINRRITADO\n{personagem.mutano}:\nEu não vou usar minhas manuais pra nada!!!\nDESESPERO\nEstamos condenados a viver eternamente nesse sofrimento!!!\nMEDO\n{personagem.cyborg}:\nNão, Não!! Não eu nao aguento!! ALGUEM AJUDA; POR FAVOR ALGUEM AJUDA AQUI; Me ajuda!\nTILINTAR DE JANELA QUEBANDO\n{personagem.robin}:\nUm grito de ajuda! Onde esta o perigo;\n{personagem.mutano}:\nPor toda nossa volta, Maninho!!\nMANHOSA\n{personagem.estelar}:\nE muito grudento...\nINDIGUINADO\n{personagem.robin}:\nEstao falando da temperatura; é so ligar o ar condicionado\n{personagem.todos}:\nGRUNIDOS & RECLAMAÇÕES\nINDIGUINADO\n{personagem.robin}:\nE isso que a vida moderna fez com voces; Os deixou moles..;\n{personagem.robin}:\nHá algum tempo, não tinhamos essas conveniências modernas, Tudo era trabalho duro\nMais isso fez o povo duro e confiante em si mesmo...\n{personagem.robin}:\nEu acho que deveriamos fazer uma viagem!\nANIMADO\n{personagem.cyborg}:\nVIAGEM, Isso parece divertido\nDESANIMADOR\n{personagem.robin}:\nMais não é!! Essa viagem é pra ser educativa!\nEMPOLGADO\n{personagem.robin}:\nPara ensina-los alto suficiência sem conveniências em um ambiente moderno, eu os trouxe velha trilha que os nossos velhos pioneiros usaram pra desbravar uma nova vida para si mesmo. Bem Vindos a trilha de ORIGOM!\nDESCONFIADA\n{personagem.ravena}:\nEntao estamos em Origom;\nESPERTINHO\n{personagem.robin}:\nAinda não! São 2.000Km pra quele lado!!!\nINDIGUINADO\n{personagem.mutano}:\nVOCE Ficou Maluco;Isso vai demorar dias!\nABRE UM PORTAL\n{personagem.ravena}:\nEu encontro voces lá!\nELA GRITA SENDO PUXADA DE VOLTA PELO ROBIN\n{personagem.robin}:\nNão vai levar alguns dias!\n{personagem.todos}: GRUUFFs\n{personagem.robin}:\nVai levar Varios meses!!\nSARCASMO\nJa que os nossos velhos pioneiros não tinha carros ou portões magicos!!!\n{personagem.todos}:\nRECLAMACÕES\n{personagem.estelar}:\nINDIGUINADA\nISSO É UM ABSURDO!!!!!\n{personagem.robin}:\nSARCASMO\nAdoro o intusiasmo Titãns!!!\nANIMADO ELE APRESENTA\nIsto é um posto de comércio, onde nossa aventura educativa começa!\nAlguem gostaria de olhar em volta; S/N;')
    Gostaria = str(input('Voce Olha em volta; S/N')).upper()
    if Gostaria == 'S':
      print('Ei vc é o Robim Vamos Pra aventura Logo')
    else:
      print('Isso é coisa de Robin, Bora continuar...')
    print(f'{personagem.estelar}:\nO Robin, o que é que tava escrito ai;\n{personagem.robin}:\nINRRITADO\nESI ou ENE!!!! S quer dizer Sim, N que dizer Não...\n{personagem.ravena}:\nENTEDIADA\nporque não dizer so Sim ou Não;\n{personagem.robin}:\nPorque é mais rapido assim!\n{personagem.mutano}:\nSim e Não já são as palavras mais curta, Maninho!!\n{personagem.robin}:\nAgora são ainda mais curtas!!\nOlha em volta S/N;\n{personagem.todos}:\n -->N<--\n{personagem.robin}:\nDESCONFIADO\nEntao Não gostaria de olhar em volta desse posto de comercio historico; O lugar onde um carpinteiro de Ohaio ou um fazendeiro de Linoines começaram sua viagem;\n{personagem.todos}:\nN!!!\n{personagem.robin}:\nDesanimado, Táá!! Entao entrem na carroça!\nANTES DE ENTRAR NA CARROÇA\n{personagem.estelar}:\nENTUSIASMADICIMA VOA AO ENCONTRO DO BOI CARROÇEIRO E O PEGA NO COLO\nAHH!!! Que adoravel!!! Eu vou chamar vc de cabeça achatada i vc vai dormi no quarto na cama comigo!!!\n{personagem.robin}:\nNão se apegue!! Nois teremos que comer-lo quando a triha ficar difícil!{personagem.estelar}:\nTRISTE\nahh!! Eu entendo!!\n{personagem.robin}:\nENPOLGADO\nPÉ Na Estrada!!!\n{personagem.ravena}:\nNOJO\nEu num vou entrar nisso ai!!n\{personagem.robin}:\nPEGA E JOGA ELA NA CARROÇA\nVai sim!!!\n{personagem.mutano}:\nALEGRE\nEU QUERO UMA SHOTGUM\nBUFETADA NA CARA VINDA DO ROBIN\n{personagem.robin}:\nBoa ideia mutano!! \nNão sabemos que perigo podemos encontrar na estrada...\nJA NA ESTRADA\n{personagem.robin}:\nARREPENDIDO/QUERENDOcontinuar\nhãn estamos indo muito bem Titans, O clima esta bom nosso ritimo esta traquilo e estamos saldaveis!\nO MUTANO NÃO PARECE BEM\n{personagem.mutano}:\nGorfo de Vômito..... \n{personagem.ravena}:\nDESANIMO\nNem sempre saudaveis!\n{personagem.cyborg}:\nDESANIMO\nEu achei que esse negocio erra pra se educativo!;\n{personagem.estelar}:\nAte agora nossa viagem foi CHATA - TEDIOSA e REPETITIVA\n{personagem.robin}:\nENTUSIASTA\nVoce resumiu bem a trilha de Origom! Parece que alguem realmente aprendeu!!\n{personagem.mutano}:\nRAIVA\nEu ja to cansado de aprender, vamos pra casa Jogar uns Vídeo-Game!!!\nMUTANO CAI DA CARROÇA\n{personagem.estelar}:\nSUSTO\nMUTANO\nMUTANO GRITA DO LADO DE FORA DA CARROÇA\n{personagem.robin}:\nSEM NOÇAO\nMutano caiu da carroça e quebrou a perna voce gostaria de 1-Continuar na trilha\n{personagem.cyborg}:\nE porque a gente continuaria na trilha; A gente tem que concert......\n{personagem.robin}:\nDEIXA EU CONTINUAR!!!\n2-checar os suprimentos\n3-olhar no mapa...\n{personagem.mutano}:\nCHOROS&GRITOS\nAi minha perninha\n{personagem.estelar}:\nEle prescisa de um Medico!\n{personagem.robin}:\n4-mudar o ritimo\n5-mudar as razoes...\n{personagem.ravena}:\nNão prescisamos de nenhuma dessas opçoes numeradas, Prescisamos de uma ambulancia!\n{personagem.robin}:\nOs pioneiros não tinham Ambulancia, ElES TinHAM SETE OPÇOES NUMERADAS!!! ENTÃO LIDE COM Isso!\nAgora onde eu estava; Claro 6-Parar\n7-.....')
    escolha = int(input('''
    Escolha a opçao antes que o mutano morra!!!
    [ 1 ] Continuar na trilha
    [ 2 ] Checar os Suprimentos
    [ 3 ] Olhar o mapa
    [ 4 ] Mudar o ritimo
    [ 5 ] Mudar as Razões 
    [ 6 ] Parar
    [ 7 ] .....
    -->
    '''))
    if escolha == 1:
      print('Era tudo que eu queria!! Mas!!! ')
    elif escolha == 2:
      print('Depois, o chorão do mutano ta machucado')
    elif escolha == 3:
      print('Era uma boa hora!!')
    elif escolha == 4:
      print('Não perdia tempo neh!!!')
    elif escolha == 5:
      print('Podemos pensar em Razoes melhores pra colocar nas questoes Enumeradas...')
    elif escolha == 6:
      print('Tá Bom ja que vcs insistem! Vamos Parar')      
      print(f'{personagem.cyborg}:\nSEIS, Vamos escolher a 6!!')
      print(f' {personagem.robin}:\nVoces escolheram parar pra descansar')
      descansar = str(input('   S ou N:\n--> '))
      if descansar == 'S':
        print(f'{personagem.todos}:\nGRITAM\n--S--')
      else:
        print('Ah taBão estou cansado vamos parar mesmo!')
    elif escolha == 7:
      print('Mal educados, Nem deixaram eu termina de falar')
    elif escolha >= 8:
      print('opçao invalida')
    else:
      print('Coisa de Robin isso ai!')
    print(f'MUSIQUINHA....\n{personagem.estelar}:\nDÓ\nVoce sentira uma leve pressão\n{personagem.mutano}:\nGRITO\n{personagem.estelar}:\nFELIZ\nBem melhor!!!\n{personagem.mutano}:\nSATISFAÇAO\nMuito obrigado {personagem.estelar}!!\n{personagem.robin}:\nA historia esta realmente sendo vivida pelo mutano... Que compartilhar oque aprendeu ate agora;\n{personagem.mutano}:\nMANHA&CHOROS\nQuelo i pa casa!\n{personagem.robin}:\nMaravilhoso!! Ja perdemos tempo suficiente vamos: conte vamos[ 1 ] = continuar com a trilha\n{personagem.mutano}:\nCHOROSSO\nEu presciso discançaaaa... !!!{personagem.robin}:\nSARCASMO\nCom licença eu não escultei...\n{personagem.mutano}:\nDescança!\n{personagem.robin}:\nNão é assim que os pioneiros escolhiam....\n{personagem.mutano}:\nTa bom, Ta bom eu quero 6!!Por favor 6;!\n{personagem.robin}:\nDesculpe sera a Opçao 1 i se formos pegos pela neve do inverno podemos nao sobreviver.... \nSUSPENSE\nDE VOLTA A TRILHA{personagem.robin}:\no clima esta frio a saude..;.. olhadinha nos companheiros.... Esta Boa! Ritimo; Constante\n{personagem.cyborg}:\nEssa é a pior experiência da minha vida!\n{personagem.robin}:\nQue bom ouvir isso {personagem.cyborg} parece que realmente se colocou no lugar dos pioneiros!! A proposito um ladrão robou seus sapatos...\n{personagem.cyborg}:\nPo cara eu vou ficar com bolhas\n{personagem.ravena}:\nEstamos com fome {personagem.robin}!!\nSUCULENCIA\n{personagem.estelar}:\nISSO!! agora o cabeça achatada esta começando a parecer delicioso!!! :p \n MUUUUuuuu \n{personagem.robin}:\nOpçao 4-Vamos checar os suprimentos..')
    escolha = int(input('''Vocer quer checar as provisoes; 
    [ 4 ] Checar as Provisões
    [ 5 ] Seguir em frente sem perde tempo
    '''))
    if escolha == 4:
      print('...SURPRESO... Robin diz: Huumm acabou as provisões')
    else:
      print('Voce nao viu que tinha ratos  e as provisões acabou!')
    print(f'{personagem.estelar}:\nVamos comer o delicioso cabeÇA achAtAdA!!\n{personagem.robin}:\nAinda não, prescisamos dele pra puxar a carroça!\n{personagem.estelar}:\nMuito Bem... Voce esta seguro por enquanto.... Me Aguarde!!\nBEIJINHONOBOI\n{personagem.robin}:\nTitans, quando acaba a comida so resta uma opçao.\n{personagem.ravena}:\nPedir uma Pizza\n{personagem.robin}:\nTIRASEUCELULARMAGICO\nSem PizzA!!!\nNos Vamos caçar... \nAqui atira num daqueles Bufalos...\n{personagem.mutano}: Recebe a SHOTGUM\n{personagem.mutano}:\nNão mesmo maninho, eu sou Vegetariano...\n{personagem.robin}:\nEssa é a trilha de Origom, ou voce come carne ou vc morre!!!\n{personagem.mutano}:\nSe todos começem legumes meus amigos bufalos nao vao prescisar se machucar....')
    comando = int(input('''
    Oque vc pretende fazer;
    [ 1 ] Seguir o conselho do mutano
    [ 2 ] Seguir seus proprios conselhos
    '''))
    if comando == 1:
      print('Ate parece que eu vou seguir conselho do mutano')
      cacar = int(input('''
    Oque vc vai fazer;
    [ 1 ] Caçar so o de comer
    [ 2 ] Matar todos os animais que ver pelafrente
    '''))
      if cacar == 1:
        print('Ate parece vou faer o limpa\nBANG\nBANG\nBANG ')
      else:
        print('Isso vamos caçar\nBANG BANG\nBANG BANG BANG\nBANG BANG BANG BANG')
    else:
      print(f'{personagem.robin}:\nATIRA atira atira, RA eu to ti vendo atras da pedra, Ra Bufalo, Esquilo, pra onde vc vai... Cervo... diga ola pro meu amiguinho... agora é com vc coelho... rarrararar balança o rabo esquilo essearbusto nao vai te salva hahahaha')
    print(f'{personagem.estelar}: Haaiimm!!! essa comida é mais que suficiente pro resto da viagem toda...\n{personagem.robin}: HUM!! Uma pena, porque ao da pra levar 45Kg\n{personagem.ravena}:\nEntao porque vc atirou em todos eles;\n{personagem.robin}:\nSINCERIDA\nPor é a unica coisa divertida nessa viagem Chata podem Divertida!!\n{personagem.todos}:\nHUMmm!!! NHAk NhaK nHAk !!! \n{personagem.cyborg}:\nUm que coisa maravilhosa!!!\n{personagem.robin}:\nTitans eu tenho Más noticias e Má noticias!! Primeira má noticia - O mutano foi picado por uma serpente\n{personagem.mutano}:\nSUSTO\nÉ u q; .....VIU A COBRA E GRITA.... Eu não consigo sentir minha mão Ta toda inchada..\n{personagem.robin}:\nAgora má noticia!! O mutano tem Desinteria!!!{personagem.mutano}:\nOque é Isso;\n{personagem.ravena}:\nFazer coco ate morrer!!! ....MORDIDA NO PEDAÇO DE CARNE...\n{personagem.mutano}: OOh OU!! ...PULO ATRAS DO ARBUSTO....\n{personagem.robin}: Enguanto isso querem olhar em Volta; S/N; \n{personagem.estelar}: Nao deveriamos ajuda-lo;\n{personagem.robin}: Ah, Desculpa. essa nao é uma questao nao lista!!!\nMUTANO MORREU.\n{personagem.estelar}: Voce nao disse que pessoas iam morrer!!\n{personagem.robin}: E isso aconte na trilha de Origom.. é super chato, voce caça, Todo mundo no grupo tem uma morte Orrivel...\n{personagem.ravena}: E quanto ao aprendizado;\n{personagem.robin}: Voces aprenderao que vao morrer!!\n{personagem.cyborg} CHOROSO: Ahh! Ainda nao acredito que o meu amigo {personagem.mutano} MORREU!!! \n{personagem1.mutano}: E isso ai!!! eu Morri!!\n{personagem.ravena} ASSUSTADA: Anhh, vc é uma fantasma!!!\n\n{personagem.cyborg}: É é, mano vc ta bem;\n{personagem1.mutano}: Oh Mano eu to otimo Olha só!! ... DANCINHA...\n{personagem.ravena} TRISTONHA: Ahh!! cara eu queria ser um fantasma!!\n{personagem1.mutano}: E so voce pegar uma Desinteria.. Gatinhhaa!!!\nE a proposito Meus amigos não estao felizes contigo!!! ....ROBIN VE FANTASMAS DOS ANIMAIS....\nDevolta a trilhA\n{personagem.robin}: Esse Vento, O ritimo esta lento.. E a saude... Fraca...\n{personagem.todos}: GRUNIDOS DE FRIO\n{personagem.robin}: {personagem.estelar} Morreu!!!\n{personagem.cyborg}: Gritos de dessespero e choro... Ah {personagem.estelar} Não!!! \n{personagem1.mutano} & {personagem1.mutano} Faz festa no lado de fora da carroça!!!\n{personagem.robin}: Ignorem os Fantasmas.... Apenas foquem em aprender as dificuldades dos pioneiros...\n{personagem1.mutano}: Mano, quando se é um fantasma vc nao prescisa aprender mais nada!! KkKkKkKkKk\nMUSICA\nAh {personagem.ravena} pegou sarampo e morreu\no {personagem.cyborg} se molhou e se doeu, pegou um resfriado e\nVirou presunto\nsem comida pra comer {personagem.robin} fez um churasco e por semanas ficou alimentado, e viu que a vida nao facil\nNA TRILHA DE Origom!\nA vida Nao e facil na trilha de Origom, Nao e nada facil na trilha de Origom\n{personagem1.todos}: ...FESTA NO IATE FANTASMA...\n{personagem.robin}: Eu to aprendendo muito!! ....ESTAA COONGEELANTTE...\nCansado : Eu cheguei ao Rio Deyse!')
    olhar = str(input('''
    Eu gostaria de Olhar em volta?
    [ S ] ou [ N ]
    -->
    '''))
    if olhar == 'S':
      print('S, concerteza!!! ')
      print('VISTA PANORAMICA')
    else:
      print('com certeza eu vou olhar em volta')
      print('VISTA PANORAMICA')
    print(f'{personagem1.mutano}: Como esta o lace de olhar em volta, Mano?\n{personagem.robin}: Otimo! Agora eu so tenho que levar a carroca ate o outro lado do rio vou estar em Origom! Alem de cacar essa e a unica parte divertida da trilha de Origom!\n{personagem1.ravena}: Mais divertida que nossa festa fantasma??\n{personagem1.mutano}: Huuhulll, Olha so esses fantasmas... HaHaHaHa.. Desiste logo mano esse iate ta bombando... SOBE ABORDO!!!')
    atravessia = int(input('''
    Oque vc Fas? 
    [ 1 ] Abandona e sobe no barco?  
    [ 2 ] Voce atravessa o rio a nado?  
    [ 3 ] Voce entra no rio com a carroca? 
    -->'''))
    if atravessia == 1:
      print('NUNCA')
      print('E o Robin, se joga no rio com a carroca')
    elif atravessia == 2:
      print('NUNCA')
      print('Tambem nao vou atravesar a nado, e se joga no rio com a carroca')
    elif atravessia == 3:
      print(f'NUNCA!! \n{personagem.robin}: Eu vou seguir essa trilha ate o final, e nao tem nada que possam fazer pra me impedir!')
      print('A festa no iate continua...')
    elif atravessia >= 4:
      print('Ops!! Opcao invalida')
    else:
      print('Ops!! Opcao invalida')
    print(f'{personagem.robin}: Parece que esta seguro por aqui!!\n AAAAhh!! \nCAI DE UMA CACHOEIRA\nNA CORRENEZA FORTE BATE NAS PEDRAS\nCARROCA ESPEDACA E TE JOGA NA MARGEM\n{personagem.robin} FRACO&ESBAFORIDO: Parabens!!! eu cheguei em Origom!!\n{personagem1.mutano} ORGULHOSO: Bom Trabalho, mano!!!!\n{personagem1.estelar}: Me diz, Oque vc aprendeu com essa nossa jornada?')
    pergunta = str(input('Diga sua resposta -- >: '))
    if pergunta == 'desinteria':
      print(pergunta)
    else:
      print(f'{personagem.robin}: Que o Robin tem Desinteria!!!')
      print('FIM')  
      break
  elif persona == 2:
    print('Vamos começar\n')
    print(f'Voce começa jogando com {personagem.ravena}')
    print('RAIVA')
    print(f'{personagem.ravena}: Alguem liga o ar-condicionado, ou eu vou suar em vc, vou suar em vc!!!\nPREGUIÇA\n{personagem.mutano}: Nossa maninho andar ate la vai demora um seculo!!!\nMELANCOLIA\n{personagem.estelar}: Nois não temos o controle remoto;\n{personagem.cyborg}: O negocio e manual tem que usar as manuais!\nINRRITADO\n{personagem.mutano}: Eu não vou usar minhas manuais pra nada!!!...DESESPERO..Estamos condenados a viver eternamente nesse sofrimento!!!\nMEDO\n{personagem.cyborg}: Não, Não!! Não eu nao aguento!! ALGUEM AJUDA; POR FAVOR ALGUEM AJUDA AQUI; Me ajuda!\nTILINTAR DE JANELA QUEBANDO\n{personagem.robin}: Um grito de ajuda! Onde esta o perigo;\n{personagem.mutano}: Por toda nossa volta, Maninho!!\nMANHOSA\n{personagem.estelar}: E muito grudento...\nINDIGUINADO\n{personagem.robin}: Estao falando da temperatura; é so ligar o ar condicionado\n{personagem.todos}: GRUNIDOS & RECLAMAÇÕES\nINDIGUINADO\n{personagem.robin}: E isso que a vida moderna fez com voces; Os deixou moles..;\n{personagem.robin}: Há algum tempo, não tinhamos essas conveniências modernas, Tudo era trabalho duro\nMais isso fez o povo duro e confiante em si mesmo...\n{personagem.robin}: Eu acho que deveriamos fazer uma viagem!\nANIMADO\n{personagem.cyborg}: VIAGEM, Isso parece divertido\nDESANIMADOR\n{personagem.robin}: Mais não é!! Essa viagem é pra ser educativa!\nEMPOLGADO\n{personagem.robin}: Para ensina-los alto suficiência sem conveniências em um ambiente moderno, eu os trouxe velha trilha que os nossos velhos pioneiros usaram pra desbravar uma nova vida para si mesmo. Bem Vindos a trilha de ORIGOM!\n{personagem.ravena}: DESCONFIADA :Entao estamos em Origom;\nESPERTINHO\n{personagem.robin}: Ainda não! São 2.000Km pra quele lado!!!\nINDIGUINADO\n{personagem.mutano}: VOCE Ficou Maluco;Isso vai demorar dias!')
    print(f'{personagem.ravena}: Eu encontro voces lá!')
    Rave = str(input('''
    A ravena é uma especie Demoniaca oque faria nesse casso;
    [ 1 ] Abre um portal pra fugir do Robin
    [ 2 ] Abre um portal pra chegar mais rapido em Origom
    -->
    '''))
    if Rave == 1:
      print('ELA GRITA SENDO PUXADA DE VOLTA PELO ROBIN')
    else:
      print('ELA GRITA SENDO PUXADA DE VOLTA PELO ROBIN')
    print(f'{personagem.robin}: Não vai levar alguns dias!\n{personagem.todos}: GRUUFFs\n{personagem.robin}: Vai levar Varios meses!! : SARCASMO : Ja que os nossos velhos pioneiros não tinha carros ou portões magicos!!!\n{personagem.todos}: RECLAMACÕES\n{personagem.estelar}: INDIGUINADA : ISSO É UM ABSURDO!!!!!\n{personagem.robin}: SARCASMO : Adoro o intusiasmo Titãns!!!\nANIMADO ELE APRESENTA : Isto é um posto de comércio, onde nossa aventura educativa começa!\nAlguem gostaria de olhar em volta; S/N;')
    Gostaria = str(input('Voce Olha em volta; S/N')).upper()
    if Gostaria == 'S':
      print('A Ravena nunca concordaria com o Robin')
    else:
      print('Isso é coisa de Robin, Bora continuar...')
    print(f'{personagem.estelar}: O Robin, o que é que tava escrito ai;\n{personagem.robin}: INRRITADO : ESI ou ENE!!!! S quer dizer Sim, N que dizer Não...\n{personagem.ravena}: ENTEDIADA : porque não dizer so Sim ou Não;\n{personagem.robin}: Porque é mais rapido assim!\n{personagem.mutano}: Sim e Não já são as palavras mais curta, Maninho!!\n{personagem.robin}: Agora são ainda mais curtas!! : Olha em volta S/N;\n{personagem.todos}:  -->N<--\n{personagem.robin}: DESCONFIADO : Entao Não gostaria de olhar em volta desse posto de comercio historico; O lugar onde um carpinteiro de Ohaio ou um fazendeiro de Linoines começaram sua viagem;\n{personagem.todos}: N!!!\n{personagem.robin}: Desanimado, Táá!! Entao entrem na carroça!\nANTES DE ENTRAR NA CARROÇA\n{personagem.estelar}: ENTUSIASMADICIMA : VOA AO ENCONTRO DO BOI CARROÇEIRO E O PEGA NO COLO\nAHH!!! Que adoravel!!! Eu vou chamar vc de cabeça achatada i vc vai dormi no quarto na cama comigo!!!\n{personagem.robin}: Não se apegue!! Nois teremos que comer-lo quando a triha ficar difícil!{personagem.estelar}: TRISTE : ahh!! Eu entendo!!\n{personagem.robin}: ENPOLGADO : PÉ Na Estrada!!!\n{personagem.ravena}: NOJO : Eu num vou entrar nisso ai!!\n{personagem.robin}: PEGA E JOGA ELA NA CARROÇA : Vai sim!!!\n{personagem.mutano}: ALEGRE : EU QUERO UMA SHOTGUM : BUFETADA NA CARA VINDA DO ROBIN\n{personagem.robin}: Boa ideia mutano!! Não sabemos que perigo podemos encontrar na estrada...\nJA NA ESTRADA\n{personagem.robin}: ARREPENDIDO/QUERENDOcontinuar : hãn estamos indo muito bem Titans, O clima esta bom nosso ritimo esta traquilo e estamos saldaveis!\nO MUTANO NÃO PARECE BEM\n{personagem.mutano}: Gorfo de Vômito..... \n{personagem.ravena}: DESANIMO : Nem sempre saudaveis!\n{personagem.cyborg}: DESANIMO : Eu achei que esse negocio erra pra se educativo!;\n{personagem.estelar}: Ate agora nossa viagem foi CHATA - TEDIOSA e REPETITIVA\n{personagem.robin}: ENTUSIASTA : Voce resumiu bem a trilha de Origom! Parece que alguem realmente aprendeu!!\n{personagem.mutano}: RAIVA : Eu ja to cansado de aprender, vamos pra casa Jogar uns Vídeo-Game!!!\nMUTANO CAI DA CARROÇA\n{personagem.estelar}: SUSTO : MUTANO... MUTANO... \nGRITOS DO LADO DE FORA DA CARROÇA\n{personagem.robin}: SEM NOÇAO : Mutano caiu da carroça e quebrou a perna voce gostaria de 1-Continuar na trilha\n{personagem.cyborg}: E porque a gente continuaria na trilha; A gente tem que concert......\n{personagem.robin}: DEIXA EU CONTINUAR!!! 2-checar os suprimentos\n3-olhar no mapa...\n{personagem.mutano}: CHOROS&GRITOS : Ai minha perninha\n{personagem.estelar}: Ele prescisa de um Medico!\n{personagem.robin}: 4-mudar o ritimo\n5-mudar as razoes...\n{personagem.ravena}: Não prescisamos de nenhuma dessas opçoes numeradas, Prescisamos de uma ambulancia!\n{personagem.robin}: Os pioneiros não tinham Ambulancia, ElES TinHAM SETE OPÇOES NUMERADAS!!! ENTÃO LIDE COM Isso! Agora onde eu estava; Claro 6-Parar\n7-.....')
    escolha = int(input('''
    Escolha a opçao antes que o mutano morra!!!
    [ 1 ] Continuar na trilha
    [ 2 ] Checar os Suprimentos
    [ 3 ] Olhar o mapa
    [ 4 ] Mudar o ritimo
    [ 5 ] Mudar as Razões 
    [ 6 ] Parar
    [ 7 ] .....
    -->
    '''))
    if escolha == 1:
      print('Voce é doido!!! o mutano caiu da carroça ')
    elif escolha == 2:
      print('Depois, o mutano ta machucado')
    elif escolha == 3:
      print('o se for pra saber se tem algum hopital aqui perto!!')
    elif escolha == 4:
      print('Não!!!')
    elif escolha == 5:
      print('Podemos pensar em Razoes melhores pra colocar nas questoes Enumeradas... Tipo PARAAAR')
    elif escolha == 6:
      print('Vamos Parar')      
      print(f'{personagem.cyborg}: SEIS, Vamos escolher a 6!!')
      print(f' {personagem.robin}: Voces escolheram parar pra descansar')
      descansar = str(input('   S ou N:\n--> '))
      if descansar == 'S':
        print(f'{personagem.todos}: GRITAM : -->S<--')
      else:
        print('que sem noçao!')
    elif escolha == 7:
      print('Tinha que ser a opcao 6, Vamos parar!')
    elif escolha >= 8:
      print('opçao invalida')
    else:
      print('Coisa de Robin isso ai!')
    print(f'MUSIQUINHA....\n{personagem.estelar}: DÓ : Voce sentirá uma leve pressão\n{personagem.mutano}: GRITA\n{personagem.estelar}: FELIZ : Bem melhor!!!\n{personagem.mutano}: SATISFAÇAO : Muito obrigado {personagem.estelar}!!\n{personagem.robin}: A historia esta realmente sendo vivida pelo mutano... Que compartilhar oque aprendeu ate agora;\n{personagem.mutano}: MANHA&CHOROS : Quelo i pa casa!\n{personagem.robin}: Maravilhoso!! Ja perdemos tempo suficiente vamos: conte vamos[ 1 ] = continuar com a trilha\n{personagem.mutano}: CHOROSSO : Eu presciso discançaaaa... !!!{personagem.robin}: SARCASMO : Com licença eu não escultei...\n{personagem.mutano}: Descançar!\n{personagem.robin}: Não é assim que os pioneiros escolhiam....\n{personagem.mutano}: Ta bom, Ta bom eu quero 6!!Por favor 6;!\n{personagem.robin}: Desculpe sera a Opçao 1 i se formos pegos pela neve do inverno podemos nao sobreviver.... \nSUSPENSE\nDE VOLTA A TRILHA{personagem.robin}: O clima esta frio a saude..;.. olhadinha nos companheiros.... Esta Boa! Ritimo; Constante\n{personagem.cyborg}: Essa é a pior experiência da minha vida!\n{personagem.robin}: Que bom ouvir isso {personagem.cyborg} parece que realmente se colocou no lugar dos pioneiros!! A proposito um ladrão robou seus sapatos...\n{personagem.cyborg}: Po cara eu vou ficar com bolhas\n{personagem.ravena}: Estamos com fome {personagem.robin}!!\n{personagem.estelar}: SUCULENCIA : ISSO!! agora o cabeça achatada esta começando a parecer delicioso!!! :p \n MUUUUuuuu \n{personagem.robin}: Opçao 4-Vamos checar os suprimentos..')
    escolha = int(input('''O Robin checar as provisoes; 
    [ 4 ] Checar as Provisões
    [ 5 ] Seguir em frente sem perde tempo
    '''))
    if escolha == 4:
      print('...SURPRESO... Robin diz: Huumm acabou as provisões')
    else:
      print('Voce nao viu que tinha ratos  e as provisões acabou!')
    print(f'{personagem.estelar}: MALDADE : Vamos comer o delicioso cabeÇA achAtAdA!!\n{personagem.robin}: Ainda não, prescisamos dele pra puxar a carroça!\n{personagem.estelar}: Muito Bem... Voce esta seguro por enquanto.... Me Aguarde!!\nBEIJINHONOBOI\n{personagem.robin}: Titans, quando acaba a comida so resta uma opçao.\n{personagem.ravena}: Pedir uma Pizza!!')
    comida = int(input('''
    Voce ta com fome oque fazer:
    [ 1 ] Criar um celular com sua magia
    [ 2 ] Nao fazer nada
    -->
    '''))
    if comida == 2:
      print('Nao to afim de nada mesmo!')
    else:
      print('O ROBIN TIRA SEU CELULAR MAGICO E JOGA PRA FORA DA CARROÇA')
    print(f'{personagem.robin}: Sem PizzA!!! Nos Vamos caçar... Aqui atira num daqueles Bufalos...\n{personagem.mutano}: Recebe a SHOTGUM\n{personagem.mutano}: Não mesmo maninho, voce se esqueceu eu sou Vegetariano...\n{personagem.robin}: Essa é a trilha de Origom, ou voce come carne ou vc morre!!!\n{personagem.mutano}: Se todos começem legumes meus amigos bufalos nao vao prescisar se machucar....')
    print(f'{personagem.robin}: entao me da isso eu vou caçar\nBANG BANG\nBANG BANG BANG\nBANG BANG BANG BANG')
    print(f'{personagem.robin}: ATIRA atira atira, RA eu to ti vendo atras da pedra, Ra Bufalo, Esquilo, pra onde vc vai... Cervo... diga ola pro meu amiguinho... agora é com vc coelho... rarrararar balança o rabo esquilo essearbusto nao vai te salva hahahaha')
    print(f'{personagem.estelar}: Haaiimm!!! essa comida é mais que suficiente pro resto da viagem toda...\n{personagem.robin}: HUM!! Uma pena, porque ao da pra levar 45Kg\n{personagem.ravena}: Entao porque vc atirou em todos eles;\n{personagem.robin}: SINCERIDA : Por é a unica coisa divertida nessa viagem Chata podem Divertida!!\n{personagem.todos}: HUMmm!!! NHAk NhaK nHAk !!! \n{personagem.cyborg}: Um que coisa maravilhosa!!!\n{personagem.robin}: Titans eu tenho Más noticias e Má noticias!! Primeira má noticia - O mutano foi picado por uma serpente\n{personagem.mutano}: SUSTO : É u q; .....VIU A COBRA E GRITA.... Eu não consigo sentir minha mão Ta toda inchada..\n{personagem.robin}: Agora má noticia!! O mutano tem Desinteria!!!{personagem.mutano}: Oque é Isso;\n{personagem.ravena}: Fazer coco ate morrer!!! ....MORDIDA NO PEDAÇO DE CARNE...\n{personagem.mutano}: OOh OU!! ...PULO ATRAS DO ARBUSTO....\n{personagem.robin}: Enguanto isso querem olhar em Volta; S/N; \n{personagem.estelar}: Nao deveriamos ajuda-lo;\n{personagem.robin}: Ah, Desculpa. essa nao é uma questao nao lista!!!\nMUTANO MORREU.\n{personagem.estelar}: Voce nao disse que pessoas iam morrer!!\n{personagem.robin}: E isso aconte na trilha de Origom.. é super chato, voce caça, Todo mundo no grupo tem uma morte Orrivel...\n{personagem.ravena}: E quanto ao aprendizado;\n{personagem.robin}: Voces aprenderao que vao morrer!!\n{personagem.cyborg} CHOROSO: Ahh! Ainda nao acredito que o meu amigo {personagem.mutano} MORREU!!! \n{personagem1.mutano}: E isso ai!!! eu Morri!!\n{personagem.ravena} ASSUSTADA: Anhh, vc é uma fantasma!!!\n{personagem.cyborg}: É é, mano vc ta bem;\n{personagem1.mutano}: Oh Mano eu to otimo Olha só!! ... DANCINHA...\n{personagem.ravena} TRISTONHA: Ahh!! cara eu queria ser um fantasma!!\n{personagem1.mutano}: E so voce pegar uma Desinteria.. Gatinhhaa!!!\nE a proposito Meus amigos não estao felizes contigo!!! ....ROBIN VE FANTASMAS DOS ANIMAIS....\nDevolta a trilhA\n{personagem.robin}: Esse Vento, O ritimo esta lento.. E a saude... Fraca...\n{personagem.todos}: GRUNIDOS DE FRIO\n{personagem.robin}: {personagem.estelar} Morreu!!!\n{personagem.cyborg}: Gritos de dessespero e choro... Ah {personagem.estelar} Não!!! \n{personagem1.estelar} & {personagem1.mutano} Faz festa no lado de fora da carroça!!!\n{personagem.robin}: Ignorem os Fantasmas.... Apenas foquem em aprender as dificuldades dos pioneiros...\n{personagem1.mutano}: Mano, quando se é um fantasma vc nao prescisa aprender mais nada!! KkKkKkKkKk\nMUSICA\nAh {personagem.ravena} pegou sarampo e morreu\no {personagem.cyborg} se molhou e se doeu, pegou um resfriado e\nVirou presunto\nsem comida pra comer {personagem.robin} fez um churasco e por semanas ficou alimentado, e viu que a vida nao facil\nNA TRILHA DE Origom!\nA vida Nao e facil na trilha de Origom, Nao e nada facil na trilha de Origom\n{personagem1.todos}: ...FESTA NO IATE FANTASMA...\n{personagem.robin}: Eu to aprendendo muito!! ....ESTAA COONGEELANTTE...\nCansado : Eu cheguei ao Rio Deyse!')
    print(f'{personagem.robin}: Eu gostaria de Olhar em volta? [ S ] ou [ N ] : S concerteza!!!\nVISTA PANORAMICA\n{personagem1.mutano}: Como esta o lace de olhar em volta, Mano?\n{personagem.robin}: Otimo! Agora eu so tenho que levar a carroca ate o outro lado do rio vou estar em Origom! Alem de cacar essa e a unica parte divertida da trilha de Origom!\n{personagem1.ravena}: Mais divertida que nossa festa fantasma??\n{personagem1.mutano}: Huuhulll, Olha so esses fantasmas... HaHaHaHa.. Desiste logo mano esse iate ta bombando... SOBE ABORDO!!!\n{personagem.robin}: NUNCA!!!!! Eu vou seguir essa trilha ate o final, e nao tem nada que possam fazer pra me impedir!\nA festa no iate continua...\n{personagem.robin}: Parece que esta seguro por aqui!!\n AAAAhh!! \nCAI DE UMA CACHOEIRA\nNA CORRENEZA FORTE BATE NAS PEDRAS\nCARROCA ESPEDACA E TE JOGA NA MARGEM\n{personagem.robin}: FRACO&ESBAFORIDO : Parabens!!! eu cheguei em Origom!!\n{personagem1.mutano}: ORGULHOSO : Bom Trabalho, mano!!!!\n{personagem1.estelar}: Me diz, Oque vc aprendeu com essa nossa jornada?')
    pergunta = str(input('''
    Diga sua resposta 
    -- >: '''))
    if pergunta == 'desinteria':
      print(pergunta)
    else:
      print(f'{personagem.robin}: Que o Robin tem Desinteria!!!')
      print('FIM')  
      break
  elif persona == 3:
    print('Vamos começar\n')
    print(f'Voce começa jogando com {personagem.estelar}')
    print('RAIVA')
    print(f'{personagem.ravena}: Alguem liga o ar-condicionado, ou eu vou suar em vc, vou suar em vc!!!\nPREGUIÇA\n{personagem.mutano}: Nossa maninho andar ate la vai demora um seculo!!!\nMELANCOLIA\n{personagem.estelar}: Nois não temos o controle remoto;\n{personagem.cyborg}: O negocio e manual tem que usar as manuais!\nINRRITADO\n{personagem.mutano}: Eu não vou usar minhas manuais pra nada!!!...DESESPERO..Estamos condenados a viver eternamente nesse sofrimento!!!\nMEDO\n{personagem.cyborg}: Não, Não!! Não eu nao aguento!! ALGUEM AJUDA; POR FAVOR ALGUEM AJUDA AQUI; Me ajuda!\nTILINTAR DE JANELA QUEBANDO\n{personagem.robin}: Um grito de ajuda! Onde esta o perigo;\n{personagem.mutano}: Por toda nossa volta, Maninho!!\nMANHOSA\n{personagem.estelar}: E muito grudento...\nINDIGUINADO\n{personagem.robin}: Estao falando da temperatura; é so ligar o ar condicionado\n{personagem.todos}: GRUNIDOS & RECLAMAÇÕES\nINDIGUINADO\n{personagem.robin}: E isso que a vida moderna fez com voces; Os deixou moles..;\n{personagem.robin}: Há algum tempo, não tinhamos essas conveniências modernas, Tudo era trabalho duro\nMais isso fez o povo duro e confiante em si mesmo...\n{personagem.robin}: Eu acho que deveriamos fazer uma viagem!\nANIMADO\n{personagem.cyborg}: VIAGEM, Isso parece divertido\nDESANIMADOR\n{personagem.robin}: Mais não é!! Essa viagem é pra ser educativa!\nEMPOLGADO\n{personagem.robin}: Para ensina-los alto suficiência sem conveniências em um ambiente moderno, eu os trouxe velha trilha que os nossos velhos pioneiros usaram pra desbravar uma nova vida para si mesmo. Bem Vindos a trilha de ORIGOM!\n{personagem.ravena}: DESCONFIADA :Entao estamos em Origom;\nESPERTINHO\n{personagem.robin}: Ainda não! São 2.000Km pra quele lado!!!\nINDIGUINADO\n{personagem.mutano}: VOCE Ficou Maluco;Isso vai demorar dias!{personagem.ravena}: Eu encontro voces lá!...\nAbre-se um portal e ela atravessa....MAS ELA GRITA SENDO PUXADA DE VOLTA PELO ROBIN{personagem.robin}: Não vai levar alguns dias!\n{personagem.todos}: GRUUFFs\n{personagem.robin}: Vai levar Varios meses!! : SARCASMO : Ja que os nossos velhos pioneiros não tinha carros ou portões magicos!!!\n{personagem.todos}: RECLAMACÕES\n{personagem.estelar}: INDIGUINADA : ISSO É UM ABSURDO!!!!!\n{personagem.robin}: SARCASMO : Adoro o intusiasmo Titãns!!!\nANIMADO ELE APRESENTA : Isto é um posto de comércio, onde nossa aventura educativa começa!\nAlguem gostaria de olhar em volta; S/N;\n{personagem.estelar}: O Robin, o que é que tava escrito ai;\n{personagem.robin}: INRRITADO : ESI ou ENE!!!! S quer dizer Sim, N que dizer Não...\n{personagem.ravena}: ENTEDIADA : porque não dizer so Sim ou Não;\n{personagem.robin}: Porque é mais rapido assim!\n{personagem.mutano}: Sim e Não já são as palavras mais curta, Maninho!!\n{personagem.robin}: Agora são ainda mais curtas!! : Olha em volta S/N;')
    Gostaria = str(input('Voce Olha em volta; S/N')).upper()
    if Gostaria == 'S':
      print('Eu quero N!')
    else:
      print('Isso é coisa de Robin, Bora continuar...')
    print(f'{personagem.todos}:  -->N<--\n{personagem.robin}: DESCONFIADO : Entao Não gostaria de olhar em volta desse posto de comercio historico; O lugar onde um carpinteiro de Ohaio ou um fazendeiro de Linoines começaram sua viagem;\n{personagem.todos}: N!!!\n{personagem.robin}: Desanimado, Táá!! Entao entrem na carroça!\nANTES DE ENTRAR NA CARROÇA\n{personagem.estelar}: ')
    estelar = int(input('''
    ENTUSIASMADICIMA : VOA AO ENCONTRO DO BOI CARROÇEIRO... Ela faz:
    [ 1 ] Monta no boi
    [ 2 ] Beija o boi
    [ 3 ] Pega o Boi no colo
    -->  
    '''))
    if estelar == 1:
      print('Que adoravel!!! Eu vou chamar vc de cabeça achatada i vc vai dormi no quarto na cama comigo!!!')
    elif estelar == 2:
      print('Que adoravel!!! Eu vou chamar vc de cabeça achatada i vc vai dormi no quarto na cama comigo!!!')
    elif estelar == 3:
      print('ELA PEGA O BOI NO COLO....Que adoravel!!! Eu vou chamar vc de cabeça achatada i vc vai dormi no quarto na cama comigo!!!')
    else:
      print('Eu queria pegar ele no colo...')
    print(f'{personagem.robin}: Não se apegue!! Nois teremos que comer-lo quando a triha ficar difícil!{personagem.estelar}: TRISTE : ahh!! Eu entendo!!\n{personagem.robin}: ENPOLGADO : PÉ Na Estrada!!!\n{personagem.ravena}: NOJO : Eu num vou entrar nisso ai!!\n{personagem.robin}: PEGA E JOGA ELA NA CARROÇA : Vai sim!!!\n{personagem.mutano}: ALEGRE : EU QUERO UMA SHOTGUM : BUFETADA NA CARA VINDA DO ROBIN\n{personagem.robin}: Boa ideia mutano!! Não sabemos que perigo podemos encontrar na estrada...\nJA NA ESTRADA\n{personagem.robin}: ARREPENDIDO/QUERENDOcontinuar : hãn estamos indo muito bem Titans, O clima esta bom nosso ritimo esta traquilo e estamos saldaveis!\nO MUTANO NÃO PARECE BEM\n{personagem.mutano}: Gorfo de Vômito..... \n{personagem.ravena}: DESANIMO : Nem sempre saudaveis!\n{personagem.cyborg}: DESANIMO : Eu achei que esse negocio erra pra se educativo!;\n{personagem.estelar}: Ate agora nossa viagem foi CHATA - TEDIOSA e REPETITIVA\n{personagem.robin}: ENTUSIASTA : Voce resumiu bem a trilha de Origom! Parece que alguem realmente aprendeu!!\n{personagem.mutano}: RAIVA : Eu ja to cansado de aprender, vamos pra casa Jogar uns Vídeo-Game!!!\nMUTANO CAI DA CARROÇA\n{personagem.estelar}: SUSTO : MUTANO... MUTANO... \nGRITOS DO LADO DE FORA DA CARROÇA\n{personagem.robin}: SEM NOÇAO : Mutano caiu da carroça e quebrou a perna voce gostaria de 1-Continuar na trilha\n{personagem.cyborg}: E porque a gente continuaria na trilha; A gente tem que concert......\n{personagem.robin}: DEIXA EU CONTINUAR!!! 2-checar os suprimentos\n3-olhar no mapa...\n{personagem.mutano}: CHOROS&GRITOS : Ai minha perninha\n{personagem.estelar}: Ele prescisa de um Medico!\n{personagem.robin}: 4-mudar o ritimo\n5-mudar as razoes...\n{personagem.ravena}: Não prescisamos de nenhuma dessas opçoes numeradas, Prescisamos de uma ambulancia!\n{personagem.robin}: Os pioneiros não tinham Ambulancia, ElES TinHAM SETE OPÇOES NUMERADAS!!! ENTÃO LIDE COM Isso! Agora onde eu estava; Claro 6-Parar\n7-.....')
    escolha = int(input('''
    Voce joga com a Estelar escolha a opçao!!!
    [ 1 ] Continuar na trilha
    [ 2 ] Checar os Suprimentos
    [ 3 ] Olhar o mapa
    [ 4 ] Mudar o ritimo
    [ 5 ] Mudar as Razões 
    [ 6 ] Parar
    [ 7 ] .....
    -->
    '''))
    if escolha == 1:
      print('Voce é doido!!! o mutano caiu da carroça ')
    elif escolha == 2:
      print('Depois, o mutano ta machucado')
    elif escolha == 3:
      print('o se for pra saber se tem algum hopital aqui perto!!')
    elif escolha == 4:
      print('Não!!!')
    elif escolha == 5:
      print('Podemos pensar em Razoes melhores pra colocar nas questoes Enumeradas... Tipo PARAAAR')
    elif escolha == 6:
      print('Vamos Parar')      
      print(f'{personagem.cyborg}: SEIS, Vamos escolher a 6!!')
      print(f' {personagem.robin}: Voces escolheram parar pra descansar')
      descansar = str(input('   S ou N:\n--> '))
      if descansar == 'S':
        print(f'{personagem.todos}: GRITAM : -->S<--')
      else:
        print('que sem noçao!')
    elif escolha == 7:
      print('Tinha que ser a opcao 6, Vamos parar!')
    elif escolha >= 8:
      print('opçao invalida')
    else:
      print('Coisa de Robin isso ai!')
    print(f'MUSIQUINHA....')
    truque = int(input('''
    A Estelar pode ajudar o mutano:
    [ 1 ] Dar um puxao na perna
    [ 2 ] fazer massagem nas costas
    [ 3 ] Buscar um remedio em super veocidade
    -->
    '''))
    if truque == 1:
      print('Voce sentirá uma leve pressão')
    elif truque == 2:
      print('Isso nao vai resolver, vou coloca sua perna no lugar vc vai sentir uma leve pressao')
    elif truque == 3:
      print('O Robin nao deixa, vou puxar sua perna, voce sentira uma leve pressao')
    print(f'{personagem.estelar}: DÓ : \n{personagem.mutano}: GRITA\n{personagem.estelar}: FELIZ : Bem melhor!!!\n{personagem.mutano}: SATISFAÇAO : Muito obrigado {personagem.estelar}!!\n{personagem.robin}: A historia esta realmente sendo vivida pelo mutano... Que compartilhar oque aprendeu ate agora;\n{personagem.mutano}: MANHA&CHOROS : Quelo i pa casa!\n{personagem.robin}: Maravilhoso!! Ja perdemos tempo suficiente vamos: conte vamos[ 1 ] = continuar com a trilha\n{personagem.mutano}: CHOROSSO : Eu presciso discançaaaa... !!!{personagem.robin}: SARCASMO : Com licença eu não escultei...\n{personagem.mutano}: Descançar!\n{personagem.robin}: Não é assim que os pioneiros escolhiam....\n{personagem.mutano}: Ta bom, Ta bom eu quero 6!!Por favor 6;!\n{personagem.robin}: Desculpe sera a Opçao 1 i se formos pegos pela neve do inverno podemos nao sobreviver.... \nSUSPENSE\nDE VOLTA A TRILHA{personagem.robin}: O clima esta frio a saude..;.. olhadinha nos companheiros.... Esta Boa! Ritimo; Constante\n{personagem.cyborg}: Essa é a pior experiência da minha vida!\n{personagem.robin}: Que bom ouvir isso {personagem.cyborg} parece que realmente se colocou no lugar dos pioneiros!! A proposito um ladrão robou seus sapatos...\n{personagem.cyborg}: Po cara eu vou ficar com bolhas\n{personagem.ravena}: Estamos com fome {personagem.robin}!!')
    boi = int(input('''
    A estelar ta de olho na suculencia do Boi e agora
    [ 1 ] Lamber o BOI 
    [ 2 ] Ficar com agua na boca
    [ 3 ] Morder a trazeira do BOI
    -->'''))
    if boi == 1:
      print('SUCULENCIA : ISSO!!')
    elif boi == 2:
      print('agora o cabeça achatada esta começando a parecer delicioso!!!')
    elif boi == 3:
      print(' MUUUUuuuu ')
    print(f'{personagem.robin}: Opçao 4-Vamos checar os suprimentos..')
    escolha = int(input('''O Robin checa as provisoes; 
    [ 4 ] Checar as Provisões
    [ 5 ] Seguir em frente sem perde tempo
    '''))
    if escolha == 4:
      print('...SURPRESO... Robin diz: Huumm acabou as provisões')
    else:
      print('Voce nao viu que tinha ratos  e as provisões acabou!')
    print(f'{personagem.estelar}: MALDADE : Vamos comer o delicioso cabeÇA achAtAdA!!\n{personagem.robin}: Ainda não, prescisamos dele pra puxar a carroça!\n{personagem.estelar}: Muito Bem... Voce esta seguro por enquanto.... Me Aguarde!!\nBEIJINHONOBOI\n{personagem.robin}: Titans, quando acaba a comida so resta uma opçao.\n{personagem.ravena}: Pedir uma Pizza!!\n....O ROBIN TIRA SEU CELULAR MAGICO E JOGA PRA FORA DA CARROÇA....\n{personagem.robin}: Sem PizzA!!! Nos Vamos caçar... Aqui atira num daqueles Bufalos...\n{personagem.mutano}: Recebe a SHOTGUM\n{personagem.mutano}: Não mesmo maninho, voce se esqueceu eu sou Vegetariano...\n{personagem.robin}: Essa é a trilha de Origom, ou voce come carne ou vc morre!!!\n{personagem.mutano}: Se todos começem legumes meus amigos bufalos nao vao prescisar se machucar....\n{personagem.robin}: entao me da isso eu vou caçar\nBANG BANG\nBANG BANG BANG\nBANG BANG BANG BANG\n{personagem.robin}: ATIRA atira atira, RA eu to ti vendo atras da pedra, Ra Bufalo, Esquilo, pra onde vc vai... Cervo... diga ola pro meu amiguinho... agora é com vc coelho... rarrararar balança o rabo esquilo essearbusto nao vai te salva hahahaha\n')
    parar = str(input('''Voce joga com a Estelar vc para o Robin S/N 
    -->''')).upper()
    if parar == 'S':
      print(f'{personagem.estelar}: Haaiimm!!! essa comida é mais que suficiente pro resto da viagem toda...')
    else:
      print('Isso é um absurso....')
    print(f'{personagem.robin}: HUM!! Uma pena, porque ao da pra levar 45Kg\n{personagem.ravena}: Entao porque vc atirou em todos eles;\n{personagem.robin}: SINCERIDA : Por é a unica coisa divertida nessa viagem Chata podem Divertida!!\n{personagem.todos}: HUMmm!!! NHAk NhaK nHAk !!! \n{personagem.cyborg}: Um que coisa maravilhosa!!!\n{personagem.robin}: Titans eu tenho Más noticias e Má noticias!! Primeira má noticia - O mutano foi picado por uma serpente\n{personagem.mutano}: SUSTO : É u q; .....VIU A COBRA E GRITA.... Eu não consigo sentir minha mão Ta toda inchada..\n{personagem.robin}: Agora má noticia!! O mutano tem Desinteria!!!{personagem.mutano}: Oque é Isso;\n{personagem.ravena}: Fazer coco ate morrer!!! ....MORDIDA NO PEDAÇO DE CARNE...\n{personagem.mutano}: OOh OU!! ...PULO ATRAS DO ARBUSTO....\n{personagem.robin}: Enguanto isso querem olhar em Volta; S/N; ')
    mutano = str(input('''
    A Estelar se preocupa....
    [ S ] preocupar
    [ N ] Nao preocupar
    -->''')).upper()
    if mutano == 'S':
      print(f'{personagem.estelar}: Nao deveriamos ajuda-lo;')
    else:
      print('MUTANO MORREU.')
    print(f'{personagem.robin}: Ah, Desculpa. essa nao é uma questao na lista!!!\n{personagem.estelar}: Voce nao disse que pessoas iam morrer!!\n{personagem.robin}: E isso aconte na trilha de Origom.. é super chato, voce caça, Todo mundo no grupo tem uma morte Orrivel...\n{personagem.ravena}: E quanto ao aprendizado;\n{personagem.robin}: Voces aprenderao que vao morrer!!\n{personagem.cyborg} CHOROSO: Ahh! Ainda nao acredito que o meu amigo {personagem.mutano} MORREU!!! \n{personagem1.mutano}: E isso ai!!! eu Morri!!\n{personagem.ravena} ASSUSTADA: Anhh, vc é uma fantasma!!!\n\n{personagem.cyborg}: É é, mano vc ta bem;\n{personagem1.mutano}: Oh Mano eu to otimo Olha só!! ... DANCINHA...\n{personagem.ravena} TRISTONHA: Ahh!! cara eu queria ser um fantasma!!\n{personagem1.mutano}: E so voce pegar uma Desinteria.. Gatinhhaa!!!\nE a proposito Meus amigos não estao felizes contigo!!! ....ROBIN VE FANTASMAS DOS ANIMAIS....\nDevolta a trilhA\n{personagem.robin}: Esse Vento, O ritimo esta lento.. E a saude... Fraca...\n{personagem.todos}: GRUNIDOS DE FRIO\n{personagem.robin}: {personagem.estelar} Morreu!!!\n{personagem.cyborg}: Gritos de dessespero e choro... Ah {personagem.estelar} Não!!! \n{personagem1.estelar} & {personagem1.mutano} Faz festa no lado de fora da carroça!!!\n{personagem.robin}: Ignorem os Fantasmas.... Apenas foquem em aprender as dificuldades dos pioneiros...\n{personagem1.mutano}: Mano, quando se é um fantasma vc nao prescisa aprender mais nada!! KkKkKkKkKk\nMUSICA\nAh {personagem.ravena} pegou sarampo e morreu\no {personagem.cyborg} se molhou e se doeu, pegou um resfriado e\nVirou presunto\nsem comida pra comer {personagem.robin} fez um churasco e por semanas ficou alimentado, e viu que a vida nao facil\nNA TRILHA DE Origom!\nA vida Nao e facil na trilha de Origom, Nao e nada facil na trilha de Origom\n{personagem1.todos}: ...FESTA NO IATE FANTASMA...\n{personagem.robin}: Eu to aprendendo muito!! ....ESTAA COONGEELANTTE...\nCansado : Eu cheguei ao Rio Deyse!')
    print(f'{personagem.robin}: Eu gostaria de Olhar em volta? [ S ] ou [ N ] : S concerteza!!!\nVISTA PANORAMICA\n{personagem1.mutano}: Como esta o lace de olhar em volta, Mano?\n{personagem.robin}: Otimo! Agora eu so tenho que levar a carroca ate o outro lado do rio vou estar em Origom! Alem de cacar essa e a unica parte divertida da trilha de Origom!\n{personagem1.ravena}: Mais divertida que nossa festa fantasma??\n{personagem1.mutano}: Huuhulll, Olha so esses fantasmas... HaHaHaHa.. Desiste logo mano esse iate ta bombando... SOBE ABORDO!!!\n{personagem.robin}: NUNCA!!!!! Eu vou seguir essa trilha ate o final, e nao tem nada que possam fazer pra me impedir!\nA festa no iate continua...\n{personagem.robin}: Parece que esta seguro por aqui!!\n AAAAhh!! \nCAI DE UMA CACHOEIRA\nNA CORRENEZA FORTE BATE NAS PEDRAS\nCARROCA ESPEDACA E TE JOGA NA MARGEM\n{personagem.robin}: FRACO&ESBAFORIDO : Parabens!!! eu cheguei em Origom!!\n{personagem1.mutano}: ORGULHOSO : Bom Trabalho, mano!!!!\n{personagem1.estelar}: Me diz, Oque vc aprendeu com essa nossa jornada?\n{personagem.robin}: Que o Robin tem Desinteria!!!')
    print('FIM')  
    break
  elif persona == 4:
    print('Vamos começar\n')
    print(f'Voce começa jogando com {personagem.mutano}')
    print('RAIVA')
    print(f'{personagem.ravena}: Alguem liga o ar-condicionado, ou eu vou suar em vc, vou suar em vc!!!\nPREGUIÇA\n{personagem.mutano}: Nossa maninho andar ate la vai demora um seculo!!!\nMELANCOLIA\n{personagem.estelar}: Nois não temos o controle remoto;\n{personagem.cyborg}: O negocio e manual tem que usar as manuais!\nINRRITADO\n{personagem.mutano}: Eu não vou usar minhas manuais pra nada!!!...DESESPERO..Estamos condenados a viver eternamente nesse sofrimento!!!\nMEDO\n{personagem.cyborg}: Não, Não!! Não eu nao aguento!! ALGUEM AJUDA; POR FAVOR ALGUEM AJUDA AQUI; Me ajuda!\nTILINTAR DE JANELA QUEBANDO\n{personagem.robin}: Um grito de ajuda! Onde esta o perigo;\n{personagem.mutano}: Por toda nossa volta, Maninho!!\nMANHOSA\n{personagem.estelar}: E muito grudento...\nINDIGUINADO\n{personagem.robin}: Estao falando da temperatura; é so ligar o ar condicionado\n{personagem.todos}: GRUNIDOS & RECLAMAÇÕES\nINDIGUINADO\n{personagem.robin}: E isso que a vida moderna fez com voces; Os deixou moles..;\n{personagem.robin}: Há algum tempo, não tinhamos essas conveniências modernas, Tudo era trabalho duro\nMais isso fez o povo duro e confiante em si mesmo...\n{personagem.robin}: Eu acho que deveriamos fazer uma viagem!\nANIMADO\n{personagem.cyborg}: VIAGEM, Isso parece divertido\nDESANIMADOR\n{personagem.robin}: Mais não é!! Essa viagem é pra ser educativa!\nEMPOLGADO\n{personagem.robin}: Para ensina-los alto suficiência sem conveniências em um ambiente moderno, eu os trouxe velha trilha que os nossos velhos pioneiros usaram pra desbravar uma nova vida para si mesmo. Bem Vindos a trilha de ORIGOM!\n{personagem.ravena}: DESCONFIADA :Entao estamos em Origom;\nESPERTINHO\n{personagem.robin}: Ainda não! São 2.000Km pra quele lado!!!\nINDIGUINADO\n{personagem.mutano}: VOCE Ficou Maluco;Isso vai demorar dias!{personagem.ravena}: Eu encontro voces lá!...\nAbre-se um portal e ela atravessa....MAS ELA GRITA SENDO PUXADA DE VOLTA PELO ROBIN{personagem.robin}: Não vai levar alguns dias!\n{personagem.todos}: GRUUFFs\n{personagem.robin}: Vai levar Varios meses!! : SARCASMO : Ja que os nossos velhos pioneiros não tinha carros ou portões magicos!!!\n{personagem.todos}: RECLAMACÕES\n{personagem.estelar}: INDIGUINADA : ISSO É UM ABSURDO!!!!!\n{personagem.robin}: SARCASMO : Adoro o intusiasmo Titãns!!!\nANIMADO ELE APRESENTA : Isto é um posto de comércio, onde nossa aventura educativa começa!\nAlguem gostaria de olhar em volta; S/N;\n{personagem.estelar}: O Robin, o que é que tava escrito ai;\n{personagem.robin}: INRRITADO : ESI ou ENE!!!! S quer dizer Sim, N que dizer Não...\n{personagem.ravena}: ENTEDIADA : porque não dizer so Sim ou Não;\n{personagem.robin}: Porque é mais rapido assim!\n{personagem.mutano}: Sim e Não já são as palavras mais curta, Maninho!!\n{personagem.robin}: Agora são ainda mais curtas!! : Olha em volta S/N;')
    Gostaria = str(input('Voce Olha em volta; S/N')).upper()
    if Gostaria == 'S':
      print('Eu quero N!')
    else:
      print('Isso é coisa de Robin, Bora continuar...')
    print(f'{personagem.todos}:  -->N<--\n{personagem.robin}: DESCONFIADO : Entao Não gostaria de olhar em volta desse posto de comercio historico; O lugar onde um carpinteiro de Ohaio ou um fazendeiro de Linoines começaram sua viagem;\n{personagem.todos}: N!!!\n{personagem.robin}: Desanimado, Táá!! Entao entrem na carroça!\nANTES DE ENTRAR NA CARROÇA\n{personagem.estelar}: ')
    estelar = int(input('''
    ENTUSIASMADICIMA : VOA AO ENCONTRO DO BOI CARROÇEIRO... Ela faz:
    [ 1 ] Monta no boi
    [ 2 ] Beija o boi
    [ 3 ] Pega o Boi no colo
    -->  
    '''))
    if estelar == 1:
      print('Que adoravel!!! Eu vou chamar vc de cabeça achatada i vc vai dormi no quarto na cama comigo!!!')
    elif estelar == 2:
      print('Que adoravel!!! Eu vou chamar vc de cabeça achatada i vc vai dormi no quarto na cama comigo!!!')
    elif estelar == 3:
      print('ELA PEGA O BOI NO COLO....Que adoravel!!! Eu vou chamar vc de cabeça achatada i vc vai dormi no quarto na cama comigo!!!')
    else:
      print('Eu queria pegar ele no colo...')
    print(f'{personagem.robin}: Não se apegue!! Nois teremos que comer-lo quando a triha ficar difícil!{personagem.estelar}: TRISTE : ahh!! Eu entendo!!\n{personagem.robin}: ENPOLGADO : PÉ Na Estrada!!!\n{personagem.ravena}: NOJO : Eu num vou entrar nisso ai!!\n{personagem.robin}: PEGA E JOGA ELA NA CARROÇA : Vai sim!!!\n{personagem.mutano}: ALEGRE : EU QUERO UMA SHOTGUM : BUFETADA NA CARA VINDA DO ROBIN\n{personagem.robin}: Boa ideia mutano!! Não sabemos que perigo podemos encontrar na estrada...\nJA NA ESTRADA\n{personagem.robin}: ARREPENDIDO/QUERENDOcontinuar : hãn estamos indo muito bem Titans, O clima esta bom nosso ritimo esta traquilo e estamos saldaveis!\nO MUTANO NÃO PARECE BEM\n{personagem.mutano}: Gorfo de Vômito..... \n{personagem.ravena}: DESANIMO : Nem sempre saudaveis!\n{personagem.cyborg}: DESANIMO : Eu achei que esse negocio erra pra se educativo!;\n{personagem.estelar}: Ate agora nossa viagem foi CHATA - TEDIOSA e REPETITIVA\n{personagem.robin}: ENTUSIASTA : Voce resumiu bem a trilha de Origom! Parece que alguem realmente aprendeu!!\n{personagem.mutano}: RAIVA : Eu ja to cansado de aprender, vamos pra casa Jogar uns Vídeo-Game!!!\nMUTANO CAI DA CARROÇA\n{personagem.estelar}: SUSTO : MUTANO... MUTANO... \nGRITOS DO LADO DE FORA DA CARROÇA\n{personagem.robin}: SEM NOÇAO : Mutano caiu da carroça e quebrou a perna voce gostaria de 1-Continuar na trilha\n{personagem.cyborg}: E porque a gente continuaria na trilha; A gente tem que concert......\n{personagem.robin}: DEIXA EU CONTINUAR!!! 2-checar os suprimentos\n3-olhar no mapa...\n{personagem.mutano}: CHOROS&GRITOS : Ai minha perninha\n{personagem.estelar}: Ele prescisa de um Medico!\n{personagem.robin}: 4-mudar o ritimo\n5-mudar as razoes...\n{personagem.ravena}: Não prescisamos de nenhuma dessas opçoes numeradas, Prescisamos de uma ambulancia!\n{personagem.robin}: Os pioneiros não tinham Ambulancia, ElES TinHAM SETE OPÇOES NUMERADAS!!! ENTÃO LIDE COM Isso! Agora onde eu estava; Claro 6-Parar\n7-.....')
    escolha = int(input('''
    Voce joga com a Estelar escolha a opçao!!!
    [ 1 ] Continuar na trilha
    [ 2 ] Checar os Suprimentos
    [ 3 ] Olhar o mapa
    [ 4 ] Mudar o ritimo
    [ 5 ] Mudar as Razões 
    [ 6 ] Parar
    [ 7 ] .....
    -->
    '''))
    if escolha == 1:
      print('Voce é doido!!! o mutano caiu da carroça ')
    elif escolha == 2:
      print('Depois, o mutano ta machucado')
    elif escolha == 3:
      print('o se for pra saber se tem algum hopital aqui perto!!')
    elif escolha == 4:
      print('Não!!!')
    elif escolha == 5:
      print('Podemos pensar em Razoes melhores pra colocar nas questoes Enumeradas... Tipo PARAAAR')
    elif escolha == 6:
      print('Vamos Parar')      
      print(f'{personagem.cyborg}: SEIS, Vamos escolher a 6!!')
      print(f' {personagem.robin}: Voces escolheram parar pra descansar')
      descansar = str(input('   S ou N:\n--> '))
      if descansar == 'S':
        print(f'{personagem.todos}: GRITAM : -->S<--')
      else:
        print('que sem noçao!')
    elif escolha == 7:
      print('Tinha que ser a opcao 6, Vamos parar!')
    elif escolha >= 8:
      print('opçao invalida')
    else:
      print('Coisa de Robin isso ai!')
    print(f'MUSIQUINHA....')
    truque = int(input('''
    A Estelar pode ajudar o mutano:
    [ 1 ] Dar um puxao na perna
    [ 2 ] fazer massagem nas costas
    [ 3 ] Buscar um remedio em super veocidade
    -->
    '''))
    if truque == 1:
      print('Voce sentirá uma leve pressão')
    elif truque == 2:
      print('Isso nao vai resolver, vou coloca sua perna no lugar vc vai sentir uma leve pressao')
    elif truque == 3:
      print('O Robin nao deixa, vou puxar sua perna, voce sentira uma leve pressao')
    print(f'{personagem.estelar}: DÓ : \n{personagem.mutano}: GRITA\n{personagem.estelar}: FELIZ : Bem melhor!!!\n{personagem.mutano}: SATISFAÇAO : Muito obrigado {personagem.estelar}!!\n{personagem.robin}: A historia esta realmente sendo vivida pelo mutano... Que compartilhar oque aprendeu ate agora;\n{personagem.mutano}: MANHA&CHOROS : Quelo i pa casa!\n{personagem.robin}: Maravilhoso!! Ja perdemos tempo suficiente vamos: conte vamos[ 1 ] = continuar com a trilha\n{personagem.mutano}: CHOROSSO : Eu presciso discançaaaa... !!!{personagem.robin}: SARCASMO : Com licença eu não escultei...\n{personagem.mutano}: Descançar!\n{personagem.robin}: Não é assim que os pioneiros escolhiam....\n{personagem.mutano}: Ta bom, Ta bom eu quero 6!!Por favor 6;!\n{personagem.robin}: Desculpe sera a Opçao 1 i se formos pegos pela neve do inverno podemos nao sobreviver.... \nSUSPENSE\nDE VOLTA A TRILHA{personagem.robin}: O clima esta frio a saude..;.. olhadinha nos companheiros.... Esta Boa! Ritimo; Constante\n{personagem.cyborg}: Essa é a pior experiência da minha vida!\n{personagem.robin}: Que bom ouvir isso {personagem.cyborg} parece que realmente se colocou no lugar dos pioneiros!! A proposito um ladrão robou seus sapatos...\n{personagem.cyborg}: Po cara eu vou ficar com bolhas\n{personagem.ravena}: Estamos com fome {personagem.robin}!!')
    boi = int(input('''
    A estelar ta de olho na suculencia do Boi e agora
    [ 1 ] Lamber o BOI 
    [ 2 ] Ficar com agua na boca
    [ 3 ] Morder a trazeira do BOI
    -->'''))
    if boi == 1:
      print('SUCULENCIA : ISSO!!')
    elif boi == 2:
      print('agora o cabeça achatada esta começando a parecer delicioso!!!')
    elif boi == 3:
      print(' MUUUUuuuu ')
    print(f'{personagem.robin}: Opçao 4-Vamos checar os suprimentos..')
    escolha = int(input('''O Robin checa as provisoes; 
    [ 4 ] Checar as Provisões
    [ 5 ] Seguir em frente sem perde tempo
    '''))
    if escolha == 4:
      print('...SURPRESO... Robin diz: Huumm acabou as provisões')
    else:
      print('Voce nao viu que tinha ratos  e as provisões acabou!')
    print(f'{personagem.estelar}: MALDADE : Vamos comer o delicioso cabeÇA achAtAdA!!\n{personagem.robin}: Ainda não, prescisamos dele pra puxar a carroça!\n{personagem.estelar}: Muito Bem... Voce esta seguro por enquanto.... Me Aguarde!!\nBEIJINHONOBOI\n{personagem.robin}: Titans, quando acaba a comida so resta uma opçao.\n{personagem.ravena}: Pedir uma Pizza!!\n....O ROBIN TIRA SEU CELULAR MAGICO E JOGA PRA FORA DA CARROÇA....\n{personagem.robin}: Sem PizzA!!! Nos Vamos caçar... Aqui atira num daqueles Bufalos...\n{personagem.mutano}: Recebe a SHOTGUM\n{personagem.mutano}: Não mesmo maninho, voce se esqueceu eu sou Vegetariano...\n{personagem.robin}: Essa é a trilha de Origom, ou voce come carne ou vc morre!!!\n{personagem.mutano}: Se todos começem legumes meus amigos bufalos nao vao prescisar se machucar....\n{personagem.robin}: entao me da isso eu vou caçar\nBANG BANG\nBANG BANG BANG\nBANG BANG BANG BANG\n{personagem.robin}: ATIRA atira atira, RA eu to ti vendo atras da pedra, Ra Bufalo, Esquilo, pra onde vc vai... Cervo... diga ola pro meu amiguinho... agora é com vc coelho... rarrararar balança o rabo esquilo essearbusto nao vai te salva hahahaha\n')
    parar = str(input('''Voce joga com a Estelar vc para o Robin S/N 
    -->''')).upper()
    if parar == 'S':
      print(f'{personagem.estelar}: Haaiimm!!! essa comida é mais que suficiente pro resto da viagem toda...')
    else:
      print('Isso é um absurso....')
    print(f'{personagem.robin}: HUM!! Uma pena, porque ao da pra levar 45Kg\n{personagem.ravena}: Entao porque vc atirou em todos eles;\n{personagem.robin}: SINCERIDA : Por é a unica coisa divertida nessa viagem Chata podem Divertida!!\n{personagem.todos}: HUMmm!!! NHAk NhaK nHAk !!! \n{personagem.cyborg}: Um que coisa maravilhosa!!!\n{personagem.robin}: Titans eu tenho Más noticias e Má noticias!! Primeira má noticia - O mutano foi picado por uma serpente\n{personagem.mutano}: SUSTO : É u q; .....VIU A COBRA E GRITA.... Eu não consigo sentir minha mão Ta toda inchada..\n{personagem.robin}: Agora má noticia!! O mutano tem Desinteria!!!{personagem.mutano}: Oque é Isso;\n{personagem.ravena}: Fazer coco ate morrer!!! ....MORDIDA NO PEDAÇO DE CARNE...\n{personagem.mutano}: OOh OU!! ...PULO ATRAS DO ARBUSTO....\n{personagem.robin}: Enguanto isso querem olhar em Volta; S/N; ')
    mutano = str(input('''
    A Estelar se preocupa....
    [ S ] preocupar
    [ N ] Nao preocupar
    -->''')).upper()
    if mutano == 'S':
      print(f'{personagem.estelar}: Nao deveriamos ajuda-lo;')
    else:
      print('MUTANO MORREU.')
    print(f'{personagem.robin}: Ah, Desculpa. essa nao é uma questao na lista!!!\n{personagem.estelar}: Voce nao disse que pessoas iam morrer!!\n{personagem.robin}: E isso aconte na trilha de Origom.. é super chato, voce caça, Todo mundo no grupo tem uma morte Orrivel...\n{personagem.ravena}: E quanto ao aprendizado;\n{personagem.robin}: Voces aprenderao que vao morrer!!\n{personagem.cyborg} CHOROSO: Ahh! Ainda nao acredito que o meu amigo {personagem.mutano} MORREU!!! \n{personagem1.mutano}: E isso ai!!! eu Morri!!\n{personagem.ravena} ASSUSTADA: Anhh, vc é uma fantasma!!!\n\n{personagem.cyborg}: É é, mano vc ta bem;\n{personagem1.mutano}: Oh Mano eu to otimo Olha só!! ... DANCINHA...\n{personagem.ravena} TRISTONHA: Ahh!! cara eu queria ser um fantasma!!\n{personagem1.mutano}: E so voce pegar uma Desinteria.. Gatinhhaa!!!\nE a proposito Meus amigos não estao felizes contigo!!! ....ROBIN VE FANTASMAS DOS ANIMAIS....\nDevolta a trilhA\n{personagem.robin}: Esse Vento, O ritimo esta lento.. E a saude... Fraca...\n{personagem.todos}: GRUNIDOS DE FRIO\n{personagem.robin}: {personagem.estelar} Morreu!!!\n{personagem.cyborg}: Gritos de dessespero e choro... Ah {personagem.estelar} Não!!! \n{personagem1.estelar} & {personagem1.mutano} Faz festa no lado de fora da carroça!!!\n{personagem.robin}: Ignorem os Fantasmas.... Apenas foquem em aprender as dificuldades dos pioneiros...\n{personagem1.mutano}: Mano, quando se é um fantasma vc nao prescisa aprender mais nada!! KkKkKkKkKk\nMUSICA\nAh {personagem.ravena} pegou sarampo e morreu\no {personagem.cyborg} se molhou e se doeu, pegou um resfriado e\nVirou presunto\nsem comida pra comer {personagem.robin} fez um churasco e por semanas ficou alimentado, e viu que a vida nao facil\nNA TRILHA DE Origom!\nA vida Nao e facil na trilha de Origom, Nao e nada facil na trilha de Origom\n{personagem1.todos}: ...FESTA NO IATE FANTASMA...\n{personagem.robin}: Eu to aprendendo muito!! ....ESTAA COONGEELANTTE...\nCansado : Eu cheguei ao Rio Deyse!')
    print(f'{personagem.robin}: Eu gostaria de Olhar em volta? [ S ] ou [ N ] : S concerteza!!!\nVISTA PANORAMICA\n{personagem1.mutano}: Como esta o lace de olhar em volta, Mano?\n{personagem.robin}: Otimo! Agora eu so tenho que levar a carroca ate o outro lado do rio vou estar em Origom! Alem de cacar essa e a unica parte divertida da trilha de Origom!\n{personagem1.ravena}: Mais divertida que nossa festa fantasma??\n{personagem1.mutano}: Huuhulll, Olha so esses fantasmas... HaHaHaHa.. Desiste logo mano esse iate ta bombando... SOBE ABORDO!!!\n{personagem.robin}: NUNCA!!!!! Eu vou seguir essa trilha ate o final, e nao tem nada que possam fazer pra me impedir!\nA festa no iate continua...\n{personagem.robin}: Parece que esta seguro por aqui!!\n AAAAhh!! \nCAI DE UMA CACHOEIRA\nNA CORRENEZA FORTE BATE NAS PEDRAS\nCARROCA ESPEDACA E TE JOGA NA MARGEM\n{personagem.robin}: FRACO&ESBAFORIDO : Parabens!!! eu cheguei em Origom!!\n{personagem1.mutano}: ORGULHOSO : Bom Trabalho, mano!!!!\n{personagem1.estelar}: Me diz, Oque vc aprendeu com essa nossa jornada?\n{personagem.robin}: Que o Robin tem Desinteria!!!')
    print('FIM')  
    break
  elif persona == 5:
    print('Vamos começar\n')
    print(f'Voce começa jogando com {personagem.cyborg}')

  else:
    print('Olha acho que vc escolheu a opçao errada')
    break
    
