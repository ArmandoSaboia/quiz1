#quiz das capitais dos estados brasileiros
print('Olá, sejam bem-vindos ao quiz sobre as capitais dos estados brasileiros. O Brasil é dividido em 26 estados e o Distrito Federal.')
rodadas=int(input('Quantas rodadas você gostaria de jogar entre 1 e 27 '))
lista_dos_estados=["Acre","Alagoas","Amapá","Amazonas","Bahia","Ceará","Distrito Federal","Espírito Santo","Goiás","Maranhão","Mato Grosso","Mato Grosso do Sul","Minas Gerais","Pará","Paraíba","Paraná","Pernambuco","Piauí","Rio de Janeiro","Rio Grande do Norte","Rio Grande do Sul","Rondônia","Roraima","Santa Catarina","São Paulo","Sergipe","Tocantins"]
lista_das_capitais=['Rio Branco','Maceió','Macapá','Manaus','Salvador','Fortaleza','Brasília','Vitória','Goiânia','São Luís','Cuiabá','Campo Grande','Belo Horizonte','Belém','João Pessoa','Curitiba','Recife','Teresina','Rio de Janeiro','Natal','Porto Alegre','Porto Velho','Boa Vista','Florianópolis','São Paulo','Aracaju','Palmas']
if rodadas>=28:
    print('ERRO, você não seguiu as instruções.')
    quit('Fim do jogo')
l2=lista_das_capitais
l1=lista_dos_estados
import random
pontos=0
for i in range(rodadas):
    estado=random.choice(l1)
    print('Qual a capital do estado:',estado)
    capital=l2[l1.index(estado)]
    ans=input('Escreva a capital: ').lower()
    if capital.lower()==ans.lower():
        print('A resposta está correta.')
        pontos+=1
    else:
        print('A resposta está errada, a resposta correta é',capital)
    l1.remove(estado)
    l2.remove(capital)
print('Fim do jogo')
print('A sua pontuação total foi de',pontos,'em',rodadas)