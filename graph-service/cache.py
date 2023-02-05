# import redis
# from fastapi import FastAPI

# def cache_middleware(app: FastAPI):
#     r = redis.Redis(host='localhost', port=6379, db=0)

#     async def cache(request, call_next):
#         # Récupérer la clé de cache à partir de la route et des paramètres de la requête
#         key = request.url.path + '?' + request.url.query
#         # Récupérer la valeur du cache si elle existe
#         value = r.get(key)
#         if value:
#             # Renvoyer la valeur du cache si elle existe
#             return value
#         # Appeler la fonction suivante dans la chaîne de middlewares si la valeur n'est pas en cache
#         response = await call_next(request)
#         # Mettre en cache la réponse
#         r.set(key, response)
#         return response
#     return cache