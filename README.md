# follow-events-backend

<h1 align="center">
  <img alt="apiLogo" title="Follow Events" src='./assets/logo.png' width="150px" />
</h1>

<h1 align="center">
   Follow Events - API
</h1>

<p align = "center">
    <b>Está é a documentação para o uso da API do Follow Events.</b>
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

<h3>Caso passe um email invalido, terá o seguinte retorno.</h3>

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

<h3>Caso o token seja inválido ou esteja incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

<h3>Caso o email, já exista, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">409 CONFLICT</span></h3>

`Formato da resposta`

```json
{
  "error": "Email already exists."
}
```

<br>

<h3>Caso o username já exista, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">409 CONFLICT</span></h3>

`Formato da resposta`

```json
{
  "error": "Username already exists."
}
```

<br>

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

<br>

<h3>Caso uma chave não seja encontrada, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "missing_keys": ["email"]
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

<h3>Caso a senha ou email sejam inválidos, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">404 NOT FOUND</span></h3>

`Formato da resposta`

```json
{
  "error": "Invalid email or password."
}
```

<br>

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

<br>

<h3>Caso o token seja inválido ou esteja incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

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

<h3>Caso o token seja inválido ou esteja incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

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

<h3>Caso o token seja inválido ou esteja incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

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

<details>

<summary style ="font-size: 18px"><b>Modelo de requisição no front end</b></summary>

```js
let bodyFormData = new FormData();
bodyFormData.append('data',{"name": "Evento1",
  "description": "uma descrição para testar",
  "event_link": "twitch",
  "event_date": "Fri, 13 May 2022 15:21:41 GMT",
  "categories": ["Games"]
});
bodyFormData.append('file', imageFile);

fetch("https://follow-events-api.herokuapp.com/events", {
  const response = await axios({
      method: 'post',
      url: 'your_api_url',
      data: bodyFormData,
      headers: {
          'Content-Type': `multipart/form-data`,
      },
  });
```

</details>

<br>

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

<h3>Caso o token seja inválido ou esteja incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

<h3>Caso o usuário não tenha permissão para criar eventos, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">401 UNAUTHORIZED</span></h3>

`Formato da resposta`

```json
{
  "error": "Must be a content creator, to create a event."
}
```

<br>

<h3>Caso o arquivo não seja uma image ou vídeo, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">415 UNSUPPORTED MEDIA TYPE</span></h3>

`Formato da resposta`

```json
{
  "error": "Only image and video files are supported"
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

<br>

<h3>Caso o id do usuário não seja encontrado, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "The id f0b72181-00fc-4bc0-ad78-b73e31d9b7 is not valid."
}
```

<br>

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

<br>

<h3>Caso o token seja inválido ou esteja incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

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

<br>

<h3>Caso o token seja inválido ou esteja incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

<h3>Caso o id não sejá encontrado, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "The id 047f9b6a-b964-4387-87d5-39719cc01028 is not in database."
}
```

<br>

</details>

<br>

---

<br>

<h2 align = "center">Rotas de categorias</h2>

<div align = "center">

`Por meio da rota de eventos será possível fazer as seguintes requisições:`

| Método                            | Descrição                         |
| --------------------------------- | --------------------------------- |
| `POST/events/<event_id>/comments` | Criar comentário em um evento     |
| `GET/events/<event_id>/comments`  | Busca os comentários de um evento |
| `PATCH/comments/<comments_id>`    | Atualizar um comentário           |
| `DELETE/comments/<comments_id>`   | Deletar um comentário             |

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

`GET/events/<user_id> - Formato da requisição`

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

<br>

<h3>Caso não passe a chave comment</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "missing_keys": ["comment"]
}
```

<br>

<h3>Caso não seja passado o token, terá o seguinte retorno</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

<h3>Caso o evento não seja encontrado, terá o seguinte retorno</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "The id 4efa7076-d7be-4c33-8e9a-b3c3bb506c is not valid."
}
```

<br>

<h3>Caso o token passado seja inválido, terá o seguinte retorno</h3>

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

<summary style ="font-size: 18px"><b>Trazer a lista de comentários de um evento</b></summary>

<br>

<h3>Por meio desta rota será possível adicionar um comentário a um evento.</h3>

<br>

`GET/events/<user_id> - Formato da requisição`

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

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Atualizar um comentário de evento</b></summary>

<br>

<h3>Por meio desta rota será possível atualizar um comentário a um evento.</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`GET/events/<user_id> - Formato da requisição`

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

<br>

<h3>Caso fique faltando a chave comments, terá o seguinte retorno</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "missing_keys": ["comment"]
}
```

<br>

<h3>Caso não seja passado o token, terá o seguinte retorno</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

<h3>Caso o token não seja valido, terá o seguinte retorno</h3>

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

<summary style ="font-size: 18px"><b>Deletar um comentário de evento</b></summary>

<br>

<h3>Por meio desta rota será possível deletar um comentário a um evento.</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`GET/events/<user_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

**Não há** corpo de reposta.

<br>

<h3>Caso não seja passado o token, terá o seguinte retorno</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

<h3>Caso o id não sejá encontrado, terá o seguinte retorno</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "The id 98542e8d-6adb-4993-8e26-a76cdf637d is not valid."
}
```

<br>

<h3>Caso o token não sejá válido, terá o seguinte retorno</h3>

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
  
 ---
<br>

<h2 align = "center">Rotas do calendário</h2>

<div align = "center">

`Por meio da rota do calendário será possível fazer as seguintes requisições:`

| Método                   | Descrição                   |
| ------------------------ | --------------------------- |
| `POST/users/<user_id>/schedule`| Criar um novo evento no calendário|
| `GET/users/<user_id>/schedule`| Lista todos os eventos do calendário |
| `DELETE/users/<user_id>/schedule/<event_id>` | Deletar um evento do calendário|

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

<br>

<br>

<h3>Caso o id do evento já tenha sido registrado no calendário.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">409 CONFLICT</span></h3>

`Formato da resposta`

```json
{
  "error": "Event already added to user's schedule"
}
```

<br>

<h3>Caso o id do evento não seja encontrado, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "The id 'f02c2181-99fc-4bc0-ad78-b73e39d9b7fc' is not in database."
}
```

<br>

<br>

<h3>Caso o id do evento não seja válido.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "The id f02c2181-99fc-4bc0-ad78-b73e39d9b7f is not valid."
}
```

<br>

<h3>Caso passe a chave errada, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "missing_keys": [
    "event_id"
  ]
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
    "event_id": "must be a string"
  }
}
```

<br>

<h3>Caso o token seja inválido ou esteja incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>



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
    "categories": [
      "Futebol"
    ],
    "comments": "https://follow-events-api.herokuapp.com/events/179a35d9-2746-4724-a938-d1ed60265b16/comments",
    "giveaway": "https://follow-events-api.herokuapp.com/events/179a35d9-2746-4724-a938-d1ed60265b16/giveaway"
  }
]
```

<br>

<h3>Caso o id do usuário não seja encontrado.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">404 NOT FOUND</span></h3>

`Formato da resposta`

```json
{
  "error": "The id b4e9e4f2-ef98-49d9-a864-03ad432c7aee is not in database."
}
```


<br>

<h3>Caso o token seja inválido ou esteja incorreto, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">401 UNAUTHORIZED</span></h3>

`Formato da resposta`

```json
{
  "error": "Invalid token."
}
```

<br>

<br>

<h3>Caso o token não seja passado.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">401 UNAUTHORIZED</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

</details>

<details>


<summary style ="font-size: 18px"><b>Deletar um compromisso do usuário</b></summary>

<br>

<h3>Só é possível deletar o evento do calendário caso esteja logado com este usuário!</h3>

<br>

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`DELETE/users/<user_id>/schedule/<event_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

```json
{
    "message": "Event deleted from calendar."
}
```

<br>

<h3>Caso o id do compromisso não seja encontrado, terá o seguinte retorno.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">404 NOT FOUND</span></h3>

`Formato da resposta`

```json
{
  "error": "Schedule not found"
}
```

<br>

<br>

<h3>Caso o token não seja passado.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "Missing authorization token"
}
```

<br>

<br>

<h3>Caso o id passado não seja válido.</h3>

<br>

<h3>Resposta Status Code &nbsp <span style="color: yellow">400 BAD REQUEST</span></h3>

`Formato da resposta`

```json
{
  "error": "The id 39761194-1352-426e-aa16-b8e38635b17 is not valid."
}
```

<br>

<br>



</details>

<br>

---
