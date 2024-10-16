# ordem de elaboração de projeto 

- Models --> criei modelos 

- utils.py -> criei utilitarios 

- views. py -> 


---
Para verificar a versão do pacote bcrypt instalado no seu ambiente Python, você pode usar o seguinte comando no terminal:

````bash
pip show bcrypt
````
ou para instalar :

````bash
pip install bcrypt    
````
 
---
## Migrar o Modelo para o Banco de Dados -> Comando para empacotar e migração:

``` Python
python manage.py makemigrations
python manage.py migrate
```

----
## comando para "rodar"
```python
python manage.py runserver
```