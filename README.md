# Exoplanet-observer 🔭🪐 

<p> Uma simples aplicação que utiliza <a href="https://pt.m.wikipedia.org/wiki/M%C3%A9todos_de_detec%C3%A7%C3%A3o_de_exoplanetas#Fotometria_de_tr%C3%A2nsito">método de trânsito planetário</a> para extrair dados de variáveis antecedentes e
consequentes e determinar a probabilidade de existência de uma determinada estrela observada.</p>

## Arquitetura do projeto 📁
 📝 fuzzy-controller.py <br>
 📝 requirements.txt
 

### Como o script funciona:
<p> Basicamente script utiliza as variáveis antecedentes fornecidas como entrada:
Magnetude do brilho da estrela observada e a profundidade de salto observado. 


## Dependências
Esse projeto possui três dependências:

- **numpy**: Para tratamento de arrays
- **matplotlib**: Para plotagem de gráficos
- **scikit-fuzzy**: toolkit de ferramentas que utilizam a lógica Fuzzy

Para instalar as dependências do código, basta ir no diretório do projeto e executar o comando no terminal:
```console
pip install -r requirements.txt
```
## Executando o código: 
Agora para executar o código é necessário informar ao controller fuzzy as informações do brilho da estrela na escala de *magnetude aparente (m)*
e percentual da queda do brilho, ou seja, *profundidade de trânsito*.

Para isso basta substituir os dados de entrada presentes no arquivo **fuzzy-controller.py** (linha 42 e 43) para os valores em que você deseja saber a
probabilidade de existência de um exoplaneta.

No código abaixo, por exemplo, é atribuido os valores de *magnetude* absoluta e a *profundidade* de trânsito no qual foi encontrado o KEPLER-186F em sua estrela hospedeira: 

```python
# Set the input values (KEPLER-186F)
exoplanet_detection_simulation.input['stellar_brightness'] = 14.74
exoplanet_detection_simulation.input['transit_depth'] = 0.0071
```
O resultado obtido com os dados disponibilidados foram: 

```console
umpreto@karen:~/projects/exoplanet-observer$ python3 fuzzy-controller.py 
exoplanet_presence: 78.01%
```
<img src="https://user-images.githubusercontent.com/49316490/236650195-8bbbef65-0f1b-4089-aab2-05156e146d6d.png" width="600"></img>


