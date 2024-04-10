<details>
 <summary><code>POST</code> <code>JSON</code> <code><b>/add_statistic_test/add_game_match</b></code></summary>

##### Parameters

> | name | type     | data type | description    |
> |------|----------|-----------|----------------|
> | None | required | JSON      | GameMatch data |

##### JSON parameters

> | name          | type         | data type | description |
> |---------------|--------------|-----------|-------------|
> | datestart     | not required | String    | "Y.m.d"     |
> | durationmatch | not required | String    | "M:S"       |
> | game          | not required | String    |             |
> | idlocation    | not required | Int       |             |
> | idsession     | not required | Int       |             |
> | modes         | not required | String    |             |
> | playedmaps    | not required | String    |             |
> | players       | not required | Int       |             |
> | submodes      | not required | String    |             |
> | timestart     | not required | String    | "H:M:S"     |
> | timeend       | not required | String    | "H:M:S"     |

##### Responses

> | http code | content-type       | response    |
> |-----------|--------------------|-------------|
> | `201`     | `application/json` | `{"id": 1}` |

##### Example cURL

> ```javascript
>  curl --header "Content-Type: application/json" --request POST --data "{\"datestart\": \"2024.01.31\",\"durationmatch\": \"15:30\",\"game\": \"Strike\",\"idlocation\": 1,\"idsession\": 1,\"modes\": \"TDM\",\"playedmaps\": \"CyberPunk\",\"players\": 7,\"submodes\": \"Hard\",\"timestart\": \"12:53:16\",\"timeend\": \"13:49:52\"}" https://mb.portal-vr.ru/add_statistic_test/add_game_match
> ```

</details>

<details>
 <summary><code>POST</code> <code>JSON</code> <code><b>/add_statistic_test/add_weapon_statistic</b></code></summary>

##### Parameters

> | name      | type     | data type | description      |
> |-----------|----------|-----------|------------------|
> | None      | required | JSON      | Weapon statistic |

##### JSON parameters

> | name       | type         | data type | description |
> |------------|--------------|-----------|-------------|
> | game_match | required     | Int       |             |
> | weapon     | required     | Int       |             |
> | kills      | not required | Int       |             |
> | headshots  | not required | Int       |             |
> | shots      | not required | Int       |             |
> | reloads    | not required | Int       |             |
> | usage_time | not required | String    | "M:S"       |

##### Responses

> | http code | content-type              | response                                                          |
> |-----------|---------------------------|-------------------------------------------------------------------|
> | `201`     | `application/json`        | `{"id": 1}`                                                       |
> | `400`     | `application/json`        | `{"code": 400, "message":"Parameter game_match was not provided"` |

##### Example cURL

> ```javascript
>  curl --header "Content-Type: application/json" --request POST --data "{\"game_match\":3,\"weapon\":1,\"kills\":45,\"headshots\":7,\"shots\":347,\"reloads\":11,\"usage_time\":\"16:52\"}" https://mb.portal-vr.ru/add_statistic_test/add_weapon_statistic
> ```

</details>

<details>
 <summary><code>POST</code> <code>JSON</code> <code><b>/add_statistic_test/add_skin_statistic</b></code></summary>

##### Parameters

> | name      | type     | data type | description    |
> |-----------|----------|-----------|----------------|
> | None      | required | JSON      | Skin statistic |

##### JSON parameters

> | name       | type         | data type | description |
> |------------|--------------|-----------|-------------|
> | game_match | required     | Int       |             |
> | skin       | required     | Int       |             |
> | usage_time | not required | String    | "M:S"       |

##### Responses

> | http code | content-type              | response                                                          |
> |-----------|---------------------------|-------------------------------------------------------------------|
> | `201`     | `application/json`        | `{"id": 1}`                                                       |
> | `400`     | `application/json`        | `{"code": 400, "message":"Parameter game_match was not provided"` |

##### Example cURL

> ```javascript
>  curl --header "Content-Type: application/json" --request POST --data "{\"game_match\":3,\"skin\":1,\"usage_time\":\"37:21\"}" https://mb.portal-vr.ru/add_statistic_test/add_skin_statistic
> ```

</details>