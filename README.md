# **Proposta de projeto** 

Ferramenta que auxilia no planejamneto de refeições e de compras para a manutenção de dietas baseadas na contabilização de macronutrientes ingeridos diariamente. 

# **Motivação** 

Muitas pessoas justificam a não adesão a dietas pela dificuldade em se planejar para preparar refeições e comprar alimentos para variar o cardápio sem sair da dieta.

# **Funcionamento**

O usuário cria um perfil no qual insere dados pessoais e o cardapio de uma dieta planejada por um nutricionista, com as refeições indicadas conforme planejamento do profissional. A ferramenta dispõe de um banco de dados no qual há a relação entre porções equivalentes de diferentes alimentos baseando-se nos macronutrientes de interesse de modo que o usuário seja capaz de consultar possíveis substituições sem prejudicar sua dieta. Além disso, a ferramenta possui um acervo de receitas elaboradas com base no cardápio inserido pelo usuário. Para auxiliar nas compras necessárias, com base no cardápio da dieta inserido, a ferramenta calcula a quantidade recomendada de alimento a se comprar para determinado intervalo de modo que seja possível suprir a dietar por todo esse periodo de modo flexível e organizado.

# **Desenvolvimento**

A plataforma utilizada para o desenvolvimento foi o Android Studio, permitindo desenvolver uma aplicação mobile de um modo mais prático utilizando Java.
Foram realizados tutoriais básicos encontrados na internet para a consolidação de conceitos iniciais como a criação de Activities, criação e edição de layouts tanto no código estático .xml quanto no editor, transferencia de dados e a navegação entre as Activities, além da melhoria da experiência do usuário.

# **Esboço**

Página inicial de Login

![image](https://user-images.githubusercontent.com/55112024/144920133-e5691385-f5f5-44f1-9c3b-22e5d0297db7.png)

Página principal onde encontram-se as refeições inseridas. O usuário pode editar (clicando sobre a refeição) ou remover (clique longo) uma refeição. Para adicionar uma nova refeição, basta clicar no "+"

![image](https://user-images.githubusercontent.com/55112024/144920164-aa218a0e-86ee-4e18-97a8-91505ea07d6d.png)

Formulário para a inserção ou edição de refeições

![image](https://user-images.githubusercontent.com/55112024/144920185-111d0cc5-a3c1-4d75-9576-42eecd732466.png)

Página com as opções de alimentos a serem substituídos divididos em macronutrientes/composição da refeição

![image](https://user-images.githubusercontent.com/55112024/144920200-c46e2170-16e4-4df6-b024-0425fb013243.png)

Exemplos de substituições em páginas que são acessadas a partir do clique nos respectivos botões

![image](https://user-images.githubusercontent.com/55112024/144920206-1c40302a-dedb-459e-9cc0-4a30d58f190a.png)
![image](https://user-images.githubusercontent.com/55112024/144920311-02140555-0716-498e-a291-4c878a6f3af0.png)
![image](https://user-images.githubusercontent.com/55112024/144920346-45725a47-afb4-4c52-b38b-d6e277d4a3b4.png)
![image](https://user-images.githubusercontent.com/55112024/144920375-dbac6869-2995-464a-bd7a-64b9c042957e.png)

## **Tutorial**

O arquivo apk referente ao projeto encontra-se no caminho "...\MealPlanner\app\build\outputs\apk\debug\app-debug.apk". Para realizar a instalação em um dispositivo Android, certifique-se conceder permissão a instalação de apps desconhecidos. Basta realizar o download e a instalação do .apk e executar o aplicativo a partir do dispositivo Android.
