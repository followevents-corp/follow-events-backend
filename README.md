# follow-events-backend

<h1 align="center">
  <img alt="apiLogo" title="Follow Events" src='./assets/follow_events_logo.svg
  ' width="100px" />
</h1>
​
<h1 align="center">
   Follow Events - API
</h1>

<p align = "center">
    <b>Está é a documentação para o uso da API do Follow Events.</b>
</p>

<br>

<h3 align = "center">URL base da API: <b>"https://follow-events-api.herokuapp.com/"</b></h3>

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

Todos os campos são obrigatórios.

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
  "id": "id",
  "username": "John Doe",
  "name": "johndoe",
  "email": "johndoe@email.com",
  "profile_picture": null,
  "creator": false
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Login do usuário</b></summary>

<br>

Todos os campos são obrigatórios.

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
  "id": "id",
  "name": "johndoe",
  "username": "John Doe",
  "email": "johndoe@email.com",
  "profile_picture": null,
  "creator": true,
  "schedule": "http://localhost:5000/users/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc/schedule",
  "events": "http://localhost:5000/events/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc",
  "access_token": "acess_token"
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Buscar por um usuário</b></summary>

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
  "schedule": "http://localhost:5000/users/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc/schedule",
  "events": "http://localhost:5000/events/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc"
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Atualizar os dados de um usuário</b></summary>

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
  "schedule": "http://localhost:5000/users/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc/schedule",
  "events": "http://localhost:5000/events/f0b72181-00fc-4bc0-ad78-b73e31d9b7fc"
}
```

<br>

</details>

<details>

<summary style ="font-size: 18px"><b>Deletar um usuário</b></summary>

<br>

Só é possível deletar o usuário caso esteja logado com este usuário!

Está rota precisa da autorização do token!

<h3 style="color: yellow">Authorization: Bearer {access_token} </h3>

<br>

`PATCH/users/<user_id> - Formato da requisição`

**Não há** corpo de requisição.

<br>

<h3>Resposta Status Code &nbsp <span style="color: #40916c">200 OK</span></h3>

`Formato da resposta`

**Não há** corpo de resposta.

</details>
