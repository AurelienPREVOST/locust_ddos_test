# Documentation

https://docs.locust.io/en/stable/

# Installation  

Pour utiliser locust on s'assure d'abord d'avoir à minima la configuration système requise
 
python =>3.9
```
python -v

#should return:
Python 3.12.4 
>>>
```

locust
```
locust -v
#should return versionning

#or for me
PS C:\Users\aurelien.PREVOST\Documents\Code\fake_ddos> python -m locust -f locustfile.py -V
locust 2.29.1 from C:\Users\aurelien.PREVOST\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\locust (Python 3.12.4, OpenSSL 3.0.13)
PS C:\Users\aurelien.PREVOST\Documents\Code\fake_ddos>
```


particularitée si besoin de lancer en direct cause privilège administrateur manquant ou variable d'environnement introuvable (exemple PC bureau)

```
python -m locust -f locustfile.py --host=http://siteatester.com
```


Une fois lancé on accède à localhost:8089 et on peux faire ses tests.


le locustfile.py doit être modifié pour adapté les endpoint et type de requete (exemple post/get...) ainsi que les data envoyé etc (header necessaire probablement etc)




# -------------------/!\ ATTENTION /!\-------------------

Par défaut, Locust envoie toutes les requêtes depuis l'IP de la machine où il est exécuté. Cela signifie que si vous lancez un test de charge depuis une seule machine, toutes les requêtes proviendront de la même IP. En fonction des paramètres de sécurité de votre serveur ou des limites de rate-limiting mises en place, cela pourrait mener à un bannissement temporaire ou permanent de cette IP.

# Solutions pour éviter le bannissement :
## 1- Utiliser des proxies :

Vous pouvez configurer Locust pour utiliser différents proxies, ce qui permettra de répartir les requêtes sur plusieurs IP. Cela nécessite d'avoir accès à plusieurs serveurs proxy.

## 2- Déployer Locust sur plusieurs machines :

Une approche courante est de déployer Locust sur plusieurs machines (utilisateurs virtuels) pour répartir les requêtes. Vous pouvez utiliser une architecture maître-esclaves pour cela.
Locust supporte une configuration distribuée où une machine agit comme maître et contrôle plusieurs esclaves. Voici comment vous pouvez le configurer :

# Configuration distribuée de Locust :
## 1- Lancer le maître :

```
#-sh-
locust -f locustfile.py --master
```

## 2- Lancer les esclaves :
Sur chaque machine esclave, exécutez la commande suivante en remplaçant MASTER_IP par l'adresse IP de la machine maître :

```
#-sh-
locust -f locustfile.py --worker --master-host=MASTER_IP
```

# Exemple de script Locust pour utiliser des proxies :
Pour utiliser des proxies, vous pouvez configurer des proxies dans vos requêtes HTTP. Voici un exemple simple en utilisant la bibliothèque requests qui peut être intégrée avec Locust :

```
#-python-
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def index(self):
        proxies = {
            "http": "http://your-proxy:port",
            "https": "http://your-proxy:port",
        }
        self.client.get("/", proxies=proxies)
    
    @task
    def about(self):
        proxies = {
            "http": "http://your-proxy:port",
            "https": "http://your-proxy:port",
        }
        self.client.get("/about", proxies=proxies)
```

# Utiliser des services de tests de charge en ligne :
Il existe également des services de tests de charge en ligne comme BlazeMeter, Loader.io, ou Flood.io qui peuvent exécuter des tests de charge à partir de multiples IP, ce qui peut aider à éviter les problèmes de bannissement.

En résumé, pour éviter que votre IP soit bannie lors d'un test de charge avec Locust :

> Utilisez des proxies pour répartir les requêtes sur plusieurs IP.  
> Déployez Locust en configuration distribuée sur plusieurs machines.  
> Envisagez d'utiliser des services de tests de charge en ligne.  