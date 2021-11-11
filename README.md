# Consult Dollar to Real using an API
Consult Dollar(US$) to Real(BRL) using an API in Python language


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Output](#Output)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## Overview

### The challenge

Users should be able to:

- Consult Dollar(US$) to Real(BRL) using an API in Python language.

### Output

```
  Cotação do Dólar (USD) em Reais (BRL).
  Na data de 2021-11-11 14:27:18
  Cotação mais alta US$ 1,00 esta: R$ 5.4945 
  Cotação mais baixa US$ 1,00 esta: R$ 5.3889
```

## My process

### Built with

- Python 3
- API (https://docs.awesomeapi.com.br/api-de-moedas)


### What I learned

- Output
- Variables
- Loops
- Librarys
  ```py
    import requests
    import json
    import time
  ```
- Python Requests
  ```py
    req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
  ```
- Handle errors
  ```py
    try:            
        
    except Exception as erro:
        
  ```


## Author

- LinkedIn - [@oarthurvil](www.linkedin.com/in/oarthurvil)


## Acknowledgments

Thank you [Solyd](https://solyd.com.br/treinamentos/), the teacher Guilherme Junqueira for the course "Basic Python".
