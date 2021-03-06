# follow-events-backend

<h1 align="center">
  <img alt="apiLogo" title="Follow Events" src='./assets/logo.png' width="150px" />
</h1>

<h1 align="center">
   Follow Events - API
</h1>

<p align = "center">
    <b>Está é a documentação para o uso da API do Follow Events.</b>
    Folllow events é uma plataforma de agendamento de eventos voltada ao mercado de Live Stream, facilitando ao usuário encontrar o que deseja e o produtor de conteúdo a destacar seus eventos e criar seus eventos de sorte pra atrair ou recompensar a audiência.
</p>

<br>

<h3 align = "center">URL base da API: <b><a target="_blank" href="https://follow-events-api.herokuapp.com/">https://follow-events-api.herokuapp.com/</a></b></h3>

<br>

---

<br>

<h2 align = "center">Rotas do usuário</h2>

<div align = "center">

`Por meio da rota de usuário será possível fazer as seguintes requisições:`

| Método                   | Descrição                   |
| ------------------------ | --------------------------- |
| `POST/users`             | Criar um novo usuário       |
| `POST/login`             | Realizar o login do usuário |
| `GET/users/<user_id>`    | Buscar por um usuário       |
| `PATCH/users/<user_id>`  | Editar um usuário           |
| `DELETE/users/<user_id>` | Deletar um usuário          |

</div>
<br>

<details>

<summary style ="font-size: 18px"><b>Criação de um novo usuário</b></summary>

<br>

<h3>Por meio desta rota é possível criar um novo usuário</h3>

<h3>Todos os campos são obrigatórios.</h3>

<br>

`POST/users - Formato da requisição`

```json
{
  "name": "johndoe",
  "username": "John Doe",
  "email": "johndoe@email.com",
  "password": "1234"
}
```

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">201 CREATED</span></h3>

`Formato da resposta`

```json
{
  "id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
  "username": "John Doe",
  "name": "johndoe",
  "email": "johndoe@email.com",
  "profile_picture": null,
  "creator": false
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Login do usuário</b></summary>

<br>

<h3>Por meio desta rota é possível realizar o login de um usuário</h3>

<h3>Todos os campos são obrigatórios.</h3>

<br>

`POST/login - Formato da requisição`

```json
{
  "name": "johndoe",
  "password": "1234"
}
```

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

```json
{
  "id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
  "name": "johndoe",
  "username": "John Doe",
  "email": "johndoe@email.com",
  "profile_picture": null,
  "creator": true,
  "schedule": "https://follow-events-api.herokuapp.com/users/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc/schedule",
  "events": "https://follow-events-api.herokuapp.com//events/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
  "access_token": "access_token"
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Buscar por um usuário</b></summary>

<br>

<h3>Por meio dessa rota é possível buscar os dados de um usuário</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`GET/users/<user_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

```json
{
  "id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
  "name": "John Doe",
  "username": "johndoe",
  "email": "johndoe@email.com",
  "profile_picture": null,
  "creator": true,
  "schedule": "https://follow-events-api.herokuapp.com/users/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc/schedule",
  "events": "https://follow-events-api.herokuapp.com/events/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc"
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Atualizar os dados de um usuário</b></summary>

<br>

<h3>Por meio dessa rota é possível atualizar os dados do usuário</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`PATCH/users/<user_id> - Formato da requisição`

```json
{
  "creator": true
}
```

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

```json
{
  "id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
  "name": "Joao",
  "username": "joao123",
  "email": "joao1234@gmail.com",
  "profile_picture": null,
  "creator": true,
  "schedule": "https://follow-events-api.herokuapp.com/users/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc/schedule",
  "events": "https://follow-events-api.herokuapp.com/events/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc"
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Deletar um usuário</b></summary>

<br>

<h3>Só é possível deletar o usuário caso esteja logado com este usuário!</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`DELETE/users/<user_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

**Não há** corpo de resposta.

<br>

</details>

<br>

---

<br>

<h2 align = "center">Rotas de eventos</h2>

<div align = "center">

`Por meio da rota de eventos será possível fazer as seguintes requisições:`

| Método                     | Descrição                                      |
| -------------------------- | ---------------------------------------------- |
| `POST/events`              | Criar um novo evento                           |
| `GET/events`               | Traz uma lista com todos os eventos            |
| `GET/events/<user_id>`     | Traz todos os eventos do usuário em especifico |
| `PATCH/events/<event_id>`  | Editar um evento                               |
| `DELETE/events/<event_id>` | Deletar um evento                              |

</div>

<br>

<details>

<summary style ="font-size: 18px"><b>Criar um novo evento</b></summary>

<br>

<h3>Por meio dessa rota é possível criar um novo evento</h3>

<h3>Todos os campos são obrigatóriso</h3>

<br>

Está rota precisa da autorização do token!

<br>

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>
<h3 style="color: yellow">Content-type: multipart/form-data</h3>

<br>

`POST/events - Formato da requisição`

Nesta rota terá que passar 2 arquivos multipart:

<b>file</b> : Será um arquivo do tipo imagem ou vídeo, com um máximo de 10mb.

<b>data</b> : Será um json no formato abaixo.

```json
{
  "name": "evento",
  "description": "descrição do evento",
  "event_link": "plataforma",
  "event_date": "Fri, 13 May 2022 15:21:41 GMT",
  "categories": ["Games", "Live"]
}
```

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">201 CREATED</span></h3>

`Formato da resposta`

```json
{
  "id": "b9caf35c-02fe-4e84-986a-1ff46c48e562",
  "name": "Evento12",
  "description": "uma descrição para testar",
  "event_date": "Fri, 13 May 2022 15:21:41 GMT",
  "type_banner": "image",
  "link_banner": "https://follow-events.s3.amazonaws.com/19b8e308-868d-4d02-b4a4-e567544e2b16.png",
  "event_link": "twitch",
  "created_at": "Sun, 01 May 2022 01:16:05 GMT",
  "creator_id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
  "quantity_users": 0,
  "categories": ["Games"],
  "comments": "https://follow-events-api.herokuapp.com/events/b9caf35c-02fe-4e84-986a-1ff46c48e562/comments",
  "giveaway": "https://follow-events-api.herokuapp.com/events/b9caf35c-02fe-4e84-986a-1ff46c48e562/giveaway"
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Trazer uma lista com todos os eventos</b></summary>

<br>

<h3>Por meio desta rota será possível ter uma lista com todos os eventos cadastrados.</h3>

<br>

`GET/events - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

```json
[
  {
    "id": "c97820b0-e0d6-45b8-b554-38d3e6dc798d",
    "name": "Evento1344444666344",
    "description": "uma descrição",
    "event_date": "12/12/2023",
    "type_banner": "image",
    "link_banner": "https://follow-events.s3.amazonaws.com/2584339d-1df6-40d0-9457-39f2dff24585.png",
    "event_link": "link",
    "created_at": "Fri, 29 Apr 2022 02:00:19 GMT",
    "creator_id": "60762d5d-0946-4702-a213-b8b070e54350",
    "quantity_users": 0,
    "categories": ["Games"],
    "comments": "https://follow-events-api.herokuapp.com/events/c97820b0-e0d6-45b8-b554-38d3e6dc798d/comments",
    "giveaway": "https://follow-events-api.herokuapp.com/events/c97820b0-e0d6-45b8-b554-38d3e6dc798d/giveaway"
  },
  {
    "id": "44d41135-36e5-432d-8c05-6ce0d66e7ce1",
    "name": "Evento212121",
    "description": "Sua descrição",
    "event_date": "12/12/2023",
    "type_banner": "video",
    "link_banner": "https://follow-events.s3.amazonaws.com/51910025-4990-4e75-baf2-f8cb08b57dcf.mp4",
    "event_link": "link",
    "created_at": "Fri, 29 Apr 2022 22:59:34 GMT",
    "creator_id": "60762d5d-0946-4702-a213-b8b070e54350",
    "quantity_users": 0,
    "categories": ["Live"],
    "comments": "https://follow-events-api.herokuapp.com/events/44d41135-36e5-432d-8c05-6ce0d66e7ce1/comments",
    "giveaway": "https://follow-events-api.herokuapp.com/events/44d41135-36e5-432d-8c05-6ce0d66e7ce1/giveaway"
  },
  {
    "id": "efa50993-b3e5-46ee-a0cf-82864d2502e1",
    "name": "Evento212121",
    "description": "coloque seu texto aqui",
    "event_date": "Fri, 13 May 2022 15:21:41 GMT",
    "type_banner": "image",
    "link_banner": "https://follow-events.s3.amazonaws.com/c428e2b2-6aba-40dd-bb9d-2f58e79acc80.png",
    "event_link": "youtube",
    "created_at": "Sat, 30 Apr 2022 01:55:48 GMT",
    "creator_id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
    "quantity_users": 0,
    "categories": ["Sports"],
    "comments": "https://follow-events-api.herokuapp.com/events/efa50993-b3e5-46ee-a0cf-82864d2502e1/comments",
    "giveaway": "https://follow-events-api.herokuapp.com/events/efa50993-b3e5-46ee-a0cf-82864d2502e1/giveaway"
  }
]
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Trazer todos eventos de usuário</b></summary>

<br>

<h3>Por meio desta rota será possível listar os eventos de um usuário.</h3>

<br>

`GET/events/<user_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

```json
[
  {
    "id": "efa50993-b3e5-46ee-a0cf-82864d2502e1",
    "name": "Evento 1",
    "description": "uma descrição",
    "event_date": "Fri, 13 May 2022 15:21:41 GMT",
    "type_banner": "image",
    "link_banner": "https://follow-events.s3.amazonaws.com/c428e2b2-6aba-40dd-bb9d-2f58e79acc80.png",
    "event_link": "youtube",
    "created_at": "Sat, 30 Apr 2022 01:55:48 GMT",
    "creator_id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
    "quantity_users": 0,
    "categories": ["Games"],
    "comments": "https://follow-events-api.herokuapp.com/events/efa50993-b3e5-46ee-a0cf-82864d2502e1/comments",
    "giveaway": "https://follow-events-api.herokuapp.com/events/efa50993-b3e5-46ee-a0cf-82864d2502e1/giveaway"
  },
  {
    "id": "efa50993-b3e5-46ee-a0cf-82864d2502e1",
    "name": "Evento 2",
    "description": "descrição do usuário",
    "event_date": "Fri, 13 May 2022 15:21:41 GMT",
    "type_banner": "image",
    "link_banner": "https://follow-events.s3.amazonaws.com/c428e2b2-6aba-40dd-bb9d-2f58e79acc80.png",
    "event_link": "youtube",
    "created_at": "Sat, 30 Apr 2022 01:55:48 GMT",
    "creator_id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
    "quantity_users": 0,
    "categories": ["Music"],
    "comments": "https://follow-events-api.herokuapp.com/events/efa50993-b3e5-46ee-a0cf-82864d2502e1/comments",
    "giveaway": "https://follow-events-api.herokuapp.com/events/efa50993-b3e5-46ee-a0cf-82864d2502e1/giveaway"
  }
]
```

</details>

<details>

<summary style ="font-size: 18px"><b>Editar um evento</b></summary>

<br>

<h3>Por meio desta rota será possível editar um evento.</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>
<h3 style="color: yellow">Content-type: multipart/form-data</h3>

<br>

Nesta rota poderá passar 2 arquivos multipart:

<b>file</b> : Será um arquivo do tipo imagem ou vídeo, com um máximo de 10mb.

<b>data</b> : Será um json com as chaves e valores.

Na edição de um usuário pode se atualizar todas as caracteristicas passadas no exemplo abaixo:

`PATCH/events/<user_id> - Formato da requisição`

```json
{
  "name": "Evento 2",
  "description": "descrição do usuário",
  "event_date": "Fri, 13 May 2022 15:21:41 GMT",
  "event_link": "youtube",
  "categories": ["Music"]
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Deletar um evento</b></summary>

<br>

<h3>Por meio desta rota é possível deletar um evento</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`DELETE/users/<user_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

**Não há** corpo de resposta.

</details>

<br>

---

<br>

<h2 align = "center">Rotas de comentários</h2>

<div align = "center">

`Por meio da rota de eventos será possível fazer as seguintes requisições:`

| Método                            | Descrição                         |
| --------------------------------- | --------------------------------- |
| `POST/events/<event_id>/comments` | Criar comentário em um evento     |
| `GET/events/<event_id>/comments`  | Busca os comentários de um evento |
| `PATCH/comments/<comment_id>`     | Atualizar um comentário           |
| `DELETE/comments/<comment_id>`    | Deletar um comentário             |

</div>

<br>

<details>

<summary style ="font-size: 18px"><b>Adicionar um comentário ao evento</b></summary>

<br>

<h3>Por meio desta rota será possível adicionar um comentário a um evento.</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`POST/events/<event_id>/comments - Formato da requisição`

```json
{
  "comment": "É o melhor evento do ano !!"
}
```

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">201 CREATED</span></h3>

`Formato da resposta`

```json
{
  "comment": "É o melhor evento do ano !!"
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Trazer a lista de comentários de um evento</b></summary>

<br>

<h3>Por meio desta rota será buscar os comentários</h3>

<br>

`GET/events/<event_id>/comments - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

```json
[
  {
    "id": "98542e8d-6adb-4993-8e26-a76cdf637dca",
    "comment": "É o melhor evento do ano !!",
    "created_at": "Sun, 01 May 2022 19:16:49 GMT",
    "user_id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
    "username": "joao123",
    "profile_picture": null
  },
  {
    "id": "795fd221-3f03-4f40-b954-4e9a5d2ff413",
    "comment": "É o melhor evento do ano !!",
    "created_at": "Sun, 01 May 2022 19:16:56 GMT",
    "user_id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
    "username": "joao123",
    "profile_picture": null
  },
  {
    "id": "b395305c-4297-4579-8f89-e8f5199bbb1b",
    "comment": "É o melhor evento do ano !!",
    "created_at": "Sun, 01 May 2022 19:16:57 GMT",
    "user_id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
    "username": "joao123",
    "profile_picture": null
  }
]
```

</details>

<details>

<summary style ="font-size: 18px"><b>Atualizar um comentário de evento</b></summary>

<br>

<h3>Por meio desta rota será possível atualizar um comentário.</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`PATCH/comments/<comment_id> - Formato da requisição`

```json
{
  "comment": "É o melhor evento do ano !!"
}
```

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

```json
{
  "id": "98542e8d-6adb-4993-8e26-a76cdf637dca",
  "comment": "olá",
  "created_at": "Sun, 01 May 2022 19:16:49 GMT",
  "user_id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
  "username": "joao123",
  "profile_picture": null
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Deletar um comentário de evento</b></summary>

<br>

<h3>Por meio desta rota será possível deletar um comentário a um evento.</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`DELETE/comments/<comment_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">204 NO CONTENT</span></h3>

`Formato da resposta`

**Não há** corpo de reposta.

</details>
  
 ---
<br>

<h2 align = "center">Rotas do calendário</h2>

<div align = "center">

`Por meio da rota do calendário será possível fazer as seguintes requisições:`

| Método                                       | Descrição                                             |
| -------------------------------------------- | ----------------------------------------------------- |
| `POST/users/<user_id>/schedule`              | Criar um novo evento no calendário pessoal            |
| `GET/users/<user_id>/schedule`               | Lista todos os eventos do calendário pessoal          |
| `DELETE/users/<user_id>/schedule/<event_id>` | Deletar um evento do calendário do calendário pessoal |

</div>
<br>

<details>

<summary style ="font-size: 18px"><b>Criação de um novo evento no calendário</b></summary>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

<h3>Campo obrigatório.</h3>

`POST/users/<user_id>/schedule - Formato da requisição`

```json
{
  "event_id": "f0b72181-00fc-4bc0-ad78-b73e31d9b7fc"
}
```

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">201 CREATED</span></h3>

`Formato da resposta`

```json
{
  "message": "Event added to calendar."
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Buscar eventos no calendário do usuário</b></summary>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`GET /users/<user_id>/schedule - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

```json
[
  {
    "id": "179a35d9-2746-4724-a938-d1ed60265b16",
    "name": "Live do Stag",
    "description": "Final da Copa do Mundo",
    "event_date": "Fri, 13 May 2022 15:21:41 GMT",
    "type_banner": "image",
    "link_banner": "https://follow-events.s3.amazonaws.com/712b4496-2600-4ea9-82ce-087941f6bc71.png",
    "event_link": "www.twitch.tv",
    "created_at": "Sun, 01 May 2022 19:09:52 GMT",
    "creator_id": "b4e9e4f2-ef98-49d9-a864-03ad432c7cee",
    "quantity_users": 1,
    "categories": ["Futebol"],
    "comments": "https://follow-events-api.herokuapp.com/events/179a35d9-2746-4724-a938-d1ed60265b16/comments",
    "giveaway": "https://follow-events-api.herokuapp.com/events/179a35d9-2746-4724-a938-d1ed60265b16/giveaway"
  }
]
```

</details>

<details>

<summary style ="font-size: 18px"><b>Deletar um evento do calendário pessoal</b></summary>

<br>

<h3>Só é possível deletar o evento do calendário caso esteja logado com este usuário!</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`DELETE/users/<user_id>/schedule/<event_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">204 NO CONTENT</span></h3>

**Não há** retorno.

</details>

<br>

---

<br>

<h2 align = "center">Rotas de eventos de sorte</h2>

<div align = "center">

`Por meio da rota do calendário será possível fazer as seguintes requisições:`

| Método                                           | Descrição                        |
| ------------------------------------------------ | -------------------------------- |
| `POST/events/<event_id>/giveaway`                | Criar um novo evento de sorte    |
| `GET/events/<event_id>/giveaway`                 | Listar todos os eventos de sorte |
| `PATCH/events/<event_id>/giveaway/<giveaway_id>` | Editar um evento de sorte        |
| `DELETE/events/<event_id>/giveaway/<giveaway_id` | Deletar um evento de sorte       |

</div>
<br>

<details>

<summary style ="font-size: 18px"><b>Criação de um novo evento de sorte</b></summary>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

<h3>Campo obrigatório.</h3>

`POST/events/<event_id>/giveaway - Formato da requisição`

```json
{
  "name": "Sorteio Hamburgão",
  "description": "Melhor X-tudo de Colatina-ES",
  "award": "X-tudão",
  "award_picture": "https://xtudoreceitas.com/wp-content/uploads/xtudo-480x270.png"
}
```

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">201 CREATED</span></h3>

`Formato da resposta`

```json
{
  "id": "8c2a81ea-e82b-46ba-a69f-71718bbcdcae",
  "name": "Sorteio Hamburgão",
  "description": "Melhor X-tudo de Colatina-ES",
  "award": "X-tudão",
  "award_picture": "https://xtudoreceitas.com/wp-content/uploads/xtudo-480x270.png",
  "active": true,
  "created_at": "Mon, 02 May 2022 18:54:03 GMT",
  "event_id": "af38606a-b45c-417d-99e5-5deb8163d698"
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Buscar eventos de sorte</b></summary>

<br>

Está rota **NÃO** precisa da autorização do token!

<br>

`GET/events/<event_id>/giveaway - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

```json
[
  {
    "id": "8c2a81ea-e82b-46ba-a69f-71718bbcdcae",
    "name": "Sorteio Hamburgão",
    "description": "Melhor X-tudo de Colatina-ES",
    "award": "X-tudão",
    "award_picture": "https://xtudoreceitas.com/wp-content/uploads/xtudo-480x270.png",
    "active": true,
    "created_at": "Mon, 02 May 2022 18:54:03 GMT",
    "event_id": "af38606a-b45c-417d-99e5-5deb8163d698"
  }
]
```

</details>
  
<details>

<summary style ="font-size: 18px"><b>Atualizar um evento de sorte</b></summary>

<br>

<h3>Só é possível atualizar o evento de sorte caso esteja logado e seja o criador do evento!</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`PATCH/events/<event_id>/giveaway/<giveaway_id> - Formato da requisição`

```json
{
  "name": "Sk8 Manaus",
  "description": "Sorteio aos inscritos do canal",
  "award": "Skate Blacksheep"
}
```

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

```json
{
  "id": "836b5372-f1b4-43d1-b387-7532507c1f74",
  "name": "Sk8 Manaus",
  "description": "Sorteio aos inscritos do canal",
  "award": "Skate Blacksheep",
  "award_picture": "https://truck.com/wp-content/uploads/sk8-480x270.png",
  "active": true,
  "created_at": "Mon, 02 May 2022 19:26:36 GMT",
  "event_id": "af38606a-b45c-417d-99e5-5deb8163d698"
}
```

</details>

<details>

<summary style ="font-size: 18px"><b>Deletar um evento de sorte</b></summary>

<br>

<h3>Só é possível deletar o evento de sorte caso esteja logado e seja o criador do evento</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`PATCH/events/<event_id>/giveaway/<giveaway_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

```json
{
  "message": "Event deleted from calendar."
}
```

</details>

---

<br>

<h2 align = "center">Possíveis erros nas requisições</h2>

<br>

<details>

<summary style ="font-size: 18px"><b>Possíveis erros nas requisições 400 BAD REQUEST</b></summary>

<br>

<h3>Caso uma chave não seja encontrada, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "missing_keys": ["name"]
}
```

<br>

<h3>Caso passe um email no formato incorreto terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Email format not acceptable: joao@, try ex.: your_mail@your_provider.com"
}
```

<br>

<h3>Caso uma chave não tenha a tipagem correta, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": {
    "name": "must be a string"
  }
}
```

<br>

<h3>Caso alguma chave tenha valores nulos, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Incoming value is empty."
}
```

<br>

<h3>Caso o name tenha mais que 100 caracteres, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Name has to be less than 100 characters. If your name is greater than that, try abbreviate it. :D"
}
```

<br>

<h3>Caso o username tenha menos de 6 caracteres ou mais de 30, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Username has to be 6 to 30 characters."
}
```

<br>

<h3>Caso o evento não esteja em uma data no futuro, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Event must be in the future"
}
```

<br>

<h3>Caso o id seja inválido, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "The id 23b15222c13e-23b1-4f31-a021-8455f1cbdae3 is not valid."
}
```

<br>

<h3>Caso o link do evento seja inválido, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "This link violates the platform rules"
}
```

<br>

<h3>Categoria do tipo incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": {
    "category 5": "must be a valid string",
    "category True": "must be a valid string",
    "category 4.6": "must be a valid string"
  }
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Possíveis erros nas requisições 401 UNAUTHORIZED</b></summary>

<br>

<h3>Caso não tenha passado nenhum token, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">401 UNAUTHORIZED</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

<h3>Caso passe um token de outro usuário, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">401 UNAUTHORIZED</span></h3>

`Formato da resposta`

```json
{
  "error": "Unauthorized"
}
```

<br>

<h3>Caso o token tenha expirado, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">401 UNAUTHORIZED</span></h3>

`Formato da resposta`

```json
{
  "error": "The token has expired"
}
```

<br>

<h3>Caso o token seja inválido, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">401 UNAUTHORIZED</span></h3>

`Formato da resposta`

```json
{
  "error": "Invalid token."
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Possíveis erros nas requisições 403 FORBIDDEN</b></summary>

<br>

<h3>Caso o email ou a senha sejam inválidos, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">403 FORBIDDEN</span></h3>

`Formato da resposta`

```json
{
  "error": "Invalid email or password."
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Possíveis erros nas requisições 404 NOT FOUND</b></summary>

<br>

<h3>Caso o id não seja encontrado, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">404 NOT FOUND</span></h3>

`Formato da resposta`

```json
{
  "error": "The id 5222c13e-23b1-4f31-a021-8455f1cbdae3 is not in database."
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Possíveis erros nas requisições 409 CONFLICT</b></summary>

<br>

<h3>Caso o username já existam, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">409 CONFLICT</span></h3>

`Formato da resposta`

```json
{
  "error": "Username already exists"
}
```

<br>

<h3>Caso o email já existam, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">409 CONFLICT</span></h3>

`Formato da resposta`

```json
{
  "error": "Email already exists"
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Possíveis erros nas requisições 413 REQUEST ENTITY TOO LARGE</b></summary>

<br>

<h3>Caso o arquivo seja maior que 10mb, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">413 REQUEST ENTITY TOO LARGE</span></h3>

`Formato da resposta`

```json
{
  "error": "The suported file is until 10MB"
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Possíveis erros nas requisições 415 UNSUPPORTED MEDIA TYPE</b></summary>

<br>

<h3>Caso o arquivo seja diferente de um vídeo ou image, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">415 UNSUPPORTED MEDIA TYPE</span></h3>

`Formato da resposta`

```json
{
  "error": "Only image and video files are supported"
}
```

<br>

</details>

<br>

<br>

Copyright (c) Follow Events, Inc. and its affiliates.
