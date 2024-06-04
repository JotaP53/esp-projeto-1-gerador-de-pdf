# Empowerdata | Semana do Python na Prática

## Projeto #1: Gerador de PDF

### Introdução

O cenário deste projeto é emitir orçamentos para os clientes de uma empresa.

O interessante de um projeto como este é que ele não se limita somente ao nicho no qual ele foi desenhado.

Se quisermos usar o mesmo script para ser aplicado em uma academia criando fichas de treino, ele também será bem vindo. Se quisermos gerar relatórios para um escritório de advocacia, também cairá como uma luva.

Uma das ferramentas que foram utilizadas neste projeto foi o Jupyter Notebook.

A importância dessa ferramenta para a elaboração do projeto se dá pelo fato de que ela é composta por células. Isto significa que não precisamos rodar todo o código para ir testando um determinado bloco, basta apenas rodar aquela célula e testá-la individualmente.

É uma ferramenta indispensável para quem estar estudando.

Licensa para uma frase que o instrutor falou durante a aula que faz muito sentido para mim e acredito que deva ser documentada:

>O melhor programador não é o que decorou comandos, mas é aquele que sabe o que a linguagem pode fazer, mesclar os conceitos e gerar resultados através disso.

### Documentação do Projeto

#### _Mostrar as informações para o usuário_

Isto será feito através do comando `print()`. Quando usado, esse comando irá printar para o usuário alguma informação na tela.

~~~~python
print("Semana do Python na Prática")
print("Eu quero aprender Python de verdade!")
~~~~

Quando for executado, será impresso na tela as mesmas frases dentro do `print()`.

#### _Receber dados do usuário_

Receber dados num programa é uma das formas de interação com o usuário. Essa interação se dará pelo comando `input()`. Veja a seguir:

~~~~python
input("Digite seu nome: ")
~~~~

Ao ser executado, esse código exibirá no terminal o texto dentro dos parênteses e o usuário poderá digitar seu nome.

#### _Armazenando dados em variáveis_

Variáveis são espaços na memória onde podemos guardar todos os dados que o usuário nos fornece ou aqueles dados que são pré concebidos no projeto. Uma analogia interessante é como se as variáveis fossem um armário com gavetas. Em cada gaveta estará um dado diferente e cada uma dessas gavetas terá um nome.

Para guardarmos variáveis utilizamos o sinal `=`. O sinal de igual sozinho cumprirá a função de atribuição.

Observe abaixo um exemplo de armazenamento.

~~~~python
projeto = "Semana do Python na prática"
~~~~

No código acima, `projeto` é o nome da variável ou, como colocamos na analogia, da gaveta do armário. `Semana do Python na Prática` é o conteúdo dessa variável. Neste caso, o conteúdo já vem pré-armazenado, ou seja, não espera-se que o usuário armazene algum dado. `=` é o atribuidor.

Como poderia ser acessado esse dado na memória? Através de um comando que já vimos anteriormente `print()`.

~~~~python
print(projeto)
~~~~

Quando essa linha de código for executada, aparecerá no terminal a frase `Semana do Python na Prática` pois é a frase que está alocada dentro da variável `projeto`.

Se o nome da variável for um nome duplo, usa-se `_` para separar os dois nomes, por exemplo: `horas_trabalhadas`.

Alguns detalhes importantes:
- Python é _case sensitive_, ou seja, ele faz diferenciação entre letras maiúsculas e minúsculas.
- Use nomes que façam sentidos.
- Não pode iniciar uma varíavel com número.
- Não pode conter espaços em brancos.

#### _Mesclando todos os conceitos aprendidos até agora_

Agora, vamos unir todos esses conceitos estudados até agora.

~~~python
projeto = input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")
~~~

Temos quatro variáveis, onde em cada variável o usuário alocará algum dado informado por ele: (1) a descrição do projeto, (2) a quantidade de horas previstas, (3) o valor da hora trabalhada e (4) o prazo estimado para a conclusão do projeto.

Depois de rodado essas linhas, aparentemente nada ocorrerá. Para que os dados fornecidos pelo usuário apareçam será necessário, como vimos, o uso do comando `print()`.

~~~python
print(projeto)
print(horas_previstas)
print(valor_hora)
print(prazo)
~~~

Depois de roda essa série de comandos, todas as informações dadas pelo usuário aparecerá no terminal.

```
Desenvolvimento python
100
20
3 meses
```
#### _Tipos de dados_
- Textos: `str`
- Números: `int`
- Comandos: `type()`, `str()`, `int()`

