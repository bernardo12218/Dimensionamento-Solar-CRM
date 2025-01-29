# Documento de Visão

## Sistema de Dimensionamento Solar e CRM

### Histórico da Revisão

|  Data  | Versão | Descrição | Autores |
|:-------|:-------|:----------|:------|
| 28/01/2025 |  **`1.00`** | Versão Inicial  | [Asaph Arruda](h[ttps://github.com/bernardommedeiros](https://github.com/ArrudaAsaph)) e [Bernardo Moura](https://github.com/bernardommedeiros) |

### 1. Objetivo do Projeto

O projeto __Sistema de Dimensionamento Solar e CRM__ tem como objetivo fornecer uma solução eficiente, integrada e acessível para o dimensionamento de sistemas fotovoltaicos e a gestão do relacionamento com clientes.

### 2. Descrição do Problema

|         __        | __   |
|:------------------|:-----|
| **_O problema_**    | Gerenciar de forma eficiente o ciclo de vendas e atendimento de clientes interessados em sistemas fotovoltaicos, além de calcular e dimensionar soluções solares personalizadas. |
| **_afetando_**      | Empresas e profissionais que trabalham com energia solar e clientes que desejam adquirir sistemas fotovoltaicos para reduzir custos de energia. |
| **_cujo impacto é_**| Dificuldade em organizar o processo de venda e acompanhamento de clientes, erro em cálculos de dimensionamento e perda de oportunidades de negócios. |
| **_uma boa solução seria_** | Um sistema que combine CRM para o acompanhamento de clientes com um módulo de cálculo de dimensionamento solar, otimizando processos e melhorando a experiência do cliente. |

### 3. Descrição dos Usuários

| Nome | Descrição | Responsabilidades |
|:---  |:--- |:--- |
| Administrador  | Gerencia as configurações gerais do sistema | Mantém o cadastro de usuários e realiza ajustes globais do sistema, adicionar kits Fotovoltaicos |
| Consultor de Vendas  | Atua no controle do fluxo de clientes e dimensionamento solar | Cadastra novos clientes, atualiza status do ciclo de vendas, insere dados de consumo energético e realiza o dimensionamento dos sistemas fotovoltaicos |


### 4. Descrição do Ambiente dos Usuários

O setor de energia solar tem crescido rapidamente, exigindo maior eficiência no atendimento ao cliente e cálculos precisos para o dimensionamento de sistemas fotovoltaicos. Atualmente, muitos processos dependem de planilhas ou sistemas dispersos, o que pode gerar falhas no acompanhamento de clientes e erros no dimensionamento.

Com este sistema, espera-se centralizar o gerenciamento de clientes e automatizar cálculos complexos de dimensionamento solar, melhorando a precisão e a velocidade de atendimento.

### 5. Principais Necessidades dos Usuários

Para empresas e consultores de vendas:
- Organizar e acompanhar o ciclo de vendas, desde a captação até o fechamento.
- Automatizar cálculos de dimensionamento solar com base no consumo energético do cliente.

Para clientes:
- Visualizar resultados claros e precisos do dimensionamento solar e impacto no custo de energia.

### 6.	Alternativas Concorrentes

As alternativas existentes são, em geral, sistemas CRM genéricos ou calculadoras solares independentes. O diferencial do sistema proposto é integrar ambas as funcionalidades em uma única plataforma, voltada especificamente para o setor fotovoltaico.

### 7.	Visão Geral do Produto

O sistema é uma aplicação integrada de CRM e dimensionamento solar. Ele permite cadastrar clientes, organizar estados do ciclo de vendas (“esperando orçamento”, “orçamento enviado”, “aguardando resposta”, entre outros) e realizar cálculos precisos de dimensionamento com base nos dados de consumo do cliente.

### 8. Requisitos Funcionais

| Código | Nome | Descrição |
|:---  |:--- |:--- |
| RF01 | Cadastro de Clientes | Consultores podem cadastrar novos clientes no sistema |
| RF02 | Atualização de Status | Consultores atualizam o status dos clientes ao longo do processo de vendas |
| RF03 | Cálculo de Dimensionamento Solar | Sistema realiza o dimensionamento de sistemas fotovoltaicos com base no consumo mensal informado |
| RF04 | Relatório de Impacto Financeiro | Gera relatório sobre a economia esperada para o cliente após a instalação do sistema |
| RF05 | Consulta do Cliente | Cliente pode acompanhar o andamento do seu processo e visualizar resultados de cálculos |

### 9. Requisitos Não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
|:---  |:--- |:--- |:--- |:--- |
| RNF01 | Design responsivo | O sistema deve adaptar-se a qualquer tamanho de tela de dispositivo, seja computador, tablet ou smartphone. | Usabilidade | Obrigatório |
| RNF02 | Criptografia de dados | Senhas de usuários devem ser gravadas de forma criptografada no banco de dados. | Segurança | Obrigatório |
| RNF03 | Controle de acesso | Só usuários autenticados podem ter acesso ao sistema. | Segurança | Obrigatório |
| RNF04 | Tempo de resposta | A comunicação entre o servidor e o cliente deve ocorrer em tempo hábil. | Performance | Desejável |
| RNF05 | Sistema Web | A aplicação deve ser um site. | Arquitetura | Obrigatório |
| RNF06 | Dados pessoais | Os clientes não devem visualizar dados de outros clientes. | Privacidade | Obrigatório |

