from app import app
from flask import render_template, request, redirect, url_for, session, flash

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/drcBrasil')
def drcBrasil():
    return render_template('drcBrasil.html')

@app.route('/comunidade')
def comunidade():
    return render_template('comunidade.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/perguntasFrequentes')
def perguntasFrequentes():
    dicionario = {
        'O que é Doença renal crônica?': 'A doença renal crônica(DRC) é definida como uma patologia com duração superior a três meses que prejudica a capacidade dos rins de filtrar as toxinas do sangue. A doença renal crônica também é referida quando há alterações na estrutura renal, encontradas em imagens renais, biópsias e outras imagens renais; Da mesma forma, a doença renal crônica é considerada uma alteração em outras funções renais, como a perda de proteínas na urina e alterações nos exames de urina. Pacientes transplantados também são considerados portadores de doença renal crônica.',
        'Pode tomar vacina?': 'Recomenda-se a vacinação contra hepatite B para todos os pacientes renais crônicos, de preferência antes de se tornarem dependentes de diálise',
        'Pode se alimentar/hidratar normalmente?': 'Para melhorar a ingestão de alimentos fundamentais e garantir o bom funcionamento do corpo humano, deve-se evitar os seguintes alimentos:\n derivados de laticínios;\n comidas processadas e embutidas, como salsichas, linguiças, presuntos, mortadelas, etc;\nchocolates;\n bebidas gaseificadas (Coca-Cola, Pepsi e cervejas);\n frutos do mar;\n miúdos, como fígado, coração, dobradinha, chouriço, etc;\n frutas, vegetais e sementes oleaginosas, como castanhas, nozes e amendoim;\n peixes de água salgada, como atum, bacalhau e sardinha;\n qualquer alimento industrializado que utiliza conservantes e acidulantes.',
        'Crianças com DRC podem frequentar a escola?': 'As crianças com Doença Renal Crônica podem sim frequentar a escola, mas n como as outras, por conta das longas horas de Hemodiálise, que acaba afetando na vida estudantil das crianças, como foi o caso do "João", que tinha 12 anos e era um dos melhores da turma, mas por conta da Doença Renal Crônica, teve que priorizar sua vida, focando no tratamento, fazendo com que ficasse difícil pra ele ir a escola.',
        'Qual a probabilidade de sobrevivência?': 'O prognóstico da criança com DRC grave depende muito da disponibilidade de recursos para tratamento. Embora tenha ocorrido grande melhora na sobrevida em longo prazo de crianças e adolescentes, nos últimos 40 anos, nos Estados Unidos, tanto para as crianças em diálise como para as transplantadas, a sobrevida de 10 anos é de apenas 80% e, como já comentado, a taxa de mortalidade ainda é de 30 a 150 vezes maior que a dos pares de idade sem doença renal.14 De fato, o tempo de sobrevida esperado para uma criança de 0 a 14 anos em diálise é de apenas 20 anos, enquanto a população de mesma idade transplantada tem uma sobrevida estimada em 50 anos. No levantamento de 2007 do USRDS, 92% das crianças que foram transplantadas sobreviveram por 5 anos, comparadas a 78% daquelas que receberam hemodiálise ou diálise peritoneal. Nos países em que a terapia renal substitutiva está disponível, a melhor forma de tratamento é, pois, o transplante renal, em todas as faixas de idade da criança.',
        'Como é feito o diagnostico DRC ': 'Os recursos diagnósticos utilizados para identificar o paciente com DRC são a A taxa de filtração glomerular(TFG), o exame sumário de urina (EAS) e um exame de imagem, preferencialmente a ultrassonografia dos rins e vias urinária',
        'Quais os sinais da DRC em bebês e crianças? Como desconfiar?': 'A suspeita de DRC deve ser iniciada pela pesquisa dos antecedentes pessoais e familiares, valorizando os dados da ultrassonografia pré-natal, antecedentes de ITU, a pesquisa de casos de MFTU ou de IRC na família e os dados epidemiológicos relativos à etiologia da IRC na infância. Pacientes com DRC podem ter poucos sintomas por longos períodos, por isso é necessária a pesquisa objetiva por meio de exames de rotina ou de avaliações específicas. Exame de urina de rotina deve ser realizado pelo menos uma vez durante cada etapa da infância.',
        'Qual especialidade medica que trata DRC?': 'Nefrologia é uma especialidade médica dedicada ao diagnóstico e tratamento clínico das doenças do sistema urinário, principalmente relacionadas ao rim. O médico especializado nas doenças do sistema urinário chama-se médico nefrologista.',
        'O que é dialise peritoneal?': 'Procedimento que ocorre no peritônio do paciente e tem como objetivo substituir a função renal. A diálise é responsável por remover as impurezas e excessos de líquidos no sangue, com auxílio de um filtro natural chamado peritônio. Ele consiste em uma membrana porosa e semipermeável que cobre os principais órgãos do abdômen. O espaço entre esses órgãos é chamado de cavidade peritoneal. Um pequeno e fino tubo denominado cateter de Tenckhoff, é implantado pela parede abdominal próximo ao umbigo, após a implantação do cateter é possível a passagem de solução de diálise até a cavidade peritoneal, realizando a drenagem em contato com o sangue, retirando junto as toxinas como a ureia, potássio e creatinina, e o excesso de liquido do corpo.',
        'O que é hemodiálise?': 'Hemodiálise é o procedimento através do qual uma máquina filtra e limpa o sangue, fazendo parte do trabalho que o rim doente não pode fazer. O procedimento retira do corpo os resíduos prejudiciais à saúde, como o excesso de sal e de líquidos.',
        'O que é tratamento conservador?': 'Consiste em todas as medidas clínicas (remédios, modificação da dieta, estilo de vida), que podem ser utilizadas para retardar a perda da função renal, reduzir os sintomas e prevenir complicações.' 
    }
    return render_template('perguntasFrequentes.html', dicionario=dicionario)