# Agrupador de palavras

Esse script pega um lista de palavras na pasta data, e os agrupa semânticamente, retornando um csv em que cada linha representa um cluster diferente, podendo no final escolher o nome do arquivo csv, onde estará as palavras e o cluster na qual elas foram agrupadas, devido ao fato do K-Means ser um clustificador não determinístico, os grupos serão diferentes a cada vez que o algoritmo for executado. 
 
## Getting Started

Basta baixar o wordCluster.py com a pasta data, e rodar o script com algum compilador python com as devidas bibliotecas instaladas.

### Prerequisites

Bibliotecas utilizadas:
```
Numpy  
Pandas  
Gensim  
Scikit  
```

## Running the tests

Ao rodar o script, será requisitado ao termino da clusterização o nome de arquivo para ser salvo, salvando por fim em formato csv.
## Built With

* Anaconda
* Jupyter


## Authors

* **Laura Gouveia** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


