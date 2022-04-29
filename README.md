# Decomposição LU para Matrizes Tridiagonais
## Este projeto consiste de duas soluções principais para determinados problemas encontrados no campo da engenharia.
- (1) Decomposição LU de matrizes tridiagonais 
- (2) Solução de sistemas com formato tridiagonal cíclico

### Iniciando o projeto
   Para iniciar o projeto, basta abrir o arquivo "index.py" e escolher algum módulo. A partir daí é necessário seguir os 
   passos recomendados pelo próprio programa.

### Escolhendo um módulo
     "Seja bem vindo ao EP 1 de cálculo numérico
      Neste trabalho possuímos duas grandes soluções:
      A primeira é a decomposição LU de uma matriz tridiagonal, enquanto que a segunda é a resolução de um sistema a partir de um matriz tridiagonal cíclica:
      Para iniciarmos, escolha um módulo:
      (1) Decomposição LU        (2) Resolução de sistemas        (3) Testes Automatizados
      Insira o módulo:"
      
      Ao escolher um número o usuário será redirecionado para uma determinada solução em outro arquivo ".py", ao inserir algum input que não se encaixa naqueles pedidos o programa acusará erro ou irá fechar automaticamente, por exemplo, neste caso "4", "dois", "", etc.
      
### Solução (1) Decomposição LU
Ao escolher a primeira solução o usuário trabalhará com uma matriz quadrática, em que o mesmo deverá introduzir a ordem e os itens das células da matriz:

      "O primeiro exercício consiste em realizar uma decomposição LU de uma matriz tridiagonal.
      Lembre-se, a matriz a ser introduzida deve ser triangularizável pelo Método de Eliminação de Gauss sem trocas de linhas
      Insira a ordem da sua matriz:"
      
Escolhendo a ordem da matriz o usuário deve introduzir todos os campos necessários para a pedidos pelo programa para a construção da matriz. A matriz sempre segue o seguinte formato:
[
 [b1.   c2.    0     ...   0],
 [a2.   b2.    c3.   ...   0],
 [0.    a3.    b3.   ...   0],
 ...
 [0.    0.     ...    an.  bn]
]

      Insira o valor de a2:
      Insira o valor de a3:
      Insira o valor de a4:
      Insira o valor de a5:
      Insira o valor de b1:
      Insira o valor de b2:
      Insira o valor de b3:
      Insira o valor de b4:
      Insira o valor de b5:
      Insira o valor de c2:
      Insira o valor de c3:
      Insira o valor de c4:
      Insira o valor de c5:
 Assim, o usuário tem a possibilidade de verificar a sua matriz de maneira mais visual e, caso tenha errado alguma informação, possa reescrever os seus dados.
      
    Exemplo:      
       [[5. 10.  0.  0.  0.]
       [ 1.  6. 11.  0.  0.]
       [ 0.  2.  7. 12.  0.]
       [ 0.  0.  3.  8. 13.]
       [ 0.  0.  0.  4.  9.]]
       
       Para continuar o programa escolha uma das opções abaixo:
       (1) A minha matriz está correta (2) Reescrever matriz
 
 A partir do momento que há a confirmação da Matriz, o computador irá gerar as matrizes do exercício:
 
    Exemplo:
      A sua matriz U é :

      [[  5.    10.     0.     0.     0.  ]
       [  0.     4.    11.     0.     0.  ]
       [  0.     0.     1.5   12.     0.  ]
       [  0.     0.     0.   -16.    13.  ]
       [  0.     0.     0.     0.    12.25]]


      O seu vetor L é:

       [ 0.2   0.5   2.   -0.25],

       ou seja, sua matriz L é

      [[ 1.    0.    0.    0.    0.  ]
       [ 0.2   1.    0.    0.    0.  ]
       [ 0.    0.5   1.    0.    0.  ]
       [ 0.    0.    2.    1.    0.  ]
       [ 0.    0.    0.   -0.25  1.  ]]

### Solução (2) Resolução de sistemas
Ao escolher a segunda solução o usuário trabalhará com uma matriz quadrática e um vetor d. A ideia é que essas duas informações resumam um sistema tridiagonal cíclico, ou seja, possua o seguinte formato
 - b1*x1 + c2*x2 + 0*x3 + 0*x4 + ... + a1*xn = d1
 - a2*x1 + b2*x2 + c3*x3 + 0*x4 + ... + 0*xn = d2
 - 0*x1 + a3*x2 + b3*x3 + 0*x4 + ... + 0*xn = d3
 - ...
 - c1*x1 + 0*x2  +   ...   + an*xn-1 + bn*xn = dn

#### A partir dai seguimos o mesmo fluxo da solução (1)
    Insira a ordem da sua matriz: n
    Insira o valor de a1:
    Insira o valor de a2:
    Insira o valor de a3:
    ...
    Insira o valor de an-1:
    Insira o valor de b1:
    Insira o valor de b2:
    Insira o valor de b3:
    ...
    Insira o valor de bn:
    Insira o valor de c1:
    Insira o valor de c2:
    Insira o valor de c3:
    ...
    Insira o valor de cn-1:
    Muito bem, agora que você já inseriu a sua matriz A, siga os próximos passos para o mapeamento do vetor d

    Insira o item d1 do seu vetor d: 
    Insira o item d2 do seu vetor d: 
    Insira o item d3 do seu vetor d: 
    ...
    Insira o item dn do seu vetor d:
A partir disso, o computador irá exibir os dados introduzidos e dar a opção de reescrevê-los
    
    Exemplo: 
     A Matriz inserida foi:
     [[ 4.  7.  0.  0.  1.]
     [ 1.  5.  8.  0.  0.]
     [ 0.  2.  4.  9.  0.]
     [ 0.  0.  3.  6. 10.]
     [11.  0.  0.  4.  7.]]

     e o vetor d foi: [3. 2. 1. 6. 5.]
    Para continuar o programa escolha uma das opções abaixo:
    (1) Os meus dados estão corretos (2) Reescrever dados
Assim termos a exibição do vetor solução x:
     
     Exemplo:
      O seu vetor solução é:
      x = [0.06744101 0.30718024 0.04958222 0.01873106 0.57997429]
      
### (3) Testes automatizados
Os testes automatizados preenchem os vetores a, b e c das matrizes e o vetor d do sistema de maneira automática, considerando n=20, a partir das seguintes expressões:
ai = (2i − 1)/4i , 1 ≤ i ≤ n − 1, an = (2n − 1)/2n,
ci = 1 − ai, 1 ≤ i ≤ n,
bi = 2, 1 ≤ i ≤ n,
di = cos(2πi^2)/n^2, 1 ≤ i ≤ n.

Caso o usuário deseje testar a solução 1 com os dados anteriores os últimos dos vetores a e c são excluidos.

