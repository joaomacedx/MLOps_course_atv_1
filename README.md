# Curso MLOps Instituto de Computação UFBA [Atividade 1](./atividade_solicitada.md):

##### Aluno 👨🏾‍🎓:  João Gabriel dos Reis Hermida Macêdo

## Configuração do Ambiente ⚙️: 
**Certifique-se de ter o Python instalado em sua máquina.**
- Este projeto foi desenvolvido utilizando python 3.12.3 

## Como configurar o ambiente de desenvolvimento:

### Clone o repositório:

```bash
$ git clone https://github.com/joaomacedx/MLOps_course_atv1.git
```

### Crie um ambiente virtual:

```bash
$ python -m venv MLOps_course_atv1
```

### Ative o ambiente virtual:

**Para usuários de Linux ou Unix:**

```bash
$ source MLOps_course_atv1/bin/activate
```

**Para usuários de Windows:**

```powershell
PS> .\MLOps_course_atv1\Scripts\activate.ps1
```

### Com o ambiente virtual ativado instale as dependências:

```bash
$ pip install -r requirements.txt
```

### Inicie a aplicação 🚀:
```bash
$ cd src
$ python server.py
```


## Documentação da API 📚

#### Usuário envia mensagem utilizando linguagem natural que será classificada para definir o retorno (Dia da Semana ou Horário)

```http
  POST /message
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `text` | `string` | **Obrigatório**. Mensagem |
#### Retorna o horário
####  Mensagem de exemplo: `Que horas são?`
``` json 
  {
    "response": "20/05/2024 19:48"
  }
```
#### Retorna o dia da semana
####  Mensagem de exemplo: `Qual é o dia hoje?`
``` json 
  {
  "response": "segunda"
  }
```
### Evidência da aplicação funcionando💯: 
![DIA DA SEMANA](/assets/teste_dia_da_semana.png)
![HORÁRIO](/assets/teste_horas.png)


