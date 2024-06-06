from fpdf import FPDF

# Variáveis onde iremos armazenar todos os nossos dados.
projeto = input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")

valor_total = int(horas_previstas) * int(valor_hora)

pdf = FPDF()

# Esse comando gera a página do PDF, mas branco. As configurações serão feitas em seguida.
pdf.add_page()

# Esse comando servirá para configurarmos a fonte que querermos usar em nosso PDF.
pdf.set_font("Arial")

# Esse comando serve para puxar nossa imagem de layout para o PDF não ficar todo brancão.
pdf.image("template.png", x=0, y=0)

# Todas as variáveis que estão sendo chamadas aqui são variáveis que já foram criadas neste projeto anteriormente.
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)

# Aqui estamos usando o comando str() para converter o resultado final em texto.
pdf.text(115, 205, str(valor_total))

# Aqui é o comando de saída, o PDF será gerado a partir daqui.
pdf.output("Orçamento.pdf")

# Para printar a mensagem final.
print("Orçamento gerado com sucesso!")